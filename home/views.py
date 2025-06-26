from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from home.models import Poll, Vote
from django.template import loader
from django.http import HttpResponse
from home.forms import VoteForm ,PollForm, DeletePollForm
from django.contrib.auth.decorators import login_required# Create your views here.
from django.contrib import messages
from django.shortcuts import get_object_or_404


@ login_required
def all_polls(request):
    all_polls = Poll.objects.all()

    context = {
        'all_polls':all_polls,
    }
    template = loader.get_template('all_polls.html')

    return HttpResponse(template.render(context,request))

from django.shortcuts import render, redirect, get_object_or_404


@login_required
def poll_detail(request, poll_id):
    req_poll = get_object_or_404(Poll, id=poll_id)
    has_voted = Vote.objects.filter(user=request.user, poll=req_poll).exists()

    if has_voted:
        form = None  # No form shown
    elif request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            selected_choice = form.cleaned_data['choice']

            if selected_choice == '1':
                req_poll.vote1 += 1
            elif selected_choice == '2':
                req_poll.vote2 += 1
            elif selected_choice == '3':
                req_poll.vote3 += 1

            req_poll.save()

            # Save that the user voted
            Vote.objects.create(user=request.user, poll=req_poll)

            return redirect('poll-detail', poll_id=poll_id)
    else:
        form = VoteForm()

    return render(request, 'poll_detail.html', {
        'req_poll': req_poll,
        'form': form,
        'has_voted': has_voted,
    })


@login_required
def create_poll(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all-polls')
    else:
        form = PollForm()
    return render(request, 'create_poll.html', {'form': form})





@login_required
def delete_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)

    if request.method == 'POST':
        form = DeletePollForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['delete_password'] == poll.delete_password:
                poll.delete()
                return redirect('all-polls')
            else:
                form.add_error('delete_password', 'Incorrect password.')
    else:
        form = DeletePollForm()

    return render(request, 'confirm_delete.html', {'form': form, 'poll': poll})