# Generated by Django 3.2.4 on 2021-11-20 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribedusers',
            name='yes_no',
            field=models.BooleanField(default=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='subscribedusers',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
