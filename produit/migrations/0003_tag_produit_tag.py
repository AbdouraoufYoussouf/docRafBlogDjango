# Generated by Django 4.0.2 on 2022-02-14 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0002_alter_produit_nom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='tag',
            field=models.ManyToManyField(to='produit.Tag'),
        ),
    ]
