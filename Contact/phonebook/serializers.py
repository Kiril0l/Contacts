from rest_framework import serializers
from phonebook.models import Phone


class PhoneDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Phone
        fields = "__all__"