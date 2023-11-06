from django.shortcuts import render, redirect
from user_auth.models import User


def auth_page(request):
    if request.method == 'POST':
        log = request.POST['login']
        passw = request.POST['password']

        users =  User.objects.filter(login=log)
        user_id = None
        
        if not users.exists():
            new_user = User(login=log, password=passw)
            new_user.save()
            user_id = new_user.id
        else:
            user_id = users[0].id

        return redirect('home/')
    
    return render(request, 'auth.html')
