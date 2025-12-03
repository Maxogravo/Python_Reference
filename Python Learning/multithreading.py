import threading
import time

def walk_dog():
    time.sleep(8)
    print("You finished walking dog")
def empty_rubbish():
    time.sleep(2)
    print("You got rid of the rubbish")
def get_mail():
    time.sleep(4)
    print("You get the mail")
    

chore1 = threading.Thread(target=walk_dog)
chore1.start()

chore2 = threading.Thread(target=empty_rubbish)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

#Does all the chores at once the the fastest ones finish first