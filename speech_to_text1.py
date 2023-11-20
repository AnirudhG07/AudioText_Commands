import speech_recognition as sr
def speech_to_text():
    recognizer=sr.Recognizer()

    while True:
        with sr.Microphone() as mic:
            print("Listening, pls go ahead... ")
            recognizer.adjust_for_ambient_noise(mic, duration=1)
            audio=recognizer.listen(mic)
        try:
            text=recognizer.recognize_google(audio)
            print("Recongnised Voice: Converting Speech to text ...")
            return text

        except Exception as e :
            if e == sr.UnknownValueError():
                print("Coudn't understand audio. PLease try again")
                return None
            elif e == sr.RequestError():
                print("Unable to access speech recognition service")
                return None
            else:
                print(e)
                return None
                
        # except sr.UnknownValueError():
        #     print(" Coudn't understand audio. PLease try again")
        #     return None
        # except sr.RequestError():
        #     print("Unable to access speech recognition service")
        #     return None
if __name__=="__main__":
    print(speech_to_text())