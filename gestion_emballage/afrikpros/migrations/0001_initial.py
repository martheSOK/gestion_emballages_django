# Generated by Django 4.2.9 on 2024-01-31 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Depot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Emballage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='afrikpros.depot')),
                ('echange_interne', models.ManyToManyField(to='afrikpros.emballage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='emballage',
            name='echange_externe',
            field=models.ManyToManyField(to='afrikpros.fournisseur'),
        ),
    ]