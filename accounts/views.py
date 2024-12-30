from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import UserRegistrationForm
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deixe o usuário inativo até aprovação
            user.save()

            # Enviar e-mail para o solicitante
            send_mail(
                'Solicitação de Cadastro Recebida',
                'Obrigado por se registrar! Sua solicitação de cadastro foi recebida e será analisada. Aguarde que em breve seu cadastro será liberado.',
                'argospanoptes@ors37innove.com.br',  # Remetente (EMAIL_HOST_USER)
                [user.email],  # Destinatário
                fail_silently=False,
            )

            messages.success(request, 'Seus dados foram enviados com sucesso. Verifique seu e-mail para mais informações.')
            return redirect('/login')  # Redirecione para a página de login ou onde preferir
    else:
        form = UserRegistrationForm()
    return render(request, 'cadastro.html', {'form': form})
