from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm, PdfUploadForm
from .models import UserProfile
import os

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def download_pdf(request):
    pdf_file_path = "media\\pdfs\\1104437525.pdf"
    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="1104437525.pdf"'
            return response
    else:
        return HttpResponse("File not found", status=404)
def inicio(request):
    return render(request, 'inicio.html')

def horario_view(request):
    # Lógica de la vista
    return render(request, 'horario.html')