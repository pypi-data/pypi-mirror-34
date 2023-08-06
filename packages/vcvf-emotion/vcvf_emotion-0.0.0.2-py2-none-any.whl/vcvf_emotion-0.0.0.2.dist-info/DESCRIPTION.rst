Info
====
`vcvf_emotion 2018-08-01`

`Author: Zhao Mingming <471106585@qq.com>`

`Copyright: This module has been placed in the public domain.`

`version:0.0.0.1`

Classes:
- `face_emotion`: get the face emotion 

Functions:

- `test()`: test function  
- `face_emotion()`:  a class
- `face_emotion.face_emotion(image,rect)`: return the face's happy confidence list 
- `face_emotion.face_emotion_flat(image,rect)`:return the face is or not happy: true or false 

How To Use This Module
======================
.. image:: funny.gif
   :height: 100px
   :width: 100px
   :alt: funny cat picture
   :align: center

1. example code:

.. code:: python
from vcvf_emotion import face_emotion as fe
import cv2

fe0=fe.face_emotion()

fe0.test()
imf=os.path.join(self.site_package,'test.jpg')
print imf
image=cv2.imread(imf)
rect=none
print(fe0.face_emotion(image,rect))
print(fe0.face_emotion_flat(image,rect))


Refresh
========



