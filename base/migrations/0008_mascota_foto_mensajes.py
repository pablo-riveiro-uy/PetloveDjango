# Generated by Django 4.1.5 on 2023-01-25 01:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0007_mascota_en_adopcion_alter_mascota_extras'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(null=True, upload_to='mascotas'),
        ),
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('destinatario', models.TextField()),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]