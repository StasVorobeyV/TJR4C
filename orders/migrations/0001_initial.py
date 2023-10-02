# Generated by Django 4.2.5 on 2023-10-01 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('robots', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=10)),
                ('quantity', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('robot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robots.robot')),
            ],
        ),
    ]
