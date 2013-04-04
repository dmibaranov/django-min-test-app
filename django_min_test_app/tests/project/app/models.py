from django_min_test_app.models import MyModel


class MyCustomModel(MyModel):
    def get_uid(self):
        return self.uid
