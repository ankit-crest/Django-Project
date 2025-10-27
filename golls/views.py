from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.template import loader
from django.template.context_processors import request
from .models import Golls as Gls
from django.forms.models import model_to_dict
from gtts import gTTS
# import speech_recognition as sr 
# from pydub import AudioSegment
import io
# from pydub.utils import which
# AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the golls index.")

def add(request):
    return HttpResponse("Call Add data.")


def show(request,slug):
    return HttpResponse(f"Call Show data for {slug}.")

def show_list(request):
      template = loader.get_template('myfirst.html')
      context = {}
      return HttpResponse(template.render(context, request))

def show_next_list(request):
      template=loader.get_template('myfirst.html')
      context = {}
      return HttpResponse(template.render(context, request))
def textInput(request):
      template=loader.get_template('inputText.html')
      context = {}
      return HttpResponse(template.render(context, request))


def voice_speak_view(request):
      template=loader.get_template('speak_and_listen.html')
      context = {}
      return HttpResponse(template.render(context, request))

def add_gls(request):
    
    gls = Gls(firstName="John", lastName="Doe")
    # gls.save()   
    gls_objects = Gls.objects.all()

    data = []
    for obj in gls_objects:
        data.append({
            "id": obj.id,
            "firstName": obj.firstName,
            "lastName": obj.lastName,
        })

    return render(request,'myfirst.html',{'data':data})

def edit(request,id):
    gls=Gls.objects.get(id=id)
    data = model_to_dict(gls)
    gls.firstName = "John-"+id
    gls.lastName = "Doe-"+id
    gls.save()
    gls=Gls.objects.get(id=id)
    data = model_to_dict(gls)

    return redirect('add_gls') 
    return JsonResponse(data, safe=False)

def delete(request,id):
    gls=Gls.objects.get(id=id)
    gls.delete()
    gls=Gls.objects.get()
    data = model_to_dict(gls)
    # return JsonResponse(data, safe=False)
    return redirect('add_gls') 

    
def speak_text(request):
    # text = request.GET.get('text', '')
    text = "This is the text file"
    if not text:
        return HttpResponse("No text provided")
    
    # Convert text to speech
    tts = gTTS(text)
    audio_fp = io.BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    
    # Return audio response
    return HttpResponse(audio_fp.read(), content_type="audio/mpeg")

def voice_page(request):
      template=loader.get_template('voice_page.html')
      context = {}
      return HttpResponse(template.render(context, request))


# Ensure pydub finds ffmpeg
import os

FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"  # Update this

# Check if ffmpeg exists
if not os.path.isfile(FFMPEG_PATH):
    raise FileNotFoundError(f"ffmpeg not found at {FFMPEG_PATH}")

# AudioSegment.converter = FFMPEG_PATH

# def process_audio(request):

#     if request.method == "POST" and request.FILES.get("audio"):
#         audio_file = request.FILES["audio"]

#         if not audio_file:
#             return JsonResponse({"error": "No audio file uploaded"})

#         # Convert uploaded audio to proper WAV
#         try:
#          audio_segment = AudioSegment.from_file(audio_file)  # auto detects format
#          wav_io = io.BytesIO()
#          audio_segment.export(wav_io, format="wav")
#          wav_io.seek(0)
#         except Exception as e:
#             # ffmpeg_path = which("ffmpeg")
#             return JsonResponse({"ffmpeg_path": audio_segment})
#             return JsonResponse({"error": f"Audio conversion failed: {str(e)}"})

#         # Speech recognition
#         recognizer = sr.Recognizer()
#         try:
#             with sr.AudioFile(wav_io) as source:
#                 audio = recognizer.record(source)
#             text = recognizer.recognize_google(audio)
           
#         except Exception as e:
#             return JsonResponse({"error": f"Speech recognition failed: {str(e)}"})

#         # Convert text to speech using gTTS
#         try:
#             tts = gTTS(text)
#             audio_fp = io.BytesIO()
#             tts.write_to_fp(audio_fp)
#             audio_fp.seek(0)
#         except Exception as e:
#             return JsonResponse({"error": f"TTS failed: {str(e)}"})

#         # Return MP3 audio response
#         response = HttpResponse(audio_fp.read(), content_type="audio/mpeg")
#         response["Content-Disposition"] = 'inline; filename="response.mp3"'
#         return response

#     return JsonResponse({"error": "No audio received"})
