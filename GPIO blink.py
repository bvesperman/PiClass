import RPi.GPIO as io
import time

io.setmode(io.BCM)
io.setup(17, io.OUT)

while True:
	io.output(17, True)
	time.sleep(5)
	io.output(17, False)
	time.sleep(5)
