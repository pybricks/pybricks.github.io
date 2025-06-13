# pybricks blocks file:{"blocks":{"languageVersion":0,"blocks":[{"type":"blockGlobalSetup","id":"bjK,wS1MYO7aiYkFSwd{","x":26,"y":23,"deletable":false,"next":{"block":{"type":"variables_set_prime_hub","id":"u8IACHtw@93XK!ZSV!]*","extraState":{"optionLevel":0},"fields":{"VAR":{"id":"M(Nj`oRAz|Nfh%D19AOf"}},"next":{"block":{"type":"variables_set_ultrasonic_sensor","id":"dZ1_$tvX@SsrW}R.iZ*}","fields":{"VAR":{"id":"34|JQ1oqFiClXIo$D;QD"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"8H?xxb)v`@hs~ttLto:U","fields":{"NAME":"D"}}}}}}}}},{"type":"blockGlobalStart","id":"3tJe|AWl0baN(wH9a$@.","x":26,"y":193,"deletable":false,"next":{"block":{"type":"blockMultiTask","id":"O#7/:=ZBcj)@Fe0^b!nx","extraState":{"optionLevel":0},"fields":{"METHOD":"MULTITASK_RACE"},"inputs":{"TASK0":{"block":{"type":"blockWaitUntil","id":"NKzEwvu=H)mf;KjODpxe","inputs":{"BOOL":{"shadow":{"type":"blockLogicTrue","id":"SFf5PmUm_s%+bh11AF/N"},"block":{"type":"blockLogicCompare","id":"a7qnEI[J][ohrH9h)PV*","fields":{"OP1":"LTE"},"inputs":{"A":{"shadow":{"type":"blockMathNumber","id":"yf#|pifeCZr%96V)9aeT","fields":{"NUM":3}},"block":{"type":"blockDistance","id":"|ye8AwnvBw(.}S#L8mp4","inputs":{"VAR":{"shadow":{"type":"variables_get_distance_device","id":".q3}:QH+RZ|Gh.%Qa`Qd","fields":{"VAR":{"id":"34|JQ1oqFiClXIo$D;QD","name":"sensor","type":"UltrasonicSensor"}}}}}}},"B":{"shadow":{"type":"blockMathNumber","id":"JY,pGi9yvDO/9mtX)qRB","fields":{"NUM":500}}}}}}}}},"TASK1":{"block":{"type":"blockWaitUntil","id":"TQt~[*b]|q$MIy6r4U1f","inputs":{"BOOL":{"shadow":{"type":"blockLogicTrue","id":"SFf5PmUm_s%+bh11AF/N"},"block":{"type":"blockButtonIsPressed","id":"M#B6ZkbzN@xsJ`F)3@z_","inputs":{"VAR":{"shadow":{"type":"variables_get_keypad","id":"Im7ym32C02FHoYNvH]p%","fields":{"VAR":{"id":"M(Nj`oRAz|Nfh%D19AOf","name":"hub","type":"PrimeHub"}}}},"VALUE0":{"shadow":{"type":"blockParametersButton","id":"?GUgjmdjLSngZGzJ:;D5","fields":{"VALUE":"LEFT"}}}}}}},"next":{"block":{"type":"blockWaitUntil","id":"lK:w#UtsUc7s5H$$c^XB","inputs":{"BOOL":{"shadow":{"type":"blockLogicTrue","id":"SFf5PmUm_s%+bh11AF/N"},"block":{"type":"blockLogicIsNone","id":"$Z{b#35BVzx6)eN3gp=C","fields":{"OP":"NOT"},"inputs":{"BOOL":{"shadow":{"type":"blockLogicTrue","id":"fOTsyo08F(ff?t+73k9d"},"block":{"type":"blockButtonIsPressed","id":"WYe]:covK6Tceb*||n(%","inputs":{"VAR":{"shadow":{"type":"variables_get_keypad","id":"-+3rVCiH+/a5;r4{8Xh5","fields":{"VAR":{"id":"M(Nj`oRAz|Nfh%D19AOf","name":"hub","type":"PrimeHub"}}}},"VALUE0":{"shadow":{"type":"blockParametersButton","id":"=d1/]PiuPMM1`RMd)/M9","fields":{"VALUE":"LEFT"}}}}}}}}}}}}}}},"next":{"block":{"type":"blockIfElse","id":"(NssOPap)Oa+4B|Rg(!W","extraState":{"optionLevel":1},"inputs":{"IF0":{"shadow":{"type":"blockLogicTrue","id":"o_v;cNY`a!zz,hwt_NEd"},"block":{"type":"blockLogicCompare","id":"dO+WDO4PqZQiZw[Yr2fD","fields":{"OP1":"LTE"},"inputs":{"A":{"shadow":{"type":"blockMathNumber","id":"yf#|pifeCZr%96V)9aeT","fields":{"NUM":3}},"block":{"type":"blockDistance","id":"Jd]]unxW-Jo?nNFA}j6c","inputs":{"VAR":{"shadow":{"type":"variables_get_distance_device","id":"]^YF3hdo0/as]B94?zJ}","fields":{"VAR":{"id":"34|JQ1oqFiClXIo$D;QD","name":"sensor","type":"UltrasonicSensor"}}}}}}},"B":{"shadow":{"type":"blockMathNumber","id":"vAcA#}9pZb[hYT#iln_a","fields":{"NUM":500}}}}}},"DO0":{"block":{"type":"blockSpeakerBeep","id":"trU/I^YU75e3jjUH0D9W","inputs":{"VAR":{"shadow":{"type":"variables_get_speaker_hub","id":"U3i8t#8x2#~}r+|TP=.-","fields":{"VAR":{"id":"M(Nj`oRAz|Nfh%D19AOf","name":"hub","type":"PrimeHub"}}}},"VALUE0":{"shadow":{"type":"unit_frequency","id":"byT/|6;]B;LO1pLp?pI:","fields":{"VALUE0":500}}},"VALUE1":{"shadow":{"type":"unit_time","id":"8gZ[9*q0o?u`4ADa%6}o","fields":{"VALUE0":100}}}}}},"ELSE":{"block":{"type":"blockSpeakerBeep","id":"ZF03DO+84HH/p*S=rhwj","inputs":{"VAR":{"shadow":{"type":"variables_get_speaker_hub","id":"izVcT]o~wTPk1sG1IrgW","fields":{"VAR":{"id":"M(Nj`oRAz|Nfh%D19AOf","name":"hub","type":"PrimeHub"}}}},"VALUE0":{"shadow":{"type":"unit_frequency","id":"ewvAA$;4tRC3yR]4GErz","fields":{"VALUE0":200}}},"VALUE1":{"shadow":{"type":"unit_time","id":"MtC)^$x/lrIMqIeAY{%Q","fields":{"VALUE0":100}}}}}}}}}}}}]},"variables":[{"name":"red","id":"zTWBdr:x]9TZ5w^0hze8","type":"ColorDef"},{"name":"orange","id":"q.tDyo+jgZZDMye7oWnb","type":"ColorDef"},{"name":"yellow","id":"]%)nHSg1LSBIPd/=|o.M","type":"ColorDef"},{"name":"green","id":"]Me#}e+(Fe5HNY2X9S:C","type":"ColorDef"},{"name":"cyan","id":"hfyUxJb9Hk9dstNnrgqc","type":"ColorDef"},{"name":"blue","id":"S}SRcf||7%So~Gl)k]U-","type":"ColorDef"},{"name":"violet","id":"PKqk(IDH3oY|mtEt6lnj","type":"ColorDef"},{"name":"magenta","id":"~kn`ES|Olk*dHVt~J3Oq","type":"ColorDef"},{"name":"white","id":",ssDGS*gf)s!{:j:Q(ZX","type":"ColorDef"},{"name":"none","id":"N8zP+udl{B!-/6E]:$s;","type":"ColorDef"},{"name":"hub","id":"M(Nj`oRAz|Nfh%D19AOf","type":"PrimeHub"},{"name":"sensor","id":"34|JQ1oqFiClXIo$D;QD","type":"UltrasonicSensor"}],"info":{"type":"pybricks","version":"1.3.2"}}
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Port
from pybricks.pupdevices import UltrasonicSensor
from pybricks.tools import multitask, run_task, wait

# Set up all devices.
hub = PrimeHub()
sensor = UltrasonicSensor(Port.D)

async def subtask():
    while not await sensor.distance() <= 500:
        await wait(0)

async def subtask2():
    while not Button.LEFT in hub.buttons.pressed():
        await wait(0)
    while Button.LEFT in hub.buttons.pressed():
        await wait(0)

async def main():
    await multitask(
        subtask(),
        subtask2(),
        race=True,
    )
    if await sensor.distance() <= 500:
        await hub.speaker.beep(500, 100)
    else:
        await hub.speaker.beep(200, 100)


run_task(main())