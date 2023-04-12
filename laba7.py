from PIL import Image
def a():
    image=Image.open("1.jpg")
    image.show()
    width, height = image.size
    print('Размер изображения:', width, height)
    f=image.format
    print('Формат', f)
    color=image.mode
    print('Цветовая модель', color)
a()

def b():
    image = Image.open("1.jpg")
    res_image=image.reduce(3)
    res_image.save('re.jpg')
    horizontal=image.transpose(Image.FLIP_LEFT_RIGHT)
    horizontal.save('h.jpg')
    vertical=image.transpose(Image.FLIP_TOP_BOTTOM)
    vertical.save('v.jpg')
b()

def c():
    images=('1.jpg','2.jpg', '3.jpg', '4.jpg', '5.jpg')
    for i in images:
        with Image.open(i) as image:
            filter=image.convert('L')
            filter.save("bw"+ str(i))
c()

def d():
    image=Image.open('1.jpg')
    w=Image.open('2.jpg')
    image.paste(w,(200,200))
    image.show()
    image.save('w.jpg')
d()