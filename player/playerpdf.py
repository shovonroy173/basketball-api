# player/playerpdf.py

from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_player_report_pdf(report):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    p.setFont("Helvetica-Bold", 20)
    p.setTitle("Player Report")

    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, height - 50, f"{report.report_title}'s Performance Report")

    p.setFont("Helvetica", 12)
    y = height - 100

    lines = [
        f"Field Goal Percentage: {report.field_goal_percentage}%",
        f"Rebounds: {report.rebounds}",
        f"Assists: {report.assists}",
        f"Steals and Blocks: {report.steals_and_blocks}",
        f"Projection: {report.projection}",
        f"Overview: {report.overview}",
        "Strengths:",
        *[f"  - {s}" for s in report.strengths],
        "Weaknesses:",
        *[f"  - {w}" for w in report.weaknesses],
    ]

    for line in lines:
        if y < 50:
            p.showPage()
            y = height - 50
        p.drawString(50, y, line)
        y -= 20

    p.showPage()
    p.save()
    buffer.seek(0)

    return buffer
