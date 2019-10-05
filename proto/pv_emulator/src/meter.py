"""
Module to produce data that emulates the power consumption of a house.
"""

import threading
import time
import random
from messenger_service import MessengerService


class Meter():
    """Mocks measurements of a house's power consumption.
    The run() method will be started and it will run in the background
    until the application exits."""

    def __init__(self, interval=1):
        """
        Starts a daemonized thread mocking measurements.
        Param interval is used to sleep interval between messages, in seconds.
        """
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        self._stop = threading.Event()
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def stop(self):
        # function for stoping thread
        print('Meter thread stopped')
        self._stop.set()

    def stopped(self):
        # function for check if thread is stopped or not
        return self._stop.isSet()

    def run(self):
        """ Method that runs forever """
        broker = MessengerService("meter")
        print(broker.channel)
        while True:
            measurement = random.randrange(0, 9000, 1)
            broker.send_measurement(f"{measurement}")
            time.sleep(self.interval)
            print(self.stopped())


example = Meter()
time.sleep(3)
print('Checkpoint')
time.sleep(2)
print('Bye')
example.stop()
print(example.stopped())
