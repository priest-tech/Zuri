from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
import pytz

def get_info(request):
    #query paramaters
    slack_name = request.GET.get('Stephen Kevin')
    track = request.GET.get('back_end')
    
    #current day of the week and UTC time
    
    utc_now = datetime.now(pytz.utc)
    day_of_week = utc_now.strftime('%A')
    utc_time = utc_now.strftime('%H:%M:%S:%Z')

    #Github URLS

    github_url = request.build_absolute_uri()
    full_source_code_url = 'https://github.com/priest-tech/Zuri/blob/stage_one/myproject/myapp/views.py'
    project_url = 'https://github.com/priest-tech/Zuri'

    #Construct the response
    
    response = {
        "Slack_name": slack_name,
        "day_of_week": day_of_week,
        "utc_time": utc_time,
        "track" : track,
        "github_url": github_url,
        "full_source_code_url": full_source_code_url,
        "project_url": project_url
    }

    return JsonResponse(response, status=200)
