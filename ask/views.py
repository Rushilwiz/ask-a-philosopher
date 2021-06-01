from django.shortcuts import render, redirect
from django.contrib import messages


from .forms import QuestionForm

# Create your views here.

def ask(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('ask')
    else:
        form = QuestionForm()

    context = {
        'form': form,
    }

    return render(request, 'ask/ask.html', context)