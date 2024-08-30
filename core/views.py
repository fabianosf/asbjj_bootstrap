from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages


def index(request):
    context = {
        "user": request.user if request.user.is_authenticated else None,
    }
    return render(request, "core/index.html")


def sobre(request):
    return render(request, "core/sobre.html")


def servicos(request):
    return render(request, "core/servicos.html")


""" 
def contato(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():           
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']            
            # Envia o e-mail
            send_mail(
                f'Novo envio de formulario {name}',
                f'Mensagem:\n{message}\n\nContato Detalhes:\nNome: {name}\nEmail: {email}\nTelefone: {phone}',
                email,  # Envia o e-mail a partir do e-mail do remetente
                ['fabiano.freitas@gmail.com'],  # Substitua pelo seu e-mail
            )
            messages.success(request, 'Sua mensagem foi enviada com sucesso !!!')
            form = ContactForm()
            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'core/contato.html', {'form': form})
"""


def contato(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            message = form.cleaned_data["message"]

            # Defina as palavras-chave e as respostas automáticas associadas
            
            automatic_responses = {
                "preço": "O preço da aula de jiu-jítsu mensal é R$ 160,00. Defesa Pessoal mensal é R$ 150,00 e Yoga mensal é R$ 200,00. Se você tiver mais dúvidas, estamos à disposição!",
                "preco": "O preço da aula de jiu-jítsu mensal é R$ 160,00. Defesa Pessoal mensal é R$ 150,00 e Yoga mensal é R$ 200,00. Se você tiver mais dúvidas, estamos à disposição!",
                "planos": "Oferecemos vários planos, incluindo mensal, trimestral e anual. Para mais detalhes, entre em contato conosco.",
                "pacotes": "Temos pacotes especiais para grupos e famílias. Consulte-nos para mais informações.",
                "outros assuntos": "Estamos aqui para ajudar com qualquer questão. Por favor, especifique melhor para que possamos ajudar.",
                "defesa pessoal": "O preço das aulas de defesa pessoal é R$ 150,00 por sessão. Oferecemos pacotes com desconto para aulas em grupo.",
                "yoga": "O preço das aulas de yoga mensal é R$ 200,00 por sessão. Temos planos especiais para quem deseja praticar regularmente.",
            }

            keywords = {
                "preço jiu-jitsu": [
                    "preço jiu-jitsu",
                    "custo jiu-jitsu",
                    "valor jiu-jitsu",
                    "mensalidade jiu-jitsu",
                    "aula jiu-jitsu preço",
                    "valor mensal do jiu-jitsu",
                ],
                "planos": ["planos", "opções de plano", "pacotes", "planos de aula"],
                "pacotes": ["pacotes", "pacotes especiais", "ofertas", "promoções"],
                "outros assuntos": [
                    "assuntos diversos",
                    "questões",
                    "dúvidas",
                    "informações",
                ],
                "defesa pessoal": [
                    "defesa pessoal",
                    "aulas defesa pessoal",
                    "preço defesa pessoal",
                    "custo defesa pessoal",
                ],
                "yoga": ["yoga", "aulas de yoga", "preço yoga", "custo yoga","mensalidade yoga"],
            }

            # Verifica se alguma das palavras-chave está presente na mensagem
            relevant_responses = [
                automatic_responses[keyword]
                for keyword in automatic_responses
                if keyword.lower() in message.lower()
            ]

            if relevant_responses:
                # Se encontrar palavras-chave relevantes, envie uma resposta automática
                response_message = f"Olá {name},\n\n{relevant_responses[0]}\n\nAqui está a sua mensagem original:\n\n'{message}'\n\nAtenciosamente,\nEquipe de Atendimento"
                send_mail(
                    "Resposta Automática: Informações Solicitadas",
                    response_message,
                    "fabiano.freitas@gmail.com",  # Substitua pelo seu e-mail de envio
                    [email],  # Envia a resposta para o e-mail do usuário
                )

            # Sempre envie um e-mail para o administrador com a mensagem original
            send_mail(
                f"Novo envio de formulário {name}",
                f"Mensagem:\n{message}\n\nContato Detalhes:\nNome: {name}\nEmail: {email}\nTelefone: {phone}",
                email,  # Envia o e-mail a partir do e-mail do remetente
                ["fabiano.freitas@gmail.com"],  # Substitua pelo seu e-mail
            )

            messages.success(request, "Sua mensagem foi enviada com sucesso !!!")
            form = ContactForm()
            return redirect("index")
    else:
        form = ContactForm()

    return render(request, "core/contato.html", {"form": form})
