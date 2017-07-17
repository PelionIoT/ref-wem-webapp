import json

from django.core.management.base import BaseCommand, CommandError

from livedevice.models import MBEDCloudAccount


class Command(BaseCommand):
    help = "Import MBED Cloud accounts"

    def add_arguments(self, parser):
        parser.add_argument('accounts_path', help='an accounts.json file')

    def handle(self, *args, **options):
        accounts_data = json.load(open(options['accounts_path'], 'rb'))
        for account_data in accounts_data:
            account = MBEDCloudAccount(
                api_key=account_data['key'],
                display_name=account_data['email'],
            )
            account.save()
