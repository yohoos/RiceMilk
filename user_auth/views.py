import json
from datetime import datetime

from django.contrib.auth import authenticate
from django.http.response import JsonResponse, Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings


# Create your views here.
class TokenView(APIView):
    def get(self, request):
        token = request.COOKIES.get(api_settings.JWT_AUTH_COOKIE)
        if token is not None:
            return Response().set_cookie(api_settings.JWT_AUTH_COOKIE, token,
                                         expires=datetime.now() + api_settings.JWT_EXPIRATION_DELTA, httponly=True)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            body = json.loads(request.body.decode('utf-8'))
            username = body['username']
            password = body['password']
        except:
            print("Can't parse request body.")

        user = authenticate(username=username, password=password)
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        expiration = datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
        expiration = expiration.timestamp() * 1000

        response = Response({'token': token, 'expires': expiration}, status=status.HTTP_201_CREATED)
        response.set_cookie(api_settings.JWT_AUTH_COOKIE, token, expires=expiration, httponly=True)

        return response


def is_authenticated(request):
    if request.method == 'GET':
        check = request.COOKIES.get(api_settings.JWT_AUTH_COOKIE) is not None
        # return Response(status=status.HTTP_200_OK)
        return JsonResponse({'is_authenticated': check})
    else:
        return Http404()
