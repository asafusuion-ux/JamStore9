from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.shortcuts import redirect

class ContactView(TemplateView):
    template_name = 'pages/contact.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_mail(
            subject=f'Новое сообщение: {subject}',
            message=f'Имя: {name}\nПочта: {email}\nТелефон: {phone}\n\nСообщение:\n{message}',
            from_email=email,
            recipient_list=['asafusuion@gmail.com'], 
        )

        return redirect('contact')