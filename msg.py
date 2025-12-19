import random, time, urllib, os
from fbchat import Client
import fbchat.models as models
from datetime import datetime
from PIL import Image

uname = #change to your username 
pwd =#and password
client = Client(uname, pwd)

red = "\033[1;31m"
blue = "\033[1;34m"
green = "\033[032m"
yellow = "\033[93m"
res = "\033[00m"
rev = "\033[7m"

def countdown(msg,id, na):
    d = input(yellow+'\nDate(Y-M-D)'+red+'[Optional]'+res+yellow+': '+res) #Leaving the date blank uses today's date
    t = input(yellow+'Time 24H format(H:M:S): '+res)
    if len(d) == 0:
        d = datetime.now().strftime("%Y-%m-%d")
    tos = d + " " + t
    print(yellow+"Sending message to "+res+red+na+yellow+" at :"+red+tos+res)
    br = datetime.strptime(tos, '%Y-%m-%d %H:%M:%S')
    while tos!=datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
        td = br - datetime.now()
        sec = td.days * 24 * 3600 + td.seconds
        years,aa = divmod(sec, 31104000)
        months, bb = divmod(aa, 2592000)
        days, cc = divmod(bb, 86400)
        hours, dd = divmod(cc, 3600)
        mins, ee = divmod(dd, 60)
        time23 = '{:2d}years, {:2d}months, {:2d}days, {:2d}hrs:{:2d}mins:{:2d}secs left'.format(years,months,days,hours,mins, ee).strip()
        print(time23 ,end="\r")
        time.sleep(1)
        sec -= 1
    fbmsg(msg, id)
    print(red+"\" "+ msg+ "\" "+res+"sent to "+red+na+res+" at "+red+tos+res)

def getuname():
    username = str(input(yellow+"\nUser's name: "+res))
    out = client.searchForUsers(username)
    for xx in out:
        if xx.is_friend:
            print(yellow+"\n"+xx.name+"\n"+xx.uid+'\n'+res)
            na, id, photo = xx.name, xx.uid, xx.photo
            return (id, na, photo)
    print(red+"Sorry, "+yellow+username+red+" is not in your friends list."+res)
    exit()

def dl_img(url, na):
    location = os.getcwd()+'/'+na+'.jpg'
    print(yellow+'Downloading image...\n'+res)
    urllib.request.urlretrieve(url, location)
    return(location)


def fbmsg(msg, UID):
    client.sendMessage(msg, thread_id=UID,
                       thread_type=models.ThreadType.USER) 


def timer():
    id, na, pic = getuname()
    pic1 = dl_img(pic, na)
    img = Image.open(pic1)
    img.show()
    print(red+"If the image doesn't show please check temp dir.\n"+res)
    if not(input('Press'+yellow+' [Enter] '+res+'to confirm user.\n')):
        msg = str(input(yellow+"\nMessage:    "+res))
        countdown(msg, id, na)
    else:
        exit()
    os.remove(pic1)

def spam():
    id, na, pic = getuname()
    pic1 = dl_img(pic, na)
    img = Image.open(pic1)
    img.show()
    print(red+"If the image doesn't show please check temp dir.\n"+res)
    if not(input('Press'+yellow+'[Enter]'+res+'to confirm user.')):
        msg = input(yellow+"\nMessage:    "+res)
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        location = "logs/" + date + ".log"
        out = open(location, "w")
        while True:
            ctime = datetime.now().strftime("%H:%M:%S")
            ra = random.randint(0, 50)
            fbmsg(msg, id)
            oin = str(green+"\"" + msg + "\"" + " sent to " + str(na) + " at " +
                     str(ctime) + " next message in " + str(ra) + " seconds."+res)
            out.write(oin)
            out.write("\n")
            print(oin)
            # Pauses the in range 0 - 50 seconds (randomly) so that facebook wont lock your account.
            time.sleep(ra)
            msg = str(random.randint(0,999999999999999999999))#You can change this to any custom message.
        out.close()
    else:
        exit()
    os.remove(pic1)

def rep():
    print("")
    choose = input(red+"[1]Spam\n"+res+
                   yellow+"[2]Timer\nChoose:     "+res)
    if choose == "1":
        try:    
            spam()
        except KeyboardInterrupt:
            print("\nExiting...")
        again = input("again?(y/n)")
        if again.lower()=="n":
            exit()
    elif choose == "2":
        try:    
            timer()
        except KeyboardInterrupt:
            print("\nExiting...")
        again = input("again?(y/n)")
        if again.lower()=="n":
            exit()
    else:
        print("Unknown input.")

while True:
    try:
        rep()
    except KeyboardInterrupt:
        print('\nExitiing...')
        exit()
