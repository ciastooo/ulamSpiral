from PIL import Image

size = input("Enter size of image:")
while 1:
    try:
        size = int(size)
        break
    except ValueError:
        print("Entered size is not a number")
        size = input("Enter size of image:")

img = Image.new('RGB', (size, size))
img.save('image.png')