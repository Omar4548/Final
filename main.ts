input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Heart)
})
input.onButtonPressed(Button.AB, function () {
    if (st1 >= 90) {
        basic.showString("excellent")
    } else if (st1 > 50) {
        basic.showString("Pass")
    } else {
        basic.showString("Fail")
    }
})
input.onButtonPressed(Button.B, function () {
    number += 1
    basic.showNumber(number)
})
input.onGesture(Gesture.Shake, function () {
    for (let index = 0; index < 10; index++) {
        increaseNumber += 1
        basic.showNumber(increaseNumber)
    }
})
let increaseNumber = 0
let st1 = 0
let number = 0
basic.showNumber(0)
basic.showString("Omar")
number = 0
st1 = 90
