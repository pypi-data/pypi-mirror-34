import os
import uuid
import functools

from django.conf.locale import LANG_INFO
from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.core.files.base import ContentFile
from django.conf import settings

from taggit.models import TaggedItemBase
from taggit.managers import TaggableManager

from .storage import OverwriteStorage
from .settings import (
    FILINGCABINET_DOCUMENT_MODEL,
    FILINGCABINET_DOCUMENTCOLLECTION_MODEL
)
from .pdf_utils import PDFProcessor, crop_image


class DocumentManager(models.Manager):
    def create_pages_from_pdf(self, doc):
        config = {
            'TESSERACT_DATA_PATH': settings.TESSERACT_DATA_PATH
        }

        if doc.original:
            pdf_file = doc.original
        elif doc.pdf_file:
            pdf_file = doc.pdf_file

        pdf = PDFProcessor(pdf_file.path, language=doc.language, config=config)

        doc.num_pages = pdf.num_pages
        doc.save()

        page_generator = zip(pdf.get_images(), pdf.get_text())
        for page_no, (img, text) in enumerate(page_generator, 1):
            page, created = Page.objects.update_or_create(
                document=doc,
                number=page_no,
                defaults={'content': text}
            )

            page.image.save(
                'page.gif',
                ContentFile(img.make_blob('gif')),
                save=False
            )
            for size_name, width in Page.SIZES:
                img.transform(resize='{}x'.format(width))
                getattr(page, 'image_%s' % size_name).save(
                    'page.gif',
                    ContentFile(img.make_blob('gif')),
                    save=False
                )
            page.save()


def get_document_path(instance, filename):
    # UUID field is already filled
    hex_name = instance.uid.hex
    hex_name_02 = hex_name[:2]
    hex_name_24 = hex_name[2:4]
    hex_name_46 = hex_name[4:6]
    name, ext = os.path.splitext(filename)
    slug = slugify(name)
    return os.path.join('docs', hex_name_02, hex_name_24,
                        hex_name_46, hex_name, slug + ext)


def get_page_image_filename(prefix, page_no, size_name=None, filetype='gif'):
    return '{prefix}-p{page}-{size}.{filetype}'.format(
        prefix=prefix,
        size=size_name,
        page=page_no,
        filetype=filetype
    )


