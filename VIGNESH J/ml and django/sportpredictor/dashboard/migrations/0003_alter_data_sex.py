# Generated by Django 4.2.7 on 2023-11-06 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0002_alter_data_sex"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="sex",
            field=models.PositiveIntegerField(
                choices=[(0, "Female"), (1, "Male")], null=True
            ),
        ),
    ]
