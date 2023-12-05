"""Admin Posts module."""

# Django
from django.contrib import admin

# Models
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = ('pk', 'user', 'title', 'photo')
    list_editable = ('title', 'photo')

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'title',
    )

    list_filter = (
        'created',
        'modified',
    )

    fieldsets = (
        ('Data post', {
            'fields': (
                'title', 'photo'
            ),
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),
                ('user', 'profile')
            ),
        }),
    )

    readonly_fields = ('created', 'modified', 'user')