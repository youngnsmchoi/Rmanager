# Generated by Django 3.1.7 on 2021-03-02 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.IntegerField()),
                ('product_name', models.CharField(max_length=64)),
                ('manufacturer', models.CharField(max_length=64)),
                ('storage_location', models.CharField(max_length=64)),
                ('team_name', models.CharField(max_length=16)),
                ('quantity', models.IntegerField()),
                ('category', models.CharField(max_length=32)),
                ('safety_stock', models.IntegerField()),
                ('note', models.TextField(blank=True, null=True)),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]