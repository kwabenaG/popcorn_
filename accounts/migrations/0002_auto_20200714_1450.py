# Generated by Django 3.0.7 on 2020-07-14 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='program',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
