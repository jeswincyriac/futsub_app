from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import sqlite3
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def home(request):

    return render(request,'home.html')

def channel(request):

    return render(request,'channel.html')

@csrf_exempt
def channelsub(request):
  try:
    data = json.loads(request.body.decode("utf-8"))
    print(data)
    conn=sqlite3.connect('SQL/Main.db')
    c=conn.cursor()
    c.execute("INSERT INTO channel1 VALUES(:channel_name,:no_subs,:avg_viewers,:avg_rating)",{'channel_name':data["name"],'no_subs':data["number"],'avg_viewers':1,'avg_rating':1})
    conn.commit()
    conn.close()
    print("success")
    return JsonResponse({'success': "true"})
  except Exception as e:
      # To be changed during production
      print(e)
      return JsonResponse({'Error': 'Something unexpected happened'}, status=500)


@csrf_exempt
def reviewsub(request):
  try:
    data = json.loads(request.body.decode("utf-8"))
    print(data["name"])
    conn=sqlite3.connect('SQL/Main.db')
    c=conn.cursor()
    c.execute("INSERT INTO ratings3 VALUES(:channel_name,:cust_name,:rating)",{'channel_name':data["channel"],'cust_name':data["name"],'rating':data["review"]})
    #rating=c.execute('''SELECT * from ratings3''').fetchall()
    #print(rating)
    conn.commit()
    conn.close()
    return JsonResponse({'success': "true"})


  except Exception as e:
      # To be changed during production
      print(e)
      return JsonResponse({'Error': 'Something unexpected happened'}, status=500)



def reg(request):

    return render(request,'formpage.html')
def review(request):

    return render(request,'review.html')

@csrf_exempt
def out(request):
     try:
        data = json.loads(request.body.decode("utf-8"))
        print(data["channel1"])
        conn=sqlite3.connect('SQL/Main.db')
        c=conn.cursor()
        channel1rating=c.execute("SELECT ratings from ratings3 where channel_name='"+data["channel1"]+"'").fetchone()
        channel2rating=c.execute("SELECT ratings from ratings3 where channel_name='"+data["channel2"]+"'").fetchone()
        print(channel1rating)
        print(channel2rating)
        channel1subs=c.execute("SELECT no_subs from channel1 where channel_name='"+data["channel1"]+"'").fetchone()
        channel2subs=c.execute("SELECT no_subs from channel1 where channel_name='"+data["channel2"]+"'").fetchone()
        conn.close()
        print(channel1subs)
        return JsonResponse({'no_subs1': channel1subs[0],'no_subs2':channel2subs[0],'avg_view1':channel1rating[0],'avg_view2':channel2rating[0]})


     except Exception as e:
        # To be changed during production
        print(e)
        return JsonResponse({'Error': 'Something unexpected happened'}, status=500)

@csrf_exempt
def regsub(request):
     try:
        data = json.loads(request.body.decode("utf-8"))
        print(data["name"])
        conn=sqlite3.connect('SQL/Main.db')
        c=conn.cursor()
        c.execute("INSERT INTO customers1 VALUES(:name)",{'name':data["name"]})
        conn.commit()
        conn.close()
        print("success")
        return JsonResponse({'success': "true"})


     except Exception as e:
        # To be changed during production
        print(e)
        return JsonResponse({'Error': 'Something unexpected happened'}, status=500)
