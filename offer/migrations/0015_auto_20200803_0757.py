# Generated by Django 3.0.7 on 2020-08-03 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0014_auto_20200803_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyform',
            name='user_who_applied',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]