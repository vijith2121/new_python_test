from django.shortcuts import render
from django.contrib import auth
from rest_framework import (
    permissions,
    request,
    response,
    status,
    views,
)
from user_list import models, serialiser

User = auth.get_user_model()

class Customer(views.APIView):
    def post(self, request):
        data = request.data
        first_name = data.get("first_name", "")
        last_name = data.get("last_name", "")
        email = data.get("email", "")
        mobile_number = data.get("mobile_number", "")
        address_line1 = data.get("address_line1", "")
        address_line2 = data.get("address_line2", "")
        city = data.get("city", "")
        state = data.get("state", "")
        pincode = data.get("pincode", "")

        user = User.objects.create(username=email,first_name=first_name,last_name=last_name,email=email)
        customer = models.Customer.objects.create(user_id=user,mobile=mobile_number,updated_by="user")
        address = models.Address.objects.create(
            custome_id=customer,addr_line1=address_line1,addr_line2=address_line2,city=city,state=state,pincode=pincode,updated_by="usera")

        serialized_data = serialiser.AddressSerializer(
            instance=address, many=False
        )
        return response.Response(
            {"result": True, "msg": "success", "data": serialized_data.data},
            status=status.HTTP_201_CREATED,
        )
