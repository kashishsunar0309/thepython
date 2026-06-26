INSTALLED_APPS = [
    'learning_logs',  # add this line
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #My settings.
    LOGIN_REDIRECT_URL = 'learning_logs: index'
]