from django.core.management import setup_environ
from min_app import settings
setup_environ(settings)

from django.test.simple import run_tests
import test_runner
run_tests([test_runner], verbosity=1)
