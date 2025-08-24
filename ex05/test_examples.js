// Примеры тестов для улучшенной версии кейс-задачи №4
// Демонстрация путей решения проблем с тестированием

// ============================================================================
// UNIT-ТЕСТЫ С JEST
// ============================================================================

describe('DateCalculator', () => {
    let calculator;
    
    beforeEach(() => {
        calculator = new DateCalculator();
    });
    
    describe('isLeapYear', () => {
        test('should correctly identify leap years', () => {
            // Стандартные високосные годы
            expect(calculator.isLeapYear(2024)).toBe(true);
            expect(calculator.isLeapYear(2020)).toBe(true);
            expect(calculator.isLeapYear(2016)).toBe(true);
            
            // Не високосные годы
            expect(calculator.isLeapYear(2023)).toBe(false);
            expect(calculator.isLeapYear(2022)).toBe(false);
            expect(calculator.isLeapYear(2021)).toBe(false);
        });
        
        test('should handle century years correctly', () => {
            // Вековые годы, кратные 400 - високосные
            expect(calculator.isLeapYear(2000)).toBe(true);
            expect(calculator.isLeapYear(1600)).toBe(true);
            
            // Вековые годы, не кратные 400 - не високосные
            expect(calculator.isLeapYear(1900)).toBe(false);
            expect(calculator.isLeapYear(2100)).toBe(false);
        });
        
        test('should throw error for years outside valid range', () => {
            expect(() => calculator.isLeapYear(1899)).toThrow('Год должен быть между 1900 и 2100');
            expect(() => calculator.isLeapYear(2101)).toThrow('Год должен быть между 1900 и 2100');
            expect(() => calculator.isLeapYear(-1)).toThrow('Год должен быть между 1900 и 2100');
        });
        
        test('should handle edge cases', () => {
            expect(calculator.isLeapYear(1900)).toBe(false);
            expect(calculator.isLeapYear(2000)).toBe(true);
            expect(calculator.isLeapYear(2100)).toBe(false);
        });
    });
    
    describe('calculateDaysToNewYear', () => {
        test('should calculate days correctly for same year', () => {
            expect(calculator.calculateDaysToNewYear('31.12.2024')).toBe(0);
            expect(calculator.calculateDaysToNewYear('30.12.2024')).toBe(1);
            expect(calculator.calculateDaysToNewYear('01.01.2024')).toBe(365); // 2024 - високосный
            expect(calculator.calculateDaysToNewYear('01.01.2023')).toBe(364); // 2023 - не високосный
        });
        
        test('should calculate days correctly for next year', () => {
            expect(calculator.calculateDaysToNewYear('01.01.2025')).toBe(364); // до 31.12.2025
            expect(calculator.calculateDaysToNewYear('31.12.2025')).toBe(0);
        });
        
        test('should handle leap year calculations', () => {
            // 2024 - високосный год (366 дней)
            expect(calculator.calculateDaysToNewYear('29.02.2024')).toBe(306);
            expect(calculator.calculateDaysToNewYear('28.02.2024')).toBe(307);
            
            // 2023 - не високосный год (365 дней)
            expect(calculator.calculateDaysToNewYear('28.02.2023')).toBe(306);
        });
        
        test('should throw error for invalid date format', () => {
            expect(() => calculator.calculateDaysToNewYear('2024-12-31')).toThrow('Неверный формат даты');
            expect(() => calculator.calculateDaysToNewYear('31/12/2024')).toThrow('Неверный формат даты');
            expect(() => calculator.calculateDaysToNewYear('31.12')).toThrow('Неверный формат даты');
            expect(() => calculator.calculateDaysToNewYear('')).toThrow('Неверный формат даты');
        });
        
        test('should throw error for invalid date values', () => {
            expect(() => calculator.calculateDaysToNewYear('32.01.2024')).toThrow('Некорректная дата');
            expect(() => calculator.calculateDaysToNewYear('29.02.2023')).toThrow('Некорректная дата');
            expect(() => calculator.calculateDaysToNewYear('31.04.2024')).toThrow('Некорректная дата');
            expect(() => calculator.calculateDaysToNewYear('00.01.2024')).toThrow('День должен быть от 1 до 31');
            expect(() => calculator.calculateDaysToNewYear('01.13.2024')).toThrow('Месяц должен быть от 1 до 12');
        });
        
        test('should throw error for future dates', () => {
            const futureYear = new Date().getFullYear() + 1;
            expect(() => calculator.calculateDaysToNewYear(`01.01.${futureYear}`)).toThrow('Дата не может быть в будущем');
        });
        
        test('should use cache for repeated calculations', () => {
            const dateString = '15.06.2024';
            
            // Первый вызов - вычисляем
            const firstResult = calculator.calculateDaysToNewYear(dateString);
            
            // Второй вызов - используем кэш
            const secondResult = calculator.calculateDaysToNewYear(dateString);
            
            expect(firstResult).toBe(secondResult);
            expect(calculator.cache.get(dateString)).toBe(firstResult);
        });
    });
});

