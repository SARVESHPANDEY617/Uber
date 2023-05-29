from django.urls import path,include
from.views import*

from users.views import*

urlpatterns  = [ 
    path('get-all-Students',GetStudentsView.as_view()),
    path('get-and-save',GetOrdersView.as_view()),
    path('delete-student/<int:pk>',DeleteStudentsView.as_view()),
]


