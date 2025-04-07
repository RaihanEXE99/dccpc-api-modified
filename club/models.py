from django.core.validators import FileExtensionValidator
from django.db import models
from tinymce.models import HTMLField


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='gallery/',
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'
        db_table = 'club_gallery'
        ordering = ['-created_at']


class Member(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(
        upload_to='members/',
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])]
    )
    batch = models.IntegerField(default=0)
    education = models.CharField(max_length=100)
    roll = models.IntegerField(default=0)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    problem_solving_experience = models.CharField(max_length=255)
    expectation = models.CharField(max_length=255)
    joined_date = models.DateField(null=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    github = models.CharField(max_length=255, null=True, blank=True)
    transaction_id = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'
        db_table = 'club_members'
        ordering = ['-created_at']


class PanelMember(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(
        upload_to='panel_members/',
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])]
    )
    designation = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    github = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    ordering = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Panel Member'
        verbose_name_plural = 'Panel Members'
        db_table = 'club_panel_members'
        ordering = ['ordering']


class Event(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])],
        upload_to='events/',
        null=True
    )
    details = HTMLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        db_table = 'club_events'
        ordering = ['-created_at']


class ContactRequest(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contact Request'
        verbose_name_plural = 'Contact Requests'
        db_table = 'club_contact_requests'
        ordering = ['-created_at']


class Notice(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField(null=True, blank=True)
    file = models.FileField(
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'pdf', 'docx', 'doc'])],
        null=True,
        blank=True,
        upload_to='notices/'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Notice'
        verbose_name_plural = 'Notices'
        ordering = ['-created_at']
