# Generated by Django 2.2.1 on 2021-06-15 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0070_auto_20210519_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='main_channel',
            field=models.CharField(blank=True, choices=[('AD0', 'AD0'), ("AD0'", "AD0'"), ('AD1', 'AD1'), ("AD1'", "AD1'")], max_length=5, null=True, verbose_name='Канал'),
        ),
    ]