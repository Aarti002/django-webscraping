# Generated by Django 3.2.4 on 2021-11-20 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoapp', '0007_auto_20211120_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribedusers',
            name='yes_no',
            field=models.BooleanField(default=False, null=True),
        ),
    ]