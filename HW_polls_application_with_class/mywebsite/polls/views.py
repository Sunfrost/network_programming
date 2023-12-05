from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Choice, Question
import logging


# Create your views here.

logger = logging.getLogger(__name__)

class IndexView(ListView):
    template_name = 'polls/index.html'
    #model = Question
    context_object_name = 'latest_question_list'

    def index(self, request):
        latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
        context = {'latest_question_list': latest_question_list}
        return render(request, 'polls/index.html', context)

    def get_queryset(self):
        return Question.objects.all().order_by('-pub_date')[:5]


class PollsDetailView(DetailView):
    template_name = 'polls/detail.html'
    model = Question

    def detail(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    logger.debug(f"vote().question_id: {question_id}")
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You did not select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class ResultsView(DetailView):
    template_name = 'polls/results.html'
    model = Question

    def results(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/results.html', {'question': question})