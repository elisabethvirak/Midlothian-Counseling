from django.urls import path
from contact import views

urlpatterns = [
    path('',views.InterestListView.as_view(),name='interest_list'),
    path('about/',views.AboutView.as_view,name='about'),
    path('interest/<int:pk>',views.InterestDetailView.as_view(),name='interest_detail'),
    path('interest/new/',views.CreateInterestView.as_view(),name='interest_new'),
    path('interest/<int:pk>/edit',views.InterestUpdateView.as_view(),name='interest_edit'),
    path('interest/<int:pk>/delete',views.InterestDeleteView.as_view(),name='interest_remove'),
    path('drafts/',views.DraftListView.as_view,name='post_draft_list'),
    path('interest/<int:pk>/comment/',views.add_comment_to_interest,name='add_comment_to_interest'),
]