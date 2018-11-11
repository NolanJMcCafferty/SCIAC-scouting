from PIL import Image
import os
#import libraries


#loop through in image in image directory
for filename in os.listdir('.'):
    #if the file is a png file, make an image object
    if filename.endswith('.png'):
        image = Image.open(filename)
        #parse the filename for the name, and the extension
        first,ext = os.path.splitext(filename)
        #grab dimensions
        w,h = image.size
        #make the crop
        image.crop((81,78,w-43,h-97)).save('newCharts/{}.png'.format(first))
        #remove the old, uncropped photo
        os.remove(filename)