# Generated by Django 4.0.6 on 2022-07-14 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shola', '0005_alter_user_first_name_alter_user_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='', max_length=11),
        ),
    ]
