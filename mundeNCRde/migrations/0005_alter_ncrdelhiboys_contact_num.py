# Generated by Django 4.1.7 on 2023-03-25 05:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mundeNCRde", "0004_alter_ncrdelhiboys_contact_num"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ncrdelhiboys",
            name="contact_num",
            field=models.CharField(
                max_length=10,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be enetered in +9999999999, upto 10 digits allowed",
                        regex="^\\+?1?\\d{9,10}$",
                    )
                ],
                verbose_name="NCR de munde da phone number",
            ),
        ),
    ]
