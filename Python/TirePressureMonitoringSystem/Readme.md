# Tire Pressure Monitoring System

SOLID principles practiced:
* Single responsibility

## My Approach
* I read the application description:
 > set an alarm if the pressure falls outside of the expected range
 
* From the description, I found two scopes of needed behavior:
  1. set an alarm
  2. check if the pressure falls outside of the expected range
 
* I started writing a (failing) test for the first scope of behavior
* I went on to write the implementation to make this test pass. I stopped.
 > Chiara is thinking:
> 
 > I realized `Alarm` was dependent from `Sensor`. I had to extract and move the responsibility to orchestrate sensor (`check if the pressure falls outside of the expected range`) and alarm (`set an alarm`) to a new `TirePressureMonitoringService`. In hindsight, it was a bit confusing that a `tire_pressure_monitoring.py` package had an `Alerting` class and that `test_tire_pressure_monitoring` was testing an `is_on` feature of `Alerting`  - I was rather expecting to see some service or application there, and not just a part of it.
 
 * I extracted the responsibility of setting the alarm to an `Alarm` class in an `alarm.py` package. I wrote tests for this. I added failing test placeholder for some `TirePressureMonitoringService` class. 
 * I iterated on `TirePressureMonitoringService` class tests. I thought of three test cases: 
   * test_check_low_pressure_and_raise_alarm
   * test_check_high_pressure_and_raise_alarm
   * test_check_regular_pressure_and_do_nothing
 > Chiara is thinking:
> 
> I realized `TirePressureMonitoringService` was dependent from `Sensor`, `Alert` and threshold values (high, low). This didn't help me write tests for the test cases. I had to rename `TirePressureMonitoringService` as `TirePressureMonitoringSystem` and extract the responsibility to assess if the psi value had to raise an alarm to a `TirePressureMonitoringService`. `TirePressureMonitoringService` had to return an `Alarm` to make the alarm status testable. I'm thinking this alarm start look a lot like a pure data structure, whose state is changed in `TirePressureMonitoringService`.
 * I refactored `Alarm` as a dataclass, renamed `TirePressureMonitoringService` in `AlarmService` and moved it to the `alarm.py` package.