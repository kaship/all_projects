import speech_recognition as sr



r=sr.Recognizer()


with sr.Microphone() as source:
    print("bolo")
    audio=r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
    except:
        print("fir se bol")
        
 
a1=0

while a1<10:
   
    with sr.Microphone() as source:
        print(".")
        audio=r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("you:"+text)
            txt=text
        except:
            print("...")
            txt="..."
            
        