"""
Project Test Suite.
"""
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

""" Tests that needs RabbitMQ mocked"""
def test_get_data_from_meter_returns_a_date_and_measurement_between_0_and_9000():
    meter = Meter()
    return_value = meter.get_data()
    assert return_value['date'] is datetime.datetime
    assert 0 <= return_value['measurement'] <= 9000

def test_pv_output_power_at_three_pm_with_a_meter_measurement_of_3400_is_minus_1061():
    """ Test pv output calculated power given a defined payload """
    payload = {
        'date': datetime.datetime(2019, 10, 1, 15, 0),
        'measurement': 3500
    }
    assert pv_simulator.Consumer().get_pv_output_power(payload) == (2461-3400)

def test_pv_raw_output_power_at_three_pm_with_a_three_pm_is_2461():
    """ Test pv output calculated power given a defined payload """
    date =  datetime.datetime(2019, 10, 1, 15, 0),
    assert pv_simulator.Consumer().get_pv_raw_output_power(date) == (2461-3400)
