# Generated by Django 4.1.2 on 2023-10-29 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0002_populate_locales"),
    ]

    operations = [
        migrations.CreateModel(
            name="Community",
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
                ("name", models.CharField(default="", max_length=120, unique=True)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="ConsumerGroup",
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
                ("name", models.CharField(default="", max_length=120, unique=True)),
                ("description", models.TextField()),
                ("communities", models.ManyToManyField(to="users.community")),
            ],
        ),
        migrations.CreateModel(
            name="ProducerGroup",
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
                ("name", models.CharField(default="", max_length=120, unique=True)),
                ("description", models.TextField()),
                ("communities", models.ManyToManyField(to="users.community")),
            ],
        ),
        migrations.AlterField(
            model_name="pendinguser",
            name="email_token",
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name="recoverpassword",
            name="email_token",
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="locale",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.supportedlocales",
            ),
        ),
        migrations.CreateModel(
            name="UserProducerInvitations",
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
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.producergroup",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserConsumerInvitations",
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
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.consumergroup",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProducerGroupCommunityInvitation",
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
                (
                    "community",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.community",
                    ),
                ),
                (
                    "producer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.producergroup",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ConsumerGroupCommunityInvitation",
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
                (
                    "community",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.community",
                    ),
                ),
                (
                    "consumer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.consumergroup",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="userprofile",
            name="groups",
            field=models.ManyToManyField(to="users.consumergroup"),
        ),
    ]
