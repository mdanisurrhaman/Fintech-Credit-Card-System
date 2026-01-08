from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response   
from rest_framework import status              

from .models import KYC
from .serializers import KYCSerializer
from .permissions import IsAdminUserCustom


# Create your views here.
class KYCSubmitAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if hasattr(request.user, 'kyc'):
            return Response(
                {"error": "KYC already submitted"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = KYCSerializer(data=request.data)  # ✅ FIX HERE

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {"message": "KYC submitted successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    


class KYCDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            kyc = request.user.kyc
            serializer = KYCSerializer(kyc)
            return Response(serializer.data)
        except KYC.DoesNotExist:
            return Response(
                {"error": "KYC not submitted"},
                status=status.HTTP_404_NOT_FOUND
            )
   



class AdminPendingKYCAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUserCustom]

    def get(self, request):
        kycs = KYC.objects.filter(status="PENDING")
        serializer = KYCSerializer(kycs, many=True)
        return Response(serializer.data)


class AdminVerifyKYCAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUserCustom ]

    def patch(self, request, kyc_id):
        try:
            kyc = KYC.objects.get(id=kyc_id)
        except KYC.DoesNotExist:
            return Response({"error":"KYC not found"},status=404)
            
        kyc.status = "VERIFIED"
        kyc.rejection_reason = None
        kyc.save()

        return Response({"massage":"KYC verified succesfully"})



class AdminRejectionKYCAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUserCustom]

    def patch(self, request, kyc_id):
        reason = request.data.get("rejection_reason")

        if not reason:
            return Response(
                {"error":"Rejection reason required"},
                status=400
            )
        try:
            kyc = KYC.objects.get(id=kyc_id)
        except KYC.DoesNotExist:
            return Response({"error":"KYC not found"},status=404)

        kyc.status = "REJECTED"
        kyc.rejection_reason = reason
        kyc.save()

        return Response({"massage":"KYC rejected successfully"})    