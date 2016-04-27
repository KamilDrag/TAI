from django.shortcuts import render, render_to_response, RequestContext
from .models import Message
from .forms import MessageForm

#def message(request):
#    message_list = Message.objects.order_by('message_date')
#    context = {'message_list': message_list}
#    return render(request, 'message.html', context)


def message(request):
    form = MessageForm(request.POST or None)
    message_list = Message.objects.order_by('message_date')
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    return render_to_response("message.html", locals(), context_instance=RequestContext(request))