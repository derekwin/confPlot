
"""
color:
  - ColorMid
  - ColorHeavy
  - ColorLight
  
marker:
  - MarkerClassic
"""

class Color:
  def __init__(self, main_color, other_color_list: list) -> None:
    self.main_color = main_color
    self.others_colors = other_color_list
    self.other_color_num = len(other_color_list)
    
  def get(self, id: int) -> tuple:
    if id == 0:
      return self.main_color
    choose = id % self.other_color_num
    return self.others_colors[choose]
    

ColorMid = Color(
  main_color = (192/255.0, 50/255.0, 26/255.0),
  other_color_list= [
    (84/255.0, 123/255.0, 180/255.0),
    (98/255.0, 156/255.0, 53/255.0),
    (108/255.0, 97/255.0, 175/255.0),
    (221/255.0, 124/255.0, 79/255.0),
    (111/255.0, 111/255.0, 111/255.0),
  ]
)

ColorHeavy = Color(
  main_color = (147/255.0, 47/255.0, 37/255.0),
  other_color_list= [
    (140/255.0, 191/255.0, 135/255.0),
    (62/255.0, 96/255.0, 141/255.0),
    (203/255.0, 148/255.0, 117/255.0),
    (78/255.0, 25/255.0, 69/255.0),
    (144/255.0, 146/255.0, 145/255.0),
  ]
)

ColorLight = Color(
  main_color = (226/255.0, 145/255.0, 53/255.0),
  other_color_list= [
    (184/255.0, 219/255.0, 179/255.0),
    (113/255.0, 154/255.0, 172/255.0),
    (114/255.0, 176/255.0, 99/255.0),
    (148/255.0, 198/255.0, 205/255.0),
    (74/255.0, 95/255.0, 126/255.0),
  ]
)


class Marker:
  def __init__(self, marker_list: list) -> None:
    self.marker_list = marker_list
    self.other_marker_num = len(marker_list)
    
  def get(self, id: int) -> tuple:
    choose = id % self.other_marker_num
    return self.marker_list[choose]

MarkerClassic = Marker(
  marker_list=[
    "o",
    "v",
    "s",
    "*",
    "X",
    "d",
    "^",
    "2"
  ]
)