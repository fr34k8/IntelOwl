# Generated by Django 4.2.16 on 2024-12-19 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("analyzers_manager", "0141_analyzer_config_mobsf_service"),
    ]

    operations = [
        migrations.AlterField(
            model_name="analyzerreport",
            name="data_model_content_type",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                limit_choices_to={"app_label": "data_model_manager"},
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AlterField(
            model_name="analyzerreport",
            name="data_model_object_id",
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]