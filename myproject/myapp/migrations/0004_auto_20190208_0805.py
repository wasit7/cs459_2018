# Generated by Django 2.1.5 on 2019-02-08 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190207_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='supplier',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
    ]
