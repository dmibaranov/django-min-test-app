from setuptools import setup, find_packages

setup(
    name="django_min_test_app",
    version="0.0.1",
    packages=find_packages(),
    author="Dmi Baranov",
    author_email="dmi.baranov@gmail.com",
    description="A min self-testing Django app package",
    url="http://github.com/d9frog9n/django-min-test-app",
    install_requires=[
        "Django",
    ],
    test_suite="runtests.main"
)
