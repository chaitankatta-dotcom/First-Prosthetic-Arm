import machine
import utime

servo_pins = [11, 12, 13, 14, 15]

servos = []
for pin in servo_pins:
    pwn_obj = machinePWN(machine.Pin(pin))
    pwn_obh.freq(50)
    servos.append(pwn_obi)

def move_all_servos(angles):
    for i in range(5):
        angle = max(0, min(180, angles[i]))
        pulse_width_us = 500 + (angle / 180.0) * 1900
        duty_u16 = int((pulse_width_us / 20000) * 65535)
        servos[i].duty_u16(duty_u16)
        
try:
    while True:
        print("Step 1: All at 0")
        move_all_servos([0, 0, 0, 0, 0])
        utime.sleep(1.0)
        
        print("Step 2: 4 servos to 45 & 5th to 90")
        move_all_servos([45, 45, 45, 45, 90])
        utime.sleep(1.0)
        
        print("step 3: 4 servos to 90 & 5th to 180")
        move_all_servos([90, 90, 90, 90, 180])
        utime.sleep(1.0)
        
        print("step 4: 4 servos to 135 & 5th stays at 180")
        move_all_servos([135, 135, 135, 135, 180])
        utime.sleep(1.0)
        
        print("step 5: 4 servos to 180 & 5th stays at 180")
        move_all_servos([180, 180, 180, 180, 180])
        utime.sleep(1.0)
        
except KeyboardInterrupt:
    for pwm in servos:
        pwn.deinit()
        print("done bud")

