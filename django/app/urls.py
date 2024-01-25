from datetime import date

from django.urls import path
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import permission_classes, api_view
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from app.schema import schema_view
from app.serializers.participant import Participant

robert = Participant({'name': 'Robert', 'age': 30, 'hobbies': [
    {'name': 'painting', 'since': date.fromisoformat('2019-04-01')},
    {'name': 'running', 'since': date.fromisoformat('2022-05-02')},
]})


participants = [robert]


@swagger_auto_schema(
    methods=['get'],
    responses={
        200: Participant(many=True),
    },
    operation_summary='list all participants',
)
@swagger_auto_schema(
    methods=['post'],
    request_body=Participant,
    responses={
        200: Participant(),
    },
    operation_summary='create participant',
)
@api_view(['GET','POST'])
@permission_classes((AllowAny,))
def handle_participants(request: Request) -> Response:
    match request.method:
        case 'GET':
            return Response(data=[participant.data for participant in participants])
        case 'POST':
            participant = Participant(data=request.data)
            participant.is_valid(raise_exception=True)
            participants.append(participant)
            return Response(data=participant.data)
    raise MethodNotAllowed(request.method or '')


urlpatterns = [
    path('participants', handle_participants),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
