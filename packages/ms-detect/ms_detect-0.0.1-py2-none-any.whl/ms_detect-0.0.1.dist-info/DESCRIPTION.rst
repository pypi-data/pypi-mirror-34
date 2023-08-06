Info
====
`ai_eye.py 2018-05-25`

`Author: Zhao Mingming <471106585@qq.com>`

`Copyright: This module has been placed in the public domain.`

`version:0.0.7`


Functions:

- `has_closed_eye`: eye's open degree


How To Use This Module
======================
.. image:: funny.gif
   :height: 100px
   :width: 100px
   :alt: funny cat picture
   :align: center

1. when u use pip install ldm==0.0.2

.. code:: python

    from ldm import landmarks
    from ai_eye import has_closed_eye
    from skimage import io
    imagepath="closed_eye/10.jfif"
    img=io.imread(imagepath)
    ldl,helptxt=landmarks(img)
    print helptxt
    for ld in ldl:
        print has_closed_eye(ld)




2. when u use  pip install ldm==0.0.4


.. code:: python

    import  ldm
    from ai_eye import has_closed_eye
    from skimage import io

    imagepath="closed_eye/10.jfif"
    ldmer=ldm.LDM()
    img=io.imread(imagepath)
    ldl,facel,helptxt=ldmer.landmarks(img)
    print helptxt
    for ld in ldl:
        print has_closed_eye(ld)


