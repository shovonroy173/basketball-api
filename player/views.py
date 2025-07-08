from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,  FileResponse, Http404
from .playerpdf import generate_player_report_pdf
from rest_framework import generics, permissions
from django.core.mail import EmailMessage
from django.conf import settings
from .models import *
from .serializers import *

def generate_player_pdf_view(request, report_id):
    try:
        report = PlayerReport.objects.get(id=report_id)
    except PlayerReport.DoesNotExist:
        raise Http404("Report not found.")

    pdf_buffer = generate_player_report_pdf(report)
    pdf_buffer.seek(0) 
    file_name = f"{report.player_name.full_name}_report.pdf"
    return FileResponse(pdf_buffer, as_attachment=True, filename=file_name)


def sent_mail_player_pdf_view(request, report_id):
    try:
        report = PlayerReport.objects.get(id=report_id)
    except PlayerReport.DoesNotExist:
        raise Http404("Report not found.")

    # Generate PDF
    pdf_buffer = generate_player_report_pdf(report)
    pdf_buffer.seek(0)

    # File name
    file_name = f"{report.player_name.full_name}_report.pdf"

    # Compose email
    email = EmailMessage(
        subject=f"Player Report - {report.player_name.full_name}",
        body=f"Hi {report.player_name.full_name},\n\nPlease find your player report attached.",
        from_email= settings.EMAIL_HOST_USER,
        to=[report.player_name.email],       
    )

    # Attach PDF
    email.attach(file_name, pdf_buffer.read(), 'application/pdf')
    email.send(fail_silently=False)

    # Return file as download as well (optional)
    # pdf_buffer.seek(0)
    # return FileResponse(pdf_buffer, as_attachment=True, filename=file_name)
    return HttpResponse("Email with PDF sent successfully.")



class PlayerContextListCreateView(generics.ListCreateAPIView):
    serializer_class = PlayerSerializer
    # permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Player.objects.all()
        return Player.objects.all()
        return Player.objects.filter(players__player_name=user).distinct()

    def perform_create(self, serializer):
        serializer.save()


class PlayerUserList(generics.ListAPIView):
    serializer_class = PlayerUserSerializer
    queryset = User.objects.filter(is_player=True)




class PlayerReportListCreateView(generics.ListCreateAPIView):
    serializer_class = PlayerReportSerializer
    # permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return PlayerReport.objects.all()
        # return PlayerReport.objects.all()
        return PlayerReport.objects.filter(player_name=user).distinct()

    def perform_create(self, serializer):
        serializer.save()



class PlayerReportDetailView(generics.RetrieveAPIView):
    serializer_class = PlayerReportSerializer
    lookup_field = 'pk'
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return PlayerReport.objects.all()
        return PlayerReport.objects.filter(player_name=user)