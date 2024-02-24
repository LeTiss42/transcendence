from django.http import JsonResponse
from .models import Champignon
from .serializers import ChampSerializer

def drink_list(request):

	#get all the champignons
	#serialize them
	#return json
	champs = Champignon.objects.all()
	serializer = ChampSerializer(champs, many=True)
	return JsonResponse(serializer.data)