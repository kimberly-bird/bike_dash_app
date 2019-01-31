# Generated by Django 2.1.5 on 2019-01-31 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=4)),
                ('description', models.CharField(max_length=255)),
                ('purchase_price', models.PositiveIntegerField()),
                ('purchase_date', models.CharField(max_length=255)),
                ('list_price', models.PositiveIntegerField(null=True)),
                ('sale_price', models.PositiveIntegerField(null=True)),
                ('sale_date', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BikeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Labor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(max_length=55)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.PositiveIntegerField()),
                ('rate_of_pay', models.PositiveIntegerField()),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bikes.Bike')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('notes', models.CharField(max_length=255)),
                ('purchase_price', models.PositiveIntegerField()),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bikes.Bike')),
                ('bikemodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bikes.BikeModel')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bikes.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='bikemodel',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bikes.Brand'),
        ),
        migrations.AddField(
            model_name='bike',
            name='bikemodel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bikes.BikeModel'),
        ),
        migrations.AddField(
            model_name='bike',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bikes.Brand'),
        ),
        migrations.AddField(
            model_name='bike',
            name='condition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bikes.Condition'),
        ),
        migrations.AddField(
            model_name='bike',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bikes.Status'),
        ),
        migrations.AddField(
            model_name='bike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
