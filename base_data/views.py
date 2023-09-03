
from rest_framework import status
from .models import Card
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from .serializers import CardSerializer

# Create your views here.


class CardAPIViews(APIView):
    parser_classes = (MultiPartParser,)

    def get(self, request):
        w = Card.objects.all()
        return Response({'posts': CardSerializer(w, many=True).data})
    
    def post(self, request):
        data = request.data.copy()
        files = data.pop('image', None)
        serializer = CardSerializer(data=data)
        
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        
        if files:
            for file in files:
                instance.image.save(file.name, file)

        return Response({'post': serializer.data})
    

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': "Method PUT not allowed"})

        try:
            isinstance = Card.objects.get(pk=pk)
        except:
            return Response({'error': "Objects does not exists"})

        serializer = CardSerializer(data=request.data, instance=isinstance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})


    def delete(self, request, *args, **kwargs):

        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': "Method DELETE not allowed"})

        
        try:
            card = Card.objects.get(pk=pk)
            card.delete()
            return Response({'post': "delete_post" + str(pk)})
        except:
            return Response({'error': 'Card not found'}, status=status.HTTP_404_NOT_FOUND)
        
        