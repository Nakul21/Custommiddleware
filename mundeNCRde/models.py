from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class NCRdelhiBoys(models.Model):
    user_name=models.CharField("NCR de munde da naam",max_length=30)
    phone_val = RegexValidator(regex=r'^\+?1?\d{9,10}$', message='Phone number must be enetered in +9999999999, upto 10 digits allowed')
    contact_num=models.CharField("NCR de munde da phone number", max_length=10, unique=True)
    created_date=models.DateTimeField(auto_created=True,auto_now_add=True)

    def __repr__(self):
        return self.user_name

