# Generated by Django 4.1.7 on 2023-03-27 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("nvc", "0002_feelingselection_feelingsession_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="FeelingGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="feeling",
            name="group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="nvc.feelinggroup",
            ),
        ),
    ]
