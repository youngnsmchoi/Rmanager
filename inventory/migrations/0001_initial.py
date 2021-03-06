# Generated by Django 3.1.7 on 2021-03-02 05:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=128)),
                ('purity', models.CharField(max_length=32)),
                ('quantity', models.IntegerField()),
                ('residual_quantity', models.IntegerField()),
                ('manufacturer', models.CharField(max_length=32)),
                ('storage_location', models.CharField(max_length=32)),
                ('category', models.CharField(max_length=32)),
                ('partname', models.CharField(max_length=32)),
                ('division', models.CharField(max_length=32)),
                ('registration_date', models.DateField()),
                ('xpiration_date', models.DateField()),
                ('comment', models.CharField(blank=True, max_length=128, null=True)),
                ('msds', models.FileField(blank=True, null=True, upload_to='')),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
