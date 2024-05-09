# Generated by Django 5.0.4 on 2024-05-09 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=14)),
                ('company', models.CharField(max_length=50)),
                ('company_website', models.CharField(max_length=50)),
                ('services', models.CharField(max_length=50)),
                ('describe', models.TextField(max_length=500)),
                ('term', models.BooleanField(default=False)),
            ],
        ),
    ]
