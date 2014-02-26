from django.apps import AppConfig

from django.utils.translation import ugettext_lazy as _


class EmailAuthConfig(AppConfig):
    name = 'django.contrib.emailauth'
    verbose_name = _("email-based authentication and authorization")
