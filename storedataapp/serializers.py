from rest_framework import serializers
from storedataapp.models import PERSON

class PERSONSerializer(serializers.ModelSerializer):
    class Meta:
        model = PERSON
        fields = ("person_id","reserved_user_id","first_name","last_name","birthdate","nationality","gender",
                 "passport_num","passport_ghost")
