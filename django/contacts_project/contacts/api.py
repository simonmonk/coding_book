from django.http import JsonResponse
from django.core import serializers
from contacts.models import Contact
import json

# Create your API calls here

def list(request):
    contacts = Contact.objects.all()
    contacts_json = serializers.serialize('json', contacts)
    return JsonResponse(json.loads(contacts_json), safe=False)