from django.db import models
from django.conf import settings

user = settings.AUTH_USER_MODEL

# Create your models here.
class KYC(models.Model):

    KYC_STATUS=(
    ('PENDING', 'Pending'),
    ('VERIFIED', 'Verified'),
    ('REJECTED', 'Rejected'),

    )

    user = models.OneToOneField(user, on_delete=models.CASCADE, related_name='kyc')

    aadhaar_number = models.CharField(max_length=12)
    pan_number = models.CharField(max_length=10)

    date_of_birth = models.DateField()
    address = models.TextField()

    status = models.CharField(max_length=10, choices=KYC_STATUS, default='PENDING')

    rejection_reason = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.status}"