// ============================================================================
// ТЕСТЫ ДЛЯ УТИЛИТАРНЫХ ФУНКЦИЙ
// ============================================================================

describe('DateUtils', () => {
    describe('isValidMonth', () => {
        test('should return true for valid months', () => {
            for (let month = 1; month <= 12; month++) {
                expect(DateUtils.isValidMonth(month)).toBe(true);
            }
        });
        
        test('should return false for invalid months', () => {
            expect(DateUtils.isValidMonth(0)).toBe(false);
            expect(DateUtils.isValidMonth(13)).toBe(false);
            expect(DateUtils.isValidMonth(-1)).toBe(false);
            expect(DateUtils.isValidMonth(100)).toBe(false);
        });
    });
    
    describe('isValidDay', () => {
        test('should return true for valid days', () => {
            for (let day = 1; day <= 31; day++) {
                expect(DateUtils.isValidDay(day)).toBe(true);
            }
        });
        
        test('should return false for invalid days', () => {
            expect(DateUtils.isValidDay(0)).toBe(false);
            expect(DateUtils.isValidDay(32)).toBe(false);
            expect(DateUtils.isValidDay(-1)).toBe(false);
            expect(DateUtils.isValidDay(100)).toBe(false);
        });
    });
    
    describe('isValidDate', () => {
        test('should return true for valid dates', () => {
            expect(DateUtils.isValidDate(1, 1, 2024)).toBe(true);
            expect(DateUtils.isValidDate(31, 12, 2024)).toBe(true);
            expect(DateUtils.isValidDate(29, 2, 2024)).toBe(true); // високосный год
        });
        
        test('should return false for invalid dates', () => {
            expect(DateUtils.isValidDate(32, 1, 2024)).toBe(false);
            expect(DateUtils.isValidDate(29, 2, 2023)).toBe(false); // не високосный год
            expect(DateUtils.isValidDate(31, 4, 2024)).toBe(false); // апрель имеет 30 дней
            expect(DateUtils.isValidDate(30, 2, 2024)).toBe(false);
        });
    });
    
    describe('isFutureDate', () => {
        test('should return true for future dates', () => {
            const futureYear = new Date().getFullYear() + 1;
            expect(DateUtils.isFutureDate(`01.01.${futureYear}`)).toBe(true);
        });
        
        test('should return false for past dates', () => {
            const pastYear = new Date().getFullYear() - 1;
            expect(DateUtils.isFutureDate(`31.12.${pastYear}`)).toBe(false);
        });
        
        test('should return false for today', () => {
            const today = new Date();
            const todayString = `${today.getDate().toString().padStart(2, '0')}.${(today.getMonth() + 1).toString().padStart(2, '0')}.${today.getFullYear()}`;
            expect(DateUtils.isFutureDate(todayString)).toBe(false);
        });
    });
});

// ============================================================================
// ТЕСТЫ ДЛЯ СИСТЕМЫ БЕЗОПАСНОСТИ
// ============================================================================

