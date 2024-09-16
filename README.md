1. Клонировать:
    ```bash
    git clone https://github.com/AqulaR/django_project.git
    cd django_project
    ```

2. Создать виртуальную среду:
    ```bash
    python -m venv testTaskEnv
    testTaskEnv\Scripts\activate.bat 
    ```

3. Установить зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Выполнить миграции:
    ```bash
    python manage.py migrate
    ```

5. Запустить:
    ```bash
    python manage.py runserver
    ```

6. Перейти по адресу: http://127.0.0.1:8000/.
