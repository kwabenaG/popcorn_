# Generated by Django 3.0.7 on 2020-08-03 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0011_offers_user_interested'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyform',
            name='offer_selected_by_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='offer_selected', related_query_name='offer_selected', to='offer.Offers'),
        ),
    ]
