import sys, PIL.Image
saved = "dithere_image.png"
img = PIL.Image.open("image.jpg").convert('L')

threshold = 128*[0] + 128*[255]

for y in range(img.size[1]):
    for x in range(img.size[0]):

        old = img.getpixel((x, y))
        new = threshold[old]
        err = (old - new) >> 3 # divide by 8
            
        img.putpixel((x, y), new)
        
        for nxy in [(x+1, y), (x+2, y), (x-1, y+1), (x, y+1), (x+1, y+1), (x, y+2)]:
            try:
                img.putpixel(nxy, img.getpixel(nxy) + err)
            except IndexError:
                pass

img.show()
img.save(saved)