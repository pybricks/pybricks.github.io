# Pairing with the Xbox Controller

{% include scaled.html
  path="/project/xbox-controller/xbox-controller.png"
  width="75%"
%}

The very first time, you'll need to pair the hub with your controller:

1. Turn the controller on.
2. Press and hold the pairing button on the back.
3. Release after a few seconds. The controller light will start flashing more
  rapidly. This is _pairing mode_.
4. _Then_ start your <a href="#block-program">program</a>. Either using the
   Pybricks app, or using the green button on the hub if you've
   already loaded the program earlier.

The hub will start looking for your
controller when the program starts. When the connection is successful, the
controller light will stop flashing and stay on for as long as the program is
running.

You can see this in the video below.

## Connecting without pairing

The next time you use it, pairing is not required. Just turn the controller on.
The hub will connect to it automatically when your program runs.

The Xbox controller remembers only one device. If you use the controller with
another LEGO hub or your Xbox console, and then with this hub again, you'll
need to pair them again as above.

## Updating the Xbox Controller

If you often use the Xbox Controller with your console, it is probably already
up to date. If you have not used it for a while or if you bought
one recently, you may need to update it.

To update the controller without a console, you can use the
<a href="https://apps.microsoft.com/detail/9nblggh30xj3?hl=en-US&gl=US" target="_blank">Xbox Accessories</a>
app on a Windows computer.
Connect the controller via USB to the computer and follow the instructions in
the app to click on “Update now”. If it is already at firmware version
5.17 or later, you don't need to do anything.

{% if include.technic == true %}
## Technic Hub limitations

Once you start your program, the Technic Hub will disconnect from your computer
to free up the connection for the Xbox Controller. This means you can't use the
Pybricks app to stop the program or change the code while the Xbox Controller
is connected.

To change your program, stop the program by pressing the green button on the hub.
Then you can connect to the hub with the Pybricks app again, and change
your program as needed.

{% endif %}
