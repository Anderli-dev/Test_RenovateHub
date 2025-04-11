from allauth.account.forms import LoginForm

class MyCustomLoginForm(LoginForm):

    def login(self, *args, **kwargs):
        self.fields["login"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Username or Email"
        })
        self.fields["password"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Password"
        })
        self.fields["remember"].widget.attrs.update({
            "class": "form-check-input"
        })
        return super().login(*args, **kwargs)