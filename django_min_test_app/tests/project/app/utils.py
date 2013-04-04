from django.conf import settings

from django_min_test_app.utils import get_two


def get_one():
    return get_two() / 2

def get_databases_count():
    return len(settings.DATABASES.keys())
