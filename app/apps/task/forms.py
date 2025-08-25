from django import forms
from .models import Task
from django.forms.widgets import DateInput
from django.contrib.auth import get_user_model
User = get_user_model()

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['assignee', 'name', 'priority', 'start_date', 'end_date', 'status']

        # 日付フィールドにカレンダーを表示
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        # ラベルの設定
        self.fields['name'].label = 'タスク名'
        self.fields['assignee'].label = '担当者'
        self.fields['priority'].label = '優先度'
        self.fields['start_date'].label = '開始予定日'
        self.fields['end_date'].label = '終了予定日'
        self.fields['status'].label = 'ステータス'

        # ログインユーザが所属するチームのメンバーだけ選択肢にする
        self.fields['assignee'].queryset = User.objects.filter(team=user.team)

        # 共通クラス追加
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned = super().clean()
        start = cleaned.get("start_date")
        end = cleaned.get("end_date")

        if start and end and end < start:
            self.add_error("end_date", "終了予定日は開始予定日以降を設定してください。")

        return cleaned
