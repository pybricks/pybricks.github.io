---
title: Absolute and relative position and the shortest path
excerpt: >
  What is the absolute or relative angle, what is the shortest path?
header:
  teaser: /learn/making-programs/basics-motor-setup-3.png

---

If you are coming to Pybricks after using the LEGO Education SPIKE app, you
might have seen references to the _position_ and the _relative position_, and
moving by the shortest path.

These terms can be somewhat ambiguous and you don't need to use them, but it
makes sense to properly define them if you used them in your previous programs.

# Relative and absolute position

According to the documentation of the latest SPIKE App (V3.4), the _relative
position_ is defined as follows:

> "This block returns the number of degrees that the specified motor has turned
> since the program started."

But this is not true. It used to be that way in previous versions of that app.
If you display the relative position now, you'll find that it instead equals
the Pybricks definition as introduced [here](/learn/motors/single-motor/).

The absolute position (or just position) is also the same angle, but it
discards whole rotations and negative values. If you wish to use this
representation in Pybricks, you can obtain it as follows:

{% include scaled.html path="/learn/motors/absolute-angle.png" width="60%"  %}

# "The shortest path"





> TODO: example where it breaks, e.g. mechanical limit, still depends where you start...

> TODO: however, explain that now it does matter about the init....

