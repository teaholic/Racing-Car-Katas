# Leaderboard

SOLID principles practiced:
* Single responsibility
* Interface Segregation

## My Approach

This approach is reflected in the commit history.

Task description:
> Write the unit tests for the Leaderboard class, including races with self driving cars. The Leaderboard calculates driver points and rankings based on results from a number of races.

### Understanding the problem
* I read the application description:
 > calculates driver points and rankings based on results from a number of races
 
* From the description, I found two scopes of needed behavior:
  1. calculates driver points based on results from a number of races
  2. calculates rankings based on results from a number of races
 
### Iteration #1
* These two scopes seem to be tested. I improved the tests to familiarize with the code. In particular, I 
  * removed the `if __name__ == "__main__"` statement and made test discoverable by adding the `Test` prefix
  * used a more pythonic way for the parametric test in `TestRace` 

> I'm thinking:
> 
> While basic leaderboard functionality is tested, driver points are represented as an internal dictionary in `Leaderboard`.
> Similarly, `Race` has a `points` method to get the driver's points. 
> There is a `Driver` data structure, but it has no knowledge of the points. This seems to me a violation of the idea [tell, don't ask](https://www.martinfowler.com/bliki/TellDontAsk.html#:~:text=Tell-Don%27t-Ask%20is%20a%20principle%20that%20helps%20people%20remember,with%20the%20functions%20that%20operate%20on%20that%20data.).
> 
> Bottom line: The responsibility of computing Driver points is scattered across `Race` and `Leaderboard` and its encapsulation can be improved.

### Iteration #2
* I started refactoring `Driver` to own a `points` attribute.
* I moved `Driver` and `SelfDrivingCar` to a `driver.py` package and `Race` to a `race.py` package to stress boundaries and question their real responsibilities.
* `Race` seems to have a sort of "__str__" method for `SelfDrivingCar`. Wrong place to implement this responsibility. I created a `DriverFactory` to create a `Driver` from a `SelfDrivingCar`. I added tests for this factory.

### Iteration #3
* I continued refactoring driver point responsibilities out of `Race`.
* I extracted the following responsibilities: `Points`(Enum), `Results`
* I renamed `DriverFactory` as `DriverService` and added a `score` method to increase `Driver` points.
* For simplicity, I'm removing the software upgrade for the `SelfDrivingCar` in the leaderboard test.
* `Race` doens't seem to have behavior. Stopping iteration here for now - I'll see if I'll still need this `Race` class or not.

### Iteration #4
* I continued refactoring scoring and ranking behavior in `Leaderboard`.
* I realized the responsibility of storing with drivers and updated scores is missing. `Driver` could have and ind attribute that can be used to retrieve `Driver` score in `Leaderboard`; `Driver.score` logic can be updated to create a new `Driver` instance with the given id and the updated score. I added tests for this.
* I need to add the responsibility of calling `DriverServiceScore` to based on `Results` and `Point`. `Race` is the best abstraction for this. A better word to express what `Results` does is `Podium`. I added tests for this.

### Iteration #5
* I continued refactoring scoring and ranking behavior in `Leaderboard`. I added test for this.
* Scoring can be further improved by creating a separated abstraction for this data and behavior. This logic needs to iterate on drivers and races - to progressively test and iterate, I wrapped this responsibility in `DriverServiceScore`.
* Ranking can be further improved by creating a separated abstraction for this data and behavior. This logic isn't complex and can be written as a two-liner. No need to create an abstraction here.
