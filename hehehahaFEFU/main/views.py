from django.shortcuts import render


def main_page(request):
    if request.method == 'POST':
        pass

    return render(request, 'index.html')
    