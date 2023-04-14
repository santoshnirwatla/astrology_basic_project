from django.shortcuts import render
import datetime
import random 
# Create your views here.

def astroinfo(request):
    list_msg=['coming days is very nice days',
              'now your time is well as you thinking',
              'upcoming generation is going very fast',
              'your going to get very big profit']
    name_list=['deepika','karrena','samanta','priyanka','mailaika']
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))
    
    if h<12:
        s = 'good moring'
    elif h<14:
        s = 'Good Afternoon'
    elif h<20:
        s = 'Good Evening'
    else:
        s = 'Good Night'
    msg = random.choice(list_msg)
    name = random.choice(name_list)
    my_dict={'msg':msg,'name':name,'wish':s,'time':date}
    return render(request,'testapp/astro.html',my_dict)
    