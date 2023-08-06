from django.contrib import admin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .models import Page
from .tasks import process_document


class PageInline(admin.StackedInline):
    model = Page
    raw_id_fields = ('document',)


class DocumentBaseAdmin(admin.ModelAdmin):
    inlines = [PageInline]
    save_on_top = True
    list_display = ('title', 'created_at', 'num_pages', 'public')
    raw_id_fields = ('user',)
    readonly_fields = ('uid',)
    prepopulated_fields = {'slug': ('title',)}
    actions = ('reprocess_document',)

    def save_model(self, request, doc, form, change):
        doc.updated_at = timezone.now()
        super(DocumentBaseAdmin, self).save_model(
            request, doc, form, change)
        if not change:
            process_document.delay(doc.pk)

    def reprocess_document(self, request, queryset):
        for instance in queryset:
            process_document.delay(instance.pk)
        self.message_user(request, _("Started reprocessing documents."))
    reprocess_document.short_description = _("Reprocess document")


class PageAdmin(admin.ModelAdmin):
    raw_id_fields = ('document',)


class PageAnnotationAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'page',)


# Register them yourself
# admin.site.register(Document, DocumentAdmin)
# admin.site.register(Page)
