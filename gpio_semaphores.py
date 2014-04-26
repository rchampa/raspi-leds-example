import os;
import time;
import threading;

#shared data
while_control = True;
my_mutex = threading.Lock();

def turn_on_red():
    os.system("echo 1 > /sys/class/gpio/gpio17/value");
def turn_off_red():
    os.system("echo 0 > /sys/class/gpio/gpio17/value");

def turn_on_yellow():
    os.system("echo 1 > /sys/class/gpio/gpio27/value");
def turn_off_yellow():
    os.system("echo 0 > /sys/class/gpio/gpio27/value");

def turn_on_green():
    os.system("echo 1 > /sys/class/gpio/gpio22/value");
def turn_off_green():
    os.system("echo 0 > /sys/class/gpio/gpio22/value");

def enable_gpios():
    os.system("echo 17 > /sys/class/gpio/export");#red
    os.system("echo 27 > /sys/class/gpio/export");#yellow
    os.system("echo 22 > /sys/class/gpio/export");#green
    os.system("echo out > /sys/class/gpio/gpio17/direction");
    os.system("echo out > /sys/class/gpio/gpio27/direction");
    os.system("echo out > /sys/class/gpio/gpio22/direction");
def disable_gpios():
    os.system("echo 17 > /sys/class/gpio/unexport");
    os.system("echo 27 > /sys/class/gpio/unexport");
    os.system("echo 22 > /sys/class/gpio/unexport");


def red_thread():
        turn_on = True;
        my_loop = True;
        global while_control;
        global my_mutex;

        while my_loop:
                with my_mutex:
                        my_loop = while_control;

                if turn_on :
                        turn_on_red();
                        #print("Red");
                        time.sleep(1);
                else :
                        turn_off_red();
                        time.sleep(2);

                turn_on = not turn_on;



def yellow_thread():
        turn_on = True;
        my_loop = True;
        global while_control;
        global my_mutex;
        time.sleep(1);

        while my_loop:
                with my_mutex:
                        my_loop = while_control;

                if turn_on :
                        turn_on_yellow();
                        #print("Yellow");
                        time.sleep(1);
                else :
                        turn_off_yellow();
                        time.sleep(2);

                turn_on = not turn_on;



def green_thread():
        turn_on = True;
        my_loop = True;
        global while_control;
        global my_mutex;
        time.sleep(2);

        while my_loop:
                with my_mutex:
                        my_loop = while_control;

                if turn_on :
                        #print("Green");
                        turn_on_green();
                        time.sleep(1);
                else :
                        turn_off_green();
                        time.sleep(2);

                turn_on = not turn_on;


def play():
        global my_mutex;
        global while_control;
        with my_mutex:
                while_control = True;

        tr = threading.Thread(target=red_thread, args=());
        tr.start();

        ty = threading.Thread(target=yellow_thread, args=());
        ty.start();

        tg = threading.Thread(target=green_thread, args=());
        tg.start();


def stop():
        global my_mutex;
        global while_control;
        with my_mutex:
                while_control = False;


def exit_app():
        turn_off_red();
        turn_off_yellow();
        turn_off_green();
        disable_gpios();


options = {
        1 : enable_gpios,
        2 : disable_gpios,
        3 : turn_on_red,
        4 : turn_off_red,
        5 : turn_on_yellow,
        6 : turn_off_yellow,
        7 : turn_on_green,
        8 : turn_off_green,
        9 : play,
        10 : stop,
        11 : exit_app,
}


while True:
    print("Select an option");
    print("1. Enable GPIOS");
    print("2. Disable GPIOS");
    print("3. Turn ON red");
    print("4. Turn OFF red");
    print("5. Turn ON yellow");
    print("6. Turn OFF yellow");
    print("7. Turn ON green");
    print("8. Turn OFF green");
    print("9. Play");
    print("10. Stop");
    print("11. Exit");

    user_input = int(input());

    if user_input==11:
        break;
    else:
        options[user_input]();


