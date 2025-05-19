# pybricks blocks file:{"blocks":{"languageVersion":0,"blocks":[{"type":"blockGlobalSetup","id":"bjK,wS1MYO7aiYkFSwd{","x":26,"y":23,"deletable":false,"next":{"block":{"type":"variables_set_inventor_hub","id":"Nrif20[GXH%@M,j+fdP|","extraState":{"optionLevel":0},"fields":{"VAR":{"id":"w`twa7#`0zd:FoNxcJf#"}}}}},{"type":"blockGlobalStart","id":"3tJe|AWl0baN(wH9a$@.","x":25,"y":165,"deletable":false,"next":{"block":{"type":"blockFlowWhile","id":"T2?DH??8K!i6HMjN3_w9","fields":{"MODE":"WHILE"},"inputs":{"BOOL":{"shadow":{"type":"blockLogicTrue","id":"HH*?CdZiFA!VrD:xFQ-y"}},"DO":{"block":{"type":"blockLightOnColor","id":"a~~(Ge6UnsLx#D05n$]}","extraState":{"optionLevel":1},"fields":{"METHOD":"LIGHT_ON"},"inputs":{"VAR":{"shadow":{"type":"variables_get_color_light_device","id":"ODTxrx}U)GcauFVs[P.~","fields":{"VAR":{"id":"w`twa7#`0zd:FoNxcJf#","name":"hub","type":"InventorHub"}}}},"COLOR":{"shadow":{"type":"variables_get_color","id":"3wGqjovrJ__=1U^Fe%7+","fields":{"COLOUR":"#ff0000","VAR":{"id":"zTWBdr:x]9TZ5w^0hze8","name":"red","type":"ColorDef"}}}}},"next":{"block":{"type":"blockWaitTime","id":"35[vQIEN7!e9.TmF*.`4","inputs":{"VALUE0":{"shadow":{"type":"unit_time","id":"wUlcM$!*ergUU76h,ceC","fields":{"VALUE0":1}}}},"next":{"block":{"type":"blockLightOnColor","id":"d#wpW}Hw;$%M79mOl.a9","extraState":{"optionLevel":1},"fields":{"METHOD":"LIGHT_ON"},"inputs":{"VAR":{"shadow":{"type":"variables_get_color_light_device","id":"*$![@@1mya*%+3OKR?_D","fields":{"VAR":{"id":"w`twa7#`0zd:FoNxcJf#","name":"hub","type":"InventorHub"}}}},"COLOR":{"shadow":{"type":"variables_get_color","id":"7{c}$!KnT[DPICoBBTCq","fields":{"COLOUR":"#00ff00","VAR":{"id":"]Me#}e+(Fe5HNY2X9S:C","name":"green","type":"ColorDef"}}}}},"next":{"block":{"type":"blockWaitTime","id":"GF|ym$vkK4o^BP^F|Le4","inputs":{"VALUE0":{"shadow":{"type":"unit_time","id":"w[a+mq1j)_:{[nO=o7z;","fields":{"VALUE0":1}}}}}}}}}}}}}}}}]},"variables":[{"name":"red","id":"zTWBdr:x]9TZ5w^0hze8","type":"ColorDef"},{"name":"orange","id":"q.tDyo+jgZZDMye7oWnb","type":"ColorDef"},{"name":"yellow","id":"]%)nHSg1LSBIPd/=|o.M","type":"ColorDef"},{"name":"green","id":"]Me#}e+(Fe5HNY2X9S:C","type":"ColorDef"},{"name":"cyan","id":"hfyUxJb9Hk9dstNnrgqc","type":"ColorDef"},{"name":"blue","id":"S}SRcf||7%So~Gl)k]U-","type":"ColorDef"},{"name":"violet","id":"PKqk(IDH3oY|mtEt6lnj","type":"ColorDef"},{"name":"magenta","id":"~kn`ES|Olk*dHVt~J3Oq","type":"ColorDef"},{"name":"white","id":",ssDGS*gf)s!{:j:Q(ZX","type":"ColorDef"},{"name":"none","id":"N8zP+udl{B!-/6E]:$s;","type":"ColorDef"},{"name":"hub","id":"w`twa7#`0zd:FoNxcJf#","type":"InventorHub"}],"info":{"type":"pybricks","version":"1.3.2"}}
from pybricks.hubs import InventorHub
from pybricks.parameters import Color
from pybricks.tools import wait

# Set up all devices.
hub = InventorHub()


# The main program starts here.
while True:
    hub.light.on(Color.RED)
    wait(1)
    hub.light.on(Color.GREEN)
    wait(1)
