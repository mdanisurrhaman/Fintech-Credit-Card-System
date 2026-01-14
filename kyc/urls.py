from django.urls import path
from .views import KYCSubmitAPIView, KYCDetailAPIView
from .views import(
    AdminPendingKYCAPIView,
    AdminVerifyKYCAPIView,
    AdminRejectionKYCAPIView,
)

urlpatterns = [
    path('submit/', KYCSubmitAPIView.as_view(), name='kyc-submit'),
    path('detail/', KYCDetailAPIView.as_view(), name='kyc-detail'),

    path("admin/kyc/pending/", AdminPendingKYCAPIView.as_view()),
    path("admin/kyc/verify/<int:kyc_id>/", AdminVerifyKYCAPIView.as_view()),
    path("admin/kyc/reject/<int:kyc_id>/", AdminRejectionKYCAPIView.as_view()),
]

