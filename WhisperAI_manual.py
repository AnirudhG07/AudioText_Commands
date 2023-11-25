import openai, os, playsound
from openai import OpenAI

OPENAI_API_KEY = "YOUR_API_KEY"
client = OpenAI(api_key=OPENAI_API_KEY)

response = client.audio.speech.create(
    model="tts-1-hd",   # "tts-1", "tts-1-hd" are 2 models
    voice="onyx",    # alloy, echo, fable, onyx, nova, and shimmer. Choose any of these voices.
    speed=1.0,  # speed varies betwen 0.0 to 4.0. 1.0 is default
    response_format="mp3", # mp3, opus, aac, and flac are supported audio formats.
    input="Hello world! This is a streaming test.",
)
response.stream_to_file("output.mp3")
# playsound "output.mp3"
playsound.playsound("output.mp3")
os.remove("output.mp3")