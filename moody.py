#moody.py
def mood_response(mood):
    responses = {
        'happy': "I'm glad you're feeling happy today!",
        'sad': "I'm sorry to hear you're feeling sad.",
        'okay': "It's alright to feel okay sometimes.",
        'excited': "That's great! What are you excited about?",
        'angry': "Take a deep breath and try to relax.",
        'calm': "It's nice to feel calm and peaceful.",
        'energetic': "Sounds like you have a lot of energy today!",
        'tired': "Take it easy and get some rest if you're feeling tired.",
        'bored': "Let's find something fun to do!",
        'anxious': "Remember to take deep breaths and focus on the present moment.",
        'confused': "It's okay to feel confused. Take your time to figure things out."
        # Add more mood responses as needed
    }
    return responses.get(mood.lower(), "I'm not sure how to respond to that.")

# main.py
import moody

def main():
    mood = input("How are you feeling today? ")
    print(moody.mood_response(mood))

if __name__ == "__main__":
    main()