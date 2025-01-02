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


    # <table border="0" cellpadding="0" cellspacing="0" class="month"> 
    # <tr>
    #     <th colspan="7" class="month">September 2025</th>
    # </tr> 
    # <tr><th class="mon">Mon</th>
    #     <th class="tue">Tue</th>
    #     <th class="wed">Wed</th>
    #     <th class="thu">Thu</th>
    #     <th class="fri">Fri</th>
    #     <th class="sat">Sat</th>
    #     <th class="sun">Sun</th>
    # </tr> 
    # <tr>
    #     <td class="mon">1</td>
    #     <td class="tue">2</td>
    #     <td class="wed">3</td>
    #     <td class="thu">4</td>
    #     <td class="fri">5</td>
    #     <td class="sat">6</td>
    #     <td class="sun">7</td>
    # </tr> 
    # <tr>
    #     <td class="mon">8</td>
    #     <td class="tue">9</td>
    #     <td class="wed">10</td>
    #     <td class="thu">11</td>
    #     <td class="fri">12</td>
    #     <td class="sat">13</td>
    #     <td class="sun">14</td>
    # </tr> 
    # <tr>
    #     <td class="mon">15</td>
    #     <td class="tue">16</td>
    #     <td class="wed">17</td>
    #     <td class="thu">18</td>
    #     <td class="fri">19</td>
    #     <td class="sat">20</td>
    #     <td class="sun">21</td>
    # </tr> 
    # <tr>
    #     <td class="mon">22</td>
    #     <td class="tue">23</td>
    #     <td class="wed">24</td>
    #     <td class="thu">25</td>
    #     <td class="fri">26</td>
    #     <td class="sat">27</td>
    #     <td class="sun">28</td>
    # </tr> 
    # <tr>
    #     <td class="mon">29</td>
    #     <td class="tue">30</td>
    #     <td class="noday">&nbsp;</td>
    #     <td class="noday">&nbsp;</td>
    #     <td class="noday">&nbsp;</td>
    #     <td class="noday">&nbsp;</td>
    #     <td class="noday">&nbsp;</td>
    # </tr> </table>



    return render(request, 'calendar/calendar.html', {'m_table': table_str,  'date_time': format_time, 'html_calendar': html_calendar, 'prog_day': prog_day})
