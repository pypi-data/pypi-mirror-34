from simple_mail.mailer import BaseSimpleMail, simple_mailer
from django.contrib.auth.models import User


class AlphaMail(BaseSimpleMail):
    template = 'simple_mail/default.html'
    email_key = 'alpha'

    def set_test_context(self):
        user_obj = User.objects.first()
        self.context = {
            'user': 'Charles',
            'user_obj': user_obj
        }

simple_mailer.register(AlphaMail)
