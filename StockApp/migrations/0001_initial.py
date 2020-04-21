# Generated by Django 3.0.3 on 2020-04-21 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Ready to Purchase'), ('SOLD', 'Item Sold'), ('RESTOCKING', 'Under Restocking')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No Issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Ready to Purchase'), ('SOLD', 'Item Sold'), ('RESTOCKING', 'Under Restocking')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No Issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Ready to Purchase'), ('SOLD', 'Item Sold'), ('RESTOCKING', 'Under Restocking')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No Issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
