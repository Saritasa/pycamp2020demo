from django.core.management.base import BaseCommand

from ...models import User


class Command(BaseCommand):
    help = 'List users'

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Found users: %d' % User.objects.count())
        )

        for user in User.objects.all():
            self.stdout.write(user.email)
