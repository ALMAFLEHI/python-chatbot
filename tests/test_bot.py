from chatbot.bot import get_response

def test_greeting_response():
    """Test that greetings get appropriate responses"""
    assert get_response("hi") in ["Hello!", "Hi there!", "Greetings!"]
    assert get_response("HELLO") in ["Hello!", "Hi there!", "Greetings!"]

def test_unknown_input():
    """Test that unknown input gets default response"""
    assert get_response("asdfghjkl") in ["I didn't understand that.", "Could you rephrase that?", "I'm still learning!"]

def test_joke_responses():
    """Test joke responses"""
    assert get_response("Tell me a joke") in [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!"
    ]

def test_empty_input():
    """Test empty input handling"""
    assert get_response("") == "Please type something!"