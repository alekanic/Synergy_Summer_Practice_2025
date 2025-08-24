// Улучшенная версия кода для кейс-задачи №4
// Демонстрация путей решения выявленных проблем

// ============================================================================
// 1. КОНФИГУРАЦИЯ И КОНСТАНТЫ
// ============================================================================

const CONFIG = {
    DATE_FORMAT: 'dd.mm.yyyy',
    MAX_YEAR: 2100,
    MIN_YEAR: 1900,
    DEFAULT_LOCALE: 'ru-RU',
    DEBOUNCE_DELAY: 300,
    CACHE_SIZE: 100
};

const DATE_CONSTANTS = {
    DAYS_IN_YEAR: 365,
    DAYS_IN_LEAP_YEAR: 366,
    MONTHS_IN_YEAR: 12,
    NEW_YEAR_MONTH: 12,
    NEW_YEAR_DAY: 31,
    FEBRUARY: 2,
    FEBRUARY_LEAP_DAY: 29
};

// ============================================================================
// 2. СИСТЕМА ЛОГИРОВАНИЯ
// ============================================================================

const Logger = {
    info: (message) => console.log(`[INFO] ${new Date().toISOString()}: ${message}`),
    error: (message) => console.error(`[ERROR] ${new Date().toISOString()}: ${message}`),
    debug: (message) => console.debug(`[DEBUG] ${new Date().toISOString()}: ${message}`),
    warn: (message) => console.warn(`[WARN] ${new Date().toISOString()}: ${message}`)
};

// ============================================================================
// 3. УТИЛИТАРНЫЕ ФУНКЦИИ
// ============================================================================

const DateUtils = {
    /**
     * Проверяет корректность месяца
     * @param {number} month - Месяц для проверки
     * @returns {boolean} true если месяц корректен
     */
    isValidMonth: (month) => month >= 1 && month <= DATE_CONSTANTS.MONTHS_IN_YEAR,
    
    /**
     * Проверяет корректность дня
     * @param {number} day - День для проверки
     * @returns {boolean} true если день корректен
     */
    isValidDay: (day) => day >= 1 && day <= 31,
    
    /**
     * Форматирует дату в локальном формате
     * @param {Date} date - Дата для форматирования
     * @returns {string} Отформатированная дата
     */
    formatDate: (date) => date.toLocaleDateString(CONFIG.DEFAULT_LOCALE),
    
    /**
     * Проверяет, является ли дата корректной
     * @param {number} day - День
     * @param {number} month - Месяц
     * @param {number} year - Год
     * @returns {boolean} true если дата корректна
     */
    isValidDate: (day, month, year) => {
        const date = new Date(year, month - 1, day);
        return date.getDate() === day && 
               date.getMonth() === month - 1 && 
               date.getFullYear() === year;
    },
    
    /**
     * Проверяет, является ли дата будущей
     * @param {string} dateString - Дата в формате дд.мм.гггг
     * @returns {boolean} true если дата в будущем
     */
    isFutureDate: (dateString) => {
        const parts = dateString.split('.');
        const inputDate = new Date(parts[2], parts[1] - 1, parts[0]);
        return inputDate > new Date();
    }
};

// ============================================================================
// 4. СИСТЕМА КЭШИРОВАНИЯ
// ============================================================================

class Cache {
    constructor(maxSize = CONFIG.CACHE_SIZE) {
        this.cache = new Map();
        this.maxSize = maxSize;
    }
    
    /**
     * Получает значение из кэша
     * @param {string} key - Ключ
     * @returns {any} Значение или undefined
     */
    get(key) {
        return this.cache.get(key);
    }
    
    /**
     * Сохраняет значение в кэш
     * @param {string} key - Ключ
     * @param {any} value - Значение
     */
    set(key, value) {
        if (this.cache.size >= this.maxSize) {
            const firstKey = this.cache.keys().next().value;
            this.cache.delete(firstKey);
        }
        this.cache.set(key, value);
        Logger.debug(`Cached result for key: ${key}`);
    }
    
    /**
     * Очищает кэш
     */
    clear() {
        this.cache.clear();
        Logger.info('Cache cleared');
    }
}

// ============================================================================
// 5. САНИТИЗАЦИЯ ДАННЫХ
// ============================================================================

const SecurityUtils = {
    /**
     * Санитизирует текст для безопасного вывода в DOM
     * @param {string} text - Текст для санитизации
     * @returns {string} Санитизированный текст
     */
    sanitizeOutput: (text) => {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    },
    
    /**
     * Валидирует и очищает пользовательский ввод
     * @param {string} input - Пользовательский ввод
     * @returns {string} Очищенный ввод
     */
    sanitizeInput: (input) => {
        return input.trim().replace(/[<>]/g, '');
    }
};

