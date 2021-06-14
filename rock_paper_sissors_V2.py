hand = 0
rocks_collected = 0
basic.show_string("Hello!, You have 4 rounds to get as many rocks as possible!")
basic.show_string("Click A to start!")
if input.button_is_pressed(Button.A):
    rocks_collected = 0
    for index in range(5):
        hand = randint(1, 3)
        if hand == 1:
            basic.show_leds("""
                . # # # .
                . # # # .
                . # # # .
                . # # # .
                . # # # .
                """)
        elif hand == 2:
            basic.show_leds("""
                . . . . .
                . # # # .
                # # # # #
                # # # # #
                . . . . .
                """)
            rocks_collected += 1
        else:
            basic.show_leds("""
                . . . # .
                . . # . #
                # # . # .
                # . # . .
                # # # . .
                """)
        basic.pause(1000)
    basic.show_number(rocks_collected)
    
