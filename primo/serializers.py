from rest_framework import serializers
from .models import Champignon

class ChampSerializer(serializers.ModelSerializer):
	class Mera:
		model = Champignon
		fields = ['id', 'name', 'type']
