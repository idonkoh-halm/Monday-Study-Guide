import traceback, inspect, random, math

######################################################
######################################################
###                                                                       ###
###                     VARIABLES AND DATA TYPES                      ###
###                                                                        ###
######################################################
######################################################


# Create a list called 'colors' containing exactly the names of 4 colors

# Store the number 12 in a variable named 'nmonths'

# Store the sum of 12345 and 54321 in the variable 'bignum'
colors=['black','yellow','goldenrod','red']
nmonths=12
bignum=int(12345+54321)

######################################################
######################################################
###                                                                        ###
### Bug fixes -- Fix the error in each of the following functions.   ###
###                                                                        ###
######################################################
######################################################

def isHinkle (first,last):
    '''Return True if person is a Hinkle'''
    # Fix the bug in this code
    if last=="Hinkle":
        return True
    else:
        return False

def factorial (n):
    '''Return the factorial of n (i.e. the result of multiplying n*n-1*n-2*...1)
    '''
    product = n
    for i in range(n):
        product = product*i
    return product



######################################################
######################################################
###                                                                        ###
###                                 FUNCTIONS                            ###
###                                                                        ###
######################################################
######################################################

# Create functions to do the following...

# Write a function titled 'addTwoDigits' that takes two arguments and returns
# the sum of them.

def addTwoDigits(dig1,dig2):
    sumof=dig1+dig2
    return sumof

# Write a function titled isOdd that returns True if a number is odd.


#def isOdd(number):
#    evenum=number-1
#    checker=float(number)/2
#    checker2=checker-0.5
#    checker3=float(evenum)/2
#    checker4=checker2-checker3
#    if checker4==0:
#        return True
#    else:
#        return False



# Write a function titled isPrime that returns True if a number is prime


######################################################
######################################################
###                                                                        ###
###                                 OBJECTS                              ###
###                                                                        ###
######################################################
######################################################


# Fix distance method to point as described in documentation string below
class Point:

    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def distance (self, otherPoint):
        '''Return the distance between self and other point'''
        return 
    
# Create an object called "Person" which is instantiated with a
# first and last name and isMale, like so
#
# Person('John','Doe',True)
# Person('Jane','Doe',False)
#
# Then, create the following methods that return nicely formatted
# names
# 
# p.getLastFirst() -> 'Doe, John' (return last, first version of name)
# p.getFormalName() -> 'Mr. John Doe' (return formal name with Mr. or Ms.)




################################################
################################################
####                                                            ####
####       GRADING CODE - DO NOT MODIFY CODE BELOW     ####
####                                                            ####
################################################
################################################

# DO NOT MODIFY THE LINES BELOW THIS
# THIS IS HOW THE TEST RUNS
class TestProblem:

    def __init__ (self, tests, description):
        self.description = description
        self.tests = tests
    
    def run_tests (self):
        for test in self.tests:
            if not run_test(*test):
                print 'Failed test # ',self.tests.index(test)+1
                print ': ',inspect.getsource(test[0])
                return False
        return True
                


def run_test (f, testval):
    try:
        result = f()
    except:
        traceback.print_exc()
        return False
    else:
        if result==testval:
            return True
        else:
            inspect.getsource(f)
            print 'Incorrect result.'
            print 'Expected : ',testval
            print 'Got value: ',result


all_tests = [
    TestProblem(
        tests=[(lambda *args: nmonths==12,True),],
        description='Store the number 12 in the variable nmonths'
        ),
    TestProblem(
        tests=[(lambda *args: len(colors)==4,True),
               (lambda *args: set([type(c)==str for c in colors])==set([True]),True)
               ],
        description='Store the names of four colors in the variable colors'
        ),
    TestProblem(
        tests=[(lambda *args: bignum==54321+12345,True)],
        description='Store the sum of 54321 and 12345 in the variable bignum'
        ),
    TestProblem(
        tests=[(lambda *args: isHinkle('Tom','Hinkle'),True),
               (lambda *args: isHinkle('Mary','Paterson'),False)],
        description='Fix the bug in isHinkle'
        ),
    TestProblem(
        tests=[(lambda *args: factorial(3),6),
               (lambda *args: factorial(7),5040),
               (lambda *args: factorial(10), 3628800)],
        description='Fix the bug in factorial',
        ),
    TestProblem(
        tests=[(lambda *args: addTwoDigits(2,3),5),
               (lambda *args: addTwoDigits(-2,2),0),
               (lambda *args: addTwoDigits(0,10),10),
               (lambda *args: addTwoDigits(4,-5),-1),
               (lambda *args: addTwoDigits(2.23,3),5.23)
               ],
        description='Create a function called addTwoDigits',
        ),
    TestProblem(
        tests=[(lambda *args: isOdd(123121),True),
               (lambda *args: isOdd(123122),False),
               (lambda *args: isOdd(88881),True),
               (lambda *args: isOdd(random.randint(1000,10000)*2),False)
               ],
        description='Create a function called isOdd',
        ),
    TestProblem(
        tests=[(lambda *args: isPrime(17),True),
               (lambda *args: isPrime(4),False),
               (lambda *args: isPrime(51),False),
               (lambda *args: isPrime(3),True),
               (lambda *args: isPrime(15485863),True),
               (lambda *args: isPrime(11111193),False)
               ],
        description='Create a function called isPrime which returns True or False depending on whether the argument is prime'),
    ]

# Class tests...

class PointTestProblem (TestProblem):

    def __init__ (self):
        self.description = 'Create distance method for Point class'
        self.tests = [
            (self.setup,None),
            (self.testOne,2),
            (self.testTwo,18),
            (self.testThree,17),
            ]

    def setup (self):
        self.p1 = Point(0,0)
        self.p2 = Point(math.sqrt(2),math.sqrt(2))
        self.p3 = Point(0,18)
        self.p4 = Point(0,17)
        
    def testOne (self):
        return self.p1.distance(self.p2)

    def testTwo (self):
        return self.p1.distance(self.p3)
        
    def testThree (self):
        return self.p1.distance(self.p4)

class PersonTestProblem (TestProblem):
    def __init__ (self):
        self.description = 'Create a Person class with appropriate methods'
        self.tests = [
            (self.setup,None),
            (lambda *args: self.p1.getLastFirst(),'Foo, John'),
            (lambda *args: self.p2.getLastFirst(),'Bar, Mary'),
            (lambda *args: self.p1.getFormalName(),'Mr. John Foo'),
            (lambda *args: self.p2.getFormalName(),'Ms. Mary Bar'),
            ]

    def setup (self):
        self.p1 = Person('John','Foo',True)
        self.p2 = Person('Mary','Bar',False)


    
all_tests.extend([
    PointTestProblem(),
    PersonTestProblem()
])

def run_all_tests ():
    ftot = 0; fscore = 0
    for tp in all_tests:
        print 'Running: ',tp.description
        ftot += 1
        if tp.run_tests():
            fscore += 1
    print 'Function Score: ',fscore,'/',ftot



run_all_tests()
