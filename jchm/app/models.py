from django.db import models


class OrgUnit(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Obj(models.Model):
    internal_id = models.CharField(max_length=16, unique=True)
    orgunit = models.ForeignKey(OrgUnit)

    def __str__(self):
        return "%s - %s" % (self.orgunit, self.internal_id)

    class Meta:
        abstract = True


class Lang(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Document(Obj):
    group = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=255, unique=True)
    lang = models.ForeignKey(Lang)

    def __str__(self):
        return "title=%s; group=%s; orgunit=%s; lang=%s" % (
            self.title, self.group, self.orgunit.name, self.lang.name
        )


class File(models.Model):
    uri = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    size = models.IntegerField()
    doc = models.ForeignKey(Document)

    def __str__(self):
        return "name=%s; size=%d; doc=%s" % (
            self.name, self.size, self.doc.title
        )
