import pyaudio
import wave
filename = input("Filename (*.wav, in directory)")+".wav"
f = wave.open(filename, mode='rb') #opsn
bpm = int(input("BPM")) #input is string gotta be integer lol

chunk = (f.getframerate()*60)//bpm #samplerate (eg. 44100) * 60 seconds per minute then divided (integer) by the bpm

p = pyaudio.PyAudio()   #i never used pyaudio this is my first ever time outputting audio from python. also crap i stepped on my hot pocket
#open stream  
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
#read data  
data = f.readframes(chunk)  

#play stream  
while data:  
    stream.write(data)
    for i in 0,1:
        data = f.readframes(chunk)  

#stop stream  
stream.stop_stream()  
stream.close()  

#close PyAudio  
p.terminate()  
