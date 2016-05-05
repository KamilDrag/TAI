from django.shortcuts import render, render_to_response, RequestContext
import django.contrib.auth as auth
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Message


def chat(request):
    if request.user.is_authenticated():
        message_list = Message.get_all()
        return render_to_response("chat.html", locals(), context_instance=RequestContext(request))
    else:
        return login(request)


def post(request):
    if Message.create_message(request):
        msg = request.POST.get('msgbox', None)
        return JsonResponse({'msg': msg, 'user': request.user})
    else:
        return HttpResponse("Cos sie popsulo")


def login(request):
    next = request.GET.get('next', '/chat/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(next)
        else:
            return HttpResponse("Account is not active at the moment.")
    return render(request, "login.html", {'next': next})


def messages(request):
    return render(request, 'messages.html', {'message_list': Message.get_all()})
