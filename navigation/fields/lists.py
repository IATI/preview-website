from wagtail.core.blocks import (
    BooleanBlock,
    CharBlock,
    ListBlock,
    PageChooserBlock,
    StructBlock,
)


class NestedPageGroup(StructBlock):

    class Meta:
        icon = 'list-ul'
        label = 'Page group'

    page = PageChooserBlock(
        help_text='Optional: top level page for the group',
        required=False,
        label='Top level page',
    )
    title = CharBlock(
        help_text='Optional: plain text title for the page group',
        label='Title',
        required=False,
    )
    page_group = ListBlock(
        PageChooserBlock(),
        required=False,
        help_text='Optional: group of sub pages, displayed as an indented list',
    )


class PageList(StructBlock):

    class Meta:
        help_text = '''
                    <strong>List of internal page links.</strong><br>
                    Optional: select the first page link to use as a title, or add a plain text title.<br>
                    Optional: short description.
                    '''
        icon = 'list-ul'
        label = 'Page list'
        form_template = 'navigation/block_forms/custom_struct.html'
        template = 'navigation/blocks/page_list.html'

    use_first_page_as_title = BooleanBlock(
        help_text='Optional: if checked, the first page in the list will be displayed as a title',
        required=False,
    )
    title = CharBlock(
        help_text='Optional: plain text title for the page list',
        label='Title',
        required=False,
    )
    description = CharBlock(
        help_text='Optional: description for the page list',
        label='Description',
        required=False,
    )
    page_list = ListBlock(
        PageChooserBlock(),
        label='Pages',
    )


class NestedPageList(StructBlock):

    class Meta:
        help_text = '''
                    <strong>List of internal page links, with optional page link sub-groups.</strong><br>
                    Optional: plain text title for sub-groups<br>
                    '''
        icon = 'list-ul'
        label = 'Nested page list'
        form_template = 'navigation/block_forms/custom_struct.html'
        template = 'navigation/blocks/nested_page_list.html'

    groups = ListBlock(
        NestedPageGroup()
    )