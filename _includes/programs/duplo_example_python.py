from pybricks.parameters import Color
from pybricks.tools import wait

from duplo import DuploTrain

# Initialize and connect to the train.
train = DuploTrain()

# This is how to control the light.
train.set_light(Color.RED)
wait(1000)

# This is how to control the sound.
train.play_sound('depart')
wait(1000)

# This is how to drive, stop, and reverse.
train.start_driving(50)
wait(1000)
train.stop_driving()
wait(1000)
train.start_driving(-50)
wait(1000)
