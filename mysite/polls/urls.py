
from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.detail, name='results'),
    path('<int:question_id>/review_result/',views.results,name='review_result'),


    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/add/',views.add,name='add'),
    path('<int:question_id>/add_choice/',views.add_choice,name='add_choice'),

    path('add_question/',views.add_question,name='add_question'),
    path('add_question1/',views.add_question1,name='add_question1'),
    path('<int:question_id>/delete_c/<int:choice_id>',views.delete_c,name='delete_c'),
    path('<int:question_id>/update_choice/<int:choice_id>',views.update_choice,name='update_choice'),
    path('<int:question_id>/update_choice_success/<int:choice_id>',views.update_choice_success,name='update_choice_success'),
    path('<int:question_id>/delete_question/',views.delete_question,name='delete_question'),
    path('<int:question_id>/update_question/',views.update_question,name='update_question'),
    path('<int:question_id>/update_question_success/',views.update_question_success,name='update_question_success'),
    path('<int:question_id>/review_choice/',views.review_choice,name='review_choice'),
    path('add_question1_success/',views.index,name='add_question1_success'),
    path('<int:question_id>/add_choice_success',views.detail,name='add_choice_success'),
    path('<int:question_id>/delete_choice_success',views.detail,name='delete_choice_success'),
    path('delete_question_success/',views.index,name='delete_question_success'),
    path('update_question_success/',views.index,name='update_question_success')

]