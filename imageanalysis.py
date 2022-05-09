import imageio
import matplotlib.pyplot as plt 

pic = imageio.imread('nameofimage.png')
plt.figure(figsize = (5,5))
plt.imshow(pic)
print('Type of the image : ' , type(pic)) 
print('Shape of the image : {}'.format(pic.shape)) 
print('Image Height {}'.format(pic.shape[0])) 
print('Image Width {}'.format(pic.shape[1])) 
height=pic.shape[0]
width=pic.shape[1]
heightList=[]
for i in range(height):
    heightList.append(i)
print(heightList)
widthList=[]
for i in range(width):
    widthList.append(i)
print(widthList)
print('Dimension of Image {}'.format(pic.ndim))
print('Value of only R channel {}'.format(pic[ 10, 50, 0]))
print('Value of only G channel {}'.format(pic[ 10, 50, 1])) 
print('Value of only B channel {}'.format(pic[ 10, 50, 2]))