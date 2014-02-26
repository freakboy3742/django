from __future__ import unicode_literals

from django.contrib.auth.tests.test_auth_backends import BaseModelBackendTest
from django.contrib.emailauth.models import User
from django.test import TestCase, override_settings, modify_settings


@modify_settings(INSTALLED_APPS={'append': 'django.contrib.emailauth'})
@override_settings(AUTH_USER_MODEL='emailauth.User')
class ModelBackendTest(BaseModelBackendTest, TestCase):
    """
    Tests for the ModelBackend using the emailauth User model.

    This isn't a perfect test, because both auth.User and emailauth.User are
    synchronized to the database, which wouldn't ordinary happen in
    production. As a result, it doesn't catch errors caused by the non-
    existence of the User table.

    The specific problem is queries on .filter(groups__user) et al, which
    makes an implicit assumption that the user model is called 'User'. In
    production, the auth.User table won't exist, so the requested join
    won't exist either; in testing, the auth.User *does* exist, and
    so does the join. However, the join table won't contain any useful
    data; for testing, we check that the data we expect actually does exist.
    """

    UserModel = User

    def create_users(self):
        self.user = User._default_manager.create_user(
            email='test@example.com',
            password='test',
        )
        self.superuser = User._default_manager.create_superuser(
            email='test2@example.com',
            password='test',
        )
