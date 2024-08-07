# Generated by Django 4.2.8 on 2024-01-01 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0548_realmuserdefault_web_channel_default_view_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="realm",
            name="direct_message_initiator_group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="+",
                to="zerver.usergroup",
            ),
        ),
        migrations.AddField(
            model_name="realm",
            name="direct_message_permission_group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="+",
                to="zerver.usergroup",
            ),
        ),
    ]
