myVariable = 0

def when_started1():
    global myVariable
    arm.spin_to_position(30, DEGREES, wait=True)
    drivetrain.turn_to_heading(0, DEGREES, wait=True)
    drivetrain.turn_for(LEFT, 35, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 15, INCHES, wait=True)
    claw.spin(FORWARD)
    arm.spin(FORWARD)
    drivetrain.turn_for(RIGHT, 48, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 37, INCHES, wait=True)
    arm.spin(REVERSE)
    wait(2, SECONDS)
    claw.spin(REVERSE)
    drivetrain.turn_for(RIGHT, 141, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 28, INCHES, wait=True)
    claw.spin(FORWARD)
    wait(2, SECONDS)
    arm.spin(FORWARD)
    wait(2, SECONDS)
    drivetrain.turn_for(RIGHT, 190, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 28, INCHES, wait=True)
    arm.spin(REVERSE)

# Calibrate the Drivetrain
calibrate_drivetrain()

when_started1()
