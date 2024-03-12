from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(MatchsDatasetModel)
admin.site.register(View_Scores_And_Fixtures)
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Check if superuser already exists
if not get_user_model().objects.filter(username='admin').exists():
    # Create a superuser
    User.objects.create_superuser('admin', '', 'admin')
    print("Superuser created successfully.")
else:
    print("Superuser already exists.")
