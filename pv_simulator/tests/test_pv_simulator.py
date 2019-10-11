"""
Project Test Suite.
"""
import json
import datetime
from pv_simulator.power_house_simulator import Meter
from pv_simulator import pv_simulator


def test_linear_function_2x_plus_1_returns_one_at_x_zero_and_three_at_x_one():
    """ Test a linear function in two points to assert that is really lineal"""
    assert pv_simulator.linear_function(2, 1, 0) == 1
    assert pv_simulator.linear_function(2, 1, 1) == 3

def test_quad_function_xx_plus_two_product_x_plus_zero_returns_zero_at_zero_and_minus_two_but_returns_eight_at_two():
    """ Test a quadratic function in three points to assert that is really lineal"""
    assert pv_simulator.quadratic_function(1, 2, 0, 0) == 0
    assert pv_simulator.quadratic_function(1, 2, 0, 2) == 8
    assert pv_simulator.quadratic_function(1, 2, 0, -2) == 0

def test_center_function_returns_396_at_8am():
    """ Test if center function returns the expected value at a given point"""
    assert int(pv_simulator.center_curve(8)) == 396

def test_get_data_from_meter_returns_a_measurement_between_0_and_9000():
    """ Ensures that the power house consumption simulator values are between 0 and 9000 """
    meter = Meter()
    return_value = meter.get_data()
    assert 0 <= return_value['measurement'] <= 9000

def test_pv_raw_output_power_at_three_pm_with_a_three_pm_is_3119_dot_25_or_lower():
    """ Test pv output calculated power given a defined payload """
    date = datetime.datetime(2019, 10, 1, 15, 0).isoformat()
    assert pv_simulator.Consumer().get_pv_raw_output_power(date) <= 3119.25 # 3119.25 is the top calculated output possible.

def test_pv_output_power_at_three_pm_with_a_meter_measurement_of_3400_is_equal_of_lower_that_the_max_possible_output():
    """ Test pv output calculated power given a defined payload, only can test that is equal or lower because of the random noise from the pv generator."""
    payload = {
        'date': datetime.datetime(2019, 10, 1, 15, 0).isoformat(),
        'measurement': 3400
    }
    encoded_payload = json.dumps(payload)
    max_possible_output_for_interval = (3119.25 - 3400) # 3119.25 is the top calculated output possible.
    assert pv_simulator.Consumer().get_pv_output_power(encoded_payload) <= max_possible_output_for_interval
