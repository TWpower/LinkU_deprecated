# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
from django.db import migrations
import datetime


def forwards_func(apps, schema_editor):
    Meeting = apps.get_model("moim", "Meeting")
    db_alias = schema_editor.connection.alias
    Meeting.objects.using(db_alias).bulk_create([
        Meeting(maker="장선혁", name="규카츠 먹을래?", place="강남", start_time=datetime.datetime(2017, 2, 22, 21, 52, 7, 777885),
                image_path="", distance_near_univ="고려대학교 10km 이내", price_range="5,000원~10,000원"),
        Meeting(maker="최지훈", name="호타루에서 우동 먹을래?", place="이대", start_time=datetime.datetime(2017, 2, 22, 22, 22, 2, 22),
                image_path="", distance_near_univ="이화여자대학교 10km 이내", price_range="5,000원~10,000원"),
    ])

    RunPythonExample = apps.get_model("moim", "RunPythonExample")
    # (app_name, 해당 앱에서 model class명)
    db_alias = schema_editor.connection.alias
    RunPythonExample.objects.using(db_alias).bulk_create([
        RunPythonExample(test_name="test_name_one", test_text="test_text_one"),
        RunPythonExample(test_name="test_name_two", test_text="test_text_two"),
    ])


def reverse_func(apps, schema_editor):
    Meeting = apps.get_model("moim", "Meeting")
    db_alias = schema_editor.connection.alias
    Meeting.objects.using(db_alias).filter(name="규카츠 먹을래?").delete()
    Meeting.objects.using(db_alias).filter(name="우동 먹을래?").delete()

    RunPythonExample = apps.get_model("moim", "RunPythonExample")
    db_alias = schema_editor.connection.alias
    RunPythonExample.objects.using(db_alias).filter(test_name="test_name_one").delete()
    RunPythonExample.objects.using(db_alias).filter(test_name="test_name_two").delete()


class Migration(migrations.Migration):

    dependencies = [
        ('moim', '0002_auto_20170219_0812'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
