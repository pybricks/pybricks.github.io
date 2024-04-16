# pybricks blocks file:{"blocks":{"languageVersion":0,"blocks":[{"type":"blockGlobalSetup","id":"bjK,wS1MYO7aiYkFSwd{","x":0,"y":0,"deletable":false,"next":{"block":{"type":"variables_set_essential_hub","id":"Vv%m_eZ+$?8)`U]+4_|L","extraState":{"optionLevel":0},"fields":{"VAR":{"id":"NTjDi;7upvcqELI?S[.z"}},"next":{"block":{"type":"variables_set_motor","id":"YF_NAJ7:ChSZ0*EUQ[`#","fields":{"VAR":{"id":"9.5u$nHeY4sFbF*sA!4)"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"vlf@Jlb%oC-1TC5L`rB|","fields":{"NAME":"A"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"+EPYxbhjZxL}m+M@kupV","fields":{"SELECTION":"Direction.CLOCKWISE"}}}}}}}}},{"type":"blockGlobalStart","id":"3tJe|AWl0baN(wH9a$@.","x":0,"y":192,"deletable":false,"next":{"block":{"type":"blockComment","id":"(Orr6QzbdbdnR,G/X,S`","fields":{"FIELDNAME":"Disable the stop button so we\ncan use it for something else."},"next":{"block":{"type":"blockHubStopButton","id":"A2QnnpIQb2P2q4G|`U$:","inputs":{"VAR":{"shadow":{"type":"variables_get_button_hub","id":"w}Z65mDe58C`BanJ:Ipz","fields":{"VAR":{"id":"NTjDi;7upvcqELI?S[.z","name":"hub","type":"EssentialHub"}}}},"VALUE0":{"shadow":{"type":"blockParametersButton","id":"a!:0{|bH@@1{rDFb%AD:","fields":{"VALUE":"CENTER"}},"block":{"type":"blockNone","id":"r6v?KC*]|UMdMVzuQs]("}}},"next":{"block":{"type":"blockFlowWhile","id":"1JD(i!zwoTjp;xjzx`n]","fields":{"MODE":"WHILE"},"inputs":{"BOOL":{"shadow":{"type":"blockLogicTrue","id":"3n*NW/(Q6{KbMslr@]q@"}},"DO":{"block":{"type":"blockIfElse","id":"JutiU7!KQs#LnF#^J:_8","extraState":{"optionLevel":1},"inputs":{"IF0":{"shadow":{"type":"blockLogicTrue","id":"tH*+gra?y9?,/Ew4(Jfr"},"block":{"type":"blockButtonIsPressed","id":"hN|z#VRXtv!16+W#n)L^","inputs":{"VAR":{"shadow":{"type":"variables_get_keypad","id":"CT%qH_/U80G?`:b~m#(N","fields":{"VAR":{"id":"NTjDi;7upvcqELI?S[.z","name":"hub","type":"EssentialHub"}}}},"VALUE0":{"shadow":{"type":"blockParametersButton","id":"8W7]OE;.Z9n{AS{d^bwK","fields":{"VALUE":"CENTER"}}}}}},"DO0":{"block":{"type":"blockLightOnColor","id":"I=e=S/Gb2_Y(0C5%/-:u","extraState":{"optionLevel":1},"fields":{"METHOD":"LIGHT_ON"},"inputs":{"VAR":{"shadow":{"type":"variables_get_color_light_device","id":"8Vd#$TFW6]B/_+mW3uDA","fields":{"VAR":{"id":"NTjDi;7upvcqELI?S[.z","name":"hub","type":"EssentialHub"}}}},"COLOR":{"shadow":{"type":"variables_get_color","id":"t$kqM*,Iv/XSpLh$*Tr3","fields":{"COLOUR":"#ff0000","VAR":{"id":"|e*]R-ph?|DS8maY)M`3","name":"red","type":"ColorDef"}}}}}}},"ELSE":{"block":{"type":"blockLightOnColor","id":"+tjdB^SRnx#cpJ}csvgZ","extraState":{"optionLevel":1},"fields":{"METHOD":"LIGHT_ON"},"inputs":{"VAR":{"shadow":{"type":"variables_get_color_light_device","id":"Iw1x!9TFdiWtcrF%0In;","fields":{"VAR":{"id":"NTjDi;7upvcqELI?S[.z","name":"hub","type":"EssentialHub"}}}},"COLOR":{"shadow":{"type":"variables_get_color","id":"4LaT7o+N`I7;UlTofpRP","fields":{"COLOUR":"#00ff00","VAR":{"id":";Fw,_kp0[[p#U:~U8v0a","name":"green","type":"ColorDef"}}}}}}}}}}}}}}}}}},{"type":"blockGlobalStart","id":"XLl[AQ+b%zs@+qN0DZFL","x":0,"y":687,"next":{"block":{"type":"blockComment","id":"N9p-9p1tVg;FUdr2N;*n","fields":{"FIELDNAME":"Optionally, you can add a different way to stop your program.\nFor example by turning a motor manually.\n\nDon't worry if you forget this. You can always stop your program\nby just turning the hub off by holding the button for three seconds."},"next":{"block":{"type":"blockWaitUntil","id":"3/XqxR}r}W6T~L#Ey2D`","inputs":{"BOOL":{"shadow":{"type":"blockLogicTrue","id":"5io~T.[ua=QS0XyBb9Nr"},"block":{"type":"blockLogicCompare","id":"a#7AMlh]KR##5GP(%^=M","fields":{"OP1":"GT"},"inputs":{"A":{"shadow":{"type":"blockMathNumber","id":")yK0@UFr]-o|8t+x@^|4","fields":{"NUM":3}},"block":{"type":"blockMotorMeasure","id":"PFt*sF^0p*`y$x~@/GnG","extraState":{"optionLevel":2},"fields":{"METHOD":"MOTOR_SPEED"},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"_2sg@O0r-tJe*|outK%A","fields":{"VAR":{"id":"9.5u$nHeY4sFbF*sA!4)","name":"motor","type":"Motor"}}}}}}},"B":{"shadow":{"type":"blockMathNumber","id":"DUxgE4?.wg8y|T6/|ns?","fields":{"NUM":100}}}}}}},"next":{"block":{"type":"blockProgramStop","id":"6A8J*GU{*8to0-n7ao{C"}}}}}}}]},"variables":[{"name":"red","id":"|e*]R-ph?|DS8maY)M`3","type":"ColorDef"},{"name":"orange","id":"jEPnVh:/H3|QE,mM`z7]","type":"ColorDef"},{"name":"yellow","id":"$(+,/VY_[{uzL-0Y!--#","type":"ColorDef"},{"name":"green","id":";Fw,_kp0[[p#U:~U8v0a","type":"ColorDef"},{"name":"cyan","id":"^U5)Kv^_T8qoG84uloH0","type":"ColorDef"},{"name":"blue","id":"]51(*A[rgqq1u/dh5_vg","type":"ColorDef"},{"name":"violet","id":"gCm@~3L-4{TALavGlyNQ","type":"ColorDef"},{"name":"magenta","id":"!?pggV|u^C#qOSz4/-s$","type":"ColorDef"},{"name":"white","id":"XwRWo?Ee7hDb3;6x!j?Q","type":"ColorDef"},{"name":"none","id":"(F{7F|3r,|G7hdo}@fH2","type":"ColorDef"},{"name":"hub","id":"NTjDi;7upvcqELI?S[.z","type":"EssentialHub"},{"name":"motor","id":"9.5u$nHeY4sFbF*sA!4)","type":"Motor"}],"info":{"type":"pybricks","version":"1.2.2"}}
from pybricks.hubs import EssentialHub
from pybricks.parameters import Button, Color, Direction, Port
from pybricks.pupdevices import Motor
from pybricks.tools import multitask, run_task, wait

# Set up all devices.
hub = EssentialHub()
motor = Motor(Port.A, Direction.CLOCKWISE)

async def main1():
    # Disable the stop button so we
    # can use it for something else.
    hub.system.set_stop_button(None)
    while True:
        await wait(1)
        if Button.CENTER in hub.buttons.pressed():
            hub.light.on(Color.RED)
        else:
            hub.light.on(Color.GREEN)

async def main2():
    # Optionally, you can add a different way to stop your program.
    # For example by turning a motor manually.

    # Don't worry if you forget this. You can always stop your program
    # by just turning the hub off by holding the button for three seconds.
    while not motor.speed() > 100:
        await wait(1)
    raise SystemExit


async def main():
    await multitask(main1(), main2())

run_task(main())