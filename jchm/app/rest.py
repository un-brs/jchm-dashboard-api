# Serializers define the API representation.
from jchm.app.models import (
    OrgUnit, Lang, Document, File, Module, OrgUnitModule
)
from rest_framework import serializers, viewsets

# Serializers define the API representation.


class OrgUnitSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = OrgUnit
        fields = ('id','name', 'description', 'address')


class LangSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Lang
        fields = ('id', 'name')


class FileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = File
        fields = ('id', 'uri', 'name', 'size', 'doc')


class DocumentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Document
        fields = (
            'internal_id', 'title', 'orgunit', 'group', 'description', 'lang')


class ModuleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Module
        fields = ('id', 'name', 'description')


class OrgUnitModuleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = OrgUnitModule
        fields = ('id', 'module', 'orgunit', 'endpoint')

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


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class OrgUnitModuleViewSet(viewsets.ModelViewSet):
    queryset = OrgUnitModule.objects.all()
    serializer_class = OrgUnitModuleSerializer
