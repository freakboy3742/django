from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.emailauth.models import User
from django.utils.translation import ugettext as _


class UserCreationForm(auth_forms.AbstractUserCreationForm):
    """
    A concrete implementation of AbstractUserCreationForm that uses an
    e-mail address as a user's identifier.
    """
    error_messages = {
        'duplicate_email': _("A user with that email already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }

    class Meta:
        model = User
        fields = ('email',)

    def clean_email(self):
        # Since User.email is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        email = self.cleaned_data['email']
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages['duplicate_email'],
            code='duplicate_email',
        )


class UserChangeForm(auth_forms.AbstractUserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
