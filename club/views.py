from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response

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
                    'education': member['education']
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

    def get_queryset(self):
        queryset = super().get_queryset()
        year = self.request.query_params.get('year')
        if year:
            queryset = queryset.filter(event_date__year=year)
        return queryset



class PanelMemberListAPIView(ListAPIView):
    serializer_class = PanelMemberSerializer
    
    def get_queryset(self):
        category = self.request.query_params.get('category', 'panel')
        return PanelMember.objects.filter(category=category)


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

class ContactCreateAPIView(CreateAPIView):
    serializer_class = ContactRequestSerializer
    queryset = ContactRequest.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contact_request = serializer.save()

        # Send email notification
        try:
            # Prepare context for email template
            email_context = {
                'contact': {
                    'name': contact_request.name,
                    'email': contact_request.email,
                    'phone': contact_request.phone or 'N/A',
                    'address': contact_request.address or 'N/A',
                    'message': contact_request.message
                }
            }

            # Email to club
            club_email = EmailMessage(
                subject=f'New Contact Request from {contact_request.name}',
                body=render_to_string('email/contact_request_club.html', email_context),
                from_email=f'DCC Programming Club <{settings.EMAIL_HOST_USER}>',
                to=['dccpc.official@gmail.com'],
                reply_to=[contact_request.email]
            )
            club_email.content_subtype = 'html'
            club_email.send()

            # Email to sender
            sender_email = EmailMessage(
                subject='We Received Your Message - DCC Programming Club',
                body=render_to_string('email/contact_request_sender.html', email_context),
                from_email=f'DCC Programming Club <{settings.EMAIL_HOST_USER}>',
                to=[contact_request.email],
            )
            sender_email.content_subtype = 'html'
            sender_email.send()

        except Exception as e:
            # Log the error, but still return a successful response
            print(f"Email sending failed: {e}")

        return Response(serializer.data, status=status.HTTP_201_CREATED)