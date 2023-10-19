# Generated by Django 4.2.5 on 2023-10-18 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appVeterinaria', '0015_alter_factura_id_orden'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula_veterinario', models.CharField(max_length=10)),
                ('motivo', models.CharField(max_length=200)),
                ('sintomas', models.CharField(max_length=200)),
                ('diagnostico', models.CharField(max_length=500)),
                ('procedimiento', models.CharField(max_length=500)),
                ('id_orden', models.CharField(max_length=10, null=True)),
                ('nombre_medicamento', models.CharField(max_length=50, null=True)),
                ('vacunas', models.CharField(max_length=200)),
                ('alergias', models.CharField(max_length=200)),
                ('detalles', models.CharField(max_length=500)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('id_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appVeterinaria.mascota')),
            ],
        ),
    ]