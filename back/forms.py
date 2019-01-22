
from django import forms


class ArticlesForm(forms.Form):
    title = forms.CharField(max_length=30,
                            error_messages={
                                'required': '标题必填',
                                'max_length': '标题长度不能超过30个字符'
                            })
    content = forms.CharField(error_messages={'required': '内容必填'})
    keywords = forms.CharField(max_length=20,
                               error_messages={
                                   'max_length': '关键字不能超过20个字符'
                               })
    describe = forms.CharField(max_length=2550,
                               error_messages={
                                   'max_length': '描述不能超过255个字符'
                               })
    tags = forms.CharField(max_length=20,
                           error_messages={
                               'max_length': '标签不能超过20个字符'
                           })
    image = forms.ImageField(required=False)
    is_public = forms.BooleanField()
    category = forms.IntegerField(required=True, error_messages={'required': '栏目必填'})

    def clean(self):
        return self.cleaned_data


class AddColumnForm(forms.Form):
    name = forms.CharField(max_length=10,
                           error_messages={'required': '栏目名字必填', 'max_length': '栏目名最长不超过10个字符'})
    alias = forms.CharField(max_length=10,
                            error_messages={
                                'required': '栏目别名必填',
                                'max_length': '栏目别名最长不超过10个字符'
                            })
    describe = forms.CharField(max_length=100,
                               error_messages={
                                   'required': '描述必填',
                                   'max_length': '描述最长不超过100个字符'
                               })
    keywords = forms.CharField(max_length=30,
                               error_messages={
                                   'max_length': '关键字不超过30个字符'
                               })
    fid = forms.IntegerField(required=False)

    def clean(self):
        return self.cleaned_data


class UpdateColumnForm(forms.Form):
    name = forms.CharField(max_length=10,
                           error_messages={'required': '栏目名字必填', 'max_length': '栏目名最长不超过10个字符'})
    alias = forms.CharField(max_length=10,
                            error_messages={
                                'required': '栏目别名必填',
                                'max_length': '栏目别名最长不超过10个字符'
                            })
    describe = forms.CharField(max_length=100,
                               error_messages={
                                   'required': '描述必填',
                                   'max_length': '描述最长不超过100个字符'
                               })
    keywords = forms.CharField(max_length=30,
                               error_messages={
                                   'max_length': '关键字不超过30个字符'
                               })
    fid = forms.IntegerField(required=False)

    def clean(self):
        return self.cleaned_data
