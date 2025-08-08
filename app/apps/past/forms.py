from django import forms
from .models import Past

class PastForm(forms.ModelForm):
    class Meta:
        model = Past
        fields = ('category', 'name', 'description', 'url', 'start_time')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ラベルの設定
        self.fields['category'].label = 'カテゴリ'
        self.fields['name'].label = 'アプリ名'
        self.fields['description'].label = 'アプリ概要'
        self.fields['url'].label = '発表動画リンク先URL'
        self.fields['start_time'].label = '発表開始時間'

        # 共通クラス追加
        for field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
