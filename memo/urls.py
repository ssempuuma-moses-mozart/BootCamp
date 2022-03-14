from django.urls import path
from .views import MemoHomeView, MemoUpdateView, MemoDeleteView,MemoDetailView


urlpatterns = [
    path('', MemoHomeView.as_view(), name = 'index'),
     path('memo/<int:pk>/update', MemoUpdateView.as_view(), name='update'),
      path('memo/details', MemoDetailView.as_view(), name='details'),
    path('memo/<int:pk>/delete', MemoDeleteView.as_view(), name='delete'),
]