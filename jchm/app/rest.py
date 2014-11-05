# Serializers define the API representation.
from jchm.app.models import OrgUnit, Lang, Document, File
from rest_framework import serializers, viewsets

# Serializers define the API representation.


class OrgUnitSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = OrgUnit
        fields = ('name',)


class LangSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Lang
        fields = ('name',)


class FileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = File
        fields = ('uri', 'name', 'size', 'doc')


class DocumentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Document
        fields = ('internal_id', 'title', 'orgunit', 'group', 'description', 'lang')

# ViewSets define the view behavior.


class OrgUnitViewSet(viewsets.ModelViewSet):
    queryset = OrgUnit.objects.all()
    serializer_class = OrgUnitSerializer


class LangViewSet(viewsets.ModelViewSet):
    queryset = Lang.objects.all()
    serializer_class = LangSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
