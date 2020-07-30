from unittest.mock import patch

from django.conf import settings
from django.test import TestCase
from django.db.utils import IntegrityError

from ..factories import UserFactory
from ..models import User


class TestUserEmailField(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory.create()
        return super().setUpTestData()

    def test_email(self):
        """Each user should have an email address."""

        self.assertTrue(hasattr(self.user, 'email'))

    def test_email_uniqueness(self):
        """Email should be unique for each user."""

        with self.assertRaises(IntegrityError):
            User.objects.create(email=self.user.email)
