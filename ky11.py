import RPi.GPIO as GPIO
import time
   
GPIO.setmode(GPIO.BCM)
   
# The output pins will be declared, which are connected with the LEDs.
LED_RED = 20
LED_GREEN = 21
GPIO.setup(LED_RED, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(LED_GREEN, GPIO.OUT, initial= GPIO.LOW)
   
print "LED-Test [press ctrl+c to end]"
  
# main program loop 
try:
        while True:
            print("LED RED is on for 2 seconds")
            GPIO.output(LED_RED,GPIO.HIGH) #LED on
            GPIO.output(LED_GREEN,GPIO.LOW) #LED off
            time.sleep(2) # Wait 2 seconds
            print("LED GREEN is on for 3 seconds") 
            GPIO.output(LED_RED,GPIO.LOW) #LED off
            GPIO.output(LED_GREEN,GPIO.HIGH) #LED on
            time.sleep(3) # Wait 3 seconds
   
# Scavengin work after the end of the program
except KeyboardInterrupt:
        GPIO.cleanup()
