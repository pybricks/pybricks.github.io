# pybricks blocks file:{"blocks":{"languageVersion":0,"blocks":[{"type":"blockGlobalSetup","id":"bjK,wS1MYO7aiYkFSwd{","x":0,"y":0,"deletable":false,"next":{"block":{"type":"variables_set_motor","id":"nhkv?*Y3-QJV4Z+Tt#d+","fields":{"VAR":{"id":"SU`hDwV#At|n9!oFWg#v"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"/0#u@~g,*ptdJCfhe|xq","fields":{"NAME":"D"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"5~PlzCIwDuAicW{XUIZ+","fields":{"SELECTION":"Direction.CLOCKWISE"}}}},"next":{"block":{"type":"variables_set_motor","id":"D~^vKe6!,tZ{RJJL-8jz","fields":{"VAR":{"id":"INn#0]HTW}^i_z6XS4t9"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"0(mMpuc1-9Z=oGH}~v)Q","fields":{"NAME":"B"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"izw*C70.Jio$i~ZDw?OW","fields":{"SELECTION":"Direction.CLOCKWISE"}}}},"next":{"block":{"type":"variables_set_motor","id":"MLWt~309`?(iB[{nYWjZ","fields":{"VAR":{"id":"Dmb*(,{+rKA,8h41R/:W"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"#,~*8aDx8wXG.o,Baw:K","fields":{"NAME":"A"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"-jU]7QXX,kQJ/qaccNZs","fields":{"SELECTION":"Direction.CLOCKWISE"}}}},"next":{"block":{"type":"variables_set_car","id":"#rV!lgT{NpZt%%/6vqB{","extraState":{"optionLevel":1},"fields":{"VAR":{"id":"h|_rzGrJcAjmf5DhWuVH"}},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"^jM(?YZ;`Kfq%)lKWq7_","fields":{"VAR":{"id":"SU`hDwV#At|n9!oFWg#v","name":"steering","type":"Motor"}}}},"VAR2":{"shadow":{"type":"variables_get_motor_device","id":"3}sczA=$fp{]m-sZQBKF","fields":{"VAR":{"id":"INn#0]HTW}^i_z6XS4t9","name":"drive1","type":"Motor"}}}},"DRIVE1":{"shadow":{"type":"variables_get_motor_device","id":";_={Tn=%Pd;jf^m5:GEi","fields":{"VAR":{"id":"Dmb*(,{+rKA,8h41R/:W","name":"drive2","type":"Motor"}}}}},"next":{"block":{"type":"variables_set_dc_motor","id":"$1hDl$/Z$M+z8ELp@F-W","fields":{"VAR":{"id":"5w(@B7`|=oU3=c8@O]E^"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"tv$YVg$CZx:a|:;^luN!","fields":{"NAME":"C"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"61#KFd$T%/oNghisM|)l","fields":{"SELECTION":"Direction.CLOCKWISE"}}}},"next":{"block":{"type":"variables_set_remote","id":"580$3gT@/(xM7%Q^rC{;","extraState":{"optionLevel":0},"fields":{"VAR":{"id":".z$ivXqYqs|`qDYZ,lQa"},"METHOD":"CONNECT_ANY"},"next":{"block":{"type":"variables_setup_any","id":"h0^c.o5;^6+9E9pjQBu?","fields":{"VAR":{"id":"sF%(fHaJtbOo!hY{i.]."}},"inputs":{"VALUE0":{"shadow":{"type":"blockMathNumber","id":"ApG*^|d1E4]1KKBg}oD/","fields":{"NUM":0}}}}}}}}}}}}}}}}}}},{"type":"blockGlobalStart","id":"3tJe|AWl0baN(wH9a$@.","x":0,"y":430,"deletable":false,"next":{"block":{"type":"blockComment","id":":]h@)}yU??Vy69TrrwG^","fields":{"FIELDNAME":"Initialize the lock in the locked state."},"next":{"block":{"type":"blockMotorDuty","id":"l)F*1P@*LT217rIPPh)f","inputs":{"VAR":{"shadow":{"type":"variables_get_simple_motor_device","id":"B4|^2I/)9w~U+@I]LBH8","fields":{"VAR":{"id":"5w(@B7`|=oU3=c8@O]E^","name":"lock","type":"DCMotor"}}}},"VALUE0":{"shadow":{"type":"unit_percent","id":"8#(Ss+W5,vtW%#WZ}M/Q","fields":{"VALUE0":-60}}}},"next":{"block":{"type":"blockWaitTime","id":"5_2Mr=W}ZbphearWmw9!","inputs":{"VALUE0":{"shadow":{"type":"unit_time","id":"mPn^fiud$`$ji7O*7ZCz","fields":{"VALUE0":600}}}},"next":{"block":{"type":"blockMotorStop","id":"Ag=C_nNvb3Y-H+@W=:qA","inputs":{"VAR":{"shadow":{"type":"variables_get_simple_motor_device","id":"eVE%hb,Z=uninnKtz_:[","fields":{"VAR":{"id":"5w(@B7`|=oU3=c8@O]E^","name":"lock","type":"DCMotor"}}}},"VALUE0":{"shadow":{"type":"parameters_stop_3","id":"vu+MT89S~*SjLm~fkvwM","fields":{"VALUE":"Stop.COAST"}}}},"next":{"block":{"type":"blockVariableSetValue","id":"?tXdrl8VHJs#Cd4}ebjv","inputs":{"VAR":{"shadow":{"type":"variables_get_any","id":"-SnvMlj?4+jvH~Ieq`:/","fields":{"VAR":{"id":"sF%(fHaJtbOo!hY{i.].","name":"locked","type":"Any"}}}},"VALUE0":{"shadow":{"type":"blockMathNumber","id":"%[2dXDtT6(f?@#stoihA","fields":{"NUM":1}},"block":{"type":"blockLogicTrueFalse","id":"7o0?cr]/M7[j|VE#dnF{","fields":{"BOOL":"TRUE"}}}},"next":{"block":{"type":"blockLightOnColor","id":"f*IBu*,kiX8PB!:![w?s","extraState":{"optionLevel":1},"fields":{"METHOD":"LIGHT_ON"},"inputs":{"VAR":{"shadow":{"type":"variables_get_color_light_device","id":"x@A}S.-@_u}7;Jt8PTI}","fields":{"VAR":{"id":".z$ivXqYqs|`qDYZ,lQa","name":"remote","type":"Remote"}}}},"COLOR":{"shadow":{"type":"variables_get_color","id":"km-=YB1N7inf})etvp|t","fields":{"COLOUR":"#0000ff","VAR":{"id":"-wKLU0+M?#y[%R(sTM?]","name":"blue","type":"ColorDef"}}}}},"next":{"block":{"type":"blockComment","id":"P%%jNm_$?zj`4jw7xRCX","fields":{"FIELDNAME":"Now we can run the main loop."},"next":{"block":{"type":"blockFlowWhile","id":".QC*kn8#o^lmSe+ca{Wj","fields":{"MODE":"WHILE"},"inputs":{"BOOL":{"shadow":{"type":"blockLogicTrue","id":"H?V+7C2Yt/q!G5_^#uxP"}},"DO":{"block":{"type":"blockComment","id":"ae|i%ztT$Wil=KQ{CiaU","fields":{"FIELDNAME":"Control steering using the left - and + buttons."},"next":{"block":{"type":"blockCarSteer","id":"mk}3O#L,jV6LOb#^,M[E","inputs":{"VAR":{"shadow":{"type":"variables_get_car_device","id":"DcBHI9u-mg8?.QC4{m8I","fields":{"VAR":{"id":"h|_rzGrJcAjmf5DhWuVH","name":"car","type":"Car"}}}},"VALUE0":{"shadow":{"type":"unit_percent","id":"(k(CLFFjO!]V?VQF*$QB","fields":{"VALUE0":0}},"block":{"type":"blockLogicTernaryDouble","id":"mCTKnbZb1xg=+Ob:oQW3","inputs":{"VAL_A":{"shadow":{"type":"blockMathNumber","id":")-8Jp]e9TL#lAfVo[XCa","fields":{"NUM":100}}},"IF_0":{"shadow":{"type":"blockLogicTrue","id":"Pg--S2e$@DdG;#vJk*4]"},"block":{"type":"blockButtonIsPressed","id":"P79#aY6wSb^h+cQ}t.G2","inputs":{"VAR":{"shadow":{"type":"variables_get_keypad","id":"z%]7_Fq/1Zn[F#4PHwHy","fields":{"VAR":{"id":".z$ivXqYqs|`qDYZ,lQa","name":"remote","type":"Remote"}}}},"VALUE0":{"shadow":{"type":"blockParametersButton","id":"U,ty45*xT9,Ef;y_VjAL","fields":{"VALUE":"LEFT_PLUS"}}}}}},"VAL_B":{"shadow":{"type":"blockMathNumber","id":"fxK%NZr2vTTH!{Z5Kj~~","fields":{"NUM":-100}}},"IF_1":{"shadow":{"type":"blockLogicTrue","id":"0UDb9Fr,xf`UNn*~DqDe"},"block":{"type":"blockButtonIsPressed","id":"b;+$jf-:u#YoE@5t/6jp","inputs":{"VAR":{"shadow":{"type":"variables_get_keypad","id":"WxQfcX8%|43DQQQ1=2`b","fields":{"VAR":{"id":".z$ivXqYqs|`qDYZ,lQa","name":"remote","type":"Remote"}}}},"VALUE0":{"shadow":{"type":"blockParametersButton","id":"Vi|(?*]5c@hsa9S$@N6]","fields":{"VALUE":"LEFT_MINUS"}}}}}},"VAL_C":{"shadow":{"type":"blockMathNumber","id":"+^0*u8NGLX)u{W{C$r$5","fields":{"NUM":0}}}}}}},"next":{"block":{"type":"blockComment","id":"0R7Ha;pYQ6nAi1}3z;2z","fields":{"FIELDNAME":"Control drive power using the right - and + buttons."},"next":{"block":{"type":"blockCarDrive","id":"xR5bV#N.Bn@0r;h3vqjI","extraState":{"optionLevel":1},"fields":{"METHOD":"CAR_DRIVE_AT_POWER"},"inputs":{"VAR":{"shadow":{"type":"variables_get_car_device","id":"F-C}:0di1OE=1ee}ZV,g","fields":{"VAR":{"id":"h|_rzGrJcAjmf5DhWuVH","name":"car","type":"Car"}}}},"ARG0":{"shadow":{"type":"unit_percent","id":"{|~3ydq0!3phdQuYc9Tj","fields":{"VALUE0":50}},"block":{"type":"blockLogicTernaryDouble","id":"-,p$uaecP1Ya#N_8?*F?","inputs":{"VAL_A":{"shadow":{"type":"blockMathNumber","id":",,D-{OXPv*?_INSDuwt}","fields":{"NUM":100}}},"IF_0":{"shadow":{"type":"blockLogicTrue","id":"Pg--S2e$@DdG;#vJk*4]"},"block":{"type":"blockButtonIsPressed","id":"V..R2p^pcQuR#9ON+#,T","inputs":{"VAR":{"shadow":{"type":"variables_get_keypad","id":"7.rvlb(/={e!y6}T~8C$","fields":{"VAR":{"id":".z$ivXqYqs|`qDYZ,lQa","name":"remote","type":"Remote"}}}},"VALUE0":{"shadow":{"type":"blockParametersButton","id":"kchR8d(vH98Fv1k`A(;;","fields":{"VALUE":"RIGHT_PLUS"}}}}}},"VAL_B":{"shadow":{"type":"blockMathNumber","id":"Uj1=Uf7}nGylj|DT(l6Z","fields":{"NUM":-100}}},"IF_1":{"shadow":{"type":"blockLogicTrue","id":"0UDb9Fr,xf`UNn*~DqDe"},"block":{"type":"blockButtonIsPressed","id":"H}/*pLBI[DJc)ZYuEN|u","inputs":{"VAR":{"shadow":{"type":"variables_get_keypad","id":"]:Om1U?zOSNMrPs;RxZa","fields":{"VAR":{"id":".z$ivXqYqs|`qDYZ,lQa","name":"remote","type":"Remote"}}}},"VALUE0":{"shadow":{"type":"blockParametersButton","id":":^X@:jBSNuypzGR_[XgN","fields":{"VALUE":"RIGHT_MINUS"}}}}}},"VAL_C":{"shadow":{"type":"blockMathNumber","id":"!7%5m~LwZt_mt8#;^CJj","fields":{"NUM":0}}}}}}},"next":{"block":{"type":"blockComment","id":"=[xKFq~4UUNuCV6{9PcT","fields":{"FIELDNAME":"Handle the lock using the center button."},"next":{"block":{"type":"blockIfElse","id":"O7i+~T_H{7B^QhhIDPbU","extraState":{"optionLevel":0},"inputs":{"IF0":{"shadow":{"type":"blockLogicTrue","id":"2lA9Fr$8z.`b2],3kBCX"},"block":{"type":"blockButtonIsPressed","id":"Y[=w:Pe1Fr41};Om^/?e","inputs":{"VAR":{"shadow":{"type":"variables_get_keypad","id":"m*E96GEjQ,BM6G#XW?Mh","fields":{"VAR":{"id":".z$ivXqYqs|`qDYZ,lQa","name":"remote","type":"Remote"}}}},"VALUE0":{"shadow":{"type":"blockParametersButton","id":"e^[N?7SBurJHzTE=6yRa","fields":{"VALUE":"CENTER"}}}}}},"DO0":{"block":{"type":"blockComment","id":"8x`q=tP;Esjs2xvSlQI$","fields":{"FIELDNAME":"If pressed, first stop driving for safety.\nSet light to red to indicate that the lock is being moved."},"next":{"block":{"type":"blockLightOnColor","id":"hRH(XnK4fNV-8+)^S`=Z","extraState":{"optionLevel":1},"fields":{"METHOD":"LIGHT_ON"},"inputs":{"VAR":{"shadow":{"type":"variables_get_color_light_device","id":"jhfgV}wgOn4hSuS6CLpy","fields":{"VAR":{"id":".z$ivXqYqs|`qDYZ,lQa","name":"remote","type":"Remote"}}}},"COLOR":{"shadow":{"type":"variables_get_color","id":"ENdtp~1`%PV8#^*iaR8x","fields":{"COLOUR":"#ff0000","VAR":{"id":"tY1NeadO^;%:Z-M{Q7g0","name":"red","type":"ColorDef"}}}}},"next":{"block":{"type":"blockCarDrive","id":"X5Go4=Y1b+fV3IP`cJS%","extraState":{"optionLevel":1},"fields":{"METHOD":"CAR_DRIVE_AT_POWER"},"inputs":{"VAR":{"shadow":{"type":"variables_get_car_device","id":"Y$[Y-R/*gd6!/kc`o/96","fields":{"VAR":{"id":"h|_rzGrJcAjmf5DhWuVH","name":"car","type":"Car"}}}},"ARG0":{"shadow":{"type":"unit_percent","id":"X%eKvQMm9%ARfy9l?zaN","fields":{"VALUE0":0}}}},"next":{"block":{"type":"blockWaitTime","id":",.Iis9rCaat1ih%}}Ru8","inputs":{"VALUE0":{"shadow":{"type":"unit_time","id":"t]eaZ!6XrP*9lH93Li[Q","fields":{"VALUE0":500}}}},"next":{"block":{"type":"blockComment","id":"_AX${/K|nVYIL9$5jE/Q","fields":{"FIELDNAME":"If currently locked, rotate at +60% power to unlock it.\nOtherwise, rotate it at -60% to lock it."},"next":{"block":{"type":"blockMotorDuty","id":"y(;xC5R/S:e0xy#PHOx@","inputs":{"VAR":{"shadow":{"type":"variables_get_simple_motor_device","id":"[H`e1}vxuTB1yveb?L6f","fields":{"VAR":{"id":"5w(@B7`|=oU3=c8@O]E^","name":"lock","type":"DCMotor"}}}},"VALUE0":{"shadow":{"type":"unit_percent","id":"+9P/l~9M|ok=BvM?Xc,r","fields":{"VALUE0":50}},"block":{"type":"blockLogicTernary","id":"2?n-hNv}ZBy5_r)|Pw]z","inputs":{"THEN":{"shadow":{"type":"blockMathNumber","id":"Ni$8e/(0?npm*4=T#^!y","fields":{"NUM":60}}},"IF":{"shadow":{"type":"blockLogicTrue","id":"cmK2HXNDe*l^_p[4?9[J"},"block":{"type":"blockVariableGetValue","id":"CV+J-fChqu.w--mHOG{Q","inputs":{"VAR":{"shadow":{"type":"variables_get_any","id":"}2p.F)g`J`E5gbfqS5IB","fields":{"VAR":{"id":"sF%(fHaJtbOo!hY{i.].","name":"locked","type":"Any"}}}}}}},"ELSE":{"shadow":{"type":"blockMathNumber","id":"|b|^,arosxA]-BGf?VKS","fields":{"NUM":-60}}}}}}},"next":{"block":{"type":"blockWaitTime","id":"N44$-Fyg.}s;t_Ms3rVP","inputs":{"VALUE0":{"shadow":{"type":"unit_time","id":"[;tvx|!)=1ZuTHEPFM.{","fields":{"VALUE0":600}}}},"next":{"block":{"type":"blockMotorStop","id":"xBRO2,u20BZ$!Mx=%9i#","inputs":{"VAR":{"shadow":{"type":"variables_get_simple_motor_device","id":"+oP3QhDY6Li#L?1,C9On","fields":{"VAR":{"id":"5w(@B7`|=oU3=c8@O]E^","name":"lock","type":"DCMotor"}}}},"VALUE0":{"shadow":{"type":"parameters_stop_3","id":"_z8IJi9BI)P%4754+2-s","fields":{"VALUE":"Stop.COAST"}}}},"next":{"block":{"type":"blockComment","id":"hCTP8OY@oOH.ag|/xUGq","fields":{"FIELDNAME":"Now we have to update the lock state.\nIf locked was True we will make it False, because it is no longer locked.\nIf locked was False we will make it True, because it is now locked.\nSo we always have to set it to the opposite value. The not block does that."},"next":{"block":{"type":"blockVariableSetValue","id":"fAE@!O}MGsz,hvVEicx]","inputs":{"VAR":{"shadow":{"type":"variables_get_any","id":"**s_ADQ/;jSoVlh|_x~P","fields":{"VAR":{"id":"sF%(fHaJtbOo!hY{i.].","name":"locked","type":"Any"}}}},"VALUE0":{"shadow":{"type":"blockMathNumber","id":"._Ri}i9a=Q%+(J]F$%8m","fields":{"NUM":0}},"block":{"type":"blockLogicIsNone","id":"gaL0i,b`$TYI2L(Hu=rX","fields":{"OP":"NOT"},"inputs":{"BOOL":{"shadow":{"type":"blockLogicTrue","id":"P5~2PARSC.VxbIV`g~8{"},"block":{"type":"blockVariableGetValue","id":"E[8Y5)4!q_Q]N_OlP`s8","inputs":{"VAR":{"shadow":{"type":"variables_get_any","id":"Gis_h1P`xq0=*iP7myyf","fields":{"VAR":{"id":"sF%(fHaJtbOo!hY{i.].","name":"locked","type":"Any"}}}}}}}}}}},"next":{"block":{"type":"blockComment","id":"7Q{V@B3OAoE@,m|gf-CO","fields":{"FIELDNAME":"Set the light color depending on the new state, so we can easily\nsee if it is locked (blue) or not (green)."},"next":{"block":{"type":"blockLightOnColor","id":"t74Pi`*/%]%@naVo~NA)","extraState":{"optionLevel":1},"fields":{"METHOD":"LIGHT_ON"},"inputs":{"VAR":{"shadow":{"type":"variables_get_color_light_device","id":"V[iwgfm@/h(hK#Xe[j~!","fields":{"VAR":{"id":".z$ivXqYqs|`qDYZ,lQa","name":"remote","type":"Remote"}}}},"COLOR":{"shadow":{"type":"variables_get_color","id":"Ch3_@PR%!i-PsemH8qKg","fields":{"COLOUR":"#ff0000","VAR":{"id":"tY1NeadO^;%:Z-M{Q7g0","name":"red","type":"ColorDef"}}},"block":{"type":"blockLogicTernary","id":"Ud5riam:{j~DuTN:On)R","inputs":{"THEN":{"shadow":{"type":"blockMathNumber","id":"J[,sJjdoxywM-:1QOj~5","fields":{"NUM":60}},"block":{"type":"variables_get_color","id":"!=C+o13h7}L)?td/ZVo:","fields":{"COLOUR":"#0000ff","VAR":{"id":"-wKLU0+M?#y[%R(sTM?]"}}}},"IF":{"shadow":{"type":"blockLogicTrue","id":"cmK2HXNDe*l^_p[4?9[J"},"block":{"type":"blockVariableGetValue","id":"0+xQH5wO3Tlp:*;A:q;!","inputs":{"VAR":{"shadow":{"type":"variables_get_any","id":"+AD{28(wMRv1u?7D|STp","fields":{"VAR":{"id":"sF%(fHaJtbOo!hY{i.].","name":"locked","type":"Any"}}}}}}},"ELSE":{"shadow":{"type":"blockMathNumber","id":"mnlP9?Z*!03)a_BhW{tb","fields":{"NUM":-60}},"block":{"type":"variables_get_color","id":"1jOZ(Dm@(8uu^wh:;1,V","fields":{"COLOUR":"#00ff00","VAR":{"id":"I_c*s!/ZlA{c_6SN-_BY"}}}}}}}},"next":{"block":{"type":"blockComment","id":"*CkFUJ77(Dty#orzH1pm","fields":{"FIELDNAME":"Make sure the button is released before we proceed to drive."},"next":{"block":{"type":"blockWaitUntil","id":"xsM1viMNkuWc)y0/%1=/","inputs":{"BOOL":{"shadow":{"type":"blockLogicTrue","id":"{[?j_D`y)Be|s[^i}_a@"},"block":{"type":"blockLogicIsNone","id":"p@Bd,2f%K7%?7U+iJ9:b","fields":{"OP":"NOT"},"inputs":{"BOOL":{"shadow":{"type":"blockLogicTrue","id":"P5~2PARSC.VxbIV`g~8{"},"block":{"type":"blockButtonIsPressed","id":"vW}p5Ty4)EX6]auDarrF","inputs":{"VAR":{"shadow":{"type":"variables_get_keypad","id":"pXhB@=fAbkCFx?VxoT;t","fields":{"VAR":{"id":".z$ivXqYqs|`qDYZ,lQa","name":"remote","type":"Remote"}}}},"VALUE0":{"shadow":{"type":"blockParametersButton","id":"3DIk#k3M;AzW@am$#LB#","fields":{"VALUE":"CENTER"}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}},"next":{"block":{"type":"blockWaitTime","id":"]hb};S1^=sM%02uBZ|Tt","inputs":{"VALUE0":{"shadow":{"type":"unit_time","id":"3[2dhv]xj:gMOf*rn3Sr","fields":{"VALUE0":50}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}]},"variables":[{"name":"red","id":"tY1NeadO^;%:Z-M{Q7g0","type":"ColorDef"},{"name":"orange","id":"f^@*I=s-_cu@rQ58T/%x","type":"ColorDef"},{"name":"yellow","id":"x.5bprt|!YOAA*oTvXQk","type":"ColorDef"},{"name":"green","id":"I_c*s!/ZlA{c_6SN-_BY","type":"ColorDef"},{"name":"cyan","id":"9Sf}f9aWUzV%Gp2(-)cN","type":"ColorDef"},{"name":"blue","id":"-wKLU0+M?#y[%R(sTM?]","type":"ColorDef"},{"name":"violet","id":"zyHO+E|G+U]juzKBeJm(","type":"ColorDef"},{"name":"magenta","id":"xJ+coHII1oCOKs=}I+[J","type":"ColorDef"},{"name":"white","id":"L6C+AWWM))j:pTk]Y%m[","type":"ColorDef"},{"name":"none","id":"Tk2LT|ldmhewOg8sER=[","type":"ColorDef"},{"name":"car","id":"h|_rzGrJcAjmf5DhWuVH","type":"Car"},{"name":"lock","id":"5w(@B7`|=oU3=c8@O]E^","type":"DCMotor"},{"name":"remote","id":".z$ivXqYqs|`qDYZ,lQa","type":"Remote"},{"name":"locked","id":"sF%(fHaJtbOo!hY{i.].","type":"Any"},{"name":"steering","id":"SU`hDwV#At|n9!oFWg#v","type":"Motor"},{"name":"drive1","id":"INn#0]HTW}^i_z6XS4t9","type":"Motor"},{"name":"drive2","id":"Dmb*(,{+rKA,8h41R/:W","type":"Motor"}],"info":{"type":"pybricks","version":"1.2.2"}}
from pybricks.parameters import Button, Color, Direction, Port
from pybricks.pupdevices import DCMotor, Motor, Remote
from pybricks.robotics import Car
from pybricks.tools import wait

