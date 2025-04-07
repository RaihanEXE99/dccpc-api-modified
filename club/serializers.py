from rest_framework import serializers

from club.models import Member, Gallery, PanelMember, Event, ContactRequest, Notice


class MemberSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        email = attrs.get('email')
        if Member.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ['Email already registered']})
        return attrs

    class Meta:
        model = Member
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class PanelMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PanelMember
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class ContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'
