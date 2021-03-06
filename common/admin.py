from django.contrib import admin
from .models import UserProfile, MemberChatRoom


admin.site.register(
    UserProfile,
    list_display=["__unicode__", "id", "type"],
    list_display_links=["id"],
)
admin.site.register(MemberChatRoom)
