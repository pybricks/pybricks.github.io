# pybricks blocks file:{"blocks":{"languageVersion":0,"blocks":[{"type":"blockGlobalSetup","id":"bjK,wS1MYO7aiYkFSwd{","x":150,"y":100,"deletable":false,"next":{"block":{"type":"variables_set_xbox_controller","id":"_vMJj{h[SJY(_ImRcU?Q","fields":{"VAR":{"id":"z_Tc)Nn.l(D[kmxXQjhK"}},"next":{"block":{"type":"variables_set_motor","id":"3|KQBw699p3!/5XZ8u/p","fields":{"VAR":{"id":"LCxnhG6y-Pu;_R=`8zc/"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"f32qHv(^3}ggNsr_}dA5","fields":{"NAME":"A"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"~pqg4|zr}+mLQFgpmY(=","fields":{"SELECTION":"Direction.CLOCKWISE"}}}}}}}}},{"type":"blockGlobalStart","id":"3tJe|AWl0baN(wH9a$@.","x":150,"y":300,"deletable":false,"next":{"block":{"type":"blockMotorRun","id":"-,9q0%WlT$P%k#^Z{uAp","extraState":{"optionLevel":0},"fields":{"METHOD":"MOTOR_RUN_FOREVER"},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"Nuk2#K_1zi}3D#U]w+G%","fields":{"VAR":{"id":"LCxnhG6y-Pu;_R=`8zc/","name":"motor","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_angularVelocity","id":"7SLHs+g1HT0K!=f^m`qO","fields":{"VALUE0":300}}}},"next":{"block":{"type":"blockFlowWhile","id":"U+r0Q+2}5r.L9![^1UHk","fields":{"MODE":"WHILE"},"inputs":{"BOOL":{"shadow":{"type":"blockLogicTrue","id":"cK?yi*~Dv!{l9~BfqMvW"}},"DO":{"block":{"type":"blockComment","id":":G54uP+6`)h5JnJh|V$.","fields":{"FIELDNAME":"Rumble the controller if the motor experiences load.\n\nThat's force feedback!"},"next":{"block":{"type":"blockIfElse","id":"KOD=h,wAhnSz/elYD,Lv","extraState":{"optionLevel":0},"inputs":{"IF0":{"shadow":{"type":"blockLogicTrue","id":"Pnpf#WGQsGRc2Td;[{;j"},"block":{"type":"blockLogicCompare","id":"Y_A)u]AU1,ft^]@7fs^O","fields":{"OP1":"GTE"},"inputs":{"A":{"shadow":{"type":"blockMathNumber","id":"vEo*2uNwk:g`8O?Ko:[k","fields":{"NUM":3}},"block":{"type":"blockMathOp","id":"Jg,Nx!h$%m7y1E$/Qj[q","extraState":{"optionLevel":0},"fields":{"OP":"ABS"},"inputs":{"NUM":{"shadow":{"type":"blockMathNumber","id":"PIuaq^Usz.8fSk!qI|tj","fields":{"NUM":0}},"block":{"type":"blockMotorMeasure","id":"/)yUwW]dc-M.DVWbae~Q","extraState":{"optionLevel":4},"fields":{"METHOD":"MOTOR_LOAD"},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"8XS~:}#~aDhO4c8M4Hgz","fields":{"VAR":{"id":"LCxnhG6y-Pu;_R=`8zc/","name":"motor","type":"Motor"}}}}}}}}}},"B":{"shadow":{"type":"blockMathNumber","id":"#.3zD:UGN;tDp?#$3r|y","fields":{"NUM":50}}}}}},"DO0":{"block":{"type":"blockGamepadRumble","id":"]le2F3ZpvvFu,$9*,tJ;","extraState":{"optionLevel":0},"inputs":{"VAR":{"shadow":{"type":"variables_get_gamepad","id":"ar3+v=^x,/Aif[mL)6A6","fields":{"VAR":{"id":"z_Tc)Nn.l(D[kmxXQjhK","name":"controller","type":"XboxController"}}}},"VALUE0":{"shadow":{"type":"unit_percent","id":"#@EQTpdn~=9=[jvLEtQx","fields":{"VALUE0":100}}},"VALUE1":{"shadow":{"type":"unit_time","id":"D3;*#lX[)FcBKZkI/lPK","fields":{"VALUE0":200}}}}}}},"next":{"block":{"type":"blockWaitTime","id":"r+3VtSH?h1!RUAeS@|47","inputs":{"VALUE0":{"shadow":{"type":"unit_time","id":"h-WZX-yp9:,nF-ZCNGg/","fields":{"VALUE0":200}}}}}}}}}}}}}}}}]},"variables":[{"name":"red","id":"FSrCOQ$#^VFjcq~UX`vn","type":"ColorDef"},{"name":"orange","id":"zOsZT],9`,y[2hG}qx:$","type":"ColorDef"},{"name":"yellow","id":"@L;1`sBnV;iC)?J7#PlG","type":"ColorDef"},{"name":"green","id":"K7YO#sRNG$_tW~Ol=pM[","type":"ColorDef"},{"name":"cyan","id":"00|D4n~c7:I^}YrQFX:p","type":"ColorDef"},{"name":"blue","id":"QcX.`!~HloWK?WhNy0Kl","type":"ColorDef"},{"name":"violet","id":"_}hYU/d+~;5V.NV0svMM","type":"ColorDef"},{"name":"magenta","id":"~@d;Zl(/hM|k@Zfxa6Rj","type":"ColorDef"},{"name":"white","id":"f0PEA`E}A5jT:$Mco6gb","type":"ColorDef"},{"name":"none","id":"l{w#_3OMBT8pFwTgvvL9","type":"ColorDef"},{"name":"controller","id":"z_Tc)Nn.l(D[kmxXQjhK","type":"XboxController"},{"name":"motor","id":"LCxnhG6y-Pu;_R=`8zc/","type":"Motor"}],"info":{"type":"pybricks","version":"1.2.2"}}
from pybricks.iodevices import XboxController
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.tools import wait

# Set up all devices.
motor = Motor(Port.A, Direction.CLOCKWISE)
controller = XboxController()


# The main program starts here.
motor.run(300)
while True:
    # Rumble the controller if the motor experiences load.

    # That's force feedback!
    if abs(motor.load()) >= 50:
        controller.rumble(100, 200)
    wait(200)