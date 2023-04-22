from PIL import Image, ImageFilter
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QLabel, QPushButton, QBoxLayout, QHBoxLayout, QVBoxLayout, QFileDialog, QMessageBox
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
import os

app = QApplication([])
win = QWidget()

box = QMessageBox()

win.resize(700, 400)
win.setWindowTitle("Easy Editor")


butPap = QPushButton("Папка")
butLev = QPushButton("Лево")
butPrav = QPushButton("Право")
butZer = QPushButton("Зеркало")
butRez = QPushButton("Резкость")
butChb = QPushButton("Ч/Б")
butBlr = QPushButton("Размытие")
butGrn = QPushButton("Границы")
butSgl = QPushButton("Сглаживание")
butGru = QPushButton("Очерчивание границ")
butDet = QPushButton("Детали")
butCon = QPushButton("Контур")
butSgm = QPushButton("Сильное сглаживание")
butGum = QPushButton("Сильное очерчивание границ")
butOrg = QPushButton("Оригинал")


lb_image = QLabel("Картинка")


spis = QListWidget()


rowGL = QHBoxLayout()

rowV2 = QVBoxLayout()

rowV2.addWidget(butPap, alignment = Qt.AlignHCenter)

rowV2.addWidget(spis, alignment = Qt.AlignHCenter)

rowV1 = QVBoxLayout()

rowV1.addWidget(lb_image, 95)

rowH1 = QHBoxLayout()

rowH2 = QHBoxLayout()

rowH1.addWidget(butLev, alignment = Qt.AlignHCenter)

rowH1.addWidget(butPrav, alignment = Qt.AlignHCenter)

rowH1.addWidget(butZer, alignment = Qt.AlignHCenter)

rowH1.addWidget(butRez, alignment = Qt.AlignHCenter)

rowH1.addWidget(butDet, alignment = Qt.AlignHCenter)

rowH1.addWidget(butGum, alignment = Qt.AlignHCenter)

rowH1.addWidget(butChb, alignment = Qt.AlignHCenter)

rowH2.addWidget(butBlr, alignment = Qt.AlignHCenter)

rowH2.addWidget(butGrn, alignment = Qt.AlignHCenter)

rowH2.addWidget(butSgl, alignment = Qt.AlignHCenter)

rowH2.addWidget(butGru, alignment = Qt.AlignHCenter)

rowH2.addWidget(butCon, alignment = Qt.AlignHCenter)

rowH2.addWidget(butSgm, alignment = Qt.AlignHCenter)

rowH2.addWidget(butOrg, alignment = Qt.AlignHCenter)

rowV1.addLayout(rowH2)

rowV1.addLayout(rowH1)

rowGL.addLayout(rowV2, 20)

rowGL.addLayout(rowV1, 80)

win.setLayout(rowGL)
win.show()

workdir = ''

def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def chooseWorkDir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showFilenamesList():
    extensions = [".jpg", ".png", ".gif", ".bmp", ".jpeg"]
    chooseWorkDir()
    try:
        filenames = filter(os.listdir(workdir), extensions)
        spis.clear()
        for filename in filenames:
            spis.addItem(filename)
    except:
        print("Ошибка")

