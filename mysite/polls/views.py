from django.template import loader
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import  render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Choice, Question

from django.utils import timezone
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:]
    data=[]
    data_q=[]
    data_chart=[]
    data_texts=[]
    for q in latest_question_list:
        data.append(q.id)
    for a in data:
        question=get_object_or_404(Question,pk=a)
        text=question.question_text
        data_texts.append(str(text))
        choice_all=question.choice_set.all()
        data_q=[]
        for c in choice_all:
            data_q.append(c.votes)
        data_chart.append(data_q)
        print(data_texts)
    context = {'latest_question_list': latest_question_list,'data':data,'data_chart':data_chart,'data_text':data_texts}
    return render(request, 'polls/index.html', context)

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    labels = []
    data = []
    for cho in question.choice_set.all():
        labels.append(cho.choice_text)
        data.append(cho.votes)
    return render(request, 'polls/detail.html', {'question': question,'labels': labels,
        'data': data})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    labels = []
    data = []
    for cho in question.choice_set.all():
        labels.append(cho.choice_text)
        data.append(cho.votes)
    return render(request, 'polls/result.html', {'question': question,'labels': labels,
        'data': data})


def add(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/add.html',{
        'question':question
    })


def add_choice(request,question_id):
    print(question_id)
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        choice_text=request.POST.get('choice_text')
        if choice_text == '':
            return render(request,'polls/add.html',{'question':question})
        question.choice_set.create(choice_text=choice_text, votes=0)
        question.save()
    return HttpResponseRedirect(reverse('polls:add_choice_success', args=(question.id,)))

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        labels = []
        data = []
        for cho in question.choice_set.all():
            labels.append(cho.choice_text)
            data.append(cho.votes)
        return render(request, 'polls/detail.html', {'question': question,'error_message': "Vui long chon.",'labels': labels,'data': data})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def add_question(request):
    return render(request,'polls/add_question.html',{})

def add_question1(request):
    if request.method == 'POST':
        question_text=request.POST.get('question_text')
        # request.POST.get('question_text').clear()
        if question_text=='':
            return render(request, 'polls/add_question.html', {'error_message': "You didn't select a choice."})
        question= Question(question_text=question_text, pub_date=timezone.now())
        question.save()
    return HttpResponseRedirect(reverse('polls:add_question1_success', args=()))


def delete_c(request,question_id,choice_id):
    question = get_object_or_404(Question, pk=question_id)
    choice=question.choice_set.get(pk=choice_id)
    choice.delete()
    question.save()
    return HttpResponseRedirect(reverse('polls:delete_choice_success', args=(question.id,)))

def update_choice(request,question_id,choice_id):
    question = get_object_or_404(Question, pk=question_id)
    choice=question.choice_set.get(pk=choice_id)
    return render(request, 'polls/update_choice.html', {'question': question,'choice':choice})



def update_choice_success(request,question_id,choice_id):
    question = get_object_or_404(Question, pk=question_id)
    choice_update=request.POST.get('choice_text')

    choice=question.choice_set.get(pk=choice_id)
    choice.choice_text=choice_update
    choice.save()
    labels = []
    data = []
    for cho in question.choice_set.all():
        labels.append(cho.choice_text)
        data.append(cho.votes)
    return render(request, 'polls/detail.html', {'question': question,'labels': labels,
        'data': data})


def delete_question(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    question.delete()
    return HttpResponseRedirect(reverse('polls:delete_question_success', args=()))


def update_question(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/update_question.html',{'question':question})


def update_question_success(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    question_update=request.POST.get('question_text')
    question.question_text=question_update
    question.save()
    return HttpResponseRedirect(reverse('polls:update_question_success', args=()))

def review_choice(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return HttpResponseRedirect(reverse('polls:review_result', args=(question.id,)))