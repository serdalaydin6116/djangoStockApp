from rest_framework import serializers
from .models import Firm, Category, Brand,Product

class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model=Firm
        fields=(
            'name',
            'phone',
            'address',
            
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields= '__all__'








# class ReservationSerializer(serializers.ModelSerializer):

#     passenger=PassengerSerializer(many=True, required=False)
#     flight=serializers.StringRelatedField()  #default =readonly
#     flight_id=serializers.IntegerField(write_only=True) #create yaparken bunu getir
#     user=serializers.StringRelatedField()  #default =readonly
#     user_id=serializers.IntegerField(write_only=True, required=False) #create yaparken bunu getir
#     class Meta:
#         model=Reservation
#         fields= (
#         'id',
#         "flight",
#         "flight_id",
#         "user",
#         "user_id",
#         "passenger",
#         )

#     def create(self, validated_data):
#         passenger_data=validated_data.pop('passenger')
#         validated_data['user_id']=self.context['request'].user.id #guncel useri yakalıyoruz
#         reservation=Reservation.objects.create(**validated_data)

#         for passenger in passenger_data:
#             pas=Passenger.objects.create(**passenger)
#             reservation.passenger.add(pas)
#         reservation.save()
#         return reservation


# class StaffFlightSerializer(serializers.ModelSerializer):
#     reservation=ReservationSerializer(many=True, read_only=True)

#     class Meta:
#         model=Flight  #flight modelinde reservation field yok
#         fields='__all__'

        
