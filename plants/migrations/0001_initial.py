# Generated by Django 3.1.4 on 2020-12-30 18:55

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
            name='Plants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='photos')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nursery', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
