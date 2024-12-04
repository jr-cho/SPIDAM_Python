# Natasha's File
import os
from pydub import AudioSegment


def convert_to_wav(input_path, output_path=None):
    if not output_path:
        output_path = os.path.splitext(input_path)[0] + ".wav"
    try:
        audio = AudioSegment.from_file(input_path)
        audio.export(output_path, format="wav")
        if os.path.exists(output_path):
            print(f"WAV file created: {output_path}")
        else:
            print("Error: WAV file not created.")
        return output_path
    except Exception as e:
        raise ValueError(f"Conversion failed: {e}")
