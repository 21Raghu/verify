# Generated by Django 3.0.8 on 2020-07-27 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verify_app', '0002_remove_user_emp_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_emp',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]