from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from pytube import YouTube



def audio_video(request):
    
    
    if request.method == 'POST':
    
        link = request.POST['link']
        
        yt = YouTube(link)
        
        ys = yt.streams.get_highest_resolution()
        
        ys.download()
        
        return render(request, 'pagina/index.html')
    return render(request, 'pagina/index.html')
    
    

def audio(request):
    
    
    if request.method == 'POST':
    
        linkA = request.POST['linkA']
        
        yt = YouTube(linkA)
        
        ys = yt.streams.get_audio_only()
        
        ys.download()
        
        return render(request, 'pagina/audio.html',)
    return render(request, 'pagina/audio.html')