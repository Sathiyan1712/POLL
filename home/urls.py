from django.urls import path

from home.views import all_polls ,poll_detail,create_poll,delete_poll

urlpatterns = [
    path("polls/", all_polls, name="all-polls"),
    path("polls/<int:poll_id>/", poll_detail, name="poll-detail"),
    path("polls/create/", create_poll, name="create-poll"),
    
    path("polls/<int:poll_id>/delete/", delete_poll, name="poll-delete"),

]
