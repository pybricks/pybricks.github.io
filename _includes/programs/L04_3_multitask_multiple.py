# pybricks blocks file:{"blocks":{"languageVersion":0,"blocks":[{"type":"blockGlobalSetup","id":"bjK,wS1MYO7aiYkFSwd{","x":150,"y":100,"deletable":false,"next":{"block":{"type":"variables_set_inventor_hub","id":"EcWRSKTzE8G1)h1pxy_j","extraState":{"optionLevel":0},"fields":{"VAR":{"id":"Zy_6It30J{80Vsd-;(:N"}},"next":{"block":{"type":"variables_set_motor","id":"G?/C.hoF~+e0MLm1/]XR","fields":{"VAR":{"id":"-ryaz=O,#fuc;%63#d(8"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"de.avh#Lb?kUra3I=?XQ","fields":{"NAME":"A"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":":~cT215Z,yT90(BW!6t1","fields":{"SELECTION":"Direction.CLOCKWISE"}}}}}}}}},{"type":"blockGlobalStart","id":"3tJe|AWl0baN(wH9a$@.","x":150,"y":300,"deletable":false,"next":{"block":{"type":"blockMultiTask","id":"pxDz+Vd)JPA.8OQA?@d~","extraState":{"optionLevel":2},"fields":{"METHOD":"MULTITASK_ALL"},"inputs":{"TASK0":{"block":{"type":"blockMotorRun","id":"%uP]UpKt.Z5BuT^OO(t]","extraState":{"optionLevel":1},"fields":{"METHOD":"MOTOR_RUN_FOR"},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"9z~1-XT3!GV5zGYaR07p","fields":{"VAR":{"id":"-ryaz=O,#fuc;%63#d(8","name":"motor","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_angularVelocity","id":"B)xRomjCX4f)}Yv9Ktu*","fields":{"VALUE0":500}}},"ANGLE":{"shadow":{"type":"unit_angle","id":"Lp%COsWzFNQ^ro[6p,QW","fields":{"VALUE0":360}}},"THEN":{"shadow":{"type":"parameters_stop_4","id":"@8n;Mo7tl7lwfb$~81xR","fields":{"VALUE":"Stop.HOLD"}}}}}},"TASK1":{"block":{"type":"blockSpeakerBeep","id":"^Laqf==@OaD#PK77_Yze","inputs":{"VAR":{"shadow":{"type":"variables_get_speaker_hub","id":"G1ptd@wqC|||bz60,I{8","fields":{"VAR":{"id":"Zy_6It30J{80Vsd-;(:N","name":"hub","type":"InventorHub"}}}},"VALUE0":{"shadow":{"type":"unit_frequency","id":"+fRxk~2PCT{`8elg9`Yy","fields":{"VALUE0":500}}},"VALUE1":{"shadow":{"type":"unit_time","id":"VBzfq/5YJXlAD7HMPdKq","fields":{"VALUE0":100}}}}}},"TASK2":{"block":{"type":"blockLightOnColor","id":"(=H1C*6Mgonvq0HprRMG","extraState":{"optionLevel":1},"fields":{"METHOD":"LIGHT_ON"},"inputs":{"VAR":{"shadow":{"type":"variables_get_color_light_device","id":"FzDTdrLd{Dk+mZN`Fy{y","fields":{"VAR":{"id":"Zy_6It30J{80Vsd-;(:N","name":"hub","type":"InventorHub"}}}},"COLOR":{"shadow":{"type":"variables_get_color","id":"VPEw$Zd$q3a|Uic)np#h","fields":{"COLOUR":"#ff0000","VAR":{"id":"GP{PP(%Lj}*K`Oi#z+Q7","name":"red","type":"ColorDef"}}}}},"next":{"block":{"type":"blockWaitTime","id":"wjat9b)]uSAV,#P@~=3.","inputs":{"VALUE0":{"shadow":{"type":"unit_time","id":"JM%@%`Sh,bmFYMddB][-","fields":{"VALUE0":500}}}},"next":{"block":{"type":"blockLightOnColor","id":"1%Fg7^P(m3n]Zc3g)kRY","extraState":{"optionLevel":1},"fields":{"METHOD":"LIGHT_ON"},"inputs":{"VAR":{"shadow":{"type":"variables_get_color_light_device","id":"VU$EM9VAGQ~irT$w,@:q","fields":{"VAR":{"id":"Zy_6It30J{80Vsd-;(:N","name":"hub","type":"InventorHub"}}}},"COLOR":{"shadow":{"type":"variables_get_color","id":"VG#8HDGc!qfyQYAi;0|l","fields":{"COLOUR":"#00ff00","VAR":{"id":"-3*J5oPEj?z:C+w?Op|]","name":"green","type":"ColorDef"}}}}},"next":{"block":{"type":"blockWaitTime","id":"2x@WZ]kpXW@(XCt3w%]j","inputs":{"VALUE0":{"shadow":{"type":"unit_time","id":"Z/R]PrNKm|4ss)GP;JQd","fields":{"VALUE0":500}}}}}}}}}}}},"TASK3":{"block":{"type":"blockPrint","id":",7N4vrJY|bs5QYyGu!/P","extraState":{"optionLevel":0},"inputs":{"TEXT0":{"shadow":{"type":"text","id":"f)Oo3Va$P9fn/a|Yb4TQ","fields":{"TEXT":"Hello"}}}},"next":{"block":{"type":"blockWaitTime","id":"SOob0II[OE829Gf8`PvG","inputs":{"VALUE0":{"shadow":{"type":"unit_time","id":"Y2SQENAIZF1|MYYnMgAp","fields":{"VALUE0":500}}}},"next":{"block":{"type":"blockPrint","id":"B1h8y@ySLW[r5iMQp[zT","extraState":{"optionLevel":0},"inputs":{"TEXT0":{"shadow":{"type":"text","id":"}9Wbw4Ak8ZAfNCCMO9)r","fields":{"TEXT":"world"}}}}}}}}}}}}}}]},"variables":[{"name":"red","id":"GP{PP(%Lj}*K`Oi#z+Q7","type":"ColorDef"},{"name":"orange","id":"FpJPQD;Ozzn!g~9ue+y0","type":"ColorDef"},{"name":"yellow","id":"lEJ$p$Re+Dd-IMNU3J7w","type":"ColorDef"},{"name":"green","id":"-3*J5oPEj?z:C+w?Op|]","type":"ColorDef"},{"name":"cyan","id":"m`RGE^Wa^3LEw@USPrh^","type":"ColorDef"},{"name":"blue","id":"!DlyU3c*,j$4!aMV:v=,","type":"ColorDef"},{"name":"violet","id":",O?ZdgF.TbjU88U$bQd;","type":"ColorDef"},{"name":"magenta","id":"OSVsW|*#DcC]+11-~=P*","type":"ColorDef"},{"name":"white","id":"ZYmh$f7MkyD/LCI^]Io]","type":"ColorDef"},{"name":"none","id":"l$v1=yeSF}5d{3eyo2O1","type":"ColorDef"},{"name":"motor","id":"-ryaz=O,#fuc;%63#d(8","type":"Motor"},{"name":"hub","id":"Zy_6It30J{80Vsd-;(:N","type":"InventorHub"}],"info":{"type":"pybricks","version":"1.3.2"}}
from pybricks.hubs import InventorHub
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.tools import multitask, run_task, wait

# Set up all devices.
hub = InventorHub()
motor = Motor(Port.A, Direction.CLOCKWISE)

async def subtask():
    hub.light.on(Color.RED)
    await wait(500)
    hub.light.on(Color.GREEN)
    await wait(500)

async def subtask2():
    print('Hello')
    await wait(500)
    print('world')

async def main():
    await multitask(
        motor.run_angle(500, 360),
        hub.speaker.beep(500, 100),
        subtask(),
        subtask2(),
    )


run_task(main())