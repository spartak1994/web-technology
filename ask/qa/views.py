from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK')

	
@require_GET
def index(request, *args, **kwargs):
    question_list = Question.objects.order_by('-id')
    paginator, page, limit = paginate(request, question_list)
    context = {
        'questions': page,
        'paginator': paginator,
        'limit': limit,
    }
    return render(request, 'qa/index-lite.html', context)
	
@require_GET
def popular(request, *args, **kwargs):
    # list of questions in desc order by rating
    question_list = Question.objects.order_by('-rating')
    paginator, page, limit = paginate(request, question_list)    
    context = {
        'questions': page,
        'paginator': paginator,
        'limit': limit,
    }
    return render(request, 'qa/popular-lite.html', context)

def question(request, question_id):
    """POST and GET methods needed"""
    q = get_object_or_404(Question, id=question_id)
    a = q.answer_set.all()
    #a = Answer.objects.filter(question=question_id).order_by('-added_at')
    form = AnswerForm(initial = {'question': question_id})
    context = {'question': q, 'answers': a, 'form': form, }
    return render(request, 'qa/question-lite.html', context)  	