from rest_framework import serializers

from ..models.user import User

from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
           'id', 'role', 'first_name', 'last_name', 'email', 'phone_number', 'password'
        ]
        read_only_fields = ['id']

    def validate_email(self, value):

        # validate if the email is valid
        try:
            validate_email(value)

        except ValidationError:
            raise serializers.ValidationError("This email is not valid.")

        return value

    def validate_password(self, value):
        # Use Django's password validator to validate the password
        try:
            validate_password(value)  # This checks password strength based on Django's default rules
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return value

    def create(self, validated_data):
        # Remove password from validated data to hash it
        password = validated_data.pop('password')

        # Create a new user and set the password hash
        user = User(**validated_data)
        user.set_password(password)  # This hashes the password
        user.save()  # Save the user

        return user