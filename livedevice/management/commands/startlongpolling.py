from django.core.management.base import BaseCommand, CommandError

from livedevice.models import MBEDCloudAccount


class Command(BaseCommand):
    help = "Start long polling all MBED Cloud accounts that don't have webhook callbacks set"

    def handle(self, *args, **options):
        for account in MBEDCloudAccount.objects.all():
            if not account.is_webhook_callback_set():
                account.start_long_polling()
