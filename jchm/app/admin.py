from django.contrib import admin
from jchm.app.models import OrgUnit, Lang, Document, File


class OrgUnitAdmin(admin.ModelAdmin):
    pass


class LangAdmin(admin.ModelAdmin):
    pass


class FileAdmin(admin.ModelAdmin):
    pass


class DocumentAdmin(admin.ModelAdmin):
    pass

admin.site.register(OrgUnit, OrgUnitAdmin)
admin.site.register(Lang, LangAdmin)
admin.site.register(Document, FileAdmin)
admin.site.register(File, DocumentAdmin)
