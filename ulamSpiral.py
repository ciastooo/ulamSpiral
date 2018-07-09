from PIL import Image

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n % 2 == 0: return False
  if n < 9: return True
  if n % 3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True   

# size = input("Enter size of image:")
size=100
while 1:
    try:
        size = int(size)
        break
    except ValueError:
        print("Entered size is not a number")
        size = input("Enter size of image:")

img = Image.new('RGB', (size, size), (255,255,255))
x = size//2
y = x
print(x, y)
i = 1   # current integer that we are checking
step = 1    # how many steps utill we "rotate" our writing direction (since we're writing in spiral)
direction = 1   # in which direction we are currently moving (0 = up, 1 = right, 2 = down, 3 = left)
while True:
    for repeat in range(0,2):
        steps_left = step;
        while steps_left > 0:
            if x < 0 or x >= size or y < 0 or y >= size:
                break
            if(is_prime(i)):
                img.putpixel((x, y), (0,0,0))
            i = i + 1
            if direction == 0:
                y = y - 1
            elif direction == 1:
                x = x + 1
            elif direction == 2:
                y = y + 1
            elif direction == 3:
                x = x - 1
            if repeat == 1:
                direction += 1
                if direction == 4:
                    direction = 0
            steps_left = steps_left - 1
    if x < 0 or x >= size or y < 0 or y >= size:
        break
    step = step + 1
    
img.save('image.png')