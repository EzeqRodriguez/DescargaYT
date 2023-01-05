from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from pytube import YouTube



def audio_video(request):
    
    
    if request.method == 'POST':
    
        link = request.POST['link']
        
        vid = YouTube(link)
        
        descarga = vid.streams.get_highest_resolution()
        
        descarga.download()
        
        return render(request, 'pagina/index.html')
    return render(request, 'pagina/index.html')
    
    

def audio(request):
    
    
    if request.method == 'POST':
    
        linkA = request.POST['linkA']
        
        aud = YouTube(linkA)
        
        descarga = aud.streams.get_audio_only()
        
        descarga.download()
        
        return render(request, 'pagina/audio.html',)
    return render(request, 'pagina/audio.html')
