# Generated by Django 2.1.5 on 2019-02-20 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('stop', models.DateField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Car')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Customer')),
            ],
        ),
    ]