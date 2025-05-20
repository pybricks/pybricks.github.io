# pybricks blocks file:{"blocks":{"languageVersion":0,"blocks":[{"type":"blockGlobalSetup","id":"bjK,wS1MYO7aiYkFSwd{","x":150,"y":100,"deletable":false,"next":{"block":{"type":"variables_set_inventor_hub","id":"EcWRSKTzE8G1)h1pxy_j","extraState":{"optionLevel":0},"fields":{"VAR":{"id":"lk?MN~GXq4mb}RGgTVKc"}},"next":{"block":{"type":"variables_set_motor","id":"G?/C.hoF~+e0MLm1/]XR","fields":{"VAR":{"id":"-ryaz=O,#fuc;%63#d(8"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"de.avh#Lb?kUra3I=?XQ","fields":{"NAME":"A"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":":~cT215Z,yT90(BW!6t1","fields":{"SELECTION":"Direction.CLOCKWISE"}}}}}}}}},{"type":"blockGlobalStart","id":"3tJe|AWl0baN(wH9a$@.","x":150,"y":300,"deletable":false,"next":{"block":{"type":"blockMultiTask","id":".dmF[tL6)oK){6VKd[Uc","extraState":{"optionLevel":0},"fields":{"METHOD":"MULTITASK_RACE"},"inputs":{"TASK0":{"block":{"type":"blockFlowRepeat","id":"b-];Nq9TbjYf#%;(k.D6","inputs":{"TIMES":{"shadow":{"type":"blockMathNumber","id":"LEIj(tsCm:tyHRZtKXv`","fields":{"NUM":5}}},"DO":{"block":{"type":"blockPrint","id":"A(]kn$0R)x?}Wdt=]:H%","extraState":{"optionLevel":0},"inputs":{"TEXT0":{"shadow":{"type":"text","id":"cjt2hOKHm-Si@Tn@bR|e","fields":{"TEXT":"Go!"}}}},"next":{"block":{"type":"blockMultiTask","id":"uktQeLW[.Z=m*Xq.R`N9","extraState":{"optionLevel":0},"fields":{"METHOD":"MULTITASK_ALL"},"inputs":{"TASK0":{"block":{"type":"blockMotorRun","id":"!d7h?CNkO,Gsu6!!J[qh","extraState":{"optionLevel":1},"fields":{"METHOD":"MOTOR_RUN_FOR"},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"$7ji}B+zdzcg4Rsz*z`=","fields":{"VAR":{"id":"-ryaz=O,#fuc;%63#d(8","name":"motor","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_angularVelocity","id":"X5x$Me7,fVRs(RjLgc:{","fields":{"VALUE0":500}}},"ANGLE":{"shadow":{"type":"unit_angle","id":"MQT:3_b|E4z*Lchb$i.!","fields":{"VALUE0":360}}},"THEN":{"shadow":{"type":"parameters_stop_4","id":"ySpDRIB+z7;t$!0vLv^T","fields":{"VALUE":"Stop.HOLD"}}}}}},"TASK1":{"block":{"type":"blockSpeakerBeep","id":"QK[1bDBz)*u:e)X]*%WX","inputs":{"VAR":{"shadow":{"type":"variables_get_speaker_hub","id":"$qce+Dt]N_3Wt2_lk2QE","fields":{"VAR":{"id":"lk?MN~GXq4mb}RGgTVKc","name":"hub","type":"InventorHub"}}}},"VALUE0":{"shadow":{"type":"unit_frequency","id":"*D67;8|hT]X;n.d5Y_S7","fields":{"VALUE0":500}}},"VALUE1":{"shadow":{"type":"unit_time","id":"3X]~iS%2nz[{*UGd_yJO","fields":{"VALUE0":700}}}}}}}}}}}}}},"TASK1":{"block":{"type":"blockFlowWhile","id":"x)*Hd=Bn*=-bwNBMeav@","fields":{"MODE":"WHILE"},"inputs":{"BOOL":{"shadow":{"type":"blockLogicTrue","id":"jzw_j1lYrj{i3n0LiW8J"}},"DO":{"block":{"type":"blockPrint","id":"#Xfc-~`3W:AhnTWYUFkN","extraState":{"optionLevel":0},"inputs":{"TEXT0":{"shadow":{"type":"text","id":"Q)-h.PF{e}AqXUhAg5db","fields":{"TEXT":"Green"}}}},"next":{"block":{"type":"blockLightOnColor","id":"H5jY;9S0!W[^WNr(lTjP","extraState":{"optionLevel":1},"fields":{"METHOD":"LIGHT_ON"},"inputs":{"VAR":{"shadow":{"type":"variables_get_color_light_device","id":"DS9d~*TL%Tf;)2MYRM0,","fields":{"VAR":{"id":"lk?MN~GXq4mb}RGgTVKc","name":"hub","type":"InventorHub"}}}},"COLOR":{"shadow":{"type":"variables_get_color","id":"nx}xS}+$C3m[U*:${9}`","fields":{"COLOUR":"#00ff00","VAR":{"id":"-3*J5oPEj?z:C+w?Op|]","name":"green","type":"ColorDef"}}}}},"next":{"block":{"type":"blockWaitTime","id":"M$q55XRcs?^Q3V#|s#BY","inputs":{"VALUE0":{"shadow":{"type":"unit_time","id":"6mHL;ctc-|s?`f[]9tMQ","fields":{"VALUE0":1000}}}},"next":{"block":{"type":"blockPrint","id":"N}!7|NNgz{;@%{I_CZ;k","extraState":{"optionLevel":0},"inputs":{"TEXT0":{"shadow":{"type":"text","id":"`*h[lR08)k}f[RE2LQ,l","fields":{"TEXT":"Red"}}}},"next":{"block":{"type":"blockLightOnColor","id":"vS$2~BC|+Mg7G|?{LNKm","extraState":{"optionLevel":1},"fields":{"METHOD":"LIGHT_ON"},"inputs":{"VAR":{"shadow":{"type":"variables_get_color_light_device","id":"]!MJdl.?(=~O!8^D`B~q","fields":{"VAR":{"id":"lk?MN~GXq4mb}RGgTVKc","name":"hub","type":"InventorHub"}}}},"COLOR":{"shadow":{"type":"variables_get_color","id":"pFW-yCRH:gnOJy+skS.w","fields":{"COLOUR":"#ff0000","VAR":{"id":"GP{PP(%Lj}*K`Oi#z+Q7","name":"red","type":"ColorDef"}}}}},"next":{"block":{"type":"blockWaitTime","id":"aGNtI(KqgdG56._MVxFZ","inputs":{"VALUE0":{"shadow":{"type":"unit_time","id":".M*.H5ZGAP4lU~Dl%83-","fields":{"VALUE0":1000}}}}}}}}}}}}}}}}}}}}}}}]},"variables":[{"name":"red","id":"GP{PP(%Lj}*K`Oi#z+Q7","type":"ColorDef"},{"name":"orange","id":"FpJPQD;Ozzn!g~9ue+y0","type":"ColorDef"},{"name":"yellow","id":"lEJ$p$Re+Dd-IMNU3J7w","type":"ColorDef"},{"name":"green","id":"-3*J5oPEj?z:C+w?Op|]","type":"ColorDef"},{"name":"cyan","id":"m`RGE^Wa^3LEw@USPrh^","type":"ColorDef"},{"name":"blue","id":"!DlyU3c*,j$4!aMV:v=,","type":"ColorDef"},{"name":"violet","id":",O?ZdgF.TbjU88U$bQd;","type":"ColorDef"},{"name":"magenta","id":"OSVsW|*#DcC]+11-~=P*","type":"ColorDef"},{"name":"white","id":"ZYmh$f7MkyD/LCI^]Io]","type":"ColorDef"},{"name":"none","id":"l$v1=yeSF}5d{3eyo2O1","type":"ColorDef"},{"name":"motor","id":"-ryaz=O,#fuc;%63#d(8","type":"Motor"},{"name":"twinkle","id":"UCxen+,P#VN.kifAuUbX","type":"Function"},{"name":"my task","id":"B#yI,^.~7BeBNd8cxcj[","type":"Function"},{"name":"hub","id":"lk?MN~GXq4mb}RGgTVKc","type":"InventorHub"},{"name":"light","id":"Jb3@2ny$yg~7R0_RJBSA","type":"InventorHub"}],"info":{"type":"pybricks","version":"1.3.2"}}
from pybricks.hubs import InventorHub
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.tools import multitask, run_task, wait

# Set up all devices.
hub = InventorHub()
motor = Motor(Port.A, Direction.CLOCKWISE)

async def subtask():
    for count in range(5):
        await wait(0)
        print('Go!')
        await multitask(
            motor.run_angle(500, 360),
            hub.speaker.beep(500, 700),
        )

async def subtask2():
    while True:
        await wait(0)
        print('Green')
        hub.light.on(Color.GREEN)
        await wait(1000)
        print('Red')
        hub.light.on(Color.RED)
        await wait(1000)

async def main():
    await multitask(
        subtask(),
        subtask2(),
        race=True,
    )


run_task(main())