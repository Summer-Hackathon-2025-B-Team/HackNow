from django import forms
from .models import Reference

class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = ('target', 'content', 'url')

        widgets = {
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ラベルの設定
        self.fields['target'].label = '対象'
        self.fields['content'].label = '内容'
        self.fields['url'].label = '参考情報リンク先URL'

        # 共通クラス追加
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
