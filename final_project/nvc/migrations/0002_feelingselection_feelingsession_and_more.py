# Generated by Django 4.1.7 on 2023-03-24 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("nvc", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FeelingSelection",
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
            ],
        ),
        migrations.CreateModel(
            name="FeelingSession",
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
                ("session_datetime", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="feeling",
            name="datetime",
        ),
        migrations.RemoveField(
            model_name="feeling",
            name="feeling_options",
        ),
        migrations.RemoveField(
            model_name="feeling",
            name="user",
        ),
        migrations.AddField(
            model_name="feeling",
            name="name",
            field=models.CharField(default="sad", max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="feeling",
            name="when_needs_met",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="feeling",
            name="when_needs_not_met",
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name="FeelingOption",
        ),
        migrations.AddField(
            model_name="feelingselection",
            name="feeling",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="nvc.feeling"
            ),
        ),
        migrations.AddField(
            model_name="feelingselection",
            name="feeling_session",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="nvc.feelingsession"
            ),
        ),
    ]