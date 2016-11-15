from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage

def MailService(asunto="probando",para=["contacto@fixter.org"],mensaje="lol",remitente="contacto@fixter.org"):
	asunto = asunto
	para = para
	remitente = remitente
	mensaje = mensaje

	elMail = EmailMessage(asunto,mensaje,to=para,from_email=remitente)
	elMail.content_subtype = 'html'
	elMail.send()
	return True

def template_email(dic):
	asunto = dic['asunto']
	para = dic['para']
	remitente = 'contacto@fixter.org'
	mensaje = get_template('plantilla_mail.html').render(Context(dic))

	elMail = EmailMessage(asunto,mensaje,to=para,from_email=remitente)
	elMail.content_subtype = 'html'
	elMail.send()
	return True
