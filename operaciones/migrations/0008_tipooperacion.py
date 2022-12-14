# Generated by Django 3.2.13 on 2022-10-13 15:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operaciones', '0007_alter_operacion_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoOperacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Precio Unitario')),
            ],
        ),
    ]
