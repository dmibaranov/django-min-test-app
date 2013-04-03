from django.test import TestCase


class MinTestCase(TestCase):
    def test_get_one(self):
        from min_app.utils import get_one
        self.failUnlessEqual(get_one(), 1)


class MinModelTestCase(TestCase):
    def test_my_custom_model(self):
        from min_app.models import MyCustomModel
        obj = MyCustomModel(uid=1)
        self.failUnlessEqual(obj.get_uid(), 1)
