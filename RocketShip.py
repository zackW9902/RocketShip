from Graphics import *




class Rocket(object):
    def __init__(self, x, y, color, win):
        self.x = x
        self.y = y
        self.color = color
        self.buildBooster(x,y, color, win)

    def buildBooster(self, x, y, color, win):
        body = Rectangle(Point(x,y),Point(x +55, y +275))
        body.setFill(color)
        engin = Polygon(Point(x,y +275),Point(x +55,y +275),Point(x +75,y +300),Point(x -25,y + 300))
        engin.setFill(color)
        cap = Polygon(Point(x,y),Point(x +25,y -25),Point(x +55,y))
        cap.setFill(color)
        fire = Image(Point(330, 625),"flame.gif")
        fire2 = Image(Point(590, 627), "flame.gif")
        bar = Line(Point(380,400),Point(400,400))
        bar.setWidth(10)
        bar2 = Line(Point(550, 400), Point(575, 400))
        bar2.setWidth(10)
        body.draw(win)
        engin.draw(win)
        cap.draw(win)
        fire.draw(win)
        fire2.draw(win)
        bar.draw(win)
        bar2.draw(win)





class Capsule(object):
    def __init__(self,x,y,color,win):
        self.drawBody(win)
        self.drawEng(win)
        self.drawTop(win,x,y,color)
    def drawTop(self, win,x,y,color):
        cap = Polygon(Point(x,y),Point(x,y - 50),Point(x + 50,y - 100),Point(x + 100,y - 100),Point(x + 150,y - 50),Point(x + 150,y))
        cap.setFill(color)
        cap.draw(win)
        #MrB = Image(Point(475, 200),"Mr.B!.jpg")
        #MrB.draw(win)
        pole = Rectangle(Point(450,50), Point(500,150))
        pole.draw(win)
        tri = Polygon(Point(450,50), Point(475,25), Point(500,50))
        tri.draw(win)
    def drawBody(self, win):
        body = Rectangle(Point(400,250),Point(550,525))
        body.draw(win)
    def drawEng(self, win):
        eng1 = Rectangle(Point(400,525),Point(550,575))
        eng2 = Rectangle(Point(425,575),Point(525,600))
        eng1.draw(win)
        eng2.draw(win)
        fire3 = Image(Point(470, 650), "flame.gif")
        fire3.draw(win)







class RocketShip(object):
    def __init__(self,win):
        cap = Capsule(400,250,'red',win)
        boost = Rocket(575,275,'orange',win)
        boost = Rocket(325,275, 'orange', win)






