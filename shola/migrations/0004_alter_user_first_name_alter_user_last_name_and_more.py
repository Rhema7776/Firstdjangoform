# Generated by Django 4.0.6 on 2022-07-14 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shola', '0003_alter_user_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='First_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Last_name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='des',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
