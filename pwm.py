import RPi.GPIO as GPIO
import time

pwm_pin = 18
pwm_freq = 50
pwm_lb = 2.78
pwm_ub = 12.78
pwm_range = pwm_ub - pwm_lb

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, pwm_freq)
pwm.start(pwm_lb)

try:
	while True:
		inp = input("degrees:")
		if inp == 'q':
			print("NI")
			break
		degree = int(inp)
		if degree > 180 or degree < 0:
			print("Out of Range")
		else:
			dc = degree*pwm_range/180 + pwm_lb
			pwm.ChangeDutyCycle(dc)

finally:
	pwm.stop()
	GPIO.cleanup()
