DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        }
}

INSTALLED_APPS = (
    'project.app',
    'django_min_test_app',)

SECRET_KEY = '12345678'