import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listner = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
                print("listning....")
                voice = listner.listen(source)
                info = listner.recognize_google(voice)
                print(info)
                return info
    except:
        pass



def send_email(receiver,subject,message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('divax12345@gmail.com', 'diya27divax')
        email = EmailMessage()
        email['From'] = 'divax12345@gmail.com'
        email['To'] = receiver
        email['Subject'] = subject
        email.set_content(message)
        server.send_message(email)
    except:
        print ('Something went wrong...')

email_list={
    'DJ' : 'divaxcontacts@gmail.com',
    'Parul' : 't0120cse481@paruluniversity.ac.in',
    'myself': 'divax12345@gamil.com',
    'diabolic' : 'bollytv.knowledge@gmail.com'
    
}

def get_email_info():
    talk("TO WHOM U WANT TO SEND THE MAIL")
    name = get_info()
    receiver = email_list[name]
    print('the message will be sent to : - ' + receiver)
    talk("tell me the subject of the mail?")
    subject = get_info()
    talk("tell me be the body of the mail")
    message = get_info()
    send_email(receiver,subject,message)
    talk('your email is sent, have fun....')
    


get_email_info()



