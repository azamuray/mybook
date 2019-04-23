# Тестовое задание от MyBook


## Запуск приложения на локальном сервере

1. Скопировать репозиторий: 
```
   git clone https://github.com/ai-rage/mybook.git
```   

2. Перейти в папку mybook
```
   cd mybook
```

3. Запустить команду с терминала:
```
   pip install -r requirements.txt
```

4. Развернуть БД:
```
   python manage.py migrate
```

5. Настроить переменные окружения через терминал:
```
   export SECRET_KEY=вашсекретныйключ
   export DEBUG_MODE=True
```
    
6. Запустить приложение:
```
   python manage.py runserver
```
