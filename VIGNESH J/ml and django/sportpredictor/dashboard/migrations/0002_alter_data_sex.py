# Generated by Django 4.2.7 on 2023-11-06 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="sex",
            field=models.PositiveIntegerField(
                choices=[(0, "Female"), (1, "Male")], max_length=10, null=True
            ),
        ),
    ]
