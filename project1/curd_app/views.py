from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import TicketForm
from .models import Ticket


@login_required(login_url="login_url")
def ticket_view(request):
    template_name = "curd_app/ticket_info.html"
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_urls")
    context = {"form": form}
    return render(request, template_name, context)


def show_view(request):
    template_name = "curd_app/show_all_list.html"
    tickets = Ticket.objects.all()
    context = {"tickets": tickets}
    return render(request, template_name, context)


def update_view(request, pk):
    obj = Ticket.objects.get(id=pk)
    form = TicketForm(instance=obj)
    if request.method == "POST":
        form = TicketForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_urls")
    template_name = 'curd_app/ticket_info.html'
    context = {'form': form}
    return render(request, template_name, context)


def delete_view(request,  pk):
    obj = Ticket.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("show_urls")
    return render(request, 'curd_app/confirm.html')
