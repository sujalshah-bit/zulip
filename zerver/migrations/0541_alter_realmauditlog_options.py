# Generated by Django 5.0.6 on 2024-06-27 00:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0540_remove_realm_create_private_stream_policy"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="realmauditlog",
            options={"ordering": ["id"]},
        ),
    ]
