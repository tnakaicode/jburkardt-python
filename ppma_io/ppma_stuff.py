import io 
 
def tokenize(f):
    for line in f:
        if line[0] != '#':
            for t in line.split():
                yield t
 
def ppmp3tobitmap(f):
    t = tokenize(f)
    nexttoken = lambda : next(t)
    assert 'P3' == nexttoken(), 'Wrong filetype'
    width, height, maxval = (int(nexttoken()) for i in range(3))
    bitmap = Bitmap(width, height, Colour(0, 0, 0))
    for h in range(height-1, -1, -1):
        for w in range(0, width):
            bitmap.set(w, h, Colour( *(int(nexttoken()) for i in range(3))))
 
    return bitmapdef loadPPM(fname):

#
# Open the input file
#
  inf = open(fname,"r")

#
# Read the magic number out of the top of the file and verify that we are
# reading from an ASCII PPM file (denoted by P3)
#
  magic = strip_comments(inf.readline())
  if (magic != "P3"):
    raise PPM_Exception, 'The file being loaded does not appear to be a valid ASCII PPM file'

#
# Get the image dimensions
#
  dimensions = strip_comments(inf.readline())
#(width, sep, height) = dimensions.partition(" ")
  (width, sep, height) = partition(dimensions," ")
  width = int(width)
  height = int(height)
  if (width <= 0) or (height <= 0):
    raise PPM_Exception, "The file being loaded does not appear to have valid dimensions (" + str(width) + " x " + str(height) + ")"

#
# Get the maximum value -- this should always be 255 
#
  max = inf.readline()
  max = int(strip_comments(max))
  if (max != 255):
    sys.stderr.write("Warning: PPM file does not have a maximum value of 255.  Image may not be handled correctly.")

#
# Create a list of the individual color components, loaded from the file
#
  color_list = []
  for line in inf:
    line = strip_comments(line)
    color_list += line.split(" ")

  inf.close()# We are done with the file -- be nice and close it 

#
# Now that we have a one dimensional list of all of the color components,
# we need to arrage those color components into a three dimensional list
# of lists of lists structured so that the outer list is a list of columns,
# and each column is a list of color components in the order red, then green
# then blue.  Note that the original image data is assumed to have its 
# color components stored in this order.
#
  image = []
  for x in range(0,width):
    image.append([])
    for y in range(0,height):
      image[x].append([int(color_list[(y * width + x) * 3]), \
	               int(color_list[(y * width + x) * 3 + 1]),
		       int(color_list[(y * width + x) * 3 + 2])])

  return image

