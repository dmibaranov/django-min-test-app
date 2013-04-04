import os
import sys


def main():
    from django.conf import settings

    cp = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(os.path.sep.join([cp, 'django_min_test_app', 'tests']))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

    from django.test.utils import get_runner
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests([])

    sys.exit(failures)


if __name__ == '__main__':
    main()
