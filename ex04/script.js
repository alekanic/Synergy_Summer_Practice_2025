document.addEventListener('DOMContentLoaded', function() {
    const dateInput = document.getElementById('dateInput');
    const calculateBtn = document.getElementById('calculateBtn');
    const daysText = document.getElementById('daysText');
    const leapYearText = document.getElementById('leapYearText');
    const daysResult = document.getElementById('daysResult');
    const leapYearResult = document.getElementById('leapYearResult');

    // Функция для определения високосного года
    function isLeapYear(year) {
        // Високосный год делится нацело на 4, но не кратен 100
        // Однако, если кратен 400, то также считается високосным
        return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
    }

    // Функция для подсчета дней до Нового года
    function calculateDaysToNewYear(dateString) {
        // Парсим дату в формате дд.мм.гггг
        const parts = dateString.split('.');
        if (parts.length !== 3) {
            throw new Error('Неверный формат даты. Используйте формат дд.мм.гггг');
        }

        const day = parseInt(parts[0]);
        const month = parseInt(parts[1]);
        const year = parseInt(parts[2]);

        // Проверяем корректность даты
        if (isNaN(day) || isNaN(month) || isNaN(year)) {
            throw new Error('Неверный формат даты');
        }

        if (month < 1 || month > 12) {
            throw new Error('Месяц должен быть от 1 до 12');
        }

        if (day < 1 || day > 31) {
            throw new Error('День должен быть от 1 до 31');
        }

        // Создаем объект Date для введенной даты
        const inputDate = new Date(year, month - 1, day);
        
        // Проверяем, что дата корректна (например, 31 февраля не существует)
        if (inputDate.getDate() !== day || inputDate.getMonth() !== month - 1 || inputDate.getFullYear() !== year) {
            throw new Error('Некорректная дата');
        }

        // Создаем дату Нового года
        const newYearDate = new Date(year, 11, 31); // 31 декабря текущего года

        // Если введенная дата после Нового года, считаем до следующего года
        if (inputDate > newYearDate) {
            const nextNewYear = new Date(year + 1, 11, 31);
            const diffTime = nextNewYear - inputDate;
            return Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        } else {
            // Считаем дни до Нового года текущего года
            const diffTime = newYearDate - inputDate;
            return Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        }
    }

    // Функция для обработки клика по кнопке
    function handleCalculate() {
        const dateString = dateInput.value.trim();
        
        if (!dateString) {
            showError('Пожалуйста, введите дату');
            return;
        }

        try {
            // Парсим дату для определения года
            const parts = dateString.split('.');
            const year = parseInt(parts[2]);
            
            // Подсчитываем дни до Нового года
            const daysToNewYear = calculateDaysToNewYear(dateString);
            
            // Определяем, является ли год високосным
            const leapYear = isLeapYear(year);
            
            // Отображаем результаты
            daysText.textContent = `${daysToNewYear} дней`;
            leapYearText.textContent = leapYear ? 'Високосный' : 'Не високосный';
            
            // Убираем классы ошибок и добавляем классы успеха
            daysResult.classList.remove('error');
            leapYearResult.classList.remove('error');
            daysResult.classList.add('success');
            leapYearResult.classList.add('success');
            
        } catch (error) {
            showError(error.message);
        }
    }

    // Функция для отображения ошибки
    function showError(message) {
        daysText.textContent = 'Ошибка';
        leapYearText.textContent = 'Ошибка';
        
        daysResult.classList.remove('success');
        leapYearResult.classList.remove('success');
        daysResult.classList.add('error');
        leapYearResult.classList.add('error');
        
        // Показываем сообщение об ошибке в консоли для отладки
        console.error(message);
    }

    // Добавляем обработчик события для кнопки
    calculateBtn.addEventListener('click', handleCalculate);

    // Добавляем обработчик события для Enter в поле ввода
    dateInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            handleCalculate();
        }
    });

    // Добавляем автоматическое форматирование даты при вводе
    dateInput.addEventListener('input', function(event) {
        let value = event.target.value.replace(/\D/g, ''); // Убираем все нецифры
        
        if (value.length >= 2) {
            value = value.slice(0, 2) + '.' + value.slice(2);
        }
        if (value.length >= 5) {
            value = value.slice(0, 5) + '.' + value.slice(5);
        }
        if (value.length > 10) {
            value = value.slice(0, 10);
        }
        
        event.target.value = value;
    });
}); 