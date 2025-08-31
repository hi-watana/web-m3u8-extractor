import ffmpeg
from faster_whisper import WhisperModel

def _extract_audio_from_m3u8(m3u8_url, output_path='output.mp3'):
	stream = ffmpeg.input(m3u8_url, hwaccel="cuda", hwaccel_device="0")
	stream = ffmpeg.output(stream, output_path, acodec="libmp3lame", vn=None, vcodec='h264_nvenc', preset='ultrafast')
	ffmpeg.run(stream, overwrite_output=True)

def _transcribe_audio(audio_path, model_size="small", language="ja"):
	model = WhisperModel(model_size, device="auto", compute_type="int8")
	segments, info = model.transcribe(audio_path, language=language)
	segment_list = [] # Use a list to collect segments
	for segment in segments:
		print(segment.text)
		segment_list.append(segment.text) # Append segment text to the list
	return " ".join(segment_list) # Join the list elements at the end

def _m3u8_to_transcript(m3u8_url, audio_path='output.mp3', model_size="small", language="ja"):
	_extract_audio_from_m3u8(m3u8_url, audio_path)
	transcript = _transcribe_audio(audio_path, model_size, language)
	return transcript
# ...existing code from m3u8_to_text.py...
