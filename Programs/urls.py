from django.urls import path
from Common.views import ProgramsView
from Programs.views import ProgramsDetailView

urlpatterns = [
    path('', ProgramsView.as_view(), name='plans-view'),
    path('<int:pk>/', ProgramsDetailView.as_view(), name='plans-detail'),
]