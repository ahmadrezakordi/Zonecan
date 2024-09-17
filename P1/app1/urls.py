from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views

from django.conf import settings
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('employeeregister/', EmployeeRegisterView.as_view(), name='employee-register'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('kelasor/', KelasorView.as_view(), name='kelasor'),
    path('kelasor/create/', KelasorCreateView.as_view(), name='kelasor-create'),
    path('kelasor/<int:pk>/', KelasorDetailView.as_view(), name='kelasor-detail'),
    path('kelasor/<int:pk>/update/', KelasorUpdateView.as_view(), name='kelasor-update'),
    path('kelasor/<int:pk>/delete/', KelasorDeleteView.as_view(), name='kelasor-delete'),

    path('kelasor/<int:pk>/parvande/', ParvandeView.as_view(), name='parvande-list'),
    path('kelasor/<int:pk>/parvande/create/', ParvandeCreateView.as_view(), name='parvande-create'),

    path('parvande/<int:pk>/', ParvandeDetailView.as_view(), name='parvande-detail'),
    path('parvande/update/<int:pk>/', ParvandeUpdateView.as_view(), name='parvande-update'),
    path('parvande/<int:pk>/delete/', ParvandeDeleteView.as_view(), name='parvande-delete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
