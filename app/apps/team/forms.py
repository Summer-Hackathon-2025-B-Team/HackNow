from django import forms
from .models import Team
from apps.course.models import Course

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('course', 'name', 'webhook_url')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # nameフィールドにplaceholderを追加
        self.fields['name'].widget.attrs.update({
            'placeholder': '例：Aチーム',
        })

        # ラベルの設定
        self.fields['course'].label = 'コース'
        self.fields['name'].label = 'チーム名'
        self.fields['webhook_url'].label = 'webhookURL'

        # status=Trueのコースだけをプルダウンに表示
        self.fields['course'].queryset = Course.objects.filter(activity_status=True)        

        # 共通クラス追加
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
