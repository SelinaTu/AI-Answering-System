import speech_recognition as sr

QUESTIONS = {
    "budget": "What is your budget?",
    "calorie_limit": "What is your calorie limit?",
    "dietary": "Do you have any dietary preferences (e.g., vegetarian, halal)?",
    "style": "What food style do you want (e.g., light, spicy, high-protein)?",
}


def _ask_with_voice(prompt: str) -> str:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(prompt)
        audio = recognizer.listen(source)
    return recognizer.recognize_google(audio)


def get_preferences(use_voice: bool = False) -> dict:
    """Gather user preferences via text or live voice input."""
    prefs = {}
    for key, q in QUESTIONS.items():
        if use_voice:
            try:
                prefs[key] = _ask_with_voice(q)
                continue
            except Exception as exc:
                print(f"Voice input failed: {exc}. Falling back to text.")
        prefs[key] = input(q + " ")
    return prefs
