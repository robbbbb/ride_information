from rest_framework import serializers
from ..models.user import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
           'id_user', 'role', 'first_name', 'last_name', 'email', 'phone_number'
        ]
        read_only_fields = ['id_user']

    def validate_email(self, value):

        # validate if the email is valid
        try:
            validate_email(value)

        except ValidationError:
            raise serializers.ValidationError("This email is not valid.")

        # validate if the user email already exists
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists")

        return value
