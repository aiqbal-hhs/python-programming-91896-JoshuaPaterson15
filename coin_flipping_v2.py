basic.show_string("Hello!, to start, please answer the following math question.")
basic.show_string("10+10  (Button a is 20 and button b is 100).")

def on_forever():
    if input.button_is_pressed(Button.A):
        basic.show_icon(IconNames.DIAMOND)
        basic.show_icon(IconNames.SMALL_DIAMOND)
        basic.show_icon(IconNames.DIAMOND)
        basic.show_icon(IconNames.SMALL_DIAMOND)
        if Math.random_boolean():
            basic.show_icon(IconNames.SKULL)
        else:
            basic.show_icon(IconNames.SQUARE)
    if input.button_is_pressed(Button.B):
        basic.show_string("Sorry, thats wrong :(")
basic.forever(on_forever)
