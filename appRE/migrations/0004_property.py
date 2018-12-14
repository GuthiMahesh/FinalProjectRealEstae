# Generated by Django 2.1.1 on 2018-12-14 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appRE', '0003_auto_20181214_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_Name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('contact_number', models.IntegerField()),
                ('pincode', models.IntegerField()),
            ],
        ),
    ]