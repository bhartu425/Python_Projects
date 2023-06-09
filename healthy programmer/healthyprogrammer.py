import datetime
from pygame import mixer 
while True:
    t = datetime.datetime.today()
    time =t.strftime('%H:%M:%S')
    if time < "17:00:00" and time >"09:00:00":
        break
    print(type(time))
    water_time = t+datetime.timedelta(seconds=10)
    water_time =water_time.strftime('%H:%M:%S')

    exercise_time=t+datetime.timedelta(seconds=30)
    exercise_time=exercise_time.strftime('%H:%M:%S')

    physical_time=t+datetime.timedelta(seconds=50)
    physical_time=physical_time.strftime('%H:%M:%S')

    while True:
        time =datetime.datetime.strftime(datetime.datetime.today(),'%H:%M:%S')
        if time==water_time:
            print('drink water')
            mixer.init()
            mixer.music.load('song1.mp3')
            mixer.music.play()
            user_intput = input('Are you drunk water (y/n):')
            if user_intput=='y':
                with open('water.txt','a') as f:
                    f.write(f'you drink water at{time}\n')
                mixer.music.stop()
            else:
                print('thats sounds bad Idiot')
                mixer.music.stop()
                
        elif time==exercise_time:
            print('its eyes exercise time ')
            mixer.init()
            mixer.music.load('song1.mp3')
            mixer.music.play()
            user_intput = input('Are you done eye exercise (y/n):')
            if user_intput=='y':
                with open('eye.txt','a') as f:
                    f.write(f'you done the eye exercise at {time}\n')
                mixer.music.stop()
            else:
                print('thats sounds bad Idiot')
                mixer.music.stop()
                
        elif time==physical_time:
            print('its physical exercise time')
            mixer.init()
            mixer.music.load('song1.mp3')
            mixer.music.play()
            user_intput = input('Are you done pyshical work (y/n):')
            if user_intput=='y':
                with open('physical.txt','a') as f:
                    f.write(f'you done physical work at {time}\n')
                mixer.music.stop()
            else:
                print('thats sounds bad Idiot')
                mixer.music.stop()
                
            break
