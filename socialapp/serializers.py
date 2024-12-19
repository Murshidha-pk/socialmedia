from rest_framework import serializers

from socialapp.models import User,Post

class UserSerializer(serializers.ModelSerializer):

    #for confirmation

    password1=serializers.CharField(write_only=True)

    password2=serializers.CharField(write_only=True)

    class Meta:

        model=User

        fields=["id","username","email","phone","password","password1","password2"]

        read_only_fields=["id","password"]

    

    def create(self,validated_data):

        password1=validated_data.pop("password1")
        password2=validated_data.pop("password2")

        if password1 != password2:

            raise serializers.ValidationError("password mismatch")
        
        return User.objects.create_user(**validated_data,password=password2)
    
class PostSerializer(serializers.ModelSerializer):

    owner=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Post

        fields="__all__"

        read_only_fields=["id","owner","created_at","updated_at","liked_by"]