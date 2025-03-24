from pystyle import *
import time

pubMP_WaterMark = ['\n██████╗ ╔██╗   ██╗██████╗ ███╗   ███╗██████╗ ',
                   '██╔══██╗║██║   ██║██╔══██╗████╗ ████║██╔══██╗',
                   '██████╔╝║██║   ██║██████╔╝██╔████╔██║██████╔╝',
                   '██╔═══╝ ║██║   ██║██╔══██╗██║╚██╔╝██║██╔═══╝ ',
                   '██║     ║████████║███████║██║ ╚═╝ ██║██║',
                   '╚═╝     ╚════════╝ ╚═════╝╚═╝     ╚═╝╚═╝  by sl0wdown']

for part in pubMP_WaterMark:
    print(Colorate.Horizontal(Colors.blue_to_red, part, 1))
    time.sleep(0.05)

print('')
