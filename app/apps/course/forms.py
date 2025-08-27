from django import forms
from .models import Course
from django.forms.widgets import DateInput

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'interim_report_date', 'last_report_date', 'activity_status')
        # 日付フィールドにカレンダーを表示
        widgets = {
            'interim_report_date': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'last_report_date': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # nameフィールドにautofocusを追加
        self.fields['name'].widget.attrs.update({
            'placeholder': '例：2025夏/基礎コース',
            'autofocus': 'autofocus'
        })

        # 活動ステータスのトグル化
        self.fields['activity_status'].widget.attrs.update({'class': 'form-check-input'})

        # ラベルの設定
        self.fields['name'].label = 'コース名'
        self.fields['interim_report_date'].label = '中間発表日'
        self.fields['last_report_date'].label = '最終発表日'
        self.fields['activity_status'].label = '活動ステータス'

        # 共通クラス追加
        for name, field in self.fields.items():
            if name != 'activity_status':
                field.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned = super().clean()
        interim = cleaned.get("interim_report_date")
        last = cleaned.get("last_report_date")

        if interim and last and last <= interim:
            self.add_error("last_report_date", "中間発表日は最終発表日より後の日付を設定してください")

        return cleaned
