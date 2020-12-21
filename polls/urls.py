from django.shortcuts import get_object_or_404, render
from django.urls import path
from.import views
from .models import Question

app_name = 'polls'

urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

def results(request, question_id):
    question =get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question' : question})