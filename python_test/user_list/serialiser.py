from rest_framework import serializers

from user_list import models


class AddressSerializer(serializers.ModelSerializer):
    firstname = serializers.SerializerMethodField()
    lastname = serializers.SerializerMethodField()
    mobilenumber = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = models.Address
        fields = [
            "firstname",
            "lastname",
            "mobilenumber",
            "email",
            "addr_line1",
            "addr_line2",
            "city",
            "state",
            "pincode",
        ]
    def get_firstname(self, obj):
        if obj.custome_id:
            return obj.custome_id.user_id.first_name
        else:
            return ""

    def get_lastname(self, obj):
        if obj.custome_id:
            return obj.custome_id.user_id.last_name
        else:
            return ""

    def get_email(self, obj):
        if obj.custome_id:
            return obj.custome_id.user_id.email
        else:
            return ""

    def get_mobilenumber(self, obj):
        if obj.custome_id:
            return obj.custome_id.mobile
        else:
            return ""
