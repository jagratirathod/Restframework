# Generated by Django 4.0.3 on 2022-04-06 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp1', '0003_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Done', 'Done'), ('Fail', 'Fail')], default='Pending', max_length=20)),
                ('order_date', models.DateTimeField()),
                ('totalprice', models.IntegerField(default='')),
                ('order_id', models.CharField(default='', max_length=60)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
