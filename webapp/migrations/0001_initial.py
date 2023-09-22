# Generated by Django 4.2.5 on 2023-09-22 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=225)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=350)),
                ('cpf', models.CharField(max_length=225)),
                ('state', models.CharField(max_length=225)),
                ('position', models.CharField(max_length=225)),
            ],
        ),
    ]