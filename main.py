def on_button_pressed_a():
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    if st1 >= 90:
        basic.show_string("excellent")
    elif st1 > 50:
        basic.show_string("Pass")
    else:
        basic.show_string("Fail")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global number
    number += 1
    basic.show_number(number)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global increaseNumber
    for index in range(10):
        increaseNumber += 1
        basic.show_number(increaseNumber)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

increaseNumber = 0
st1 = 0
number = 0
basic.show_number(0)
basic.show_string("Omar")
number = 0
st1 = 90