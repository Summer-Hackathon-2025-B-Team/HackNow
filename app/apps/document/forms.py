# Djangoのformsモジュールをインポートする。フォームを作成・管理するための機能を使えるようにする。
from django import forms
# 同じアプリ内（このファイルと同じ階層）にあるmodels.pyからKnowledgeモデルをインポートしています。
from .models import Document


# Documentモデルと連動するフォームクラスDocumentFormを定義する。
class DocumentForm(forms.ModelForm):
    class Meta:
        # このフォームはDocumentモデルを元に作られることを指定する。
        model = Document

        # フォームに含めるフィールドはnameとlinkのみ。作成者もではないの？
        fields = ('name', 'url', )
        # nameフィールドは1行入力のテキストボックスにし、Bootstrapのform-controlクラスをつける。
        # urlフィールドは複数行入力できるテキストエリアにし、Bootstrapのform-controlクラスをつけ、表示行数は5行にする。
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # 他フォームと同じインターフェースに合わせる
        super().__init__(*args, **kwargs)

        # ラベルの設定
        self.fields['name'].label = '資料名'
        self.fields['url'].label = 'リンク'

        for field in self.fields.values():
            # 既存の class があっても上書きせず追記したい場合は下記2行に差し替え可
            # base = field.widget.attrs.get("class", "")
            # field.widget.attrs["class"] = (base + " form-control").strip()
            field.widget.attrs.update({"class": "form-control"})
