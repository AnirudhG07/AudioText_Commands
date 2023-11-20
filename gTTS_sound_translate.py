from gtts import gTTS
import playsound
from googletrans import Translator
import os

def translate_text(text, target_language='ja'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text
def gtts_sound(gtts_sentence):

    # Use gTTS to convert the description to speech
    tts = gTTS(text=gtts_sentence, lang='en')
    # lang='...'
    # en	English
    # es	Spanish
    # fr	French
    # de	German
    # it	Italian
    # ja	Japanese
    # ko	Korean
    # zh-CN	Mandarin Chinese (China Mainland)
    # zh-TW	Mandarin Chinese (Taiwan)
    # pt-BR	Portuguese (Brazil)
    # ru	Russian
    # hi	Hindi
    # ar	Arabic
    # ta	Tamil
    # te	Telugu
    # tr	Turkish
    # vi	Vietnamese

    # Save the generated speech to a file (e.g., "gtts_sentence.mp3")
    tts.save("gtts_sentence.mp3")

    # Play the audio using the playsound library
    playsound.playsound("gtts_sentence.mp3")
    os.remove("gtts_sentence.mp3")


    return
if __name__ == "__main__":
    gtts_sent=input("Input a sentence: ")
    gtts_sent=translate_text(gtts_sent)
    print(gtts_sent)
    gtts_sound(gtts_sent)

