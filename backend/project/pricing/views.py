from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from .models import PricingConfiguration
from .serializers import PricingConfigurationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PricingConfigurationViewSet(ListAPIView):
    queryset = PricingConfiguration.objects.all()
    serializer_class = PricingConfigurationSerializer


@api_view(["POST"])
def CreatePricingConfiguration(request):
    if request.method == "POST":
        serializer = PricingConfigurationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
