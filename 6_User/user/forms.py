from django import forms
from .models import User


class SingUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    YESNO_CHOICES = (('male', 'male'), ('female', 'female'))
    gender = forms.TypedChoiceField(choices=YESNO_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = User
        # 여기엔 왜 "gender" 가 없어도 나올 까요?, 아래 LoginForm 과 모양을 비교해 보아요!
        fields = ['username', 'password', 'confirm_password', 'bio']

    def clean(self):
        # 지금은 개념이 어려우니 비밀번호를 검사해 주는 함수라고 생각해주세요!
        cleaned_data = super(SingUpForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class LogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }