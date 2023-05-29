from rest_framework import serializers
from users.models import(Students,Orders,StudentsAddress)


class Studentsserializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class Ordersserializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields ='__all__'

class StudentsAddressserializers(serializers.ModelSerializer):
    class Meta:
        model = StudentsAddress
        fields ='__all__'

class StudentDetailsAdresssserialiazers(serializers.ModelSerializer):
    address = StudentsAddressserializers
    class Meta:
        model = ('first_name','last_name','mobile_number','adress')

    
