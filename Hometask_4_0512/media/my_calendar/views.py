from django.http import HttpResponse
from django.shortcuts import render
import calendar
import datetime
import time

  # Create your views here.

def my_calendar(request):
    calen = calendar.HTMLCalendar(calendar.MONDAY)
    html_calendar = calen.formatmonth(2025,9)
    # html_calendar = calen.formatyear(2025)
    # return HttpResponse(html_calendar)
    
    # текущая дата, из который нужно вытащить год
    today = datetime.date.today()
    # дата начала года 
    first_day_year = datetime.date(today.year, 1, 1)
    # разница в 256 дней (минус 1)
    delta = datetime.timedelta(days=(256-1))
    prog_day = first_day_year + delta
  

    curent_time = time.time()

    local_time = time.localtime(curent_time)

    # модель форматирования
    format_time = time.strftime("%D, %H:%M", local_time)
  
    # таблица умножения от 1 до 10

    table_str = "<table border='2' cellpadding='4' cellspacing='0'> <tr> <th colspan ='10' align = center> Таблица умножения от 1 до 10 </th></tr>"

    for tr in [1,2,3,4,5,6,7,8,9,10]:
        table_str += "<tr>"
        for th in [1,2,3,4,5,6,7,8,9,10]:
            table_str += f"<th> {tr*th} </th>"
        table_str += "</tr>"
    table_str += "</table>"


    



    return render(request, 'calendar/calendar.html', {'m_table': table_str,  'date_time': format_time, 'html_calendar': html_calendar, 'prog_day': prog_day})
