---
title: "Measuring sensor values"
redirect_from:
  - /learn/sensors/
excerpt: >
  Learn to use sensors with the Wait Until block and the Conditional Repeat block.
header:
  teaser: /learn/sensors/overview.jpg
requirements:
  image: /learn/sensors/overview.jpg
  width: 100%
  labels:
    - text: Sensor
      x: 18%
      y: 25%
      location: above
    - text: |
        Hub with builtin
        motion sensors
      x: 25%
      y: 48%
      location: left
    - text: |
        Buttons work
        like sensors
      x: 32%
      y: 58%
      location: right
    - text: Motor
      x: 23%
      y: 76%
      location: below
    - text: |
        The robot operates
        in its environment.
      x: 65%
      y: 80%
      location: below
    - text: |
        Your program makes the
        motors respond to what
        sensors measure.
      x: 73%
      y: 25%
      location: above
  caption: >
      Sensors give robots a sense of their environment.
img_sensor_setup_1:
  image: /learn/sensors/setup-1.png
  alt: Setup step 1
  width: 100%
  caption: >
    1. Create a new program and configure your sensor on the right port. Add
    a Conditional Repeat block, a Print block and a Wait Time block to print
    repeatedly. This will print <i>Distance: abc</i> four times per second.
    You'll add the actual sensor value in the next step.
  labels:
    - text: Setup blocks
      x: 10%
      y: 20%
      location: below
    - text: Ultrasonic Sensor Setup block
      x: 48%
      y: 46%
      location: right
    - text: |
        Configure all your
        sensors in the setup
      x: 45%
      y: 60%
      location: right
    - text: |
        Repeatedly print
        two text values.
      x: 60%
      y: 83%
      location: below
img_sensor_setup_2:
  image: /learn/sensors/setup-2.png
  alt: Setup step 2
  width: 100%
  caption: >
    2. From the Input blocks tab, choose the Measure Distance block and drop it
    into the second value in the Print block. Now it will print the measured
    distance instead of the text <i>abc</i>.
  labels:
    - text: | 
        Measure Distance block
      x: 43%
      y: 19%
      location: right
    - text: |
        If you set up multiple sensors
        that measure distance, pick the
        right one here.
      x: 69%
      y: 63%
      location: above
    - text: |
        Each time your program gets here,
        this block measures the distance
        and passes it to the Print block.
      x: 59%
      y: 65%
      location: below
    - text: |
        Measured distance
        values in mm.
      x: 25%
      y: 90%
      location: right
img_data_log_1:
  image: /learn/sensors/datalog-1.png
  alt: Datalog step 1
  width: 100%
  caption: >
    1. Copy the recorded measurements.
  labels:
    - text: 1. Right-click the output pane.
      x: 50%
      y: 15%
      location: above
    - text: 2. Select all data.
      x: 54%
      y: 38%
      location: right
    - text: 3. Copy the data.
      x: 54%
      y: 27%
      location: right
    - text: 4. Clear data before next experiment.
      x: 50%
      y: 46%
      location: below
img_data_log_2:
  image: /learn/sensors/datalog-2.png
  alt: Datalog step 2
  width: 100%
  caption: >
    2. Paste the data into a new spreadsheet and indicate separation by comma.
    This creates a column for time and a column for the distance. (If you use a
    different app that doesn't prompt you for this automatically,
    choose Data > Text to Columns in your app to achieve the same.
    If that doesn't work,
    paste it into a plain text file first, and import that file into your
    spreadsheet.)
  labels:
    - text: |
        1. Attempt to paste
        in the first cell
      x: 15%
      y: 20%
      location: above
    - text: 2. Data is separated by a comma.
      x: 32%
      y: 38%
      location: above
    - text: 3. Preview the result.
      x: 38%
      y: 70%
      location: right
    - text: 4. Click OK.
      x: 78%
      y: 80%
      location: right
img_data_log_3:
  image: /learn/sensors/datalog-3.png
  alt: Datalog step 3
  width: 100%
  caption: >
    3. Select the columns and begin inserting a chart. These steps should be
    similar in most spreadsheet apps. You may be able to go here directly
    by clicking on a chart icon.
  labels:
    - text: |
        1. Select
        first column.
      x: 8%
      y: 20%
      location: above
    - text: |
        2. Shift and click
        to select second
        column.
      x: 28%
      y: 20%
      location: above
    - text: 3. Insert
      x: 49.5%
      y: 7.5%
      location: right
    - text: 4. Chart...
      x: 65%
      y: 12%
      location: right
