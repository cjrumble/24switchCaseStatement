Switch
case is a
powerful
decision - making
construct
commonly
used in modular
programming.In
this
tutorial, we’ll
explain
multiple
ways
to
implement
the
Python
switch
case
statement.

When
you
don’t
want
a
conditional
block
cluttered
with multiple if conditions, then, switch case can give a cleaner way to implement control flow in your program.

Python
Switch
Case
Statement

Unlike
other
programming
languages, Python
doesn’t
provide
a
switch
case
instrument
over
the
self.

However, it
has
many
other
constructs
like
a
dictionary, lambda function, and classes to write a custom implementation of the Python switch case statement.

If you are keen to know why Python doesn’t have a switch case, then do
refer
the
explanation
at
PEP
3103.

Before
diving
into
further, let’s
have
a
quick
view
of
the
most
common
example
of
a
switch
case
statement in the
C
programming
language.

A
Typical
Switch
Case in C
Programming

In
C, you
can
only
pass
an
integer or enum
value
to
the
switch - case
statement.
Unlike
the if… else block
which
requires
evaluating
expressions in each
condition, the
switch
has
a
single
point
of
interaction
which
leads
to
different
paths
of
execution.
A
switch is a
control
instruction
which
decides
the
control
to
flow
based
on
the
value
of
a
variable or an
expression.
In
the
below
example, the
variable ‘dayOfWeek’ is a
constant
integer
variable
which
represents
days in a
week.And
the
switch - case
block
prints
the
name
of
the
day
based
on
its
value.

switch(dayOfWeek)
{
    case
1: \
    printf("%s", Monday);
break;
case
2:
printf("%s", Tuesday);
break;
case
3:
printf("%s", Wednesday);
break;
case
4:
printf("%s", Thursday);
break;
case
5:
printf("%s", Friday);
break;
case
6:
printf("%s", Saturday);
break;
case
7:
printf("%s", Sunday);
break;
default:
printf("Incorrect day");
break;
}
There
are
a
couple
of
facts
to
consider
for the switch - case statement.

The expression under the switch gets evaluated once.
It should result in a constant integer value.[Note: In
Python, we
can
alter
this
behavior.]
A
case
with a duplicate value should not appear.
If no case matches, then the default case gets executed.
Implement Python Switch Case Statement

Switch Case using a Dictionary

It is simple to use a dictionary for implementing the Python switch case statement.Follow the below steps.

First, define individual functions for every case.
Make sure there is a function / method to handle the default case.
Next, make a dictionary object and store each of the function beginning with the 0th index.
After that, write a switch() function accepting the day of the week as an argument.
The switch() calls the get() method on the dictionary object which returns the function matching the argument and invokes it simultaneously.
# Implement Python Switch Case Statement using Dictionary


def monday():
    return "monday"


def tuesday():
    return "tuesday"


def wednesday():
    return "wednesday"


def thursday():
    return "thursday"


def friday():
    return "friday"


def saturday():
    return "saturday"


def sunday():
    return "sunday"


def default():
    return "Incorrect day"


switcher = {
    1: monday,
    2: tuesday,
    3: wednesday,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
}


def switch(dayOfWeek):
    return switcher.get(dayOfWeek, default)()


print(switch(1))
print(switch(0))
The
output is as follows:

Monday
Incorrect
day
Switch
Case
using
a
Class

It is quite
easy
to
use
a


class for implementing the Python switch case statement.Let’s do it with an example.


In
the
below
example, there is a
PythonSwitch


class which defines the switch() method.


It
takes
the
day
of
the
week as an
argument, converts
it
to
string and appends
to
the ‘case_’ literal.After
that, the
resultant
string
gets
passed
to
the
getattr()
method.
The
getattr()
method
returns
a
matching
function
available in the


class .
    If
    the
    string
    doesn’t
    find
    a
    match, then
    the
    getattr()
    returns
    the
    lambda function as default.


The


class also have the definition for functions specific to different cases.
# Implement Python Switch Case Statement using Class


class PythonSwitch:

    def switch(self, dayOfWeek):
        default = "Incorrect day"
        return getattr(self, 'case_' + str(dayOfWeek), lambda: default)()

    def case_1(self):
        return "Monday"

    def case_2(self):
        return "Tuesday"

    def case_3(self):
        return "Wednesday"


s = PythonSwitch()

print(s.switch(1))
print(s.switch(0))
The
output is as follows:

Monday
Incorrect
day
