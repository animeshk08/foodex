# Generated by Django 2.2.6 on 2019-10-28 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20191027_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='offer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.Offer'),
        ),
    ]
