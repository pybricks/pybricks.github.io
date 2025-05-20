# pybricks blocks file:{"blocks":{"languageVersion":0,"blocks":[{"type":"blockGlobalSetup","id":"bjK,wS1MYO7aiYkFSwd{","x":150,"y":100,"deletable":false,"next":{"block":{"type":"variables_set_inventor_hub","id":"EcWRSKTzE8G1)h1pxy_j","extraState":{"optionLevel":0},"fields":{"VAR":{"id":"=E`PZ8ua82=buIe{[S~D"}},"next":{"block":{"type":"variables_set_motor","id":"G?/C.hoF~+e0MLm1/]XR","fields":{"VAR":{"id":"U#T3E19ze3uB{:E%i5kN"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"de.avh#Lb?kUra3I=?XQ","fields":{"NAME":"A"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":":~cT215Z,yT90(BW!6t1","fields":{"SELECTION":"Direction.CLOCKWISE"}}}}}}}}},{"type":"blockGlobalStart","id":"3tJe|AWl0baN(wH9a$@.","x":149,"y":287,"deletable":false,"next":{"block":{"type":"blockMotorRun","id":"%uP]UpKt.Z5BuT^OO(t]","extraState":{"optionLevel":1},"fields":{"METHOD":"MOTOR_RUN_FOR"},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"9z~1-XT3!GV5zGYaR07p","fields":{"VAR":{"id":"U#T3E19ze3uB{:E%i5kN","name":"motor","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_angularVelocity","id":"B)xRomjCX4f)}Yv9Ktu*","fields":{"VALUE0":500}}},"ANGLE":{"shadow":{"type":"unit_angle","id":"Lp%COsWzFNQ^ro[6p,QW","fields":{"VALUE0":360}}},"THEN":{"shadow":{"type":"parameters_stop_4","id":"@8n;Mo7tl7lwfb$~81xR","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockMotorRun","id":"Go7ReTE-Rzn-n]A#.u|D","extraState":{"optionLevel":1},"fields":{"METHOD":"MOTOR_RUN_FOR"},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"U.qjJ1bWS7Ja;%FHrT)7","fields":{"VAR":{"id":"U#T3E19ze3uB{:E%i5kN","name":"motor","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_angularVelocity","id":"%G%RtY[pnmX!Uz2dK/7w","fields":{"VALUE0":500}}},"ANGLE":{"shadow":{"type":"unit_angle","id":"%N.)10QLD(^I)n^NF@IG","fields":{"VALUE0":-360}}},"THEN":{"shadow":{"type":"parameters_stop_4","id":":6Jc!]`7)%ziK{+6:1WS","fields":{"VALUE":"Stop.HOLD"}}}}}}}}},{"type":"blockGlobalStart","id":"4N7LKuP6:Y@$YVN3I!$6","x":150,"y":485,"next":{"block":{"type":"blockFlowRepeat","id":"VwJ.}r8@~A=K95q:bIU5","inputs":{"TIMES":{"shadow":{"type":"blockMathNumber","id":"3@!ZsVObjqSauSPn.=4B","fields":{"NUM":10}}},"DO":{"block":{"type":"blockLightOnColor","id":"]WL/M[Vx}(6hdSha2LUg","extraState":{"optionLevel":1},"fields":{"METHOD":"LIGHT_ON"},"inputs":{"VAR":{"shadow":{"type":"variables_get_color_light_device","id":"Qh,pS)c(.%8~08A@{Ad(","fields":{"VAR":{"id":"=E`PZ8ua82=buIe{[S~D","name":"hub","type":"InventorHub"}}}},"COLOR":{"shadow":{"type":"variables_get_color","id":"W$SUbgbxbp4(h.S_%q(9","fields":{"COLOUR":"#ff0000","VAR":{"id":"~.fwrrt.Yb1N|J@/Ne+q","name":"red","type":"ColorDef"}}}}},"next":{"block":{"type":"blockWaitTime","id":".~lEqEmC[zj=g66@VLki","inputs":{"VALUE0":{"shadow":{"type":"unit_time","id":"[#MamJVx+]Dte~[@J9WA","fields":{"VALUE0":250}}}},"next":{"block":{"type":"blockLightOnColor","id":"siWra[y-5!JtO._!J0dm","extraState":{"optionLevel":1},"fields":{"METHOD":"LIGHT_ON"},"inputs":{"VAR":{"shadow":{"type":"variables_get_color_light_device","id":".)QUH;$xKYARU$qd580T","fields":{"VAR":{"id":"=E`PZ8ua82=buIe{[S~D","name":"hub","type":"InventorHub"}}}},"COLOR":{"shadow":{"type":"variables_get_color","id":"}59tj.ldr!ED8]QipTa1","fields":{"COLOUR":"#00ff00","VAR":{"id":"{P4]-Sk#,S|#Cgn^*hVK","name":"green","type":"ColorDef"}}}}},"next":{"block":{"type":"blockWaitTime","id":"?D_K=VJAB`/on7movMN%","inputs":{"VALUE0":{"shadow":{"type":"unit_time","id":"/4{8kNOA;6b2^C(skDuD","fields":{"VALUE0":250}}}}}}}}}}}}}}}}]},"variables":[{"name":"red","id":"~.fwrrt.Yb1N|J@/Ne+q","type":"ColorDef"},{"name":"orange","id":"-1U3lu+ENYzrrqd[]d^0","type":"ColorDef"},{"name":"yellow","id":"Mrb`$LrJ]?(TKRWhBn`W","type":"ColorDef"},{"name":"green","id":"{P4]-Sk#,S|#Cgn^*hVK","type":"ColorDef"},{"name":"cyan","id":"Nr[P4b-_a#g|d}+sZDoB","type":"ColorDef"},{"name":"blue","id":"P_582T.y4`OR%)+=2,Aa","type":"ColorDef"},{"name":"violet","id":"+|8a:;x5JLj6GjCZc`?~","type":"ColorDef"},{"name":"magenta","id":"-Dz@~G+xopHe+h3_aBw9","type":"ColorDef"},{"name":"white","id":"6%-KxV9t*OhDh;@y-k:T","type":"ColorDef"},{"name":"none","id":")!/_(Y,#eGy+-IlgQE!7","type":"ColorDef"},{"name":"hub","id":"=E`PZ8ua82=buIe{[S~D","type":"InventorHub"},{"name":"motor","id":"U#T3E19ze3uB{:E%i5kN","type":"Motor"}],"info":{"type":"pybricks","version":"1.3.2"}}
from pybricks.hubs import InventorHub
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.tools import multitask, run_task, wait

# Set up all devices.
hub = InventorHub()
motor = Motor(Port.A, Direction.CLOCKWISE)

async def main1():
    await motor.run_angle(500, 360)
    await motor.run_angle(500, -360)

async def main2():
    for count in range(10):
        await wait(0)
        hub.light.on(Color.RED)
        await wait(250)
        hub.light.on(Color.GREEN)
        await wait(250)


async def main():
    await multitask(main1(), main2())

run_task(main())