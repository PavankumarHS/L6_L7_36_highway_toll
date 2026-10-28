import pytest
from highway_toll import toll_for, toll_charge, pass_advice


# Branch: axles < 2 => True
def test_branch_invalid_axle_raises():
    with pytest.raises(ValueError, match="invalid axle count"):
        toll_for(1, False, False)

# Branch: axles < 2 => False, axles in BASE_TOLL => True (2)
def test_branch_axle_in_base_toll_2():
    assert toll_for(2, False, False) == 100

# Branch: axles in BASE_TOLL => True (3)
def test_branch_axle_in_base_toll_3():
    assert toll_for(3, False, False) == 150

# Branch: axles in BASE_TOLL => True (4)
def test_branch_axle_in_base_toll_4():
    assert toll_for(4, False, False) == 250

# Branch: axles in BASE_TOLL => False
def test_branch_axle_not_in_base_toll():
    assert toll_for(6, False, False) == 400

# Branch: is_peak => True
def test_branch_is_peak_true():
    assert toll_for(2, True, False) == 125.0

# Branch: is_peak => False
def test_branch_is_peak_false():
    assert toll_for(2, False, False) == 100

# Branch: has_fastag => True, axles == 2 => True
def test_branch_fastag_axle_2():
    assert toll_for(2, False, True) == 90.0

# Branch: has_fastag => True, axles == 2 => False
def test_branch_fastag_axle_not_2():
    assert toll_for(3, False, True) == 142.5

# Branch: has_fastag => False
def test_branch_no_fastag():
    assert toll_for(4, False, False) == 250

# Branch: peak + fastag + axle==2
def test_branch_peak_fastag_axle_2():
    assert toll_for(2, True, True) == 112.5

# Branch: peak + fastag + axle!=2
def test_branch_peak_fastag_axle_5():
    assert toll_for(5, True, True) == 475.0

# Branch: vehicle in EXEMPT => True (ambulance)
def test_branch_exempt_ambulance():
    assert toll_charge("ambulance", 2, False, False) == 0

# Branch: vehicle in EXEMPT => True (fire_engine)
def test_branch_exempt_fire_engine():
    assert toll_charge("fire_engine", 3, True, False) == 0

# Branch: vehicle in EXEMPT => False
def test_branch_not_exempt():
    assert toll_charge("bus", 4, False, False) == 250

# Branch: pass_advice cost > pass_price => buy_pass
def test_branch_pass_buy():
    trips = [(False, False), (False, False)]
    assert pass_advice(trips, 2, 150) == "buy_pass"

# Branch: pass_advice cost == pass_price => either
def test_branch_pass_either():
    trips = [(False, False), (False, False)]
    assert pass_advice(trips, 2, 200) == "either"

# Branch: pass_advice cost < pass_price => pay_per_trip
def test_branch_pass_pay_per_trip():
    trips = [(False, False)]
    assert pass_advice(trips, 2, 200) == "pay_per_trip"

# Branch: for loop executes (non-empty trips)
def test_branch_loop_executes():
    trips = [(True, True), (False, False)]
    assert pass_advice(trips, 2, 200) == "buy_pass"

# Branch: for loop does not execute (empty trips), cost < pass_price
def test_branch_loop_empty():
    assert pass_advice([], 2, 100) == "pay_per_trip"

# Branch: empty trips cost == pass_price
def test_branch_loop_empty_either():
    assert pass_advice([], 2, 0) == "either"
