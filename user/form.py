
from django import forms

from user.models import User


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=10,
                               min_length=4,
                               required=True,
                               error_messages={
                                   'required': '用户名是必填项',
                                   'min_length': '用户名不能少于4个字符',
                                   'max_length': '用户名不能超过10个字符'
                               })
    password = forms.CharField(min_length=6,
                               required=True,
                               error_messages={
                                   'required': '密码是必填项',
                                   'min_length': '密码少于6个字符'
                               })
    password2 = forms.CharField(required=True,
                                error_messages={
                                    'required': '确认密码是必填项'
                                })

    def clean_username(self):
        # 只校验姓名
        username = self.cleaned_data['username']
        stu = User.objects.filter(username=username).first()
        if stu:
            raise forms.ValidationError('名字已存在')
        return self.cleaned_data['username']

    def clean_password2(self):
        # 校验密码和确认密码是否一致
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password2 != password:
            raise forms.ValidationError('确认密码与密码不一致')
        return self.cleaned_data['password']