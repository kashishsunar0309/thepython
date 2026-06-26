INSTALLED_APPS = [
    # My apps.
    'learning_logs',
    'accounts',
    #Third party apps. 
    'django_bootstrap5',
    # Default django apps.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# My settings.
LOGIN_REDIRECT_URL = 'learning_logs:index'
LOGIN_URL = 'accounts:login'