# maps views to a URL

from django.urls import path

from . import views

# This namespace helps Django diffrentiate the apps in case 
# there are same name urls
app_name = 'polls'
####

urlpatterns = [
    # /polls/
    path('', views.IndexView.as_view(), name='index'),
    # /polls/<q_id>/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # /polls/<q_id>/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # /polls/<q_id>/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
