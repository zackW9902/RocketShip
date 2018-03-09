from Graphics import *




class Rocket(object):
    def __init__(self, x, y, color, win):
        self.x = x
        self.y = y
        self.color = color
        self.buildBooster(x,y, color, win)


class Capsule(object):
    def __init__(self):()
    window = Circle(Point(475,200),10.5)
    cap = Polygon(Point(550,250),Point(550,200),Point(500,150),Point(450,150),Point(400,200),Point(400,250))
    cap.setFill()
    cap.setOutline("black")
    cap.draw(win)



class Booster(object):
    def __init__(self):
        boosters = Rectangle(Point(275,300),Point(375,550))
        boosters.setFill ("red")
        boosters.setOutline ("black")




class RocketShip(object):
    def __init__(self):



