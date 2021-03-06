from django.shortcuts import render, get_object_or_404, redirect
from .utils import get_apikeys, getaccess_token
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import Page


def index(request):
    page_list = Page.objects.all()
    urls = ('', " ", "/")
    check = False
    if (query:= request.GET.get("q")):
        page = get_object_or_404(Page, permalink__iexact=query)
        if query in urls:
            check = True
    else:
        page = get_object_or_404(Page, permalink='/')
        check = True
    context = {'page_list': page_list, 'page': page, 'check': check}
    return render(request, 'pages/page.html', context)


def contact(request):
    contact_form = ContactForm()
    submitted = None

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject, message = contact_form.get_details()

            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[
                    settings.EMAIL_HOST_USER,
                    'olaisaiah54@gmail.com',
                    'isaiaholaoye91@gmail.com'
                ],
                fail_silently=False,
            )
            return redirect('/contact?submitted=True')
        else:
            contact_form = ContactForm()
    if 'submitted' in request.GET:
        submitted = True

    context = {'form': contact_form, 'submitted': submitted}

    return render(request, 'pages/contact.html', context)


def unfollow_bot(request):
    api, api_key = get_apikeys()
    endpoint = None

    if (get_token := request.GET.get('token')) == 'gettoken':
        endpoint = getaccess_token(request, api, api_key)

    if request.method == 'POST':
        token, total_unfollow = request.POST.get(
            'token_num'), request.POST.get('count')
        
        if token and total_unfollow != 'Unfollow Once?':
            api = getaccess_token(request, api, api_key, token)
            if api:
                return HttpResponse(f'{api.verify_credentials()}')
            return HttpResponse('<h1>Couldn\'n authenticate User, Please try again :)</h1>')
        return HttpResponse('<h1> Opps! fill in the form correctly :( </h1>')

    context = {'endpoint': endpoint}

    return render(request, 'pages/bot.html', context)
