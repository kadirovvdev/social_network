from django.contrib import admin
from .models import User, Shared, UserConfirm

admin.site.register(User)
admin.site.register(Shared)
admin.site.register(UserConfirm)