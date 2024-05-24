# pybricks blocks file:{"blocks":{"languageVersion":0,"blocks":[{"type":"blockGlobalSetup","id":"bjK,wS1MYO7aiYkFSwd{","x":58,"y":62,"deletable":false,"next":{"block":{"type":"variables_set_prime_hub","id":"J4Mh?hP(%)+U[Tyb/Vcx","extraState":{"optionLevel":0},"fields":{"VAR":{"id":"?B*LMb=RRyZ2D!Ga70K="}}}}},{"type":"blockGlobalStart","id":"3tJe|AWl0baN(wH9a$@.","x":58,"y":221,"deletable":false,"next":{"block":{"type":"blockLightOnColor","id":"8uhAnkudr.8M*sgMEiH9","extraState":{"optionLevel":1},"fields":{"METHOD":"LIGHT_ON"},"inputs":{"VAR":{"shadow":{"type":"variables_get_color_light_device","id":"PTOZEl!d_{:-Tdi;R.$f","fields":{"VAR":{"id":"?B*LMb=RRyZ2D!Ga70K=","name":"hub","type":"PrimeHub"}}}},"COLOR":{"shadow":{"type":"variables_get_color","id":"!3T@q:^}|!6eU5@MrNU4","fields":{"COLOUR":"#ff0000","VAR":{"id":"2!Q,.L(`u1NHj)hMR@~d","name":"red","type":"ColorDef"}}}}},"next":{"block":{"type":"blockWaitTime","id":"?;N2C(WRD-D?d!mLcolS","inputs":{"VALUE0":{"shadow":{"type":"unit_time","id":"9q$^ih4dGhXtX9h5Nf;:","fields":{"VALUE0":1000}}}},"next":{"block":{"type":"blockLightOnColor","id":"(b.xw=,~jgQqgMTgF;qE","extraState":{"optionLevel":1},"fields":{"METHOD":"LIGHT_ON"},"inputs":{"VAR":{"shadow":{"type":"variables_get_color_light_device","id":"9Qe9kCd4Nyv^W7ud+4Q[","fields":{"VAR":{"id":"?B*LMb=RRyZ2D!Ga70K=","name":"hub","type":"PrimeHub"}}}},"COLOR":{"shadow":{"type":"variables_get_color","id":"+##,?Mlvly,Wu+fh83ux","fields":{"COLOUR":"#00ff00","VAR":{"id":"ZCu7W_i=[NYi_OphQ`Dg","name":"green","type":"ColorDef"}}}}},"next":{"block":{"type":"blockWaitTime","id":"BVF/]irR}4Gs,6-C5/:V","inputs":{"VALUE0":{"shadow":{"type":"unit_time","id":"V%9;.:|3J^BtT9(^sXXM","fields":{"VALUE0":1000}}}}}}}}}}}}}]},"variables":[{"name":"red","id":"2!Q,.L(`u1NHj)hMR@~d","type":"ColorDef"},{"name":"orange","id":"=t7?R_+B-;RhOGpv#fp)","type":"ColorDef"},{"name":"yellow","id":"xI0s.g|:AlM.y_@P9N||","type":"ColorDef"},{"name":"green","id":"ZCu7W_i=[NYi_OphQ`Dg","type":"ColorDef"},{"name":"cyan","id":"$|i8}ncC^)pExy/Y8DIs","type":"ColorDef"},{"name":"blue","id":"AJZ5ctH[xiH}tv^[T97`","type":"ColorDef"},{"name":"violet","id":"bRKKNX23Tq_z,U#U,]yx","type":"ColorDef"},{"name":"magenta","id":"164y(C~tH^3YN?NN0BXY","type":"ColorDef"},{"name":"white","id":"[%G2_I-}VEhNO~eChIFj","type":"ColorDef"},{"name":"none","id":"G{C]0Hc$}ylJo|bn2yJp","type":"ColorDef"},{"name":"hub","id":"?B*LMb=RRyZ2D!Ga70K=","type":"PrimeHub"}],"info":{"type":"pybricks","version":"1.2.3"}}
from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait

# Set up all devices.
hub = PrimeHub()


# The main program starts here.
hub.light.on(Color.RED)
wait(1000)
hub.light.on(Color.GREEN)
wait(1000)
