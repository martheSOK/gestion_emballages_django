# Generated by Django 5.0.1 on 2024-03-11 16:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Depot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomdepot', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Emballage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=50, null=True)),
                ('quantite', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_fournisseur', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EchangeInterne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite_echange', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('emballage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afrikpros.emballage')),
            ],
        ),
        migrations.CreateModel(
            name='EchangeExterne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite_echange', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('emballage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afrikpros.emballage')),
                ('fournisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afrikpros.fournisseur')),
            ],
            options={
                'unique_together': {('fournisseur', 'emballage')},
            },
        ),
        migrations.AddField(
            model_name='emballage',
            name='echange_externe',
            field=models.ManyToManyField(through='afrikpros.EchangeExterne', to='afrikpros.fournisseur'),
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, null=True)),
                ('prenom', models.CharField(max_length=50, null=True)),
                ('contact', models.IntegerField(null=True)),
                ('adresse', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(max_length=50, null=True)),
                ('depot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='afrikpros.depot')),
                ('echange_interne', models.ManyToManyField(through='afrikpros.EchangeInterne', to='afrikpros.emballage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='echangeinterne',
            name='personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afrikpros.personnel'),
        ),
        migrations.AlterUniqueTogether(
            name='echangeinterne',
            unique_together={('personnel', 'emballage')},
        ),
    ]