describe('SecurityUtils', () => {
    describe('sanitizeOutput', () => {
        test('should escape HTML tags', () => {
            expect(SecurityUtils.sanitizeOutput('<script>alert("xss")</script>')).toBe('&lt;script&gt;alert("xss")&lt;/script&gt;');
            expect(SecurityUtils.sanitizeOutput('<img src="x" onerror="alert(1)">')).toBe('&lt;img src="x" onerror="alert(1)"&gt;');
        });
        
        test('should preserve safe text', () => {
            expect(SecurityUtils.sanitizeOutput('Hello World')).toBe('Hello World');
            expect(SecurityUtils.sanitizeOutput('123.45')).toBe('123.45');
            expect(SecurityUtils.sanitizeOutput('')).toBe('');
        });
    });
    
    describe('sanitizeInput', () => {
        test('should remove dangerous characters', () => {
            expect(SecurityUtils.sanitizeInput('<script>')).toBe('script&gt;');
            expect(SecurityUtils.sanitizeInput('alert(1)')).toBe('alert(1)');
        });
        
        test('should trim whitespace', () => {
            expect(SecurityUtils.sanitizeInput('  hello  ')).toBe('hello');
            expect(SecurityUtils.sanitizeInput('\n\t')).toBe('');
        });
        
        test('should preserve safe input', () => {
            expect(SecurityUtils.sanitizeInput('15.06.2024')).toBe('15.06.2024');
            expect(SecurityUtils.sanitizeInput('Hello World')).toBe('Hello World');
        });
    });
});

// ============================================================================
// ТЕСТЫ ДЛЯ СИСТЕМЫ КЭШИРОВАНИЯ
// ============================================================================

describe('Cache', () => {
    let cache;
    
    beforeEach(() => {
        cache = new Cache(3); // кэш на 3 элемента
    });
    
    test('should store and retrieve values', () => {
        cache.set('key1', 'value1');
        cache.set('key2', 'value2');
        
        expect(cache.get('key1')).toBe('value1');
        expect(cache.get('key2')).toBe('value2');
    });
    
    test('should return undefined for non-existent keys', () => {
        expect(cache.get('nonexistent')).toBeUndefined();
    });
    
    test('should handle cache size limit', () => {
        cache.set('key1', 'value1');
        cache.set('key2', 'value2');
        cache.set('key3', 'value3');
        cache.set('key4', 'value4'); // должен вытеснить key1
        
        expect(cache.get('key1')).toBeUndefined();
        expect(cache.get('key2')).toBe('value2');
        expect(cache.get('key3')).toBe('value3');
        expect(cache.get('key4')).toBe('value4');
    });
    
    test('should clear cache', () => {
        cache.set('key1', 'value1');
        cache.set('key2', 'value2');
        
        cache.clear();
        
        expect(cache.get('key1')).toBeUndefined();
        expect(cache.get('key2')).toBeUndefined();
    });
});

// ============================================================================
// ИНТЕГРАЦИОННЫЕ ТЕСТЫ
// ============================================================================

describe('Integration Tests', () => {
    test('should handle complete workflow', () => {
        const calculator = new DateCalculator();
        
        // Тестируем полный цикл работы
        const result = calculator.calculateDaysToNewYear('15.06.2024');
        const isLeap = calculator.isLeapYear(2024);
        
        expect(typeof result).toBe('number');
        expect(result).toBeGreaterThanOrEqual(0);
        expect(typeof isLeap).toBe('boolean');
        expect(isLeap).toBe(true); // 2024 - високосный год
    });
    
    test('should handle multiple calculations with cache', () => {
        const calculator = new DateCalculator();
        const testDate = '20.07.2024';
        
        // Первый расчет
        const result1 = calculator.calculateDaysToNewYear(testDate);
        
        // Второй расчет (должен использовать кэш)
        const result2 = calculator.calculateDaysToNewYear(testDate);
        
        // Результаты должны быть одинаковыми
        expect(result1).toBe(result2);
        
        // Проверяем, что результат в кэше
        expect(calculator.cache.get(testDate)).toBe(result1);
    });
});

// ============================================================================
// ТЕСТЫ ПРОИЗВОДИТЕЛЬНОСТИ
// ============================================================================

describe('Performance Tests', () => {
    test('should handle large number of calculations efficiently', () => {
        const calculator = new DateCalculator();
        const startTime = performance.now();
        
        // Выполняем 1000 расчетов
        for (let i = 0; i < 1000; i++) {
            calculator.calculateDaysToNewYear('15.06.2024');
        }
        
        const endTime = performance.now();
        const executionTime = endTime - startTime;
        
        // Время выполнения должно быть менее 100мс
        expect(executionTime).toBeLessThan(100);
    });
    
    test('should use cache for repeated calculations', () => {
        const calculator = new DateCalculator();
        const testDate = '15.06.2024';
        
        // Первый расчет
        const startTime1 = performance.now();
        calculator.calculateDaysToNewYear(testDate);
        const time1 = performance.now() - startTime1;
        
        // Второй расчет (из кэша)
        const startTime2 = performance.now();
        calculator.calculateDaysToNewYear(testDate);
        const time2 = performance.now() - startTime2;
        
        // Второй расчет должен быть быстрее
        expect(time2).toBeLessThan(time1);
    });
});

