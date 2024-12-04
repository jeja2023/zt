from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('phone_number',)  # 添加额外的字段

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')