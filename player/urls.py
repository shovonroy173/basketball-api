from django.urls import path
from .views import *

urlpatterns = [
    path('report/<int:report_id>/', generate_player_pdf_view, name='player_report_pdf'),
    path('report/send-mail/<int:report_id>/', sent_mail_player_pdf_view, name='send-player-pdf-email'),
    path('list/', PlayerContextListCreateView.as_view(), name='player-list'),
    path('user-list/', PlayerUserList.as_view(), name='player-user-list'),
    path('report-list/', PlayerReportListCreateView.as_view(), name='player-report-list'),
    path('report-detail/<int:pk>/', PlayerReportDetailView.as_view(), name='player-report-detail'),
]
