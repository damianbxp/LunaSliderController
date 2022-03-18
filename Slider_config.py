"""
Slider
"""
# pins

x_motor = 0
y_motor = 0
endstop_pins = [0,0,0,0]


steps_per_mm = (200/(3.14159*12), 200/4)  # (steps for full rotation/circumference, steps for full rotation/thread pitch)
"""
Scara
"""
# pins
servos_pins = [0,0,0,0]

# mechanical
arm1_len = 200
arm2_len = 300

big_servo_limit = 180
big_servo_pwm_range = (2200, 7000)

small_servo_limit = 180
big_servo_pwm_range = (2200, 7000)
