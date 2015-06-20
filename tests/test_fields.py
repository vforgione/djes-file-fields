import os

from django.conf import settings
from django.core.files import File
from django.core.files.images import ImageFile
from example.app.models import ImageModel, FileModel
import pytest


files_dir = os.path.join(os.path.dirname(__file__), "test_files")


def clean_out_media_dir():
    for filename in os.listdir(settings.MEDIA_ROOT):
        if filename != ".gitkeep":
            os.remove(os.path.join(settings.MEDIA_ROOT, filename))


@pytest.mark.django_db
def test_image_field():
    instance = ImageModel()
    instance.picture = ImageFile(open(os.path.join(files_dir, "test.jpg"), "rb"))
    instance.save()
    assert instance.to_dict() == {
        "id": 1,
        "picture": "./test.jpg"
    }
    clean_out_media_dir()


@pytest.mark.django_db
def test_file_field():
    instance = FileModel()
    instance.document = File(open(os.path.join(files_dir, "test.txt")))
    instance.save()
    assert instance.to_dict() == {
        "id": 1,
        "document": "./test.txt"
    }
    clean_out_media_dir()
