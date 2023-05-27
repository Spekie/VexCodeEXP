myVariable = 0

def when_started1():
    global myVariable
    drivetrain.set_drive_velocity(100, PERCENT)

def onevent_bumper_g_pressed_0():
    global myVariable
    brain.screen.set_fill_color(Color.RED)
    brain.screen.draw_rectangle(0, 0, 109, 107)

calibrate_drivetrain()

bumper_g.pressed(onevent_bumper_g_pressed_0)
# 15 ms
wait(15, MSEC)

when_started1()
