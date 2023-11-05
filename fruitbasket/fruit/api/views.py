from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from fruit.models import Fruit
from fruit.api.serializers import FruitSerializer


############### CLASS VIEWS ###############
class FruitListCreateAPIVıew(APIView):
    def get(self, request):
        fruits = Fruit.objects.filter(stock=True)
        serializer = FruitSerializer(fruits, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FruitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class FruitDetailAPIView(APIView):
    def get_object(self, pk):
        fruit_instance = get_object_or_404(Fruit, pk=pk)
        return fruit_instance

    def get(self, request, pk):
        fruit = self.get_object(pk=pk)
        serializer = FruitSerializer(fruit)
        return Response(serializer.data)

    def put(self, request, pk):
        fruit = self.get_object(pk=pk)
        serializer = FruitSerializer(fruit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        fruit = self.get_object(pk=pk)
        fruit.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )


############### FUNCTIONAL METHODS ###############
# @api_view(["GET", "POST"])
# def fruit_list_create_api_view(request):
#     if request.method == "GET":
#         fruits = Fruit.objects.filter(stock=True)
#         serializer = FruitSerializer(fruits, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = FruitSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "PUT", "DELETE"])
# def fruit_detail_api(request, pk):
#     try:
#         fruit_instance = Fruit.objects.get(pk=pk)
#     except Fruit.DoesNotExist:
#         return Response(
#             data={
#                 "errors": {
#                     "code": 404,
#                     "message": "Aranılan kriterlere uygun ürün bulunamadı.",
#                 }
#             },
#             status=status.HTTP_404_NOT_FOUND,
#         )
#     if request.method == "GET":
#         serializer = FruitSerializer(fruit_instance)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = FruitSerializer(fruit_instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#         fruit_instance.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT,
#         )