// ============================================================================
// ТЕСТЫ ГРАНИЧНЫХ СЛУЧАЕВ
// ============================================================================

describe('Edge Cases', () => {
    test('should handle leap year edge cases', () => {
        const calculator = new DateCalculator();
        
        // 29 февраля в високосный год
        expect(calculator.calculateDaysToNewYear('29.02.2024')).toBe(306);
        
        // 28 февраля в не високосный год
        expect(calculator.calculateDaysToNewYear('28.02.2023')).toBe(306);
        
        // 29 февраля в не високосный год должно вызывать ошибку
        expect(() => calculator.calculateDaysToNewYear('29.02.2023')).toThrow('Некорректная дата');
    });
    
    test('should handle year boundaries', () => {
        const calculator = new DateCalculator();
        
        // Последний день года
        expect(calculator.calculateDaysToNewYear('31.12.2024')).toBe(0);
        
        // Первый день года
        expect(calculator.calculateDaysToNewYear('01.01.2024')).toBe(365);
        
        // Переход между годами
        expect(calculator.calculateDaysToNewYear('01.01.2025')).toBe(364);
    });
    
    test('should handle century years', () => {
        const calculator = new DateCalculator();
        
        // 2000 - високосный (кратен 400)
        expect(calculator.isLeapYear(2000)).toBe(true);
        
        // 2100 - не високосный (не кратен 400)
        expect(calculator.isLeapYear(2100)).toBe(false);
    });
});

// ============================================================================
// МОКИ И СТАБЫ ДЛЯ ТЕСТИРОВАНИЯ
// ============================================================================

describe('Mock Tests', () => {
    test('should work with mocked Date', () => {
        // Мокаем Date для тестирования
        const originalDate = global.Date;
        const mockDate = new Date('2024-06-15');
        
        global.Date = jest.fn(() => mockDate);
        global.Date.now = jest.fn(() => mockDate.getTime());
        
        const calculator = new DateCalculator();
        
        // Тестируем с зафиксированной датой
        expect(DateUtils.isFutureDate('16.06.2024')).toBe(true);
        expect(DateUtils.isFutureDate('14.06.2024')).toBe(false);
        
        // Восстанавливаем оригинальный Date
        global.Date = originalDate;
    });
});

// ============================================================================
// ТЕСТЫ ДЛЯ UI (если доступен DOM)
// ============================================================================

if (typeof document !== 'undefined') {
    describe('UI Tests', () => {
        beforeEach(() => {
            // Создаем тестовый DOM
            document.body.innerHTML = `
                <input type="text" id="dateInput" placeholder="дд.мм.гггг">
                <button id="calculateBtn">Рассчитать</button>
                <div id="daysResult">
                    <span id="daysText"></span>
                </div>
                <div id="leapYearResult">
                    <span id="leapYearText"></span>
                </div>
                <div id="loadingIndicator" style="display: none;">Вычисляем...</div>
                <div id="errorContainer" style="display: none;"></div>
            `;
        });
        
        test('should initialize UI correctly', () => {
            const ui = new UI();
            
            expect(ui.dateInput).toBeDefined();
            expect(ui.calculateBtn).toBeDefined();
            expect(ui.daysText).toBeDefined();
            expect(ui.leapYearText).toBeDefined();
        });
        
        test('should format date input correctly', () => {
            const ui = new UI();
            
            // Симулируем ввод
            ui.dateInput.value = '15062024';
            ui.formatDateInput(ui.dateInput);
            
            expect(ui.dateInput.value).toBe('15.06.2024');
        });
        
        test('should show loading indicator', () => {
            const ui = new UI();
            
            ui.showLoading();
            
            expect(ui.calculateBtn.disabled).toBe(true);
            if (ui.loadingIndicator) {
                expect(ui.loadingIndicator.style.display).toBe('block');
            }
        });
        
        test('should hide loading indicator', () => {
            const ui = new UI();
            
            ui.hideLoading();
            
            expect(ui.calculateBtn.disabled).toBe(false);
            if (ui.loadingIndicator) {
                expect(ui.loadingIndicator.style.display).toBe('none');
            }
        });
    });
} 