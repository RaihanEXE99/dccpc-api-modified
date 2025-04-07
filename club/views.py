from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from club.models import (
    Member,
    Gallery,
    PanelMember,
    Event,
    ContactRequest,
    Notice
)
from club.serializers import (
    MemberSerializer,
    GallerySerializer,
    PanelMemberSerializer,
    EventSerializer,
    ContactRequestSerializer,
    NoticeSerializer
)


class MemberCreateAPIView(CreateAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        if response.status_code == status.HTTP_201_CREATED:
            member = response.data
            member_email = member['email']

            email_body = render_to_string('email/registration.html', {
                'member': {
                    'email': member_email,
                    'name': member['name'],
                    'batch': member['batch'],
                }
            })

            email = EmailMessage(
                subject='Welcome to DCC Programming Club!',
                body=email_body,
                from_email=f'DCC Programming Club <{settings.EMAIL_HOST_USER}>',
                cc=['dccpc.official@gmail.com'],
                to=[member_email]
            )
            email.content_subtype = 'html'
            email.send()

        return response


class GalleryListAPIView(ListAPIView):
    serializer_class = GallerySerializer
    queryset = Gallery.objects.all()


class PanelMemberListAPIView(ListAPIView):
    serializer_class = PanelMemberSerializer
    queryset = PanelMember.objects.all()


class EventListAPIView(ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class EventRetrieveAPIView(RetrieveAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class ContactCreateAPIView(CreateAPIView):
    serializer_class = ContactRequestSerializer
    queryset = ContactRequest.objects.all()


class NoticeListAPIView(ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer


class NoticeRetrieveAPIView(RetrieveAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
