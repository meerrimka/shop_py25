from django.shortcuts import render
from .serializers import ContactSerializer
from rest_framework import mixins, viewsets, status
from .models import Contact
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



class ContactAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, 
                     mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(email=self.request.user.email)
    