# Generated by Django 3.0 on 2021-06-26 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0072_auto_20210618_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='add_green_card_id',
            field=models.CharField(blank=True, max_length=70, null=True, verbose_name='ID дополнительной зеленой карточки'),
        ),
    ]
