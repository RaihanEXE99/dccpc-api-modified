import datetime

from django.contrib import admin

from .models import (
    Gallery,
    Member,
    PanelMember,
    Event,
    ContactRequest,
    Notice
)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'created_at')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = (
        'name',
        'batch',
        'roll',
        'phone',
        'image',
        'joined_date',
        'created_at'
    )
    list_filter = ('batch',)
    search_fields = ('name', 'email', 'roll', 'phone')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', ('email', 'phone'), ('education', 'image'), ('batch', 'roll'))
        }),
        ('Additional Information', {
            'fields': ('problem_solving_experience', 'expectation', 'joined_date')
        }),
        ('Social Media', {
            'fields': ('facebook', 'github', 'linkedin'),
            'classes': ('collapse',)  # Collapsible section
        }),
        ('Payment Details', {
            'fields': ('transaction_id',),
        })
    )

    actions = ['mark_as_joined_today']

    def mark_as_joined_today(self, request, queryset):
        """Mark selected members as joined today."""
        queryset.update(joined_date=datetime.date.today())
        self.message_user(request, "Selected members marked as joined today.")

    mark_as_joined_today.short_description = "Mark joined date as today"


@admin.register(PanelMember)
class PanelMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'ordering', 'created_at')
    list_editable = ('ordering',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'designation', 'ordering', 'image')
        }),
        ('Social Media', {
            'fields': ('facebook', 'github', 'linkedin'),
            'classes': ('collapse',)
        })
    )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    empty_value_display = '-empty-'


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'created_at')
    empty_value_display = '-empty-'