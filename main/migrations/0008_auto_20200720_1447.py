# Generated by Django 3.0.7 on 2020-07-20 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200714_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_reverse', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
