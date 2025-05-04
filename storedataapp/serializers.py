from rest_framework import serializers
from storedataapp.models import PERSON

class PERSONSerializer(serializers.ModelSerializer):
    class Meta:
        model = PERSON
        fields = ("person_id","reserved_user_id","pronoun_id","first_name",
                 "middle_name","last_name","birthdate","nationality","gender",
                 "passport_num_hash","passport_num_salt","passport_photo_ref",
                 "bio","avatar_ref")