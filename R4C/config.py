SECRET_KEY = 'your_secret_key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'TJ_db',  # ваше имя базы данных
        'USER': 'postgres',  # ваше имя пользователя базы данных
        'PASSWORD': 'stasv',  # ваш пароль базы данных
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
