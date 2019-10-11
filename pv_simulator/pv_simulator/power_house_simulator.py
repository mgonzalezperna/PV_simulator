"""
Module to produce data that emulates the power consumption of a house.
"""
import json
import time
import random
import datetime
from pv_simulator.messenger_service import MessengerService


class Meter:
    """Mocks measurements of a house's power consumption."""

    def __init__(self):
        """ Sets up the the meter."""
        self.starttime = datetime.datetime(2019, 10, 1, 0, 0)
        self.broker = MessengerService('meter')

    def get_data(self):
        """Return a dict with the data to send"""
        self.starttime += datetime.timedelta(minutes=15)
        measurement_time = self.starttime.isoformat()
        measurement = random.randrange(0, 9000, 1)
        return {
            'date': measurement_time,
            'measurement': measurement
        }

    def send_data(self, payload, queue_name=None):
        """Sends the data to the broker"""
        encoded_payload = json.dumps(payload)
        print(queue_name)
        if queue_name is None:
            self.broker.send_measurement(encoded_payload)
        else:
            self.broker.send_measurement(encoded_payload, queue_name)

def main(total_intervals=100):
    """
    Sender method
    Param total_intervals is used to set an ending to the sender loop.
    """
    meter = Meter()
    for _interval in range(total_intervals):
        payload = meter.get_data()
        meter.send_data(payload)
        time.sleep(0.5)

if __name__ == '__main__':
    main()
