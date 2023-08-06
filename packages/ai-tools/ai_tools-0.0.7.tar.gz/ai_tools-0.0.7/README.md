Info
====
`ai_tool 2018-05-25`

`Author: Zhao Mingming <471106585@qq.com>`

`Copyright: This module has been placed in the public domain.`

`version:0.0.6`


Functions:

- `draw_curve`: draw a curve in a image and return the image 
- `image2text`: translate a image to be text style
- `save2server`: save a image on the local server 
- `image2bw`:  turn a gray image to be a binary weights image

How To Use This Module
======================
.. image:: funny.gif
   :height: 100px
   :width: 100px
   :alt: funny cat picture
   :align: center

1. example code:


.. code:: python

    
    x=np.array([-0.2,0.3,0.4,0.5])
    y=np.array([0.2,0.4,0.1,-0.4])
    norm(x,np.array([0,500]))

    img=draw_curve(x,y)
    img=draw_curve(x,y,title='my title',xlabel='my x label',ylabel='my y lable')
    
    img=cv2.imread('../examples/faces/2007_007763.jpg')
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # img2bw
    img_bw= image2bw(img_gray)


    print img.shape
    image2text(img,(80,40))
    image2text(img,(80,40))



Refresh
========
20180531