// ============================================================================
// 6. ОСНОВНОЙ КЛАСС КАЛЬКУЛЯТОРА
// ============================================================================

class DateCalculator {
    constructor() {
        this.cache = new Cache();
        Logger.info('DateCalculator initialized');
    }
    
    /**
     * Определяет, является ли год високосным
     * @param {number} year - Год для проверки
     * @returns {boolean} true если год високосный
     * @throws {Error} Если год вне допустимого диапазона
     */
    isLeapYear(year) {
        if (year < CONFIG.MIN_YEAR || year > CONFIG.MAX_YEAR) {
            throw new Error(`Год должен быть между ${CONFIG.MIN_YEAR} и ${CONFIG.MAX_YEAR}`);
        }
        
        const isLeap = (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
        Logger.debug(`Year ${year} is ${isLeap ? 'leap' : 'not leap'}`);
        return isLeap;
    }
    
    /**
     * Подсчитывает количество дней до Нового года
     * @param {string} dateString - Дата в формате дд.мм.гггг
     * @returns {number} Количество дней до Нового года
     * @throws {Error} При некорректной дате
     */
    calculateDaysToNewYear(dateString) {
        // Проверяем кэш
        const cachedResult = this.cache.get(dateString);
        if (cachedResult !== undefined) {
            Logger.debug(`Using cached result for ${dateString}`);
            return cachedResult;
        }
        
        // Парсим дату
        const parts = dateString.split('.');
        if (parts.length !== 3) {
            throw new Error('Неверный формат даты. Используйте формат дд.мм.гггг');
        }
        
        const day = parseInt(parts[0]);
        const month = parseInt(parts[1]);
        const year = parseInt(parts[2]);
        
        // Валидация
        if (isNaN(day) || isNaN(month) || isNaN(year)) {
            throw new Error('Неверный формат даты');
        }
        
        if (!DateUtils.isValidMonth(month)) {
            throw new Error('Месяц должен быть от 1 до 12');
        }
        
        if (!DateUtils.isValidDay(day)) {
            throw new Error('День должен быть от 1 до 31');
        }
        
        if (!DateUtils.isValidDate(day, month, year)) {
            throw new Error('Некорректная дата');
        }
        
        if (DateUtils.isFutureDate(dateString)) {
            throw new Error('Дата не может быть в будущем');
        }
        
        // Создаем объекты дат
        const inputDate = new Date(year, month - 1, day);
        const newYearDate = new Date(year, 11, 31);
        
        let daysToNewYear;
        
        if (inputDate > newYearDate) {
            // Если введенная дата после Нового года, считаем до следующего года
            const nextNewYear = new Date(year + 1, 11, 31);
            const diffTime = nextNewYear - inputDate;
            daysToNewYear = Math.floor(diffTime / (1000 * 60 * 60 * 24));
        } else {
            // Считаем дни до Нового года текущего года
            const diffTime = newYearDate - inputDate;
            daysToNewYear = Math.floor(diffTime / (1000 * 60 * 60 * 24));
        }
        
        // Кэшируем результат
        this.cache.set(dateString, daysToNewYear);
        
        Logger.info(`Calculated ${daysToNewYear} days to New Year for ${dateString}`);
        return daysToNewYear;
    }
}

// ============================================================================
// 7. УПРАВЛЕНИЕ UI
// ============================================================================

class UI {
    constructor() {
        this.calculator = new DateCalculator();
        this.debounceTimer = null;
        this.initializeElements();
        this.bindEvents();
        Logger.info('UI initialized');
    }
    
    /**
     * Инициализирует DOM элементы
     */
    initializeElements() {
        this.dateInput = document.getElementById('dateInput');
        this.calculateBtn = document.getElementById('calculateBtn');
        this.daysText = document.getElementById('daysText');
        this.leapYearText = document.getElementById('leapYearText');
        this.daysResult = document.getElementById('daysResult');
        this.leapYearResult = document.getElementById('leapYearResult');
        this.loadingIndicator = document.getElementById('loadingIndicator');
        this.errorContainer = document.getElementById('errorContainer');
    }
    
    /**
     * Привязывает обработчики событий
     */
    bindEvents() {
        this.calculateBtn.addEventListener('click', () => this.handleCalculate());
        
        this.dateInput.addEventListener('keypress', (event) => {
            if (event.key === 'Enter') {
                this.handleCalculate();
            }
        });
        
        // Дебаунсинг для форматирования
        this.dateInput.addEventListener('input', (event) => {
            clearTimeout(this.debounceTimer);
            this.debounceTimer = setTimeout(() => {
                this.formatDateInput(event.target);
            }, CONFIG.DEBOUNCE_DELAY);
        });
    }
    
