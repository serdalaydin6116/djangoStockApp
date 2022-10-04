from rest_framework import serializers, validators
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer