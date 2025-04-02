import random
import time
from openai import OpenAI
from dotenv import load_dotenv
import os
from . import responses
from .nlp_utils import preprocess_text
from .alien_persona import ALIEN_PROMPT


# Initialize OpenAI
load_dotenv()
client = OpenAI(api_key=os.getenv("your_key_here"))

# Rate limiting
last_api_call = 0

def get_alien_response(user_input):
    """Get AI response with error handling"""
    global last_api_call
    
    # Rate limit (1 call per second)
    if time.time() - last_api_call < 1:
        time.sleep(1 - (time.time() - last_api_call))
    last_api_call = time.time()

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": ALIEN_PROMPT},
                {"role": "user", "content": user_input}
            ],
            temperature=0.9,
            timeout=10
        )
        return response.choices[0].message.content
        
    except Exception as e:
        error_msg = str(e).encode('ascii', 'ignore').decode('ascii')
        fallbacks = [
            "*static* My translator broke! Try again later.",
            "*glitch* Zog-7 to mothership: Need more cosmic credits!",
            "*beep boop* Human, your planet's WiFi is terrible!"
        ]
        return random.choice(fallbacks)

def get_response(user_input):
    """Hybrid response system"""
    # Rule-based first
    tokens = preprocess_text(user_input)
    for intent in responses.RESPONSES.values():
        if 'patterns' in intent:
            for pattern in intent['patterns']:
                if pattern in tokens:
                    return random.choice(intent['responses'])
    
    # AI fallback
    return get_alien_response(user_input)

def run_chatbot():
    """CLI version"""
    print("👽 Zog-7: *blinking lights* Greetings flesh-bag!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            print(random.choice(responses.RESPONSES["alien_farewell"]["responses"]))
            break
        print(f"👽 Zog-7: {get_response(user_input)}")