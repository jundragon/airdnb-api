from rest_framework.decorators import api_view

# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status
from .models import Room
from .serializers import ReadRoomSerializer, CreateRoomSerializer


@api_view
def rooms_view(request):
    if request.method == "GET":
        rooms = Room.objects.all()
        serializer = ReadRoomSerializer(rooms, many=True).data
        return Response(serializer)
    elif request.method == "POST":
        serializer = CreateRoomSerializer(data=request.data)
        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "DELETE"])
# def list_rooms(request):
#     rooms = room_models.Room.objects.all()
#     serialized_Rooms = room_serializers.RoomSerializer(rooms, many=True)
#     return Response(data=serialized_Rooms.data)


# class ListRoomsView(APIView):
#     def get(self, request):
#         rooms = room_models.Room.objects.all()
#         serializer = room_serializers.RoomSerializer(rooms, many=True)
#         return Response(serializer.data)


# class ListRoomsView(ListAPIView):

#     queryset = Room.objects.all()
#     serializer_class = ReadRoomSerializer


class SeeRoomView(RetrieveAPIView):

    queryset = Room.objects.all()
    serializer_class = ReadRoomSerializer
