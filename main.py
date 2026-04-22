from microbit import *

# ---- SETTINGS (adjust after testing) ----
CLEAN_THRESHOLD = 300
MODERATE_THRESHOLD = 600

# ---- FUNCTIONS ----
def read_air():
    return pin0.read_analog()

def show_clean():
    display.show(Image.HAPPY)

def show_moderate():
    display.show(Image.MEH)

def show_polluted():
    # Flash skull (encounter effect)
    for i in range(3):
        display.show(Image.SKULL)
        sleep(200)
        display.clear()
        sleep(200)
    display.scroll("BAD")

def vibrate():
    # Optional vibration motor on P1
    pin1.write_digital(1)
    sleep(300)
    pin1.write_digital(0)

def process_air(value):
    if value < CLEAN_THRESHOLD:
        show_clean()
        
    elif value < MODERATE_THRESHOLD:
        show_moderate()
        
    else:
        show_polluted()
        vibrate()

# ---- MAIN LOOP ----
while True:

    # 🔘 BUTTON A = manual scan
    if button_a.was_pressed():
        air = read_air()
        process_air(air)
        sleep(1000)

    # 🤚 SHAKE = quick scan
    if accelerometer.was_gesture("shake"):
        air = read_air()
        process_air(air)
        sleep(1500)

    # ⏱️ AUTO SCAN every few seconds
    air = read_air()
    if air >= MODERATE_THRESHOLD:
        # Passive alert if air gets bad
        show_polluted()
        vibrate()
        sleep(2000)

    sleep(200)def on_forever():
    pass
basic.forever(on_forever)
