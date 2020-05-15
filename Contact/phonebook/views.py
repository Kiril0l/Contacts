from django.shortcuts import render
from rest_framework import generics
from phonebook.serializers import PhoneDetailSerializer
from phonebook.models import Phone
from phonebook.permissions import IsOwnerOrOnly
from rest_framework.permissions import IsAuthenticated


class PhoneCreateView(generics.CreateAPIView):
    serializer_class = PhoneDetailSerializer


class PhoneListView(generics.ListAPIView):
    serializer_class = PhoneDetailSerializer
    permission_classes = (IsAuthenticated, )
    def get_queryset(self):
        user = self.request.user
        return Phone.objects.filter(user_id=user)


class PhoneDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PhoneDetailSerializer
    queryset = Phone.objects.all()
    permission_classes = (IsOwnerOrOnly, )
    def get_queryset(self):
        user = self.request.user
        return Phone.objects.filter(user_id=user)
