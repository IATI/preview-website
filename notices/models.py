from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.html import strip_tags
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.snippets.models import register_snippet
from common.utils import ForeignKeyField
from dashboard.edit_handlers import MultiFieldPanel
from notices.edit_handlers import DisplayTypeFieldPanel

NOTICE_TYPES = [
    ('notice', 'Notice (blue)'),
    ('alert', 'Alert (yellow)'),
    ('warning', 'Warning (red)'),
]

DISPLAY_LOCATIONS = [
    ('all', 'All pages in site'),
    ('selected_page', 'Selected page only'),
    ('selected_page_and_children', 'Selected page and child pages'),
    ('children_only', 'Children of selected page'),
]


class AbstractNotice(models.Model):
    """Abstract class for a notice."""

    class Meta:
        abstract = True

    notice_type = models.CharField(
        max_length=255,
        choices=NOTICE_TYPES,
        default=NOTICE_TYPES[0][0]
    )
    content = RichTextField(
        help_text='Content for the notice',
        features=['h2', 'link', 'bold'],
    )

    translation_fields = [
        'content',
    ]

    def __str__(self):
        """Get a string representation of the snippet, the content."""
        return strip_tags(self.content.replace('</', ' </'))


@register_snippet
class GlobalNotice(AbstractNotice):
    """A snippet class for global notices."""

    class Meta:
        verbose_name_plural = 'Global notice'

    panels = [
        FieldPanel('content'),
        FieldPanel(
            'notice_type',
            widget=forms.RadioSelect,
            classname='non-floated-options',
        ),
    ]

    def clean(self):
        """Make sure that no more than one instance of a given model is created."""
        model = self.__class__
        if (model.objects.count() > 0 and self.id != model.objects.get().id):
            raise ValidationError("Can only create 1 %s instance." % model._meta.verbose_name)
        super().clean()

    def has_add_permission(self, request):
        """Hide the "Add" button when there is already an instance."""
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        return super().has_add_permission(request)


@register_snippet
class PageNotice(AbstractNotice):
    """A snippet class for page notices."""

    allow_dismiss = models.BooleanField(
        default=False,
        blank=True,
    )
    display_location = models.CharField(
        max_length=255,
        choices=DISPLAY_LOCATIONS,
        default=DISPLAY_LOCATIONS[1][0]
    )
    page = ForeignKeyField(
        model='wagtailcore.Page',
        required=False,
        on_delete=models.CASCADE,
    )

    panels = [
        FieldPanel('content'),
        FieldPanel(
            'notice_type',
            widget=forms.RadioSelect,
            classname='non-floated-options',
        ),
        MultiFieldPanel(
            [
                FieldPanel('allow_dismiss'),
            ],
            heading='Allow dismiss',
            description='Select to allow visitors to dismiss this message for two weeks.'
        ),
        MultiFieldPanel(
            [
                DisplayTypeFieldPanel(),
            ],
            heading='Display location',
            description='Select the location of this notice. If more than one notice is applicable to a page, the most specific wil be displayed.'
        ),
    ]

    def clean(self):
        if self.display_location != DISPLAY_LOCATIONS[0][0] and not self.page:
            raise ValidationError({
                'page': 'This field is required'
            })
        return super().clean()