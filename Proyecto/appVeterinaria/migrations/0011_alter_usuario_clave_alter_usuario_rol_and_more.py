# Generated by Django 4.2 on 2023-05-22 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appVeterinaria', '0010_rename_cedula_orden_factura_id_orden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='clave',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
