# Generated by Django 4.0.2 on 2022-02-12 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.TextField(max_length=200, null=True)),
                ('prix', models.FloatField(null=True)),
            ],
        ),
    ]
