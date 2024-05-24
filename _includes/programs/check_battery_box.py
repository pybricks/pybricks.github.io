# pybricks blocks file:{"blocks":{"languageVersion":0,"blocks":[{"type":"blockGlobalSetup","id":"bjK,wS1MYO7aiYkFSwd{","x":147,"y":113,"deletable":false,"next":{"block":{"type":"variables_setup_imported_function","id":"mmmuN.Yy~CIfQ^E4hBAA","fields":{"FROM_MODULE":{"id":"Hrw(k#JyYct/cpv`@%^7"},"VAR":{"id":"6g0FiVZcBf,Mn$_tXn^v"}},"next":{"block":{"type":"variables_set_motor","id":"8U6qOU[NGwNhRZ0,=qP3","fields":{"VAR":{"id":"5T.INh8Jt9PGyCe^3.tO"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"FHPSFi@823}Lv:Gr{EF_","fields":{"NAME":"A"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"z7Lds8Dx;L4tSTqoXaHW","fields":{"SELECTION":"Direction.CLOCKWISE"}}}},"next":{"block":{"type":"variables_set_motor","id":"w@l1e#`(;WaDmr=`[x/W","fields":{"VAR":{"id":"N~D~e}(1|DLx0gC2%J}e"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"~k!dY$V?H?=@$/vi7l_T","fields":{"NAME":"B"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"NIO9zQ!S^#FE)weA;6ZM","fields":{"SELECTION":"Direction.CLOCKWISE"}}}}}}}}}}},{"type":"blockGlobalStart","id":"3tJe|AWl0baN(wH9a$@.","x":149,"y":350,"deletable":false,"next":{"block":{"type":"blockMotorDuty","id":"CB,VMd-0;@:T7YlEslr$","inputs":{"VAR":{"shadow":{"type":"variables_get_simple_motor_device","id":"j@~n[h=#8Orml`c{1?ch","fields":{"VAR":{"id":"5T.INh8Jt9PGyCe^3.tO","name":"A","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_percent","id":"Bi}o0t$2dK6T%`cg#v~S","fields":{"VALUE0":100}}}},"next":{"block":{"type":"blockMotorDuty","id":"*(,MCwx`13Oep{f%^u-+","inputs":{"VAR":{"shadow":{"type":"variables_get_simple_motor_device","id":"JHwgZ9x6zH{Ruu5p(B~6","fields":{"VAR":{"id":"N~D~e}(1|DLx0gC2%J}e","name":"B","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_percent","id":"[k`zi2t]0Z3*^kA]86]J","fields":{"VALUE0":100}}}},"next":{"block":{"type":"blockWaitForever","id":"SZ9QldC3FEzWocdU;TFy"}}}}}}}]},"variables":[{"name":"red","id":"y!$k?Y3Qtw:vjVs8V?M]","type":"ColorDef"},{"name":"orange","id":"8}(Db$9e]Sz;@?Sj2/]A","type":"ColorDef"},{"name":"yellow","id":"f9nN|_eSyjqX^Q/yx5W+","type":"ColorDef"},{"name":"green","id":"y}m(2TuhFLV/%vwE_{!U","type":"ColorDef"},{"name":"cyan","id":"B]9/I]t-lQLbz=XCcvQV","type":"ColorDef"},{"name":"blue","id":"qL^[vyNMP.a64tu^C+Zr","type":"ColorDef"},{"name":"violet","id":"|/1U=y^~^[-t%zq}+ove","type":"ColorDef"},{"name":"magenta","id":"Go0-DAnzQINl%.|Z|tWC","type":"ColorDef"},{"name":"white","id":"N8aOg%It#.,{2[3zwB5!","type":"ColorDef"},{"name":"none","id":"uYz]0PBI.GJ/`-TX1:9z","type":"ColorDef"},{"name":"allow_missing_motors","id":"Hrw(k#JyYct/cpv`@%^7","type":"ModuleImported"},{"name":"Motor","id":"6g0FiVZcBf,Mn$_tXn^v","type":"FunctionImported"},{"name":"A","id":"5T.INh8Jt9PGyCe^3.tO","type":"Motor"},{"name":"B","id":"N~D~e}(1|DLx0gC2%J}e","type":"Motor"},{"name":"motor","id":"i]6,b3w^_I|0/WtMlL#B","type":"Motor"}],"info":{"type":"pybricks","version":"1.2.3"}}
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait

from allow_missing_motors import Motor

# Set up all devices.
A = Motor(Port.A, Direction.CLOCKWISE)
B = Motor(Port.B, Direction.CLOCKWISE)


# The main program starts here.
A.dc(100)
B.dc(100)
while True:
    wait(1000)
