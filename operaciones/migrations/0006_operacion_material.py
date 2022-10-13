# Generated by Django 3.2.3 on 2021-06-02 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0002_auto_20210602_0204'),
        ('operaciones', '0005_alter_operacion_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='operacion',
            name='material',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to='materiales.material',
                verbose_name='Material'),
            preserve_default=False,
        ),
    ]