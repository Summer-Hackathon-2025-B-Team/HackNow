from django.shortcuts import render
from datetime import date

def index_view(request):

    # 一般ユーザの場合
    if not request.user.is_staff:

        interim_report_date = ""
        last_report_date = ""
        days_left_interim = ""
        days_left_last = ""

        # 条件分岐しながらteamにrequest.user.teamを代入
        if team := request.user.team: 

            # ユーザに紐づくチームが存在する場合
            course = team.course
            interim_report_date = course.interim_report_date
            last_report_date = course.last_report_date
            days_left_interim = (interim_report_date - date.today()).days
            days_left_last = (last_report_date - date.today()).days

        return render(request, 'home/index.html', {
            'interim_report_date': interim_report_date,
            'last_report_date': last_report_date,
            'days_left_interim': days_left_interim,
            'days_left_last': days_left_last,
        })
    
    # 管理ユーザの場合
    else:
        return render(request, 'home/index.html', {
        })
