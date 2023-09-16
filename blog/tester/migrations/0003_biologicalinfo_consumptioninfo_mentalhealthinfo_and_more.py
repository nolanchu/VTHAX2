# Generated by Django 4.2.1 on 2023-09-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0002_healthinfo_miscinfo_mymodel_personinfo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BiologicalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sleep', models.PositiveSmallIntegerField()),
                ('sunscreen', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ConsumptionInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diet', models.CharField(choices=[('V', 'Vegetarian'), ('NV', 'Non-Vegetarian')], max_length=2)),
                ('water', models.PositiveSmallIntegerField()),
                ('bmi', models.DecimalField(decimal_places=2, max_digits=5)),
                ('smoking', models.BooleanField()),
                ('alcohol', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='MentalHealthInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friends', models.PositiveSmallIntegerField()),
                ('stress', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalActivityInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.PositiveSmallIntegerField()),
                ('desk', models.PositiveSmallIntegerField()),
                ('transportation', models.CharField(choices=[('a', 'Human-powered transport'), ('b', 'Motorized transport')], max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='HealthInfo',
        ),
        migrations.RemoveField(
            model_name='personinfo',
            name='alcohol',
        ),
        migrations.RemoveField(
            model_name='personinfo',
            name='bmi',
        ),
        migrations.RemoveField(
            model_name='personinfo',
            name='smoking',
        ),
    ]
