#!pip install -U faster-whisper ffmpeg-python
#!apt-get install -y ffmpeg

#m3u8_url = 'https://fast.wistia.com/embed/medias/gukws7niwp.m3u8'
##m3u8_url = 'https://fast.wistia.com/embed/medias/sttq0tqmic.m3u8'
#
#m3u8_url_tmp = input('Enter M3U8 URL: ').strip()
#m3u8_url = m3u8_url_tmp if m3u8_url_tmp else m3u8_url
#
#m3u8_url

import ffmpeg

def extract_audio_from_m3u8(m3u8_url, output_path='output.mp3'):
    stream = ffmpeg.input(m3u8_url, hwaccel="cuda", hwaccel_device="0")
    stream = ffmpeg.output(stream, output_path, acodec="libmp3lame", vn=None, vcodec='h264_nvenc', preset='ultrafast')
    ffmpeg.run(stream, overwrite_output=True)

from faster_whisper import WhisperModel

def transcribe_audio(audio_path, model_size="small"):
    model = WhisperModel(model_size, device="auto", compute_type="int8")
    segments, info = model.transcribe(audio_path, language="ja")
    segment_list = [] # Use a list to collect segments
    for segment in segments:
        print(segment.text)
        segment_list.append(segment.text) # Append segment text to the list
    return " ".join(segment_list) # Join the list elements at the end

def m3u8_to_transcript(m3u8_url, audio_path='output.mp3', model_size="small"):
    extract_audio_from_m3u8(m3u8_url, audio_path)
    transcript = transcribe_audio(audio_path, model_size)
    return transcript


#url = m3u8_url
#text = m3u8_to_transcript(url, model_size='medium')
#
#
#display(text)
#
#
#