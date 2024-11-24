# Natasha's File
import os
from pydub import AudioSegment


def convert_to_wav(input_path, output_path=None):
    if not output_path:
        output_path = os.path.splitext(input_path)[0] + ".wav"
    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, format="wav")
    return output_path