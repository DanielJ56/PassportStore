from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from storedataapp.models import PERSON
from storedataapp.serializers import PERSONSerializer
from django.http import JsonResponse
from django.http import HttpResponse

import json

#from myapi.models import students
#from myapi.serializers import studentsSerializer

# Create your views here.

@csrf_exempt
def store_data(request):
    if (request.method == "POST"):
        data_body = request.body
        request_json = json.loads(data_body)


        entry_pronoun_id = request_json["pronoun_id"]
        entry_first = request_json["first_name"]

        entry_last_name = request_json["last_name"]
        entry_birth = request_json["birthdate"]
        entry_nat = request_json["nationality"]



        
        person_entry = PERSON(person_id = entry_person_id, 
                              reserved_user_id =entry_reserved_user_id,
                              pronoun_id = entry_pronoun_id,
                              birthdate = entry_birthdate,
                              first_name = entry_first_name,
                              middle_name = entry_middle_name,
                              last_name = entry_last_name,
                              nationality = entry_nationality
                             )
        person_entry.save()
        json_response = {"status":"200"}
        return JsonResponse(json_response)
