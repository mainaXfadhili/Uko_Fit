# Generated by Django 5.1.5 on 2025-01-29 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dimba', '0010_alter_contact_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaryEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
