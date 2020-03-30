import sys
import PIL.Image


def dithering(imgIn, imgOut, trame=3, show=False):
    """Transforme une image en trame dither"""
    img = PIL.Image.open(imgIn).convert('L')
    threshold = 128 * [0] + 128 * [255]

    for y in range(img.size[1]):
        for x in range(img.size[0]):

            old = img.getpixel((x, y))
            new = threshold[old]
            err = (old - new) >> trame  # divide by 2^trame

            img.putpixel((x, y), new)

            for nxy in [(x + 1, y), (x + 2, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x, y + 2)]:
                try:
                    img.putpixel(nxy, img.getpixel(nxy) + err)
                except IndexError:
                    pass
    if show:
        img.show()
    img.save(imgOut)

if __name__ == "__main__":
    dithering("image.jpg", "dithere_image.png", trame=3, show=True)
