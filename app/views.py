from django.shortcuts import render
from .models import *
import requests

# Create your views here.


def home(request):
    jobs = Projects.objects.all()
    tools = TechstackTools.objects.all()
    backends = TechstackBackend.objects.all()
    frontends = TechstackFrontend.objects.all()
    databases = TechstackDatabases.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        whatsapp = request.POST.get("whatsapp")
        message = request.POST.get("message")

        send_contact_to_discord(name, email, whatsapp, message)
    context = {
        "jobs": jobs,
        "tools": tools,
        "backends": backends,
        "frontends": frontends,
        "databases": databases
    }
    return render(request, "index.html", context)

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1491138668445040881/IzwgD1qCvhgqzHat8Gy1Bco0LUauLTCQo4uMFQsRD3e9q_Mqz9ANURDhaGNse20S_evH"

def send_contact_to_discord(name, email, whatsapp, message):
    content = f"""
📩 New Contact Message

👤 Name: {name}
📧 Email: {email}
📱 WhatsApp: {whatsapp}

📝 Message:
{message}
"""

    try:
        requests.post(DISCORD_WEBHOOK_URL, json={"content": content})
    except Exception as e:
        print("Error sending to Discord:", e)

def error(request):
    return render(request, "error.html")


