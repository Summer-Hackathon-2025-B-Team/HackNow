from django.shortcuts import render
from datetime import date
from django.utils import timezone
from apps.task.models import Task
from apps.team.models import Team
from apps.meeting.models import Meeting

def index_view(request):

    user = request.user

    # 一般ユーザの場合
    if not user.is_staff:

        interim_report_date = ""
        last_report_date = ""
        days_left_interim = ""
        days_left_last = ""
        due_today_tasks = Task.objects.none()
        overdue_tasks = Task.objects.none()
        next_meeting = ""

        # ユーザがチームに属している場合（条件分岐しながらteamにrequest.user.teamを代入）
        if team := user.team: 

            # ユーザに紐づくチームが存在する場合
            course = team.course
            interim_report_date = course.interim_report_date
            last_report_date = course.last_report_date
            days_left_interim = (interim_report_date - date.today()).days
            days_left_last = (last_report_date - date.today()).days

            # DateField に対して比較する場合はtimezone.localdate()を使う（時刻無し）
            today = timezone.localdate()  
            # DateTimeField に対して比較するときはtimezone.now()を使う（時刻あり）
            today_datetime = timezone.now()

            # 当日期限タスク
            due_today_tasks = Task.objects.filter(
                team=user.team,
                end_date=today,
                status__in=[1, 2]
            )

            # 期限切れタスク（今日より前のタスク）　※__lt は "less than"（より小さい） という意味
            overdue_tasks = Task.objects.filter(
                team=user.team,
                end_date__lt=today,
                status__in=[1, 2]
            )

            # 今日以降の次回ミーティング日時を昇順で並び替え、最初の1件だけを取得
            next_meeting = (
                Meeting.objects
                # gteは「greater than or equal（以上）」を意味
                .filter(team=team, next_datetime__gte=today_datetime)
                .order_by('next_datetime')
                .first()
            )

        return render(request, 'home/index.html', {
            'interim_report_date': interim_report_date,
            'last_report_date': last_report_date,
            'days_left_interim': days_left_interim,
            'days_left_last': days_left_last,
            'due_today_tasks': due_today_tasks,
            'overdue_tasks': overdue_tasks,            
            'next_meeting': next_meeting,
        })
    
    # 管理ユーザの場合
    else:

        active_teams = (
            Team.objects
            .filter(course__activity_status=1)
            .prefetch_related('members')       # チームのユーザ一覧をまとめて取得
            .prefetch_related('task_set')       # チームのタスク一覧をまとめて取得
            .select_related('course')           # コース情報もまとめて取得
        )

        return render(request, 'home/index.html', {
            'active_teams': active_teams,
        })
