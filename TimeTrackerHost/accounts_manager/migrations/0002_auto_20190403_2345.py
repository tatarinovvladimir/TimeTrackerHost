# Generated by Django 2.1.5 on 2019-04-03 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Custom_User',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]