# pybricks blocks file:{"blocks":{"languageVersion":0,"blocks":[{"type":"blockGlobalSetup","id":"bjK,wS1MYO7aiYkFSwd{","x":26,"y":23,"deletable":false,"next":{"block":{"type":"variables_set_motor","id":"`ckvX72RRO2%rJ%B|(M6","fields":{"VAR":{"id":"I53Xcpt{AF/^Y~er!Ae."}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"voXqQmvRsz}to7s^|3B#","fields":{"NAME":"A"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"T#QvY]QaZJS(-z[LvR54","fields":{"SELECTION":"Direction.COUNTERCLOCKWISE"}}}},"next":{"block":{"type":"variables_set_motor","id":"p3aVuKxCqO{AWWf)qy9}","fields":{"VAR":{"id":"WU?-A7sr@(wylvY9bml."}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"8P:X%+o@Fhoyr13,cY#x","fields":{"NAME":"B"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"APQW8~Z9Ow68Y$oBKHn-","fields":{"SELECTION":"Direction.CLOCKWISE"}}}},"next":{"block":{"type":"variables_set_drive_base","id":")7*br?PVxjM-e620.S`_","fields":{"VAR":{"id":"tx+grocr(+gz|!!aOwj["}},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"(mx$![/|%~SNmQfJxt(_","fields":{"VAR":{"id":"I53Xcpt{AF/^Y~er!Ae.","name":"left","type":"Motor"}}}},"VAR2":{"shadow":{"type":"variables_get_motor_device","id":"`zb:UrDtrwr#hhJ!y:TM","fields":{"VAR":{"id":"WU?-A7sr@(wylvY9bml.","name":"right","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_distance","id":"QNa,,]3Gx,ncIY9)^]`0","fields":{"VALUE0":56}}},"VALUE1":{"shadow":{"type":"unit_distance","id":")FU%$Ue*_bTxp2bwgNH:","fields":{"VALUE0":128}}}},"next":{"block":{"type":"variables_set_ultrasonic_sensor","id":"dZ1_$tvX@SsrW}R.iZ*}","fields":{"VAR":{"id":"34|JQ1oqFiClXIo$D;QD"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"8H?xxb)v`@hs~ttLto:U","fields":{"NAME":"D"}}}}}}}}}}}}},{"type":"blockGlobalStart","id":"3tJe|AWl0baN(wH9a$@.","x":27,"y":315,"deletable":false,"next":{"block":{"type":"blockMultiTask","id":"]Ztnk0#VmzR+|I9-!g,l","extraState":{"optionLevel":0},"fields":{"METHOD":"MULTITASK_RACE"},"inputs":{"TASK0":{"block":{"type":"blockFlowWhile","id":"tZ)lr]zQ)hl27m2{*m4`","fields":{"MODE":"WHILE"},"inputs":{"BOOL":{"shadow":{"type":"blockLogicTrue","id":"L;4*UHt3i,X[AAH|UJUr"}},"DO":{"block":{"type":"blockDriveBaseDrive2","id":"G@bVK4{+O$dJH}E6M`qJ","extraState":{"optionLevel":2},"fields":{"METHOD":"DRIVEBASE_DRIVE_STRAIGHT"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"E~3nl#7UwK8+BZK`M8gD","fields":{"VAR":{"id":"tx+grocr(+gz|!!aOwj[","name":"robot","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_distance","id":"qemo/vm`||tp:9gb]l2U","fields":{"VALUE0":250}}},"ARG1":{"shadow":{"type":"parameters_stop_4","id":"zDFf^0%DiZ0Uw,vpT%UY","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockDriveBaseDrive2","id":"SmW.0hfQ`e_SS(M/K.A~","extraState":{"optionLevel":3},"fields":{"METHOD":"DRIVEBASE_DRIVE_TURN"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"+lzYK-a@kU[j`M]n0I9#","fields":{"VAR":{"id":"tx+grocr(+gz|!!aOwj[","name":"robot","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_angle","id":"^W3MkldHaVj*bKZHrB8D","fields":{"VALUE0":90}}},"ARG1":{"shadow":{"type":"parameters_stop_4","id":"JhEPjYe[q6XhAtS9gqjJ","fields":{"VALUE":"Stop.HOLD"}}}}}}}}}}},"TASK1":{"block":{"type":"blockWaitUntil","id":"A#F+/vZ]Rw02-)VdkpQ%","inputs":{"BOOL":{"shadow":{"type":"blockLogicTrue","id":"K_i061]`,kDSyuIRWK^v"},"block":{"type":"blockLogicCompare","id":".aiCa*48@0ST`FF7I2ek","fields":{"OP1":"LTE"},"inputs":{"A":{"shadow":{"type":"blockMathNumber","id":"]^m4TiuI@|Uy#CIdVb3i","fields":{"NUM":3}},"block":{"type":"blockDistance","id":"@3eU[VTJ/FLIZv8W%7M@","inputs":{"VAR":{"shadow":{"type":"variables_get_distance_device","id":"VT5E*f,FYe^icOj88XMN","fields":{"VAR":{"id":"34|JQ1oqFiClXIo$D;QD","name":"sensor","type":"UltrasonicSensor"}}}}}}},"B":{"shadow":{"type":"blockMathNumber","id":"!1Gt[7/I.^[(snG7~_cm","fields":{"NUM":500}}}}}}}}}}}}}]},"variables":[{"name":"red","id":"zTWBdr:x]9TZ5w^0hze8","type":"ColorDef"},{"name":"orange","id":"q.tDyo+jgZZDMye7oWnb","type":"ColorDef"},{"name":"yellow","id":"]%)nHSg1LSBIPd/=|o.M","type":"ColorDef"},{"name":"green","id":"]Me#}e+(Fe5HNY2X9S:C","type":"ColorDef"},{"name":"cyan","id":"hfyUxJb9Hk9dstNnrgqc","type":"ColorDef"},{"name":"blue","id":"S}SRcf||7%So~Gl)k]U-","type":"ColorDef"},{"name":"violet","id":"PKqk(IDH3oY|mtEt6lnj","type":"ColorDef"},{"name":"magenta","id":"~kn`ES|Olk*dHVt~J3Oq","type":"ColorDef"},{"name":"white","id":",ssDGS*gf)s!{:j:Q(ZX","type":"ColorDef"},{"name":"none","id":"N8zP+udl{B!-/6E]:$s;","type":"ColorDef"},{"name":"left","id":"I53Xcpt{AF/^Y~er!Ae.","type":"Motor"},{"name":"right","id":"WU?-A7sr@(wylvY9bml.","type":"Motor"},{"name":"sensor","id":"34|JQ1oqFiClXIo$D;QD","type":"UltrasonicSensor"},{"name":"robot","id":"tx+grocr(+gz|!!aOwj[","type":"DriveBase"}],"info":{"type":"pybricks","version":"1.3.2"}}
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, run_task, wait

# Set up all devices.
sensor = UltrasonicSensor(Port.D)
left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B, Direction.CLOCKWISE)
robot = DriveBase(left, right, 56, 128)

async def subtask():
    while True:
        await wait(0)
        await robot.straight(250)
        await robot.turn(90)

async def subtask2():
    while not await sensor.distance() <= 500:
        await wait(0)

async def main():
    await multitask(
        subtask(),
        subtask2(),
        race=True,
    )


run_task(main())