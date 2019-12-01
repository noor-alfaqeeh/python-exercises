print("............exercise1...........")
import statistics as st
x=[3,1.5,4.5,6.75,2.25,5.75,2.25]

print(st.mean(x))
print(st.harmonic_mean(x))
print(st.median(x))
print(st.median_low(x))
print(st.median_high(x))
print(st.median_grouped(x))
print(st.mode(x))
print(st.pstdev(x))
print(st.pvariance(x))
print(st.stdev(x))
print(st.variance(x))

print("............exercise2...........")
import random
print( random.random() )
print ( random.randrange(10) )
print ( random.choice(['Ali', 'Khalid', 'Hussam']) )
print ( random.sample(range(1000), 10) )
print ( random.choice('Orange Academy') )
items = [1,5,8,9,2,4]
random.shuffle(items)
print( items )
print ( random.randint(20, 30) )
print ( random.randrange(1000, 2111, 5) )
print ( random.uniform(10000, 11000))

print("............exercise3...........")
import math
print ('pi: %.30f' % math.pi)

print (math.sin(30))
print (math.cos(200))
print (math.tan(180))

print(math.floor(10.8))
print(math.ceil(10.8))

print("............exercise4...........")
from PIL import Image,ImageDraw,ImageFilter
x=Image.open("ice2.png")
print(x.format,x.size,x.mode)
x.show()

image_flip=x.transpose(Image.FLIP_TOP_BOTTOM)
image_flip.show()
grayscale_image=x.convert('L')
grayscale_image.show()
crop=x.crop((0,0,50,50))
crop.show()

draw=ImageDraw.Draw(x)
draw.line((0,0)+x.size,fill=(255,255,255))
draw.line((0,x.size[1],x.size[0],0),fill=(255,255,255))
draw.text((x.size[0]/2-x.size[0]/2,x.size[1]/2+20),"Noor",fill=(255,255,0))
x.show()


new=x.filter(ImageFilter.EDGE_ENHANCE)
new.show()

new=x.filter(ImageFilter.FIND_EDGES)
new.show()

new=x.filter(ImageFilter.SMOOTH)
new.show()

new=x.filter(ImageFilter.SHARPEN)
new.show()

alpha=0.5
x2=Image.open("ice3.jpg").resize(x.size)
Image.blend(x,x2,alpha).save("New.JPG".format(alpha))
x=Image.open("New.JPG")
x.show()

blurred=x.filter(ImageFilter.BLUR)
blurred.show()

size=(128,128)
x.thumbnail(size)
x.show()

rot=x.rotate(90)
rot.show()

mask=Image.open("mask2.png")
mask=mask.resize(x.size)
Image.composite(x,x2,mask).save("noor.jpg")
new=Image.open("noor.jpg")
new.show()
