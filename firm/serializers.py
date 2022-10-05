from rest_framework import serializers
from .models import Firm, Category, Brand, Product, Stock
from users.models import Auth_User

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


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields= '__all__'








class ProductSerializer(serializers.ModelSerializer):

    product=FirmSerializer(many=True, required=False)
    category=serializers.StringRelatedField()  #default =readonly
    category_id=serializers.IntegerField(write_only=True) #create yaparken bunu getir
    brand=serializers.StringRelatedField()  #default =readonly
    brand_id=serializers.IntegerField(write_only=True, required=False) #create yaparken bunu getir
    class Meta:
        model=Product
        fields= (
        'id',
        "p_name",
        "p_name_id",
        "category",
        "category_id",
        "stock",
        
        )

    def create(self, validated_data):
        product_data=validated_data.pop('product')
        validated_data['user_id']=self.context['request'].user.id #guncel useri yakalıyoruz
        firm=Firm.objects.create(**validated_data)

        for product in product_data:
            pro=Product.objects.create(**product)
            firm.product.add(pro)
        firm.save()
        return firm


# class StaffFlightSerializer(serializers.ModelSerializer):
#     reservation=ReservationSerializer(many=True, read_only=True)

#     class Meta:
#         model=Flight  #flight modelinde reservation field yok
#         fields='__all__'

        
