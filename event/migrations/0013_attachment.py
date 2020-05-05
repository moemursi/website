# Generated by Django 2.2.10 on 2020-05-05 18:27

from django.db import migrations, models
import django.db.models.deletion
import event.enums
import uuid


class Migration(migrations.Migration):

    dependencies = [("event", "0012_registration_status")]

    operations = [
        migrations.CreateModel(
            name="Attachment",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "type",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "SLIDES"), (1, "FILE"), (2, "IMAGE")],
                        default=event.enums.AttachmentType(0),
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        blank=True, null=True, upload_to="event/attachment/"
                    ),
                ),
                (
                    "external_url",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "DRAFT"), (1, "PUBLISHED"), (2, "DELETED")],
                        default=event.enums.AttachmentStatus(0),
                    ),
                ),
                ("registration_required", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="attachments",
                        to="event.Session",
                    ),
                ),
            ],
        )
    ]
