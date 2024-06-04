from django.db import models
from django.contrib.auth.models import AbstractUser


ORDINARY_USER, ADMIN, MANAGER = ('ordinary_user', 'admin','manager')
VIA_EMAIL, VIA_PHONE = ('via_email', 'via_phone')
NEW, CONFIRM, DONE, DONE_PHOTO = ('new', 'confirm', 'done', 'done_photo')


class User(AbstractUser):
    USER_TYPES = (
        (ORDINARY_USER, ORDINARY_USER),
        (ADMIN, ADMIN),
        (MANAGER, MANAGER)
    )
    user_role = models.CharField(max_length=50, choices=USER_TYPES, default=ORDINARY_USER)
    user_status = models.BooleanField(default=False)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    authentication_method = models.CharField(max_length=10, choices=[(VIA_EMAIL, 'Email'), (VIA_PHONE, 'Phone')])
    authentication_identifier = models.CharField(max_length=100, unique=True)

    photo = models.ImageField(upload_to='user_photos', default='default/user.jpg')
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Prefer not to say')
    )
    gender = models.CharField(max_length=1, choices=gender_choices, default='N')

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username


class Shared(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared_items')
    item_name = models.CharField(max_length=100)
    item_description = models.TextField()
    shared_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shared_items'

    def __str__(self):
        return f"{self.user} | {self.item_name}"


class UserConfirm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='confirmation')
    confirmation_code = models.CharField(max_length=50)
    confirmed = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_confirmations'

    def __str__(self):
        return f"{self.user.username}"

