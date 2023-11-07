from django.shortcuts import render, redirect
from user_auth.models import User


def auth_page(request):
    if request.method == 'POST':
        log = request.POST['login']
        passw = request.POST['password']

        user =  User.objects.filter(login=log)
        user_id = None
        
        if not user.exists():
            new_user = User(login=log, password=passw)
            new_user.save()
            user_id = new_user.id
        else:
            if user[0].password != passw:
                return render(request, 'auth.html', context={'error_message': 'погоняло уже занято'})
            user_id = user[0].id

        return redirect('home/')
    
    return render(request, 'auth.html')


