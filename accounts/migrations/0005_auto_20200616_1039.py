# Generated by Django 2.2.13 on 2020-06-16 10:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instances', '0003_auto_20200615_0637'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_auto_20200615_0637'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userinstance',
            unique_together={('user', 'instance')},
        ),
    ]