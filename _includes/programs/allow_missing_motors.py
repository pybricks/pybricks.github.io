#
################################################################################
# You can import this file in your project if you want to ignore errors about
# motors not being connected.
#
# Usually, error messages are helpful reminders that you have to plug the cables
# the right way. But sometimes you want to make a general-purpose program if you
# don't know how the cables will be wired yet.
#
# Step 1: Upload this file (allow_missing_motors.py) in the Pybricks editor.
#
# Step 2: In your block project, add the import block from the external tasks
# category. Fill in the fields such that it looks like this:
#
# from allow_missing_motors import Motor
#
# If you use Python, just add the above line below the usual imports.
################################################################################
#
from pybricks.pupdevices import Motor as _Motor, DCMotor as _DCMotor
from pybricks.parameters import Direction

# A function or method that just does nothing.
def do_nothing(*args, **kwargs):
    return 0

# A class that does nothing and allows any method calls.
class NoneMotor:
    def __getattr__(self, name):
        return do_nothing

# Class like DCMotor, but raises no exception if you
# call a nonexistent method like run_angle on it.
class AnyDCMotor(_DCMotor):
    def __getattr__(self, name):
        return do_nothing

# Helper function that creates a Motor-like object, but
# suppresses exceptions about motors not being connected.
def Motor(port, direction=Direction.CLOCKWISE):
    try:
        # Give a normal motor object if such device is connected.
        return _Motor(port, direction)
    except OSError:
        try:
            # Otherwise return a DC motor if there is one, but allow
            # and ignore calls to methods that require encoders.
            return AnyDCMotor(port, direction)
        except OSError:
            # If nothing is attached, still succeed and return an object
            # that just does nothing.
            return NoneMotor()


# Also allow any-way-around use of the DCMotor class.
DCMotor = Motor