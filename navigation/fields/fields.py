"""Module to define navigation fields."""

from wagtail.core.fields import StreamField
from wagtail.core.blocks import (
    StreamBlock,
)
from navigation.fields import (
    TypeA,
    TypeB,
    TypeC,
)


def navigation(blank=False):
    """Return a stream of different module types."""
    required = not blank
    return StreamField(
        StreamBlock(
            [
                ('type_a', TypeA()),
                ('type_b', TypeB()),
                ('type_c', TypeC()),
            ],
            max_num=1,
            required=required,
        ),
        blank=blank
    )
