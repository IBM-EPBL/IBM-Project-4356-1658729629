import RPi.GPIO as GPIO		
import time
LED = 40			        
GPIO.setwarnings(False) 	
GPIO.setmode(GPIO.BOARD)	
GPIO.setup(LED, GPIO.OUT)	
while True:
  GPIO.output(LED,GPIO.HIGH)
  time.sleep(1)
  GPIO.output(LED,GPIO.LOW)
  time.sleep(1)
