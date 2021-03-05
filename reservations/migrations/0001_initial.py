# Generated by Django 3.1.4 on 2021-03-05 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=40)),
                ('email', models.EmailField(blank=True, default=None, max_length=254)),
                ('passport', models.CharField(default=None, max_length=40)),
                ('nationality', models.CharField(default=None, max_length=40)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=15)),
                ('category', models.CharField(default=None, max_length=40)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reservations.companies')),
            ],
        ),
    ]