img_data_log_4:
  image: /learn/sensors/datalog-4.png
  alt: Datalog step 4
  width: 100%
  caption: >
    4. Configure the chart. Choose XY (Scatter) or similar. Select 'Lines Only'.
  labels:
    - text: 1. Create an XY chart
      x: 30%
      y: 47%
      location: left
    - text: 2. Lines only.
      x: 68%
      y: 46%
      location: below
    - text: 3. Finish.
      x: 85%
      y: 71%
      location: below
img_data_log_5:
  image: /learn/sensors/datalog-5.png
  alt: Datalog step 5
  width: 100%
  caption: >
    5. The end result. You can add additional labels for the X and Y axes for clarity.
  labels:
    - text: X-axis with time in ms.
      x: 57%
      y: 72%
      location: below
    - text: |
        Y-axis with
        distance in mm.
      x: 28%
      y: 50%
      location: left
    - text: |
        The robot was moved away
        from the wall and back again.
      x: 54%
      y: 40%
      location: right
movement:
  image: measuring-values/graph.svg
  alt: Recording movement
  width: 100%
  caption: >
    Distance and speed recording when driving the robot back and forth using
    the program shown above. Even if you hadn't seen it move, you can determine
    much of what it did by carefully looking at the graph.
  labels:
    - text: Maximum position (250 mm).
      x: 50%
      y: 11%
      location: right
    - text: Top speed.
      x: 32%
      y: 19%
      location: right
    - text: |
        500 ms
        pause.
      x: 42%
      y: 55%
      location: below
    - text: |
        Negative speed
        means reverse.
      x: 70%
      y: 76%
      location: below
L05_1_circle_scan:
  image: measuring-values/L05_1_circle_scan.svg
  alt: Recording movement
  width: 100%
  caption: >
    Graph for Challenge #5.1.G: A recording of the ultrasonic sensor measurement
    as the robot makes several full rotations. Based on this data, can you
    figure out where the robot is placed relative to the walls?
  labels:
    - text: Starting orientation
      x: 42%
      y: 55%
      location: right
challenge_wall:
  image: measuring-values/challenge_wall.svg
  alt: Recording movement
  width: 65%
  caption: >
    Overview for Challenge #5.1.H: Record data while driving in a square to
    determine where the robot started relative to the walls.
L05_1_datalog:
  image: measuring-values/L05_1_datalog.svg
  alt: Ultrasonic sensor distance measurement
  width: 100%
  caption: Recording of the distance measurement displayed in a graph.
---

Robots can't actually see or feel the way humans do, but by adding _sensors_ to
them, they can collect and report information about the environment around
them. LEGO robots come with a variety of sensors to measure distance, color, light
intensity, motion, and applied force. 

Your programs can interpret sensor information in ways that will make
your robot seem to respond to its environment, as if it is experiencing it. For
example, you can make your robot drive and turn around if it sees an obstacle.

{% include diagram.html data=page.requirements %}

In this section, you'll learn how to measure and report sensor values. Knowing
what each sensor measures is essential for building robots that can reliably
react to their environment.

We'll use [Inventor Bot with the SPIKE Ultrasonic
Sensor](/learn/building-a-robot/spike-prime/) to measure distance in the
following examples. This is a good way to practice with sensors because you can
easily see what is going on. Once you've mastered the essentials with this
sensor, you'll be better prepared to apply the same techniques to the color
sensor in the next chapter.

