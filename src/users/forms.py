from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.forms import SetPasswordForm as BaseSetPasswordForm

from .models import User


class UserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm):
        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = "Can’t be too similar to your other personal information.<br>" \
                                             "Must contain at least 8 characters.<br>" \
                                             "Can’t be a commonly used password.<br>" \
                                             "Can’t be entirely numeric.<br>"


class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = User
        fields = ('email',)

