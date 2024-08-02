import openai

def transcribe_audio(openai_API, audio_file_path, openai_model):
    openai.api_key = openai_API

    audio_file= open(audio_file_path, "rb")
    transcript = openai.Audio.transcribe(openai_model, audio_file)
    return transcript["text"]
