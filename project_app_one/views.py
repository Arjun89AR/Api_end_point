from rest_framework.decorators import api_view
from rest_framework.response import   Response
from rest_framework import status
from  . serializer import ReminderSerializer

@api_view(['POST'])
def reminder(request):
    serializers = ReminderSerializer(data=request.data)

    if serializers.is_valid():
        serializers.save()
        return Response({'Message':'Reminder created successfully', 'data':serializers.data},status=status.HTTP_201_CREATED  )

    return Response({'error':serializers.errors}, status=status.HTTP_400_BAD_REQUEST)