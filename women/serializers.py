import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women


# serializer отвечает за обработку данных
class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ["title", "content", "cat"]

# def encode():
#     model = WomenModel('Angeline Ajlie', 'Content: Angeline Ajlie')
#     model_str = WomenSerializer(model)
#     print(model_str.data, type(model_str.data), sep='\n')
#     json = JSONRenderer().render(model_str.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Angeline Ajlie","content":"Content: Angeline Ajlie"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
