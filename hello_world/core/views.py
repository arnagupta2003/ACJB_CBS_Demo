from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)
def signing(request):
    # print("req:", request.POST.get("email"))
    # print("req:", request.POST.get("password"))
            
    # query = f"SELECT * FROM demo_user WHERE name = '{username}'"
    email = request.POST.get("email")
    password = request.POST.get("password")
    query =  f"SELECT * FROM users WHERE email='{email}' AND password = '{password}'"
    with connection.cursor() as cursor:
        cursor.execute(query)
        users = cursor.fetchall()
        # print(users)
        if(len(users)==0):
            messages.error(request, 'Wrong Password/User')
            return redirect("/")

    # return JsonResponse({"User":users})
    return render(request, 'user_page.html', {'user_list': users})
