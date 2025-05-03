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
    pagination_class = None  # Disable pagination for this view to return all images

    def get_queryset(self):
        queryset = super().get_queryset()
        year = self.request.query_params.get('year')
        limit = self.request.query_params.get('limit')
        
        if year:
            queryset = queryset.filter(event_date__year=year)
        
        if limit and limit.isdigit():
            queryset = queryset[:int(limit)]
            
        return queryset


class HomeGalleryListAPIView(ListAPIView):
    """API view that returns only 4 most recent gallery images for the homepage"""
    serializer_class = GallerySerializer
    pagination_class = None  # Disable pagination for this view too
    queryset = Gallery.objects.all()[:4]


class PanelMemberListAPIView(ListAPIView):
    serializer_class = PanelMemberSerializer

    def get_queryset(self):
        # Get the category from query params, default to 'panel' if not provided
        category = self.request.query_params.get('category', 'panel')

        # Define valid categories based on the model choices
        valid_categories = [choice[0] for choice in PanelMember.CATEGORY_CHOICES]

        # Check if the provided category is valid, otherwise default to 'panel'
        # This prevents potential errors if an invalid category is sent.
        # Alternatively, you could raise a ValidationError here if you prefer strict checking.
        if category not in valid_categories:
            category = 'panel' # Or return PanelMember.objects.none() if you prefer empty list for invalid

        # Filter the queryset based on the validated category
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