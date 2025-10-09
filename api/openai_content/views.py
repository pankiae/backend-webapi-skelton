from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.openai_logic import text_generation

# Create your views here.

class Channel(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        res = text_generation.text_generation(request.data.get("q"))

        return Response(
            {"detail": res}, 
            status=201 # 201 Created is often used for successful POST requests
        )