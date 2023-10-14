from rest_framework import serializers
from package.models import User , Package , Subscription

class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','password']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def create(self , validated_date):
        password = validated_date.pop('password',None)
        instance = self.Meta.model(**validated_date)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        
