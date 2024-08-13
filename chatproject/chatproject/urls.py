from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_chat(request):
    return redirect('chat:index')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include(('chat.urls', 'chat'), namespace='chat')),
    path('', redirect_to_chat, name='root'),
]