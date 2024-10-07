import customtkinter
from .read_json import read_json
import json

main_frame = customtkinter.CTk(fg_color= ('#FE2EF7'))
# создали главный (розовый цвет)(сам дисплей)

config = read_json(name_json= 'config.json')
#настройки кода json
# print(json.dumps(config, indent= 4))
#
WIDTH = config['mainframe']['width']
#шырина проекта
HEIGHT = config['mainframe']['height']
#длина проекта
main_frame.geometry(f'{WIDTH}x{HEIGHT}')
#обчисления дисплея проекта
