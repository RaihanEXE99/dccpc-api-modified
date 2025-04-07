from django.urls import path

from .views import (
    MemberCreateAPIView,
    GalleryListAPIView,
    PanelMemberListAPIView,
    EventListAPIView,
    ContactCreateAPIView,
    EventRetrieveAPIView,
    NoticeListAPIView,
    NoticeRetrieveAPIView
)

urlpatterns = [
    path('members/', MemberCreateAPIView.as_view(), name='member-create'),
    path('gallery/', GalleryListAPIView.as_view(), name='gallery-list'),
    path('panel-members/', PanelMemberListAPIView.as_view(), name='panel-list'),
    path('events/', EventListAPIView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventRetrieveAPIView.as_view(), name='event-detail'),
    path('notices/', NoticeListAPIView.as_view(), name='notice-list'),
    path('notices/<int:pk>/', NoticeRetrieveAPIView.as_view(), name='notice-detail'),
    path('contact/', ContactCreateAPIView.as_view(), name='contact-create'),
]