    /**
     * Форматирует ввод даты
     * @param {HTMLInputElement} input - Поле ввода
     */
    formatDateInput(input) {
        let value = input.value.replace(/\D/g, '');
        
        if (value.length >= 2) {
            value = value.slice(0, 2) + '.' + value.slice(2);
        }
        if (value.length >= 5) {
            value = value.slice(0, 5) + '.' + value.slice(5);
        }
        if (value.length > 10) {
            value = value.slice(0, 10);
        }
        
        input.value = value;
    }
    
    /**
     * Показывает индикатор загрузки
     */
    showLoading() {
        if (this.loadingIndicator) {
            this.loadingIndicator.style.display = 'block';
        }
        this.calculateBtn.disabled = true;
    }
    
    /**
     * Скрывает индикатор загрузки
     */
    hideLoading() {
        if (this.loadingIndicator) {
            this.loadingIndicator.style.display = 'none';
        }
        this.calculateBtn.disabled = false;
    }
    
    /**
     * Показывает ошибку
     * @param {string} message - Сообщение об ошибке
     */
    showError(message) {
        this.daysText.textContent = 'Ошибка';
        this.leapYearText.textContent = 'Ошибка';
        
        this.daysResult.classList.remove('success');
        this.leapYearResult.classList.remove('success');
        this.daysResult.classList.add('error');
        this.leapYearResult.classList.add('error');
        
        if (this.errorContainer) {
            this.errorContainer.textContent = SecurityUtils.sanitizeOutput(message);
            this.errorContainer.style.display = 'block';
        }
        
        Logger.error(`UI Error: ${message}`);
    }
    
    /**
     * Показывает успешный результат
     * @param {number} daysToNewYear - Количество дней до Нового года
     * @param {boolean} isLeapYear - Является ли год високосным
     */
    showSuccess(daysToNewYear, isLeapYear) {
        this.daysText.textContent = SecurityUtils.sanitizeOutput(`${daysToNewYear} дней`);
        this.leapYearText.textContent = SecurityUtils.sanitizeOutput(
            isLeapYear ? 'Високосный' : 'Не високосный'
        );
        
        this.daysResult.classList.remove('error');
        this.leapYearResult.classList.remove('error');
        this.daysResult.classList.add('success');
        this.leapYearResult.classList.add('success');
        
        if (this.errorContainer) {
            this.errorContainer.style.display = 'none';
        }
        
        Logger.info(`Successfully displayed results: ${daysToNewYear} days, ${isLeapYear ? 'leap' : 'not leap'} year`);
    }
    
    /**
     * Обрабатывает нажатие кнопки расчета
     */
    async handleCalculate() {
        const dateString = SecurityUtils.sanitizeInput(this.dateInput.value.trim());
        
        if (!dateString) {
            this.showError('Пожалуйста, введите дату');
            return;
        }
        
        this.showLoading();
        
        try {
            // Имитируем асинхронную операцию для демонстрации
            await new Promise(resolve => setTimeout(resolve, 100));
            
            // Парсим дату для определения года
            const parts = dateString.split('.');
            const year = parseInt(parts[2]);
            
            // Подсчитываем дни до Нового года
            const daysToNewYear = this.calculator.calculateDaysToNewYear(dateString);
            
            // Определяем, является ли год високосным
            const leapYear = this.calculator.isLeapYear(year);
            
            // Отображаем результаты
            this.showSuccess(daysToNewYear, leapYear);
            
        } catch (error) {
            this.showError(error.message);
        } finally {
            this.hideLoading();
        }
    }
}

// ============================================================================
// 8. ИНИЦИАЛИЗАЦИЯ ПРИ ЗАГРУЗКЕ ДОКУМЕНТА
// ============================================================================

document.addEventListener('DOMContentLoaded', function() {
    try {
        const ui = new UI();
        Logger.info('Application started successfully');
    } catch (error) {
        Logger.error(`Failed to initialize application: ${error.message}`);
        console.error('Application initialization failed:', error);
    }
});

// ============================================================================
// 9. ЭКСПОРТ ДЛЯ ТЕСТИРОВАНИЯ
// ============================================================================

if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        DateCalculator,
        DateUtils,
        SecurityUtils,
        Cache,
        Logger,
        CONFIG,
        DATE_CONSTANTS
    };
} 