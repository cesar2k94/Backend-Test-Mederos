# Generated by Django 3.1.5 on 2021-02-02 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='created',
            new_name='requested',
        ),
    ]