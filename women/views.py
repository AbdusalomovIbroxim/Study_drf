from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer


# Create your views here.

class WomenAPIView(APIView):
    def get(self, request):
        post = Women.objects.all()
        return Response({'post': WomenSerializer(post, many=True).data})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'Error': "Method PUT not allowed"})

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({"Error": "Object does not exists"})

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'Error': "Method DELETE not allowed"})
        try:
            id = Women.objects.get(pk=pk)
        except:
            return Response({"Error": "Object does not exists"})
        serializer = Women.objects.first(id=id)
        serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
