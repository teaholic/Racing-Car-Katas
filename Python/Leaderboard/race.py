class Race(object):

    _points = [25, 18, 15]

    def __init__(self, name, results):
        self.name = name
        self.results = results
        self.driver_names = {}
        for driver in results:
            name = driver.name
            if isinstance(driver, SelfDrivingCar):
                name = "Self Driving Car - {} ({})".format(driver.country, driver.algorithm_version)
            self.driver_names[driver] = name