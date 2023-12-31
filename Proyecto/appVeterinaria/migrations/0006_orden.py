# Generated by Django 4.2 on 2023-05-22 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appVeterinaria', '0005_alter_mascota_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id_orden', models.AutoField(primary_key=True, serialize=False)),
                ('cedula_dueño', models.CharField(max_length=10)),
                ('cedula_veterinario', models.CharField(max_length=10)),
                ('nombre_medicamento', models.CharField(max_length=50, null=True)),
                ('fecha', models.DateField(auto_now=True)),
                ('id_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appVeterinaria.mascota')),
            ],
        ),
    ]
