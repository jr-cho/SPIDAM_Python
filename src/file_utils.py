# Natasha's File
from pydub import AudioSegment

m4a_file = './data/clap.m4a'
wav_filename = 'output.wav'

def convert(m4a_file): 
    sound = AudioSegment.from_file(m4a_file, format='m4a')
    file_handle = sound.export(wav_filename, format='wav')