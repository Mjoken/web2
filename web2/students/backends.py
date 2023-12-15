from django.contrib.auth.backends import BaseBackend
from students.models import Student
class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Student.objects.get(email=username)
            if user.check_password(password):
                return user
        except Student.MultipleObjectsReturned:
            user = Student.objects.filter(email=username.order_by('id').first())
        except Student.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Student.objects.get(pk=user_id)
        except Student.DoesNotExist:
            return None