from rest_framework import serializers
from .models import User
from users.services import get_details, check_email


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'email',
                  'first_name',
                  'last_name',
                  'password',
                  'location', )

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        if check_email(validated_data['email']):
            raise serializers.ValidationError('E-mail is not exists')

        details = get_details(validated_data['email'])
        if 'error' not in details:
            if 'first_name' not in validated_data and details["name"]["givenName"] != None:
                validated_data['first_name'] = details["name"]["givenName"]
            if 'last_name' not in validated_data and details["name"]["familyName"] != None:
                validated_data['last_name'] = details["name"]["familyName"]

            validated_data['location'] = details["location"]



        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
