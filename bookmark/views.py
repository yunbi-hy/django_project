from django.shortcuts import render
from django.views.generic.list import ListView  ##말그대로 djang의 views에 generic의 list로 부터 삽입한다. ListView를.
##북마크 리스트뷰는 리스트뷰에 상속받아서 만들어진다,#
from .models import Bookmark
# models에 정의한 북마크Bookmark라는 모델을 가져온다.#
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# 장고에 있는 views의 generic의 edit라는 곳에 CreateView를 넣는다.#
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView


class BookmarkListView(ListView):  ##실제 뷰클래스를 정의한것. 리스트뷰를 상속받아서 모델ㅇ라는 변수에 정의한 북마크 모델 연결
    model = Bookmark
    paginate_by = 6

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('bookmark:list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix ='_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')

