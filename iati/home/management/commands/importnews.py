import json
import datetime
from django.utils.text import slugify
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ValidationError
from news.models import NewsIndexPage, NewsPage


class Command(BaseCommand):
    """A command for manage.py that imports news from a JSON file.
    """

    help = 'Import news given a JSON file.'

    def add_arguments(self, parser):
        parser.add_argument('json_file', nargs='+', type=str)

    def handle(self, *args, **options):
        """The default function Django BaseCommand needs to run."""

        if not options['json_file']:
            raise CommandError('Please pass the path to a JSON file as the first positional argument.')

        news_index_page = NewsIndexPage.objects.live().first()
        if news_index_page is not None:
            with open(options['json_file'][0]) as json_file:
                json_data = json.load(json_file)

                for page_data in json_data:
                    try:
                        news_page = NewsPage(
                            title_en=page_data["title"],
                            slug_en=slugify(page_data["title"]),
                            heading_en=page_data["title"],
                            content_editor_en=json.dumps([{'type': 'paragraph', 'value': page_data["content"]}]),
                            title=page_data["title"],
                            slug=slugify(page_data["title"]),
                            heading=page_data["title"],
                            content_editor=json.dumps([{'type': 'paragraph', 'value': page_data["content"]}]),
                            date=datetime.datetime.strptime(page_data["date"], "%Y-%m-%d").date()
                        )
                        news_index_page.add_child(instance=news_page)
                        news_page.save_revision().publish()
                        self.stdout.write(self.style.SUCCESS(page_data["title"]))
                    except ValidationError:
                        self.stdout.write(self.style.NOTICE(page_data["title"]))

            self.stdout.write(self.style.SUCCESS('Successfully imported news.'))