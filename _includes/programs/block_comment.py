# pybricks blocks file:{"blocks":{"languageVersion":0,"blocks":[{"type":"blockGlobalSetup","id":"bjK,wS1MYO7aiYkFSwd{","x":0,"y":0,"deletable":false,"next":{"block":{"type":"variables_set_motor","id":"YF_NAJ7:ChSZ0*EUQ[`#","fields":{"VAR":{"id":"9.5u$nHeY4sFbF*sA!4)"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"vlf@Jlb%oC-1TC5L`rB|","fields":{"NAME":"A"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"+EPYxbhjZxL}m+M@kupV","fields":{"SELECTION":"Direction.CLOCKWISE"}}}}}}},{"type":"blockGlobalStart","id":"3tJe|AWl0baN(wH9a$@.","x":0,"y":192,"deletable":false,"next":{"block":{"type":"blockComment","id":"(Orr6QzbdbdnR,G/X,S`","fields":{"FIELDNAME":"Run the motor to the zero marker"},"next":{"block":{"type":"blockMotorRun","id":"DnnRjc*J!E_7a7F%j2`A","extraState":{"optionLevel":2},"fields":{"METHOD":"MOTOR_RUN_TO"},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"-r~*xc{V{szPs5.CtbQ]","fields":{"VAR":{"id":"9.5u$nHeY4sFbF*sA!4)","name":"motor","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_angularVelocity","id":"garUF6YIPmEG%ir{a.9h","fields":{"VALUE0":500}}},"ANGLE":{"shadow":{"type":"unit_angle","id":"N1Q~Ek_It,Mbt6v`G9_1","fields":{"VALUE0":0}}},"THEN":{"shadow":{"type":"parameters_stop_4","id":"^=Kb;?L#Ru-A)NXd;rM!","fields":{"VALUE":"Stop.HOLD"}}}}}}}}}]},"variables":[{"name":"red","id":"|e*]R-ph?|DS8maY)M`3","type":"ColorDef"},{"name":"orange","id":"jEPnVh:/H3|QE,mM`z7]","type":"ColorDef"},{"name":"yellow","id":"$(+,/VY_[{uzL-0Y!--#","type":"ColorDef"},{"name":"green","id":";Fw,_kp0[[p#U:~U8v0a","type":"ColorDef"},{"name":"cyan","id":"^U5)Kv^_T8qoG84uloH0","type":"ColorDef"},{"name":"blue","id":"]51(*A[rgqq1u/dh5_vg","type":"ColorDef"},{"name":"violet","id":"gCm@~3L-4{TALavGlyNQ","type":"ColorDef"},{"name":"magenta","id":"!?pggV|u^C#qOSz4/-s$","type":"ColorDef"},{"name":"white","id":"XwRWo?Ee7hDb3;6x!j?Q","type":"ColorDef"},{"name":"none","id":"(F{7F|3r,|G7hdo}@fH2","type":"ColorDef"},{"name":"motor","id":"9.5u$nHeY4sFbF*sA!4)","type":"Motor"},{"name":"hub","id":"NTjDi;7upvcqELI?S[.z","type":"EssentialHub"}],"info":{"type":"pybricks","version":"1.2.2"}}
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor

# Set up all devices.
motor = Motor(Port.A, Direction.CLOCKWISE)


# The main program starts here.
# Run the motor to the zero marker
motor.run_target(500, 0)