class TaggedDocument(TaggedItemBase):
    content_object = models.ForeignKey(
        FILINGCABINET_DOCUMENT_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('Document Tag')
        verbose_name_plural = _('Document Tags')


@python_2_unicode_compatible
class AbstractDocument(models.Model):
    LANGUAGE_CHOICES = [(k, LANG_INFO[k]['name']) for k in LANG_INFO
                        if 'name' in LANG_INFO[k]]

    uid = models.UUIDField(default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=500, default='', blank=True)
    slug = models.SlugField(max_length=250, blank=True)
    description = models.TextField(default='', blank=True)

    pdf_file = models.FileField(
        max_length=255,
        storage=OverwriteStorage(),
        upload_to=get_document_path, blank=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True,
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s',
        verbose_name=_("User")
    )

    created_at = models.DateTimeField(default=timezone.now, null=True)
    updated_at = models.DateTimeField(default=timezone.now, null=True)

    num_pages = models.PositiveIntegerField(default=0)

    language = models.CharField(max_length=10, blank=True,
                                default=settings.LANGUAGE_CODE,
                                choices=settings.LANGUAGES)

    public = models.BooleanField(default=False)
    tags = TaggableManager(
        through=TaggedDocument, blank=True,
        related_name='+'
    )

    objects = DocumentManager()

    class Meta:
        verbose_name = _('document')
        verbose_name_plural = _('documents')
        abstract = True

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.slug:
            return reverse('document-detail', kwargs={
                'pk': self.pk,
                'slug': self.slug
            })
        return reverse('document-detail_short', kwargs={
            'pk': self.pk
        })

    @property
    def has_original(self):
        if not hasattr(self, 'original_id'):
            return False
        if not self.original_id:
            return False
        return True

    def get_file_path(self):
        if self.pdf_file:
            return self.pdf_file.path
        if self.has_original:
            return self.original.get_file_path()
        return ''

    def get_file_url(self):
        if self.pdf_file:
            return self.pdf_file.url
        if self.has_original:
            return self.original.get_file_url()
        return ''

    def get_page_image_url_template(self):
        doc_path = get_document_path(self, 'page.gif')
        path, _ = os.path.splitext(doc_path)
        return get_page_image_filename(
            path, '{page}', size_name='{size}'
        )


class Document(AbstractDocument):
    class Meta(AbstractDocument.Meta):
        swappable = 'FILINGCABINET_DOCUMENT_MODEL'


def get_page_filename(instance, filename, size=''):
    doc_path = get_document_path(instance.document, 'page.gif')
    path, ext = os.path.splitext(doc_path)
    return get_page_image_filename(path, instance.number, size_name=size)


@python_2_unicode_compatible
class Page(models.Model):
    SIZES = (
        # Wide in px
        ('large', 1000),
        ('normal', 700),
        ('small', 180)
    )

    UPLOAD_FUNCS = {
        size[0]: functools.partial(get_page_filename, size=size[0])
        for size in SIZES
    }

    document = models.ForeignKey(
        FILINGCABINET_DOCUMENT_MODEL,
        on_delete=models.CASCADE
    )
    number = models.IntegerField(default=1)

    content = models.TextField(blank=True)
    image = models.ImageField(
        max_length=255,
        storage=OverwriteStorage(),
        upload_to=functools.partial(get_page_filename, size='original'))
    image_large = models.ImageField(
        max_length=255,
        storage=OverwriteStorage(),
        upload_to=UPLOAD_FUNCS['large'])
    image_normal = models.ImageField(
        max_length=255,
        storage=OverwriteStorage(),
        upload_to=UPLOAD_FUNCS['normal'])
    image_small = models.ImageField(
        max_length=255,
        storage=OverwriteStorage(),
        upload_to=UPLOAD_FUNCS['small'])

    class Meta:
        ordering = ('number',)

    def __str__(self):
        return '%s - %s' % (self.document, self.number)


def get_page_annotation_filename(instance, filename):
    # UUID field is already filled
    filename = instance.page.image.name
    base_name, _ = os.path.splitext(filename)
    return '%s-annotation-%s.gif' % (
        base_name,
        instance.pk
    )


@python_2_unicode_compatible
class PageAnnotation(models.Model):
    page = models.ForeignKey(
        Page, null=True, on_delete=models.SET_NULL
    )

    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True,
        related_name='%(app_label)s_%(class)s',
        on_delete=models.SET_NULL,
        verbose_name=_("User")
    )

    top = models.IntegerField(null=True, blank=True)
    left = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to=get_page_annotation_filename,
                              storage=OverwriteStorage(),
                              max_length=255, blank=True)

    def __str__(self):
        return '%s (%s)' % (self.title, self.page)

    def save(self, *args, **kwargs):
        image_cropped = kwargs.pop('image_cropped', False)
        res = super(PageAnnotation, self).save(*args, **kwargs)
        if not image_cropped and self.valid_rect():
            image_bytes = crop_image(
                self.page.image.path,
                self.left, self.top, self.width, self.height
            )
            self.image.save(
                'page_annotation.gif',
                ContentFile(image_bytes),
                save=False
            )
            return self.save(image_cropped=True)
        return res

    def valid_rect(self):
        return (self.left is not None and
                self.top is not None and
                self.width is not None and
                self.height is not None)


class CollectionDocument(models.Model):
    collection = models.ForeignKey(
        FILINGCABINET_DOCUMENTCOLLECTION_MODEL,
        related_name='%(app_label)s_%(class)s',
        on_delete=models.CASCADE
    )
    document = models.ForeignKey(
        FILINGCABINET_DOCUMENT_MODEL,
        related_name='%(app_label)s_%(class)s',
        on_delete=models.CASCADE
    )


class AbstractDocumentCollection(models.Model):
    slug = models.SlugField(max_length=250, blank=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    public = models.BooleanField(default=True)

    documents = models.ManyToManyField(
        FILINGCABINET_DOCUMENT_MODEL,
        related_name='%(app_label)s_%(class)s',
        blank=True,
        through=CollectionDocument,
        through_fields=('collection', 'document')
    )

    class Meta:
        abstract = True


class DocumentCollection(AbstractDocumentCollection):
    class Meta(AbstractDocumentCollection.Meta):
        swappable = 'FILINGCABINET_DOCUMENTCOLLECTION_MODEL'
