from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView
from core.forms import ContactForm
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.core.mail import send_mail

# Create your views here.

class AngularApp(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(AngularApp, self).get_context_data(**kwargs)
        context['ANGULAR_URL'] = settings.ANGULAR_URL
        return context


class SampleView(View):
	"""View to render django template to angular"""
	def get(self, request):
		return HttpResponse("OK!")


class NgTemplateView(View):
	"""View to render django template to angular"""
	def get(self, request):
		return render(request, 'template.html', {"django_variable": "This is a django context variable"})
		

def contact(request):
    form_class = ContactForm
    
    if request.method == 'POST':
        # form = form_class(data=request.POST)
        form = form_class(request.POST)
        print '>>>>>>>>>>>>>>>>>>>> \n >>>>> \ninside request \n >>>>>>>>>>'
        print form

        if form.is_valid():
            # saveForm = form_class(request.POST)
            form.save()

            print '>>>>>>>>\n inside form \n>>>>>>>>>>>>>>>'

            # contact_name = request.POST.get(
            #     'contact_name'
            # , '')
            # contact_email = request.POST.get(
            #     'contact_email'
            # , '')
            # form_content = request.POST.get('content', '')
    
            # # Email the profile with the 
            # # contact information
            # template = get_template('contact_template.txt')
            # context = Context({
            #     'contact_name': contact_name,
            #     'contact_email': contact_email,
            #     'form_content': form_content,
            # })
            # content = template.render(context)
    
            # email = EmailMessage(
            #     "New contact form submission",
            #     content,
            #     "Your website" +'',
            #     ['arpad.web@gmail.com'],
            #     headers = {'Reply-To': contact_email }
            # )
            # email.send()
            
            # send_mail(
            #     'Subject here',
            #     form_content,
            #     'arpad.web@gmail.com',
            #     ['asztell@yahoo.com'],
            #     fail_silently=False,
            # )

            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })