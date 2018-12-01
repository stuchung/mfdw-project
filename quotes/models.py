from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATUS_CHOICES = (
    ('NEW', 'New Site'),
    ('EX', 'Existing Site')
)

PRIORITY_CHOICES = (
    ('U', 'Urgent - 1 week or less'),
    ('N', 'Normal - 2 to 4 weeks'),
    ('L', 'Low - Still Researching')
)

class Quote(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(blank=True, max_length=60)
    company = models.CharField(blank=True, max_length=60)
    address = models.CharField(blank=True, max_length=200)
    phone = models.CharField(blank=True, max_length=30)
    email = models.EmailField()
    web = models.URLField(blank=True)
    description = models.TextField(blank=True)
    sitestatus = models.CharField(max_length=20, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=40, choices = PRIORITY_CHOICES)
    jobfile = models.FileField(upload_to='uploads/', blank=True)
    submitted = models.DateField(auto_now_add=True)
    quotedate = models.DateField(blank=True, null=True)
    quoteprice = models.DecimalField(max_digits=7, decimal_places=2, blank=True, default=0)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
