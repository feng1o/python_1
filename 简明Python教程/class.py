#!/usr/bin/python
#_*_coding:utf-8_*_
# FileName: class.py


class Person(object):
    """docstring for  Person"""

    cnum = 0

    def __init__(self, arg):
        super(Person, self).__init__()
        self.arg = arg
        print("{0} is being created ".format(self.arg))
        Person.cnum += 1

    def __del__(self):
        print("{0} is being delted ".format(self.arg))
        Person.cnum -= 1

    @staticmethod  # 二选一 staticFun = staticmethod(statiacFun())
    def staticFun():
        print("static fun  class initialized %d" % Person.cnum)
    # staticFun = staticmethod(staticFun)


class Robot:
    '''Represents a robot, with a name.'''

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        '''Initializes the data.'''
        self.name = name
        print('(Initialize {0})'.format(self.name))

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def __del__(self):
        '''I am dying.'''
        print('{0} is being destroyed!'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{0} was the last one.'.format(self.name))
        else:
            print('There are still {0:d} robots working.'.format(
                Robot.population))

    def sayHi(self):
        '''Greeting by the robot.

        Yeah, they can do that.'''
        print('Greetings, my master call me {0}.'.format(self.name))

    def howMany():
        '''Prints the current population.'''
        print('We have {0:d} robots.'.format(Robot.population))
    howMany = staticmethod(howMany)


def main():
    droid1 = Robot('R2-D2')
    droid1.sayHi()
    Robot.howMany()

    droid2 = Robot('C-3P0')
    droid2.sayHi()
    Robot.howMany()

    print("\nRobots can do some work here.\n")

    print("Robots have finished their work. So let's destroy them.")

    del droid1
    del droid2

    Robot.howMany()

if __name__ == '__main__':
	p1 = Person(1)
	p2 = Person(2)
	Person.staticFun()
	p2.staticFun()
	del p2
	Person.staticFun()
	main()
else:
    print("objvar.py was imported!")




















        
