import ffmpeg

def convert_to_mp3audio(input_filename, output_filename, audioformat = "mp3"):
    file = ffmpeg.input(input_filename)
    audio = file.audio.filter("atrim", duration = 30)
    audio_out = ffmpeg.output(audio, output_filename, format = audioformat)
    ffmpeg.run(audio_out)
