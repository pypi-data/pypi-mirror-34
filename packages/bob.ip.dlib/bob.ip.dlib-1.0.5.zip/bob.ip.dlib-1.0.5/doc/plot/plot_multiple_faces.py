import bob.io.base
import bob.io.image
import bob.io.base.test_utils
import bob.ip.dlib
import pkg_resources
import os
from matplotlib import pyplot
import bob.ip.draw
import bob.ip.facedetect

#print "###################################"
#print os.path.join(pkg_resources.resource_filename(__name__, 'data'), 'multiple-faces.jpg')

# detect multiple bob
bob_color_image = bob.io.base.load(bob.io.base.test_utils.datafile('multiple-faces.jpg', 'bob.ip.dlib'))
bob_bounding_box, _ = bob.ip.facedetect.detect_all_faces(bob_color_image)

# detect multiple dlib
dlib_color_image = bob.io.base.load(bob.io.base.test_utils.datafile('multiple-faces.jpg', 'bob.ip.dlib'))
dlib_bounding_box, _ = bob.ip.dlib.FaceDetector().detect_all_faces(dlib_color_image)

# create figure
for b in bob_bounding_box:
    bob.ip.draw.box(bob_color_image, b.topleft, b.size, color=(255, 0, 0))

for b in dlib_bounding_box:
    bob.ip.draw.box(dlib_color_image, b.topleft, b.size, color=(255, 0, 0))

ax = pyplot.subplot(1, 2, 1)
ax.set_title("Dlib")
pyplot.imshow(bob.io.image.to_matplotlib(dlib_color_image).astype("uint8"))
pyplot.axis('off')

ax = pyplot.subplot(1, 2, 2)
ax.set_title("Bob")
pyplot.imshow(bob.io.image.to_matplotlib(bob_color_image).astype("uint8"))
pyplot.axis('off')

