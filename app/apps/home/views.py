from django.shortcuts import render
from datetime import date

def index_view(request):

    # 一般ユーザの場合
    if not request.user.is_staff:

        interim_report_date = ""
        last_report_date = ""
        days_left_interim = ""
        days_left_last = ""

        if request.user.team:
            interim_report_date = request.user.team.course.interim_report_date
            last_report_date = request.user.team.course.last_report_date
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
