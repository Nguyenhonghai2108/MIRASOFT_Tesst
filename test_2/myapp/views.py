import os
import base64
import logging
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import Account
from .serializers import AccountSerializer

# Configure logging
logger = logging.getLogger(__name__)

# Base directory for HTML file lookup
BASE_DIRECTORY = "C:/imprints_html_file"
ENVIRONMENTS = {0: "AWS", 1: "K5", 2: "T2"}
APPS = {0: "app1", 1: "app2"}

class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'registerID'

class ShowSerialPasoView(APIView):
    parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs):
        data = request.data
        file_name = data.get("file")
        app_env = data.get("app_env")
        contract_server = data.get("contract_server")

        if not file_name or app_env not in ENVIRONMENTS or contract_server not in APPS:
            return JsonResponse({
                "success": False,
                "filename": "",
                "content": "",
                "message": "Invalid request parameters"
            }, status=400)

        # Construct file path
        file_path = os.path.join(BASE_DIRECTORY, ENVIRONMENTS[app_env], APPS[contract_server], f"{file_name}.html")
        
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            return JsonResponse({
                "success": False,
                "filename": "",
                "content": "",
                "message": "File not found"
            }, status=404)

        try:
            with open(file_path, "rb") as file:
                content = base64.b64encode(file.read()).decode('utf-8')
            
            return JsonResponse({
                "success": True,
                "filename": f"{file_name}.html",
                "content": content,
                "message": "Seal Info response successfully"
            })
        except Exception as e:
            logger.error(f"Error reading file: {str(e)}")
            return JsonResponse({
                "success": False,
                "filename": "",
                "content": "",
                "message": "Error processing file"
            }, status=500)