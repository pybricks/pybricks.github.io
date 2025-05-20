# pybricks blocks file:{"blocks":{"languageVersion":0,"blocks":[{"type":"blockGlobalSetup","id":"bjK,wS1MYO7aiYkFSwd{","x":150,"y":100,"deletable":false,"next":{"block":{"type":"variables_set_inventor_hub","id":"EcWRSKTzE8G1)h1pxy_j","extraState":{"optionLevel":0},"fields":{"VAR":{"id":"lk?MN~GXq4mb}RGgTVKc"}},"next":{"block":{"type":"variables_set_motor","id":"G?/C.hoF~+e0MLm1/]XR","fields":{"VAR":{"id":"-ryaz=O,#fuc;%63#d(8"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"de.avh#Lb?kUra3I=?XQ","fields":{"NAME":"A"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":":~cT215Z,yT90(BW!6t1","fields":{"SELECTION":"Direction.CLOCKWISE"}}}}}}}}},{"type":"blockGlobalStart","id":"3tJe|AWl0baN(wH9a$@.","x":150,"y":300,"deletable":false,"next":{"block":{"type":"blockMultiTask","id":"pxDz+Vd)JPA.8OQA?@d~","extraState":{"optionLevel":0},"fields":{"METHOD":"MULTITASK_RACE"},"inputs":{"TASK0":{"block":{"type":"blockMotorRun","id":"%uP]UpKt.Z5BuT^OO(t]","extraState":{"optionLevel":1},"fields":{"METHOD":"MOTOR_RUN_FOR"},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"9z~1-XT3!GV5zGYaR07p","fields":{"VAR":{"id":"-ryaz=O,#fuc;%63#d(8","name":"motor","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_angularVelocity","id":"B)xRomjCX4f)}Yv9Ktu*","fields":{"VALUE0":500}}},"ANGLE":{"shadow":{"type":"unit_angle","id":"Lp%COsWzFNQ^ro[6p,QW","fields":{"VALUE0":360}}},"THEN":{"shadow":{"type":"parameters_stop_4","id":"@8n;Mo7tl7lwfb$~81xR","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockPrint","id":"p/wP=CDWp%Tls|}cTR10","extraState":{"optionLevel":0},"inputs":{"TEXT0":{"shadow":{"type":"text","id":",nVMzv|Y{TX.?J8i];Am","fields":{"TEXT":"Complete!"}}}}}}}},"TASK1":{"block":{"type":"blockWaitTime","id":"]?D(4L,q+1A1lhy-%8gE","inputs":{"VALUE0":{"shadow":{"type":"unit_time","id":"Rwpa[QVRkXo0?O3)mFtP","fields":{"VALUE0":2000}}}},"next":{"block":{"type":"blockPrint","id":"XgHP},ebpB@Tg^2!F[Fp","extraState":{"optionLevel":0},"inputs":{"TEXT0":{"shadow":{"type":"text","id":"{(t9=A|a5S|Bi=m2KihD","fields":{"TEXT":"I got stuck!"}}}}}}}}}}}}]},"variables":[{"name":"red","id":"GP{PP(%Lj}*K`Oi#z+Q7","type":"ColorDef"},{"name":"orange","id":"FpJPQD;Ozzn!g~9ue+y0","type":"ColorDef"},{"name":"yellow","id":"lEJ$p$Re+Dd-IMNU3J7w","type":"ColorDef"},{"name":"green","id":"-3*J5oPEj?z:C+w?Op|]","type":"ColorDef"},{"name":"cyan","id":"m`RGE^Wa^3LEw@USPrh^","type":"ColorDef"},{"name":"blue","id":"!DlyU3c*,j$4!aMV:v=,","type":"ColorDef"},{"name":"violet","id":",O?ZdgF.TbjU88U$bQd;","type":"ColorDef"},{"name":"magenta","id":"OSVsW|*#DcC]+11-~=P*","type":"ColorDef"},{"name":"white","id":"ZYmh$f7MkyD/LCI^]Io]","type":"ColorDef"},{"name":"none","id":"l$v1=yeSF}5d{3eyo2O1","type":"ColorDef"},{"name":"motor","id":"-ryaz=O,#fuc;%63#d(8","type":"Motor"},{"name":"hub","id":"lk?MN~GXq4mb}RGgTVKc","type":"InventorHub"}],"info":{"type":"pybricks","version":"1.3.2"}}
from pybricks.hubs import InventorHub
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.tools import multitask, run_task, wait

# Set up all devices.
hub = InventorHub()
motor = Motor(Port.A, Direction.CLOCKWISE)

async def subtask():
    await motor.run_angle(500, 360)
    print('Complete!')

async def subtask2():
    await wait(2000)
    print('I got stuck!')

async def main():
    await multitask(
        subtask(),
        subtask2(),
        race=True,
    )


run_task(main())