import pyttsx3

def text_to_speech(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('voice', 'en')
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    text = input("Enter text: ")
    text_to_speech(text)
