from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from order.models import Order
from order.serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self): #он вытаскивает все в экран и , он выведет все что принадлежит нам, отфильтрует
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset
    
    
class OrderConfirmAPIView(APIView):
    def get(self, request, code):
        order = get_object_or_404(Order, activation_code=code)
        if not order.is_confirm:

            order.is_congirm = True
            order.status = 'in_processing'
            activation_code = ''
            order.save(update_fields=['is_confirm', 'status', 'activation_code'])
            return Response({'message': 'Вы подтвердили заказ!'},
            status=status.HHTP_200_OK)
        return Response({'message': 'Вы уже подтвердили !'}, status=status.HHTP_400_BAD_REQUEST)