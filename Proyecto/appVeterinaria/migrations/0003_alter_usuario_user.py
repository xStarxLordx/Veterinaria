# Generated by Django 4.2 on 2023-05-18 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appVeterinaria', '0002_alter_usuario_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='user',
            field=models.CharField(max_length=20),
        ),
    ]
