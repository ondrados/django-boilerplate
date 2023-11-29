from djoser.email import (
    ActivationEmail as BaseActivationEmail,
    ConfirmationEmail as BaseConfirmationEmail,
    PasswordResetEmail as BasePasswordResetEmail,
    PasswordChangedConfirmationEmail as BasePasswordChangedConfirmationEmail,
    UsernameChangedConfirmationEmail as BaseUsernameChangedConfirmationEmail,
    UsernameResetEmail as BaseUsernameResetEmail,
)


class ActivationEmail(BaseActivationEmail):
    template_name = "emails/activation.html"


class ConfirmationEmail(BaseConfirmationEmail):
    template_name = "emails/confirmation.html"


class PasswordResetEmail(BasePasswordResetEmail):
    template_name = "emails/password_reset.html"


class PasswordChangedConfirmationEmail(BasePasswordChangedConfirmationEmail):
    template_name = "emails/password_changed_confirmation.html"


class UsernameChangedConfirmationEmail(BaseUsernameChangedConfirmationEmail):
    template_name = "emails/username_changed_confirmation.html"


class UsernameResetEmail(BaseUsernameResetEmail):
    template_name = "emails/username_reset.html"
