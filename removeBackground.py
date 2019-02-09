from PIL import Image

def show():
    f = input("\n Hello, user. "
                  "\n \n Please type in the path to your file and press 'Enter': ")
    myfile = open(f, 'r')

    img = Image.open(f)
    rgb_im = img.convert('RGB')

    pixelMap = rgb_im.load()

    img = Image.new(img.mode, img.size)
    pixelsNew = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = rgb_im.getpixel((i, j))
            if (r+b+g)/3 > 150:
                pixelMap[i, j] = (255, 255, 255,255)
            else:
                pixelsNew[i, j] = pixelMap[i, j]
    img.show()


show()
