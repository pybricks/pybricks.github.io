from pybricks.iodevices import LWP3Device
from pybricks.parameters import Color
from pybricks.tools import wait, StopWatch, run_task

# Device identifier for the Duplo Hub.
DUPLO_TRAIN_ID = 0x20

# Mapping that converts colors to LEGO color identifiers.
COLORS = {
    Color.NONE: 0,
    Color.MAGENTA: 2,
    Color.BLUE: 3,
    Color.GREEN: 6,
    Color.YELLOW: 7,
    Color.ORANGE: 8,
    Color.RED: 9,
}

# Mapping that converts sound names to indexes.
SOUNDS = {
    "brake": 3,
    "depart": 5,
    "water": 7,
    "horn": 9,
    "steam": 10
}

async def awaitable(value=None):
    return value

class DuploTrain():
    """Class to connect to the Duplo train and send commands to it."""

    def __init__(self):
        """Scans for a train, connect, and prepare it to receive commands."""
        print("Searching for the train. Make sure it is on and blinking its front light.")
        self.device = LWP3Device(DUPLO_TRAIN_ID, name=None, timeout=10000)

        # Allows speaker to be used
        self.device.write(bytes([0x0a, 0x00, 0x41, 0x01, 0x01, 0x01, 0x00, 0x00, 0x00, 0x01]))

        # State values so we can avoid updating the speed too often.
        self.last_power = 0
        self.timer = StopWatch()

        print("Connected!")
        wait(500)

    def play_sound(self, sound=None, duration=None):
        """Plays the specified sound."""
        try:
            index = SOUNDS[sound.lower()]
        except:
            index = int(sound)
        return self.device.write(bytes([0x08, 0x00, 0x81, 0x01, 0x11, 0x51, 0x01, index]))

    def set_light(self, color):
        """Turns on the train light at the requested color."""
        if color not in COLORS:
            return awaitable() if run_task() else None
        return self.device.write(bytes([0x08, 0x00, 0x81, 0x11, 0x11, 0x51, 0x00, COLORS[color]]))

    def start_driving(self, power):
        """Drives at a given "power" level between -100 and 100."""

        # Cap the power value and cut off values below -25% which won't move
        # the train, only make noise.
        power = max(-100, min(power, 100))
        if abs(power) < 25:
            power = 0

        # If the speed has hardly changed and we recently sent that value,
        # don't send now to avoid overloading the BLE link.
        if abs(power - self.last_power) <= 5 and self.timer.time() < 200:
            return awaitable() if run_task() else None

        # Update power state and send the value.
        self.last_power = power
        self.timer.reset()
        power_send = power + 256 if power < 0 else power  
        return self.device.write(bytes([0x08, 0x00, 0x81, 0x00, 0x01, 0x51, 0x00, power_send]))

    def stop_driving(self):
        """Stops driving."""
        return self.start_driving(0)


# Extra "functions" that allow us to call methods of the train object using
# block coding, which currently does not have a method call block.
def start_driving(train: DuploTrain, power):
    return train.start_driving(power)

def set_light(train: DuploTrain, color):
    return train.set_light(color)

def play_sound(train: DuploTrain, sound):
    return train.play_sound(sound)