# Set up all devices.
steering = Motor(Port.D, Direction.CLOCKWISE)
drive1 = Motor(Port.B, Direction.CLOCKWISE)
drive2 = Motor(Port.A, Direction.CLOCKWISE)
car = Car(steering, [drive1, drive2])
lock = DCMotor(Port.C, Direction.CLOCKWISE)
remote = Remote(timeout=None)

# Initialize variables.
locked = 0


# The main program starts here.
# Initialize the lock in the locked state.
lock.dc(-60)
wait(600)
lock.stop()
locked = True
remote.light.on(Color.BLUE)
# Now we can run the main loop.
while True:
    # Control steering using the left - and + buttons.
    car.steer(100 if Button.LEFT_PLUS in remote.buttons.pressed() else (-100 if Button.LEFT_MINUS in remote.buttons.pressed() else 0))
    # Control drive power using the right - and + buttons.
    car.drive_power(100 if Button.RIGHT_PLUS in remote.buttons.pressed() else (-100 if Button.RIGHT_MINUS in remote.buttons.pressed() else 0))
    # Handle the lock using the center button.
    if Button.CENTER in remote.buttons.pressed():
        # If pressed, first stop driving for safety.
        # Set light to red to indicate that the lock is being moved.
        remote.light.on(Color.RED)
        car.drive_power(0)
        wait(500)
        # If currently locked, rotate at +60% power to unlock it.
        # Otherwise, rotate it at -60% to lock it.
        lock.dc(60 if locked else -60)
        wait(600)
        lock.stop()
        # Now we have to update the lock state.
        # If locked was True we will make it False, because it is no longer locked.
        # If locked was False we will make it True, because it is now locked.
        # So we always have to set it to the opposite value. The not block does that.
        locked = not locked
        # Set the light color depending on the new state, so we can easily
        # see if it is locked (blue) or not (green).
        remote.light.on(Color.BLUE if locked else Color.GREEN)
        # Make sure the button is released before we proceed to drive.
        while Button.CENTER in remote.buttons.pressed():
            wait(1)
    wait(50)