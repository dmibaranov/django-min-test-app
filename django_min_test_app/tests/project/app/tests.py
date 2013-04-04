from django.conf import settings
from django.test import TestCase


class MinTestCase(TestCase):
    def test_get_one(self):
        from project.app.utils import get_one
        self.failUnlessEqual(get_one(), 1)

    def test_get_databases_count(self):
        from project.app.utils import get_databases_count
        my_count = len(settings.DATABASES.keys())
        self.failUnlessEqual(get_databases_count(), my_count)


class MinModelTestCase(TestCase):
    def test_my_custom_model(self):
        from project.app.models import MyCustomModel
        obj = MyCustomModel(uid=1)
        self.failUnlessEqual(obj.get_uid(), 1)
