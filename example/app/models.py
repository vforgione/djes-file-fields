from django.db import models

from djes.models import Indexable
from djes_file_fields.fields import FileField, ImageField


class FileModel(Indexable):
    document = models.FileField()

    class Mapping(object):
        document = FileField()


class ImageModel(Indexable):
    picture = models.ImageField()

    class Mapping(object):
        picture = ImageField()
