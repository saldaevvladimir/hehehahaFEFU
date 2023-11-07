from django.shortcuts import render


def main_page(request):
    if request.method == 'POST':
        match request.POST['action']:
            case 'CREATE GYM':
                pass
            case 'RANDOM GYM':
                pass
            case 'PRIVATE GYM':
                pass

    return render(request, 'index.html')
    