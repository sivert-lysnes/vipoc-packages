import time

import vipoc.motor

vipoc.motor.init_motors() #Turns all motors off, and sets direction to cw

time.sleep(1)

# Controlling an arbitrary motor anytime
vipoc.motor.on(0) #Turns motor 0 on, doesnt do anything with direction

time.sleep(1)

vipoc.motor.up(0) #Sets motor 0 to turn ccw

time.sleep(1)

vipoc.motor.down(0) #Sets motor 0 to turn cw

motor = vipoc.motor.Motor(0)

time.sleep(1)

for i in range(10):
    motor.on()
    
    time.sleep(0.1)
    
    motor.off()
    
    time.sleep(0.1)