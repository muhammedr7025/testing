from rest_framework.views import APIView,Response
from .models import Enric
from .serilizers import EnricSerializer
from rest_framework import status

# Create your views here.
class EnricApi(APIView):
    def post(self,request):
        name=request.data.get('name')
        print(name)
        review=request.data.get('review')
        Enric.objects.create(name=name,review=review)
        return Response(data="review created",status=status.HTTP_200_OK)

    
    def get(self,request):
        data=Enric.objects.all()
        data=EnricSerializer(data,many=True).data
        return Response(data=data,status=status.HTTP_200_OK)
        