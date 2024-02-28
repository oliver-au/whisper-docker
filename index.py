import sys
import whisper

def format_time_vtt(seconds):
  """Convert seconds to WebVTT time format."""
  hours, remainder = divmod(int(seconds), 3600)
  minutes, seconds = divmod(remainder, 60)
  milliseconds = (seconds - int(seconds)) * 1000
  return f"{hours:02}:{minutes:02}:{seconds:02}.{int(milliseconds):03}"

def create_vtt_file(segments, file_path):
  with open(file_path, 'w', encoding='utf-8') as file:
    file.write("WEBVTT\n\n")  # WebVTT file header
    for i, segment in enumerate(segments, start=1):
      start_time = format_time_vtt(segment['start'])
      end_time = format_time_vtt(segment['end'])
      text = segment['text']
      file.write(f"{start_time} --> {end_time}\n{text}\n\n")

def transcribe_audio(file_path, whisper_model):
  model = whisper.load_model(whisper_model)  # Adjust model size as needed
  result = model.transcribe(file_path)
  segments = result.get('segments', [])
  vtt_file_name = file_path.rsplit('.', 1)[0] + ".vtt"  # Generate VTT file name from input file
  create_vtt_file(segments, vtt_file_name)

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Usage: python index.py <audio_file_path> <whisper_model>")
    sys.exit(1)
  
  audio_file = sys.argv[1]
  whisper_model = sys.argv[2]
  transcribe_audio(audio_file, whisper_model)