class ImageProcessor():
    def __init__(self):
        self.img = None
        self.fn = None
        self.path = None
        self.image = None
        self.save_dir = "Modified/"

    def loadImage(self, path, filename):
        self.fn = filename
        self.path = path
        self.f_p = os.path.join(self.path, self.fn)
        self.img = Image.open(self.f_p)
        self.image = 1
    
    def showImage(self, path):
        lb_image.hide()
        pmi = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pmi = pmi.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pmi)
        self.image = 1
        lb_image.show()

    def do_bw(self):
        if self.image == 1:
            self.img = self.img.convert("L")
            self.do_save()
            impt = os.path.join(self.path, self.save_dir, self.fn)
            self.showImage(impt)
        else:
            box.setText("Ошибка, выбери картинку!")
            box.exec_()
        

    def do_left(self):
        if self.image == 1:
            self.img = self.img.transpose(Image.ROTATE_90)
            self.do_save()
            impt = os.path.join(self.path, self.save_dir, self.fn)
            self.showImage(impt)
        else:
            box.setText("Ошибка, выбери картинку!")
            box.exec_()

    def do_right(self):
        if self.image == 1:
            self.img = self.img.rotate(270, expand=True)
            self.do_save()
            impt = os.path.join(self.path, self.save_dir, self.fn)
            self.showImage(impt)
        else:
            box.setText("Ошибка, выбери картинку!")
            box.exec_()

    def do_mirrow(self):
        if self.image == 1:
            self.img = self.img.transpose(Image.FLIP_LEFT_RIGHT)
            self.do_save()
            impt = os.path.join(self.path, self.save_dir, self.fn)
            self.showImage(impt)
        else:
            box.setText("Ошибка, выбери картинку!")
            box.exec_()

    def do_sharply(self):
        if self.image == 1:
            self.img = self.img.filter(ImageFilter.SHARPEN)
            self.do_save()
            impt = os.path.join(self.path, self.save_dir, self.fn)
            self.showImage(impt)
        else:
            box.setText("Ошибка, выбери картинку!")
            box.exec_()

    def do_blur(self):
        if self.image == 1:
            self.img = self.img.filter(ImageFilter.GaussianBlur(2))
            self.do_save()
            impt = os.path.join(self.path, self.save_dir, self.fn)
            self.showImage(impt)
        else:
            box.setText("Ошибка, выбери картинку!")
            box.exec_()

    def do_gran(self):
        if self.image == 1:
            self.img = self.img.filter(ImageFilter.FIND_EDGES)
            self.do_save()
            impt = os.path.join(self.path, self.save_dir, self.fn)
            self.showImage(impt)
        else:
            box.setText("Ошибка, выбери картинку!")
            box.exec_()

    def do_sglg(self):
        if self.image == 1:
            self.img = self.img.filter(ImageFilter.SMOOTH)
            self.do_save()
            impt = os.path.join(self.path, self.save_dir, self.fn)
            self.showImage(impt)
        else:
            box.setText("Ошибка, выбери картинку!")
            box.exec_()

    def do_grnu(self):
        if self.image == 1:
            self.img = self.img.filter(ImageFilter.EDGE_ENHANCE)
            self.do_save()
            impt = os.path.join(self.path, self.save_dir, self.fn)
            self.showImage(impt)
        else:
            box.setText("Ошибка, выбери картинку!")
            box.exec_()

    def do_sglm(self):
        if self.image == 1:
            self.img = self.img.filter(ImageFilter.SMOOTH_MORE)
            self.do_save()
            impt = os.path.join(self.path, self.save_dir, self.fn)
            self.showImage(impt)
        else:
            box.setText("Ошибка, выбери картинку!")
            box.exec_()

    def do_grnm(self):
        if self.image == 1:
            self.img = self.img.filter(ImageFilter.EDGE_ENHANCE_MORE)
            self.do_save()
            impt = os.path.join(self.path, self.save_dir, self.fn)
            self.showImage(impt)
        else:
            box.setText("Ошибка, выбери картинку!")
            box.exec_()

    def do_coun(self):
        if self.image == 1:
            self.img = self.img.filter(ImageFilter.CONTOUR)
            self.do_save()
            impt = os.path.join(self.path, self.save_dir, self.fn)
            self.showImage(impt)
        else:
            box.setText("Ошибка, выбери картинку!")
            box.exec_()

    def do_detl(self):
        if self.image == 1:
            self.img = self.img.filter(ImageFilter.DETAIL)
            self.do_save()
            impt = os.path.join(self.path, self.save_dir, self.fn)
            self.showImage(impt)
        else:
            box.setText("Ошибка, выбери картинку!")
            box.exec_()

    def do_save(self):
        path = os.path.join(self.path, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        impt = os.path.join(path, self.fn)
        self.img.save(impt)

workimage = ImageProcessor()

def showChosenImage():
    filename = spis.selectedItems()[0].text()
    workimage.loadImage(workdir, filename)
    workimage.showImage(workimage.f_p)

def showChosenImageOriginal():
    if workimage.image == 1:
        filename = spis.selectedItems()[0].text()
        workimage.loadImage(workdir, filename)
        workimage.showImage(workimage.f_p)
    else:
        box.setText("Ошибка, картинки нет!")
        box.exec_()

spis.itemClicked.connect(showChosenImage)

butPap.clicked.connect(showFilenamesList)

butChb.clicked.connect(workimage.do_bw)

butRez.clicked.connect(workimage.do_sharply)

butPrav.clicked.connect(workimage.do_right)

butLev.clicked.connect(workimage.do_left)

butZer.clicked.connect(workimage.do_mirrow)

butBlr.clicked.connect(workimage.do_blur)

butGrn.clicked.connect(workimage.do_gran)

butSgl.clicked.connect(workimage.do_sglg)

butGru.clicked.connect(workimage.do_grnu)

butSgm.clicked.connect(workimage.do_sglm)

butGum.clicked.connect(workimage.do_grnm)

butDet.clicked.connect(workimage.do_detl)

butCon.clicked.connect(workimage.do_coun)

butOrg.clicked.connect(showChosenImageOriginal)

app.exec_()

'''from pygame import *
from random import *
init()

w = 600
h = 600
GREEN = (0,255,0)
YELLOW = (255,255,0)
RED = (255,0,0)

cellsize = 24
wcells = w//cellsize
hcells = h//cellsize
x, y = 1, 1
kx, ky = 1, 0

win = display.set_mode((w,h))
display.set_caption("Snake")
clock = time.Clock()

class Segment(sprite.Sprite):
    def __init__(self,x,y,cellcolor):
        self.image = Surface((cellsize-2,cellsize-2))
        self.image.fill(cellcolor)
        self.rect = self.image.get_rect(topleft=(x,y))
    def draw(self):
        win.blit(self.image,self.rect)

snake = []
snake.append(Segment(x,y,GREEN))

randomx = randint(0,wcells-1)*cellsize+1
randomy = randint(0,hcells-1)*cellsize+1
food = Segment(randomx,randomy,RED)

myfont = font.SysFont('Comic Sans MS', 30)

lose = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = False
            elif e.key == K_LEFT:
                kx, ky = -1, 0
            elif e.key == K_RIGHT:
                kx, ky = 1, 0
            elif e.key == K_UP:
                kx, ky = 0, -1
            elif e.key == K_DOWN:
                kx, ky = 0, 1

                
    win.fill((0,0,0))
    if not lose:
        for col in range(0,w+1,cellsize):
            draw.line(win,(66,66,66),(col,0),(col,w))
        for row in range(0,h+1,cellsize):
            draw.line(win,(66,66,66),(0,row),(h,row))

        last = len(snake)-1
        x = snake[last].rect.x + kx*cellsize
        y = snake[last].rect.y + ky*cellsize
        snake.append(Segment(x,y,GREEN))
        snake.pop(0)

        if x > w or x < 0 or y > h or y < 0:
            print("Game over!")
            lose = True
        for i in range(len(snake)-1):
            if snake[i].rect.x == x and snake[i].rect.y == y:
                print("Game over!")
                lose = True

        food.draw()

        for s in snake:
            s.draw()

        if x == food.rect.x and y == food.rect.y:
           snake.append(Segment(x,y,GREEN))
           randomx = randint(0,wcells-1)*cellsize+1
           randomy = randint(0,hcells-1)*cellsize+1
           food.rect.x = randomx
           food.rect.y = randomy

        text = myfont.render(str(len(snake)), False, YELLOW)
        win.blit(text,(10,10))
    else:
        text = myfont.render("Game over! Your result: "+str(len(snake)), False, YELLOW)
        win.blit(text,((w-text.get_width())//2,(h-text.get_height())//2))
        display.update()
        time.delay(3000)
        x, y = 1, 1
        kx, ky = 1, 0
        snake = []
        snake.append(Segment(x,y,GREEN))
        lose = False
    display.update()
    clock.tick(7)
quit()'''