from rest_framework import serializers
from users.models import(Students,Orders)

class Studentsserializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class Ordersserializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields ='_all_'

    
