# Generated by Django 4.2.4 on 2023-08-19 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_aluno_celular'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
