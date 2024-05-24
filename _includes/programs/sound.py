# pybricks blocks file:{"blocks":{"languageVersion":0,"blocks":[{"type":"blockGlobalSetup","id":"bjK,wS1MYO7aiYkFSwd{","x":61,"y":53,"deletable":false,"next":{"block":{"type":"variables_set_prime_hub","id":"J4Mh?hP(%)+U[Tyb/Vcx","extraState":{"optionLevel":0},"fields":{"VAR":{"id":"8{)UPIZ0fi_J2[}H?3kY"}}}}},{"type":"blockGlobalStart","id":"3tJe|AWl0baN(wH9a$@.","x":59,"y":198,"deletable":false,"next":{"block":{"type":"blockFlowRepeat","id":"o-!Xp?0)ho^6DWKIj8QV","inputs":{"TIMES":{"shadow":{"type":"blockMathNumber","id":"j(/frvcFYT}Bl,U4ikRP","fields":{"NUM":3}}},"DO":{"block":{"type":"blockSpeakerBeep","id":"Z6xsp|T[lUK$VXVA~L4m","inputs":{"VAR":{"shadow":{"type":"variables_get_speaker_hub","id":"4T2wSVRW]R~V)?edHfvI","fields":{"VAR":{"id":"8{)UPIZ0fi_J2[}H?3kY","name":"hub","type":"PrimeHub"}}}},"VALUE0":{"shadow":{"type":"unit_frequency","id":"{D?;64b.IB1j_}`kL1;N","fields":{"VALUE0":500}}},"VALUE1":{"shadow":{"type":"unit_time","id":"Ucdy1GN#iO.xOdL$|c-A","fields":{"VALUE0":100}}}},"next":{"block":{"type":"blockWaitTime","id":"IO}A2K]6gcL7KTI]m4C$","inputs":{"VALUE0":{"shadow":{"type":"unit_time","id":"jGK3q^my}}ivtfDAPBY^","fields":{"VALUE0":500}}}}}}}}}}}}]},"variables":[{"name":"red","id":"rd4;Bv=[R{_LB]gx7fpb","type":"ColorDef"},{"name":"orange","id":"XN$)z4,Jg.t_^6rq9@t$","type":"ColorDef"},{"name":"yellow","id":"AU{ttkMcfxZ=e?zR2Yxm","type":"ColorDef"},{"name":"green","id":"jvSAoL?oE-Hm`{dH_Gkb","type":"ColorDef"},{"name":"cyan","id":"F^k9?45k([V!zaA5#Q2}","type":"ColorDef"},{"name":"blue","id":"-hTjBi:pQD7zXvBAh_0N","type":"ColorDef"},{"name":"violet","id":"a:?o^+Jmx{Ty;J.QR[2d","type":"ColorDef"},{"name":"magenta","id":"3s|Bj$I2iK`-Xn1SvqL2","type":"ColorDef"},{"name":"white","id":"kLZ+c57(Y4mfIS~YUYe^","type":"ColorDef"},{"name":"none","id":"iq/tZO-Ik#SJHk%uh*@h","type":"ColorDef"},{"name":"hub","id":"8{)UPIZ0fi_J2[}H?3kY","type":"PrimeHub"}],"info":{"type":"pybricks","version":"1.2.3"}}
from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# Set up all devices.
hub = PrimeHub()


# The main program starts here.
for count in range(3):
    hub.speaker.beep(500, 100)
    wait(500)
