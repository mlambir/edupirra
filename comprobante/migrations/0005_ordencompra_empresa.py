# Generated by Django 2.2.9 on 2022-07-15 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0006_auto_20220715_1728'),
        ('comprobante', '0004_comprobante_data_arreglada'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordencompra',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empresa.Empresa'),
        ),
    ]
