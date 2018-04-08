from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from .models import Chose, Question
from django.http import Http404
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
# Create your views here.


def index(request):
    return HttpResponse('Привет - это магазин автозапчастей')



# class IndexView(generic.ListView):
#     template_name = 'page/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         """Return the last five published questions."""
#         # return Question.objects.order_by('-pub_date')[:5]
#         return Question.objects.filter(
#             pub_date__lte=timezone.now()
#         ).order_by('-pub_date')[:5]


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'page/detail.html'
#
#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Question.objects.filter(pub_date__lte=timezone.now())
#
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'page/results.html'


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('page/index.html')
#     context = {'latest_question_list': latest_question_list}
#     # context = RequestContext(request, {
#     #     'latest_question_list': latest_question_list,
#     # })
#     # output = ", ".join([q.question_text for q in latest_question_list])
#     # return HttpResponse(template, context)
#     return render(request, 'page/index.html', context)
#
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     return render(request, "page/detail.html", {'question': question})
#
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'page/results.html', {'question': question})


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_chose = question.chose_set.get(pk=request.POST['chose'])
#     except (KeyError, Chose.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'page/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a chose.",
#         })
#     else:
#         selected_chose.votes += 1
#         selected_chose.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('page:results', args=(question.id,)))




