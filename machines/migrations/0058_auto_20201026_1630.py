# Generated by Django 3.0 on 2020-10-26 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0057_auto_20201026_1624'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Operator_reason',
            new_name='Repairer_master_reason',
        ),
        migrations.RenameField(
            model_name='repair_rawdata',
            old_name='operator_reason',
            new_name='repairer_master_reason',
        ),
    ]
