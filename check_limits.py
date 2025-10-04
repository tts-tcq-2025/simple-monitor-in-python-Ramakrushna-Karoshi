def is_temperature_ok(temperature):
    """Checks if the temperature is within the safe operating range."""
    if temperature < 0 or temperature > 45:
        print('Temperature is out of range!')
        return False
    return True

def is_soc_ok(soc):
    """Checks if the State of Charge (SoC) is within the safe operating range."""
    if soc < 20 or soc > 80:
        print('State of Charge is out of range!')
        return False
    return True

def is_charge_rate_ok(charge_rate):
    """Checks if the charge rate is within the safe operating range."""
    if charge_rate > 0.8:
        print('Charge rate is out of range!')
        return False
    return True

def battery_is_ok(temperature, soc, charge_rate):
    """
    Checks if the battery parameters are all within safe operating ranges.
    Returns True if all parameters are OK, False otherwise.
    """
    temp_ok = is_temperature_ok(temperature)
    soc_ok = is_soc_ok(soc)
    charge_rate_ok = is_charge_rate_ok(charge_rate)

    return temp_ok and soc_ok and charge_rate_ok

if __name__ == '__main__':
    # Test cases for battery_is_ok
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False) # Temperature and SoC out of range
    assert(battery_is_ok(-5, 50, 0.5) is False) # Temperature out of range
    assert(battery_is_ok(25, 10, 0.5) is False) # SoC out of range
    assert(battery_is_ok(25, 50, 0.9) is False) # Charge rate out of range
    assert(battery_is_ok(40, 75, 0.75) is True) # All good

    print("All battery_is_ok assertions passed!")

    # Individual test cases for predictability and testability
    # Test is_temperature_ok
    assert(is_temperature_ok(25) is True)
    assert(is_temperature_ok(-1) is False)
    assert(is_temperature_ok(46) is False)
    assert(is_temperature_ok(0) is True)
    assert(is_temperature_ok(45) is True)

    # Test is_soc_ok
    assert(is_soc_ok(70) is True)
    assert(is_soc_ok(19) is False)
    assert(is_soc_ok(81) is False)
    assert(is_soc_ok(20) is True)
    assert(is_soc_ok(80) is True)

    # Test is_charge_rate_ok
    assert(is_charge_rate_ok(0.7) is True)
    assert(is_charge_rate_ok(0.81) is False)
    assert(is_charge_rate_ok(0.8) is True)

    print("All individual component assertions passed!")
