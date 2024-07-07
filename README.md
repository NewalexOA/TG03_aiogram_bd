### [Описание на русском языке](#русский)

### [Description in English](#english)

---

## <a name="русский"></a>Описание на русском языке

### Описание

Это учебный проект бота для Telegram, созданный в рамках задания:

1. Запрашивать у пользователя имя, возраст и класс (grade), в котором он учится.
2. Сохранять введенные данные в таблицу students базы данных school_data.db.

### Функциональность бота

#### 1. Запрос данных у пользователя

Бот запрашивает у пользователя имя, возраст и класс (grade). Для этого используется механизм состояний (FSM) из библиотеки aiogram. Пользователь последовательно вводит запрашиваемые данные, которые проверяются на корректность. 

#### 2. Сохранение данных в базу данных

После ввода всех данных бот сохраняет их в таблицу `students` базы данных `school_data.db`. Для этого используется библиотека sqlite3. Таблица `students` содержит следующие колонки:
- `id` (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- `name` (TEXT, NOT NULL)
- `age` (INTEGER, NOT NULL)
- `grade` (TEXT, NOT NULL)

### Структура проекта

Проект состоит из следующих файлов и директорий:

- `main.py`: Главный файл для запуска бота. Инициализирует бота и диспетчер, устанавливает команды и запускает опрос обновлений.
- `config.py`: Файл конфигурации, содержащий токен бота.
- `handlers.py`: Содержит обработчики команд и сообщений бота, включая запрос данных и их сохранение.
- `database.py`: Содержит функции для работы с базой данных SQLite.
- `requirements.txt`: Список зависимостей проекта.

### Установка и запуск

1. **Клонирование репозитория**:
    ```sh
    git clone https://github.com/NewalexOA/TG03_aiogram_bd.git
    cd TG03_aiogram_bd
    ```

2. **Создание виртуального окружения и установка зависимостей**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # для Linux и macOS
    .\venv\Scripts\activate  # для Windows
    pip install -r requirements.txt
    ```

3. **Создание файла конфигурации**:
    - Создайте файл `config.py` в корне проекта и добавьте в него ваш токен Telegram бота:
      ```python
      BOT_TOKEN = 'ваш_токен_бота'
      ```

4. **Запуск бота**:
    ```sh
    python main.py
    ```

---

## <a name="english"></a>Description in English

### Description

This is an educational project for a Telegram bot, created as part of an assignment:

1. Request the user's name, age, and grade.
2. Save the entered data into the `students` table of the `school_data.db` database.

### Bot Functionality

#### 1. Requesting User Data

The bot requests the user's name, age, and grade. This is done using the finite state machine (FSM) mechanism from the aiogram library. The user sequentially enters the requested data, which is validated for correctness.

#### 2. Saving Data to the Database

After entering all the data, the bot saves it into the `students` table of the `school_data.db` database. This is done using the sqlite3 library. The `students` table contains the following columns:
- `id` (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- `name` (TEXT, NOT NULL)
- `age` (INTEGER, NOT NULL)
- `grade` (TEXT, NOT NULL)

### Project Structure

The project consists of the following files and directories:

- `main.py`: The main file for running the bot. It initializes the bot and dispatcher, sets commands, and starts polling for updates.
- `config.py`: Configuration file containing the bot token.
- `handlers.py`: Contains handlers for bot commands and messages, including data requests and saving.
- `database.py`: Contains functions for working with the SQLite database.
- `requirements.txt`: List of project dependencies.

### Installation and Launch

1. **Clone the repository**:
    ```sh
    git clone https://github.com/NewalexOA/TG03_aiogram_bd.git
    cd your_repository
    ```

2. **Create a virtual environment and install dependencies**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # for Linux and macOS
    .\venv\Scripts\activate  # for Windows
    pip install -r requirements.txt
    ```

3. **Create a configuration file**:
    - Create a file named `config.py` in the root directory of the project and add your Telegram bot token:
      ```python
      BOT_TOKEN = 'your_bot_token'
      ```

4. **Run the bot**:
    ```sh
    python main.py
    ```
