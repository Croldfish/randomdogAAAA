import dog
from PIL import Image
x = int(input("How many dogs do you want?(NUMBERS ONLY) "))
for i in range(0,x):
    dog.getDog(filename='randog')
    img = Image.open('randog.jpg')
    img.show()

