# Generated by Django 4.2 on 2023-05-23 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appVeterinaria', '0013_alter_orden_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='anulada',
            field=models.BooleanField(null=True),
        ),
    ]
