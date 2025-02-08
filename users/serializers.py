from django.utils.timezone import now
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from users.models import CustomUser

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):

        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("No se encontró una cuenta con este email.")
        return value

class PasswordResetSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField(min_length=8, write_only=True)

    def validate_token(self, value):
        try:
            user = CustomUser.objects.get(reset_token=value)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("Token inválido.")

        if user.reset_token_expires_at and user.reset_token_expires_at < now():
            raise serializers.ValidationError("El token ha expirado.")

        return value

    def save(self):
        token = self.validated_data['token']
        new_password = self.validated_data['new_password']

        user = CustomUser.objects.get(reset_token=token)
        user.set_password(new_password)
        user.reset_token = None
        user.reset_token_expires_at = None
        user.save()
