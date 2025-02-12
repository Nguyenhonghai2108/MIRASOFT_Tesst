import logging
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Account
from .serializers import AccountSerializer

# Configure logging
logger = logging.getLogger(__name__)

class AccountListCreateView(generics.ListCreateAPIView):
    """Get all accounts with pagination & create new account"""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def list(self, request, *args, **kwargs):
        logger.info("Fetching accounts with pagination")
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        try:
            logger.info("Creating a new account")
            return super().create(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error creating account: {str(e)}")
            return Response({"error": "Failed to create account"}, status=status.HTTP_400_BAD_REQUEST)

class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Get, update, and delete a specific account"""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'registerID'

    def retrieve(self, request, *args, **kwargs):
        logger.info(f"Fetching account {kwargs['registerID']}")
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        try:
            logger.info(f"Updating account {kwargs['registerID']}")
            return super().update(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error updating account: {str(e)}")
            return Response({"error": "Failed to update account"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            logger.info(f"Deleting account {kwargs['registerID']}")
            return super().destroy(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error deleting account: {str(e)}")
            return Response({"error": "Failed to delete account"}, status=status.HTTP_400_BAD_REQUEST)
