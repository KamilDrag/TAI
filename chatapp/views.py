from django.shortcuts import render, render_to_response, RequestContext
import django.contrib.auth as auth
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Message
from .forms import MessageForm

#def message(request):
#    message_list = Message.objects.order_by('message_date')
#    context = {'message_list': message_list}
#    return render(request, 'message.html', context)

def chat(request):
    form = MessageForm(request.POST or None)
    message_list = Message.objects.order_by('message_date')
    if request.method == "POST":
        if request.user.is_authenticated():
            content = request.POST.get("message_content")
            Message.objects.create(nick=request.user, message_content=content)
        else:
            return HttpResponse("You cannot send message until you are logged.")

    return render_to_response("chat.html", locals(), context_instance=RequestContext(request))

def post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        if msg is None:
            msg = "..."
        m = Message(nick=request.user, message_content=msg)
        m.save()
        return JsonResponse({ 'msg': msg, 'user': str(request.user) })
    else:
        return HttpResponse('Request must be POST.')


#def message(request):
#    form = MessageForm(request.POST or None)
#    message_list = Message.objects.order_by('message_date')
#    if form.is_valid():
#        save_it = form.save(commit=False)
#        save_it.save()
#    return render_to_response("message.html", locals(), context_instance=RequestContext(request))


def login(request):
    next = request.GET.get('next', '/chat/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Account is not active at the moment.")
        #else:
            #return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request, "login.html", {'next': next})

def messages(request):
    message_list = Message.objects.order_by('message_date')
    return render(request, 'messages.html', {'message_list': message_list})