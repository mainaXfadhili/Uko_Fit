# Generated by Django 5.0.2 on 2024-12-12 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dimba', '0005_remove_turf_opening_hours_group_level_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='level',
        ),
        migrations.RemoveField(
            model_name='group',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default='General Inquiry', max_length=200),
        ),
        migrations.AlterField(
            model_name='group',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='group_images/'),
        ),
        migrations.AlterModelTable(
            name='contact',
            table='contact',
        ),
    ]
