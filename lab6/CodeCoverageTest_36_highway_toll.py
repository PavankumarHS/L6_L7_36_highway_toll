import pytest
from highway_toll import toll_for, toll_charge, pass_advice


def test_toll_for_2_axle_base():
    assert toll_for(2, False, False) == 100

def test_toll_for_2_axle_peak():
    assert toll_for(2, True, False) == 125.0

def test_toll_for_2_axle_fastag():
    assert toll_for(2, False, True) == 90.0

def test_toll_for_2_axle_peak_fastag():
    assert toll_for(2, True, True) == 112.5

def test_toll_for_3_axle_base():
    assert toll_for(3, False, False) == 150

def test_toll_for_3_axle_peak():
    assert toll_for(3, True, False) == 187.5

def test_toll_for_3_axle_fastag():
    assert toll_for(3, False, True) == 142.5

def test_toll_for_3_axle_peak_fastag():
    assert toll_for(3, True, True) == 178.12

def test_toll_for_4_axle_base():
    assert toll_for(4, False, False) == 250

def test_toll_for_4_axle_peak():
    assert toll_for(4, True, False) == 312.5

def test_toll_for_4_axle_fastag():
    assert toll_for(4, False, True) == 237.5

def test_toll_for_4_axle_peak_fastag():
    assert toll_for(4, True, True) == 296.88

def test_toll_for_other_axle_base():
    assert toll_for(5, False, False) == 400

def test_toll_for_other_axle_peak():
    assert toll_for(5, True, False) == 500.0

def test_toll_for_other_axle_fastag():
    assert toll_for(5, False, True) == 380.0

def test_toll_for_other_axle_peak_fastag():
    assert toll_for(5, True, True) == 475.0

def test_toll_for_invalid_axle():
    with pytest.raises(ValueError, match="invalid axle count"):
        toll_for(1, False, False)

def test_toll_for_zero_axle():
    with pytest.raises(ValueError, match="invalid axle count"):
        toll_for(0, False, False)

def test_toll_charge_ambulance_exempt():
    assert toll_charge("ambulance", 2, False, False) == 0

def test_toll_charge_fire_engine_exempt():
    assert toll_charge("fire_engine", 4, True, True) == 0

def test_toll_charge_non_exempt():
    assert toll_charge("truck", 3, False, False) == 150

def test_toll_charge_non_exempt_peak_fastag():
    assert toll_charge("car", 2, True, True) == 112.5

def test_pass_advice_buy_pass():
    trips = [(False, False), (False, False)]
    assert pass_advice(trips, 2, 150) == "buy_pass"

def test_pass_advice_either():
    trips = [(False, False), (False, False)]
    assert pass_advice(trips, 2, 200) == "either"

def test_pass_advice_pay_per_trip():
    trips = [(False, False), (False, False)]
    assert pass_advice(trips, 2, 300) == "pay_per_trip"

def test_pass_advice_empty_trips_either():
    assert pass_advice([], 2, 0) == "either"

def test_pass_advice_empty_trips_pay_per_trip():
    assert pass_advice([], 2, 50) == "pay_per_trip"
