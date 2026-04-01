
from django.shortcuts import render
from django.http import JsonResponse
import random
import requests

# This must be defined outside the function to track the last message
last_msg = ""

def index(request):
    return render(request, 'template_chatbot.html')

def get_first_message(request):
    return JsonResponse({"message": "Hello there! I am your chatbot robot."})

def chat_response(request):
    global last_msg
    # Get the 'message' parameter from the frontend (Vue.js)
    user_text = request.GET.get('message', '').strip()

    # Repeat check: Prevent the user from sending the same message twice in a row
    if user_text == last_msg and user_text != "":
        return JsonResponse({"message": "STOP REPEATING YOURSELF!"})
    
    last_msg = user_text
    txt = user_text.lower()

    # 1. Image Logic: Returns a random image from picsum
    if txt == "gimme image":
        rid = random.randint(1, 9999)
        return JsonResponse({"message": f'<img src="https://picsum.photos/200/300?id={rid}">' })

    # 2. Wikipedia Logic: Creates a clickable link for a given topic
    elif txt.startswith("tell me about "):
        topic = user_text[14:].strip()
        url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
        return JsonResponse({"message": f'Wikipedia: <a href="{url}" target="_blank">{url}</a>'})

    # 3. Help Logic: Lists available commands
    elif txt == "help" or txt == "h":
        return JsonResponse({"message": "Available commands: 'help', 'gimme image', 'tell me about [topic]', 'weather in [city]'"})

    # 4. Weather Logic: Returns a simple weather message
    elif txt.startswith("weather in "):
        city = txt[11:].strip()
        # Mock data for assignment purposes
        return JsonResponse({"message": f"The weather in {city.capitalize()} is currently 15°C and sunny. ☀️"})

    # Default Message: When the robot doesn't recognize the input
    return JsonResponse({"message": "I didn't understand. Try 'help' to see what I can do!"})