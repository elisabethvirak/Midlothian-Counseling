from django.urls import path
from contact import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('interest/<int:pk>',views.InterestDetailView.as_view(),name='interest_detail'),
    path('interest/new/',views.InterestListView.as_view(),name='interest_list'),
    path('interest/new/',views.CreateInterestView.as_view(),name='interest_form'),
    path('interest/<int:pk>/edit',views.InterestUpdateView.as_view(),name='interest_edit'),
    path('interest/<int:pk>/delete',views.InterestDeleteView.as_view(),name='interest_remove'),
    path('drafts/',views.DraftListView.as_view(),name='interest_draft_list'),
    path('interest/<int:pk>/comment/',views.add_comment_to_interest,name='add_comment_to_interest'),
    path('comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/remove/',views.comment_remove,name='comment_remove'),
    path('interest/<int:pk>/publish/',views.interest_published,name='interest_published')
]