from django import forms
from apps.task.models import Task
from apps.user.models import User  # あなたのUserモデル

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['assignee', 'name', 'priority', 'start_date', 'end_date', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # セレクトボックスに表示されるテキストを「name」に変更
        self.fields['assignee'].label_from_instance = lambda obj: obj.name
