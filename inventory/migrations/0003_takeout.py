# Generated by Django 3.1.7 on 2021-03-02 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0002_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Takeout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carry_day', models.DateField()),
                ('carry_team', models.CharField(max_length=16)),
                ('receive_company', models.CharField(max_length=32)),
                ('receive_tel', models.CharField(max_length=16)),
                ('receive_user', models.CharField(max_length=16)),
                ('material_name', models.CharField(max_length=64)),
                ('material_info', models.CharField(max_length=64)),
                ('purpose', models.CharField(max_length=64)),
                ('pack_date', models.DateField()),
                ('production_capacity', models.CharField(max_length=32)),
                ('carry_capacity', models.CharField(max_length=32)),
                ('residual_quantity', models.CharField(max_length=32)),
                ('delivery', models.CharField(max_length=16)),
                ('note', models.TextField(blank=True, null=True)),
                ('modify_date', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]