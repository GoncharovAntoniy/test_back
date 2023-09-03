from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    price = serializers.IntegerField(default='0')
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField() 
    image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)


    def create(self, validated_data):
        return Card.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.time_create = validated_data.get('time_create', instance.time_create)
        instance.time_update = validated_data.get('time_update', instance.time_update)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.cat_id = validated_data.get('cat_id', instance.cat_id)
        instance.id = validated_data.get('id', instance.id)
        
        instance.save()
        return instance