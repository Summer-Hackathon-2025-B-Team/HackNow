# Djangoのformsモジュールをインポートする。フォームを作成・管理するための機能を使えるようにする。
from django import forms
# 同じアプリ内（このファイルと同じ階層）にあるmodels.pyからKnowledgeモデルをインポートしています。
from .models import Knowledge

# Knowledgeモデルと連動するフォームクラスKnowledgeFormを定義する。forms.ModelFormを継承しているので、モデルのフィールドと自動的に対応するフォームになる。
class KnowledgeForm(forms.ModelForm):
    # モデルフォームの設定情報(どのモデルを使うか、どのフィールドをフォームに含めるかなど)をまとめる内部クラス。
    class Meta:
        # このフォームはKnowledgeモデルを元に作られることを指定する。
        model = Knowledge
        # フォームに含めるフィールドはtitleとcontentのみ。
        fields = ('title', 'content')
        # 各フォームの見た目や入力方法をカスタマイズするためのウィジェットを指定する。
        # titleフィールドは1行入力のテキストボックスにし、Bootstrapのform-controlクラスをつける。
        # contentフィールドは複数行入力できるテキストエリアにし、Bootstrapのform-controlクラスをつけ、表示行数は6行にする。
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # ラベルの設定
        self.fields['title'].label = 'タイトル'
        self.fields['content'].label = '内容'

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
