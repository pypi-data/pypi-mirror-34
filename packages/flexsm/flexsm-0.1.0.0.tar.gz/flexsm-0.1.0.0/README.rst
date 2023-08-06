**********
Installing
**********

.. code-block:: sh

 pip install flexsm

You can easily install flexsm with pip:


********************************************
Importing, creating states and state machine
********************************************

Creating states and state machines is pretty straightforward:

.. code-block:: python

 from flexsm import *
 
 root = State("root")
 state1 = State("state 1")
 state2 = State("state 2")
 
 sm = StateMachine(root)

*******************************
Transitions and input variables
*******************************

Transitions are responsible for getting from one state to another. They usually start in one state and end in another. If the next state is only known at runtime, e.g. if it depends on an input variable "x", then you can override the transition method *getNextState*:

.. code-block:: python

 @addTransition(state=root)
 class WaitForSomeValueToBecomeSmall(Transition):
     def getNextState(self, x):
         if x>15:
             return state2
         else:
             return state1

This piece of code allows us to transition from state *root* to *state 1* if x is smaller than 15, for example by calling:

.. code-block:: python

 sm.update("x", 10)

or to *state 2* if x is 15 or bigger.

There is also an input variable *time_in_state*, which contains the amount of time we've been in the current state in seconds. The minimal guaranteed resolution for time_in_state is 0.1 seconds, which can be changed in the StateMachine construction:

.. code-block:: python

 sm = StateMachine(root, time_resolution=0.01)

By overriding the *check* method, we can transition if we are in the state 5 seconds or longer:

.. code-block:: python

 @addTransition(state=state1, next=state2)
 class WaitAMoment(Transition):
     def check(self, time_in_state, x):
         return time_in_state > 5
 
     def onTrigger(self, time_in_state, x):
         print("""We are in this boring
             state since {:.2f} seconds, 
             with x being {}""".format(time_in_state, x))

We also override *onTrigger*, which is called when the transition is triggered. Note how the parameters for onTrigger and check are equal. The parameters for all transition methods are name sensitive. So you can't simply use the parameter y instead of x and expect y to be 100 if you run sm.update("x", 100). For the same transition, the parameters for getNextState, check and onTrigger even have to be equal!

Transition.check will only be called if the value of one of its parameters changed. Thus, if your code in the check method takes a lot of time, try to avoid frequently changing parameters like time_in_state.

*************
Parent states
*************

Consider the following example:

.. code-block:: python

 airbourne = State("Airbourne")
 doing360spin = State("Spin 360", parent=airbourne)
 
 sm = StateMachine(doing360spin)

In this case, we are not only in the state *doing360spin*, but also in the state *airbourne*. Thus, any transitions defined on *airbourne* will be considered as well. For example, an airplane could go into an emergency state if its fuel is getting low. Such emergency transitions would be interesting for all states in the air.