You can also follow along
with [other sensors](/learn/getting-started/what-do-you-need/#choosing-sensors)
that measure distance. If you don't have any sensors, you can still measure the
motor angle, as you'll see later in this chapter.

**Challenge #5.1.A: Robot sensations** ⸺ Create a table of human senses. For
each sense, describe what you can sense and how you sense it. Which of these
senses are available to your robot? Which sensors can be used to measure them?
Consider not just the sensors that you can plug in but also the sensors built
into the hub. **Research** ⸺ Download the [specifications](https://assets.education.lego.com/v3/assets/blt293eea581807678a/blt62a78c227edef070/5f8801b9a302dc0d859a732b/techspecs_techniccolorsensor.pdf?locale=en-us) for the SPIKE
Color Sensor.
Search the web to find specifications for the other sensors and the hub.
To find them, use search keywords from the Color Sensor data sheet. Determine
what each sensor measures and fill in your table with senses. For each value,
write down which units the values are reported in and how fast you can measure
them.
{: .notice--primary}

# Measuring sensor values

Let's start with a program to measure distance values. 
Create a new program and add the Ultrasonic Sensor Setup block. Then
create a loop that prints sensor values repeatedly by following these steps:

{% include diagram.html data=page.img_sensor_setup_1 %}

{% include diagram.html data=page.img_sensor_setup_2 %}

When you run the program, you should see a continuous stream of values in the
output pane. Move the robot around to see the values change. If values aren't
coming in or appear delayed, make sure the output pane is scrolled all the way
down. It should then continue to scroll down on its own.

Notice that the Measure Distance block has a rounded shape, unlike any of the
notched, rectangular blocks you've used so far. Any block that provides a
<i>value</i> has such a rounded shape. It does not do anything on its own, but
it passes its value to the block that you place it in. In this example, the
distance value was passed to the Print block. The underlying value (_abc_) is
ignored and the passed value (a number for distance) is used instead.

**Challenge #5.1.B: Blind spots** ⸺ The Ultrasonic Sensor measures the distance
to other objects by emitting an inaudible sound and measuring how long it takes
for the echo to come back. What is the nearest and farthest distance that you
can measure? Begin by pointing the sensor at a solid surface
like a wall or door. What does it report when it doesn't detect anything at
all? **Discuss** ⸺ What is the impact of different materials or the size and
shape of objects? Prepare a list of every day objects such as walls, curtains,
glass windows, pencils, coffee mugs or clothing. For each object, predict how
well the sensor will detect it. Discuss how well it will work up close or far
out, pointing straight at it or at an angle. Verify your hypotheses by
observing the measured values.
{: .notice--primary}


**Challenge #5.1.C: Measure and share** ⸺ The technique to display sensor
values works with any sensor. You'll learn to use all sensors in the coming
chapters, but you can already explore what they measure now. Create programs
similar to the one above, but set up different sensors. **Presentation** ⸺ Each
team member explores one sensor in detail. If a sensor can measure more than one
thing, coordinate the extra work with your team. For each sensor,
create a short demonstration and take turns presenting your findings. What can your
sensor measure? How accurate is it? Try it under various conditions, such
as in the dark or outside. Is there anything that surprised you?
{: .notice--primary}

# Recording sensor values

Displaying sensor values as you just did is a good way to gauge how well the
sensor works as you place it in different positions. To get a
better picture of what the robot sees during a mission, you can _record_
measurements for some time and analyze the recording afterward.

Create the following program to record distance values for
5 seconds. It is similar to your previous program, but it adds a Stopwatch
Setup block (from the Setup tab) and a Measure Time block (from the Input tab)
to display the elapsed time alongside the distance measurement. Note that the
Print block is configured to display a comma (`,`) between printed values.

{% include block-program.html
path="L05_1_datalog"
caption="Recording the distance measurement for 5 seconds."
width="90%"
%}

Run the program and move the robot around. The output pane gradually fills up
with 50 pairs of time (in milliseconds) and distance (mm) values. The Wait Time
block waits 100 ms between measurements, so the entire program runs in about 50
× 100 ms = 5000 ms, or five seconds.

You can display the measured data in a
graph to better see how the robot was moved. From the following graph, you can
see that the robot started about 320 mm from the wall. Then it was moved
farther back for two seconds and then towards the wall again towards the end
of the experiment.

{% include diagram.html data=page.L05_1_datalog %}

# Making your own graphs (optional)

By recording data, you can verify that your program or mission works as you
intended. For example, you could record color
sensor values and verify that a motor stops moving when it sees a black line. 

Making your own graphs is optional. You can skip this section if you are short
on time for your competition. Otherwise, it can be a great addition to your
presentation or innovation project. It's also a really useful skill to learn
beyond robotics.

The following steps show how to create a graph of the data you just recorded. 
You can use your favorite spreadsheet app if you already have one.
We'll use [LibreOffice](https://www.libreoffice.org/) here. It is
free and can be installed on most computers. 

{% include diagram.html data=page.img_data_log_1 %}

{% include diagram.html data=page.img_data_log_2 %}

{% include diagram.html data=page.img_data_log_3 %}

{% include diagram.html data=page.img_data_log_4 %}

{% include diagram.html data=page.img_data_log_5 %}

**Challenge #5.1.D: Where did the time go?** ⸺ In the experiment above, the
measurements are spaced almost exactly 100 ms apart. This might give you the
impression that measuring and printing values takes no time at all. Actually,
it only appears that way because 100 ms is plenty of time to send a few numbers
to your computer in the background without holding up your program. If you
print more text more quickly, you will see it start to impact
the time. To see this, try reducing the wait time to 1 ms. Click the > icon
on the Print block to add another value and make it print something like
"looooooong text". Analyze the time between the measurements. What is the
smallest and biggest gap? Are the time differences constant or do they change a
lot? **Discuss** ⸺ Could you have done the original experiment with the 100 ms
pause without the stopwatch block? Why is it still better to keep it?
{: .notice--primary}

# Recording movement  (optional)

Most LEGO motors have a built-in sensor that measures the traveled angle.
The drive base uses this information to figure out how far it has traveled. You
can read these measurements with the Drive Base Measure block from the Input tab.
This can be used to record information about how your robot moves, as shown in
the following example.

{% include block-program.html
path="L05_1_record_movement"
caption="Recording movement. This uses the Multitask block to drive and record
values at the same time. It is configured to run until <i>one task</i> completes
so that data recording stops when the experiments ends."
width="100%"
%}

As before, this program produces comma-separated data points that you can
copy to a spreadsheet editor if you want to make your own graph. The result
is similar to the following graph.

{% include diagram.html data=page.movement %}


**Challenge #5.1.E: Ramp it up** ⸺ Add two Drive Base Configuration blocks
to your program to choose a new drive speed and acceleration. Verify that it
reaches your configured top speed at the given acceleration. To verify the
acceleration, take the change in speed and divide it by the time it took to get
to top speed. You can determine this from the printed values, or using a graph
similar to the one above.
{: .notice--primary}

**Challenge #5.1.G: Where am I?** ⸺ Create a program that records the
Ultrasonic Sensor distance measurement as the robot turns around, as shown
below. Place the robot in a corner and run the experiment. Create a graph with
the robot angle on the x-axis and the sensor distance on the y-axis. An example
result is given below. Based on the graph alone, can you determine the
distances to the walls? What about the starting angle with respect to the
walls? **Discuss** ⸺ Some data points appear to be missing (they are not behind
the picture). Where are they? If you squint, you can almost see two line
segments that dip down in the middle. Compare the angles of both dips. How far
are they apart, and why? Why does a line graph not work in this case? Some
angles appear to have multiple clearly distinct distance values. What does this
overlap mean? Why does this occur just in between the two dips mentioned above?
Why is it useful to show the robot angle on the x-axis, instead of the time
like we did so far?
{: .notice--primary}

{% include diagram.html data=page.L05_1_circle_scan %}

{% include block-program.html
path="L05_1_circle_scan"
caption="The program for Challenge #5.1.G records the Ultrasonic Sensor distance
while the robot turns around."
width="100%"
%}


**Challenge #5.1.H: Hitting a wall** ⸺ Now it is your turn to design and
implement an experiment to determine the robot's position. This time, have the
robot drive in a square parallel to the walls of a corner, as shown below. You
decide which values to record and plot in a graph. For example, you might
record the Ultrasonic Sensor distance or drive base angle. For this experiment,
choose time for the X-axis.  **Discuss** ⸺ Before you run your experiment,
sketch what you think the graphs will look like. Assume that you start in
corner A and that Q is 250 mm and R is 500 mm. Run the experiment and verify
your prediction. Next, run the experiment from starting position B, C, or D.
Based on the data, ask your teammates where they think the robot started.
{: .notice--primary}

{% include diagram.html data=page.challenge_wall %}
