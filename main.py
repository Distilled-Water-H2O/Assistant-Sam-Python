# introduction  // author: Distilled Water
"""
- this is an assistant application like siri made with openai

NOTE: this is based of the old OpenAI ChatCompletion.
"""

# libraries
import win32com.client
import speech_recognition as sr
import webbrowser
import openai

# initializing speaker
speaker = win32com.client.Dispatch("SAPI.SpVoice")


# speach recognition
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-uk")
            print(f"user said: {query}\n")
            return query
        except Exception as e:
            return "some error occurred, try again"


openai.api_key = 'sk-API_KEY'


def chat_with_bot(messages):
    chat_log = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return chat_log.choices[0].message

# Upper stuff


def main():
    chat_history = []

    # chat-loop
    while True:
        # taking commands
        print("listening...")
        text = take_command()

        # allow opening Websites
        if 'open youtube' in text.lower():
            speaker.speak("opening youtube")
            webbrowser.open("https://youtube.com")  # add as much as you can

        # handle control
        if text == 'stop':
            break
        if text == 'continue':
            continue

        chat_history.append({
                'role': 'system',
                'content': text
            })

        # Generate a response
        bot_response = chat_with_bot(chat_history)

        print("Sam    :", bot_response['content'])
        speaker.Speak(bot_response['content'])

        chat_history.append({
                'role': 'system',
                'content': bot_response['content']
            })
        
if __name__ == "__main__":
    main()
