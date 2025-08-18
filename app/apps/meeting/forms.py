from django import forms
from django.forms import inlineformset_factory
from .models import Meeting, Agenda
import datetime
from django.forms.widgets import DateInput
from django.utils import timezone

class MeetingForm(forms.ModelForm):

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

    next_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})        
    )
    next_time = forms.ChoiceField(
        required=False,
        choices=[(f"{h:02d}:{m:02d}", f"{h:02d}:{m:02d}") 
                 for h in range(0, 24) for m in (0, 30)],
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = Meeting
        fields = ['name', 'date', 'time', 'homework', 'next_date', 'next_time']

        widgets = {
            "homework": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # ラベルの設定
        self.fields['date'].label = '実施日時'
        self.fields['name'].label = 'ミーティング名'
        self.fields['homework'].label = '持ち帰り事項'
        self.fields['next_date'].label = '次回ミーティング日時'

        if self.instance and self.instance.datetime:
            dt_local = timezone.localtime(self.instance.datetime)  # タイムゾーン調整
            self.fields["date"].initial = dt_local.date()
            self.fields["time"].initial = dt_local.strftime("%H:%M")

        if self.instance and self.instance.next_datetime:
            nd_local = timezone.localtime(self.instance.next_datetime)
            self.fields['next_date'].initial = nd_local.date()
            self.fields['next_time'].initial = nd_local.strftime("%H:%M")

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):

        instance = super().save(commit=commit)

        date = self.cleaned_data.get("date")
        time = self.cleaned_data.get("time")        
        if date and time:
            hour, minute = map(int, time.split(":"))
            instance.datetime = datetime.datetime.combine(date, datetime.time(hour, minute))

        next_date = self.cleaned_data.get("next_date")
        next_time = self.cleaned_data.get("next_time")
        if next_date and next_time:
            hour, minute = map(int, next_time.split(":"))
            instance.next_datetime = datetime.datetime.combine(next_date, datetime.time(hour, minute))
        else:
            instance.next_datetime = None  # 空欄の場合は None にする

        if commit:
            instance.save()
        return instance


# 議事管理テーブルの項目を表示
AgendaFormSet = inlineformset_factory(
    Meeting, Agenda,
    fields=["name", "content"],
    widgets = {
        "name": forms.TextInput(attrs={"class": "form-control"}),
        "content": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
    },
    extra=0,       # デフォルトで1つ表示
    can_delete=True  # 行を削除できるようにする
)
