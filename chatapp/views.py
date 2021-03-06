from django.shortcuts import render, render_to_response, RequestContext
import django.contrib.auth as auth
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Message
from .forms import *
from django.contrib.sessions.models import Session
from django.utils import timezone
from .activation import Activation
from django.core.exceptions import ObjectDoesNotExist


def chat(request):
    if request.user.is_authenticated():
        message_list = Message.get_all()
        user_list = get_all_logged_in_users()
        users = User.objects.all()
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
    if request.user.is_authenticated and request.user.username:
        username = request.user.username
        context = {
            "username": username
        }
        return render(request, "already_logged_in.html", context=context)
    else:
        next = request.GET.get('next', '/chat/')
        form = LoginForm(request.POST or None)

        if request.method == "POST" and form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Account is not active at the moment.")
        return render(request, "login.html", {'next': next, 'form': form})


def messages(request):
    return render(request, 'messages.html', {'message_list': Message.get_all()})


def get_all_logged_in_users():
    # Query all non-expired sessions
    # use timezone.now() instead of datetime.now() in latest versions of Django
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    uid_list = []

    # Build a list of user ids from that query
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))

    # Query all logged in users based on id list
    return User.objects.filter(id__in=uid_list)


def sign_up(request):
    if request.user.is_authenticated and request.user.username:
        username = request.user.username
        context = {
            "username": username
        }
        return render(request, "already_registered.html", context=context)
    else:
        title = 'Zarejestruj się.'
        next = request.GET.get('next', '/sent_mail')
        form = SignUpForm(request.POST or None)
        context = {
            "title": title,
            "form":  form,
            "next": next,
        }
        if form.is_valid():
            instance = form.save(commit=False)
            username = form.cleaned_data.get("username")
            password = form.clean_password()
            email = form.clean_email()
            instance.save()

            user = User.objects.create_user(username=username, password=password, email=email)
            user.is_active = False
            user.save()
            key = Activation.key_gen()

            sign_up_object = SignUp.objects.get(username=username)
            sign_up_object.key = key
            sign_up_object.save()

            Activation.send_mail("poczta.interia.pl", 587, "chat.tai@interia.pl", "chat.tai", "56789098765tai", email, key)

            return HttpResponseRedirect(next)
        else:
            return render(request, "sign_up.html", context)


def activate(request):
    sid = (request.GET.get('id'))
    try:
        sign_up_object = SignUp.objects.get(key=sid)
        user = User.objects.get_by_natural_key(sign_up_object.username)
        if not user.is_active:
            user.is_active = True
            sign_up_object.solved = True
            sign_up_object.save()
            user.save()
        return render(request, "activated.html", context=None)
    except ObjectDoesNotExist:
        return HttpResponse("Object not exist :(")


def contact(request):
    return render(request, "contact.html", context=None)


def logout(request):
    auth.logout(request)
    return render(request, "logout.html", context=None)


def sent_mail(request):
    return render(request, "sent_mail.html", context=None)


def custom_404(request):
    return render(request, "404.html", context=None)


def del_message(request):
    mid = (request.GET.get('id'))
    if request.user.is_staff:
        message = Message.objects.get(pk=mid)
        message.delete()
    return chat(request)


def account(request):
    if request.user.is_authenticated and request.user.username:
        form = AccountForm(request.POST or None)
        next = request.GET.get('next', '/account_changed')
        context = {
            "form": form,
        }
        if request.method == "POST":
            if form.is_valid():
                user = User.objects.get_by_natural_key(request.user.username)
                user.set_password(form.cleaned_data.get("new_password"))
                user.save()
                return HttpResponseRedirect(next)
            return render(request, "account.html", context=context)
        else:
            return render(request, "account.html", context=context)
    else:
        return login(request)


def account_changed(request):
    return render(request, "account_changed.html", context=None)
