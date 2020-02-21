from modelcluster.fields import ParentalKey
from django.db import models
from django.utils.functional import cached_property
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.core.models import Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from common.utils import ForeignKeyField, WagtailImageField


class BaseRelatedPageItem(models.Model):
    class Meta:
        abstract = True

    page = ForeignKeyField(
        model='wagtailcore.Page',
        required=True,
        on_delete=models.CASCADE,
        help_text='Page link for the item'
    )


class BaseRelatedItem(BaseRelatedPageItem):
    class Meta:
        abstract = True

    title = models.CharField(
        max_length=255,
        help_text='Title for the item',
    )
    description = models.CharField(
        max_length=255,
        help_text='Description for the item',
    )
    image = WagtailImageField(
        required=True,
        help_text='Image for the item'
    )


class GettingStartedItem(BaseRelatedItem):
    class Meta:
        abstract = True

    link_label = models.CharField(
        max_length=255,
        help_text='Link label for the item',
    )


class GettingStartedItems(Orderable, GettingStartedItem):
    item = ParentalKey('HomePage', related_name='getting_started_items')

    title_required = True

    translation_fields = [
        'title',
        'description',
        'link_label',
    ]

    panels = [
        PageChooserPanel('page'),
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('link_label'),
    ]


class BaseRelatedOptionalItem(BaseRelatedPageItem):
    class Meta:
        abstract = True

    title = models.CharField(
        max_length=255,
        blank=True,
        help_text='Optional: title for the item. Defaults to the selected page title if left blank',
    )
    description = models.CharField(
        max_length=255,
        blank=True,
        help_text='Optional: description for the item. Defaults to the selected page excerpt if left blank',
    )

    @cached_property
    def get_title(self):
        title = self.title
        if not title:
            title = self.page.specific.heading

        return title

    @cached_property
    def get_description(self):
        description = self.description
        if not description:
            description = getattr(self.page.specific, 'excerpt', None)

        return description


class IATIInActionFeaturedItem(BaseRelatedOptionalItem):
    class Meta:
        abstract = True

    image = WagtailImageField(
        required=False,
        help_text='Optional: image for the item. Defaults to the selected page image if left blank'
    )
    quote = models.CharField(
        max_length=255,
        blank=True,
        help_text='Optional: quote for the item',
    )
    quotee = models.CharField(
        max_length=255,
        blank=True,
        help_text='Optional: the source of the quote',
    )

    @cached_property
    def get_image(self):
        image = self.image
        if not image:
            image = getattr(self.page.specific, 'feed_image', None)
        if not image:
            image = getattr(self.page.specific, 'header_image', None)

        return image


class IATIInActionFeaturedItems(Orderable, IATIInActionFeaturedItem):
    item = ParentalKey('HomePage', related_name='iati_in_action_featured_item')

    translation_fields = [
        'title',
        'description',
        'quote',
        'quotee',
    ]

    panels = [
        PageChooserPanel('page'),
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('quote'),
        FieldPanel('quotee'),
    ]


class IATIInActionItems(Orderable, BaseRelatedOptionalItem):
    item = ParentalKey('HomePage', related_name='iati_in_action_items')

    translation_fields = [
        'title',
        'description',
    ]

    panels = [
        PageChooserPanel('page'),
        FieldPanel('title'),
        FieldPanel('description'),
    ]


class IATIToolsItems(Orderable, BaseRelatedPageItem):
    item = ParentalKey('HomePage', related_name='iati_tools_items')

    panels = [
        PageChooserPanel('page'),
    ]