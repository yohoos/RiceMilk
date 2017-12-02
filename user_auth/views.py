import json
from datetime import datetime

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings


# Create your views here.
class TokenView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        token = request.COOKIES.get(api_settings.JWT_AUTH_COOKIE)
        if token == None:
            return Response({'authenticated': False})
        else:
            jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
            payload = jwt_decode_handler(token)
            exp_ms = payload['exp'] * 1000

            return Response({'authenticated': True, 'expires': exp_ms})

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
        print("Generated payload: " + str(payload))
        token = jwt_encode_handler(payload)
        print("Generated token: " + str(token))
        expiration = datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
        utc_ms = expiration.timestamp() * 1000
        print("expiration in ms: " + str(utc_ms))

        response = Response({'token': token, 'expires': utc_ms}, status=status.HTTP_201_CREATED)
        response.set_cookie(api_settings.JWT_AUTH_COOKIE, token, expires=expiration, httponly=True)

        return response


class RefreshView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

        token = request.COOKIES.get(api_settings.JWT_AUTH_COOKIE)
        if token == None:
            return Response("No Token Found", status=status.HTTP_401_UNAUTHORIZED)

        payload = jwt_decode_handler(token)
        print("Decoded payload is: " + str(payload))

        new_expiration = datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
        time_since_orig = datetime.utcnow().timestamp() - (payload['orig_iat'] * 1000)
        max_refresh_time = api_settings.JWT_REFRESH_EXPIRATION_DELTA.microseconds / 1000

        if time_since_orig >= max_refresh_time:
            return Response("Exceeded max refresh time. Log in again manually.", status=status.HTTP_406_NOT_ACCEPTABLE)

        utc_ms = new_expiration.timestamp() * 1000

        response = Response({'token': token, 'expires': utc_ms}, status=status.HTTP_200_OK)
        response.set_cookie(api_settings.JWT_AUTH_COOKIE, token, expires=new_expiration, httponly=True)

        return response


class LogoutView(APIView):
    def post(self, request):
        response = Response("Logged out.", status=status.HTTP_200_OK)
        response.delete_cookie(api_settings.JWT_AUTH_COOKIE)

        return response
