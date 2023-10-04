from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def process_json(request):
    data = request.data  # Получить данные JSON из запроса
    # Обработайте данные JSON здесь по вашей логике
    try:
        response_data = {
            'message': 'JSON data received and processed successfully',
            'data': data
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except:
        response_data = {
            'message': 'Error processing JSON data'
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
