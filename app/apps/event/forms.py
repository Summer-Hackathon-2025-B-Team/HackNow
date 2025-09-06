from django import forms
from .models import Event
from django.forms.widgets import DateInput
import datetime
from django.utils import timezone

class EventForm(forms.ModelForm):

    date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})        
    )
    time = forms.ChoiceField(
        required=False,
        choices=[(f"{h:02d}:{m:02d}", f"{h:02d}:{m:02d}") 
                 for h in range(0, 24) for m in (0, 30)],
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = Event
        fields = ('datetime', 'title', 'publish_status', 'detail_url', 'zoom_url')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 公開ステータスのトグル化
        self.fields['publish_status'].widget.attrs.update({'class': 'form-check-input'})

        # ラベルの設定
        self.fields['title'].label = 'イベント名'
        self.fields['publish_status'].label = '公開ステータス'
        self.fields['detail_url'].label = '詳細ページリンク先URL'
        self.fields['zoom_url'].label = 'Zoomリンク先URL'

        # 共通クラス追加
        for name, field in self.fields.items():
            if name != 'publish_status':
                field.widget.attrs.update({'class': 'form-control'})

        if self.instance and self.instance.datetime:
            dt_local = timezone.localtime(self.instance.datetime)  # タイムゾーン調整
            self.fields["date"].initial = dt_local.date()
            self.fields["time"].initial = dt_local.strftime("%H:%M")

    def save(self, commit=True):

        instance = super().save(commit=commit)

        date = self.cleaned_data.get("date")
        time = self.cleaned_data.get("time")        
        if date and time:
            hour, minute = map(int, time.split(":"))
            instance.datetime = datetime.datetime.combine(date, datetime.time(hour, minute))

        if commit:
            instance.save()
        return instance
