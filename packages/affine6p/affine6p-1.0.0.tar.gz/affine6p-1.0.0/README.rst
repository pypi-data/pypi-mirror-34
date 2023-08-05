==========
affine6p
==========

The Python affine6p lib is to estimate affine transformation parameters between two sets of 2D points.::

    | x' |   | a  b  p | | x |
    | y' | = | c  d  q | | y |
    | 1  |   | 0  0  1 | | 1 |

.. image:: https://gitlab.com/yoshimoto/affine6p-py/raw/master/affine6p.png
   :alt: Example transformation
   :height: 398px
   :width: 342px

When the sets are more than three points, the lib estimate parameters with the least squares method.

In making this lib, I used a lot of ideas in nudged lib. Ref: https://github.com/axelpale/nudged-py

Install
-----------
Use pip::

    pip install affine6p

Usage
-----------

You have lists of points for the **original** and **converted** of the transformation function to be estimated::

    import affine6p
    origin = [[0,0], [1,0], [0,1], [1,1]]
    convert = [[0,0], [1,0], [0,1], [1,1.1]]
    trans = affine6p.estimate(origin, convert)
    trans.get_matrix()
    # [[1.0, 0.0, 0.0],
    # [0.050000000000000044, 1.05, -0.02499999999999991],
    # [0, 0, 1]]
    affine6p.estimate_error(trans, origin, convert)
    # 0.025000000000000022

When the number of origin is **1**, assume the following relationship::

    a = d = 1 and b = c = 0

When the number of origin is **2**, assume the following relationship as described in *estimate_helmert*.::

    a = d and b = -c 

You can access **Transform class members**.::

    trans.a() # params[0]
    trans.b() # params[1]
    trans.c() # params[2]
    trans.d() # params[3]
    trans.p() # params[4]
    trans.q() # params[5]
    trans.get_matrix() # [[a, b, p], [c, d, q], [0, 0, 1]]
    trans.get_rotation_x() # math.atan2(-b, a)
    trans.get_rotation_y() # math.atan2(c, d)
    trans.get_scale_x() # sqrt(a*a + b*b)
    trans.get_scale_y() # sqrt(c*c + d*d)
    trans.get_scale() # sqrt((scale_x*scale_x+scale_y*scale_y)*0.5)
    trans.get_translation() # [p, q]
    trans.params # [a, b, c, d, p, q]

You can apply **transform** or **rotate** to 2D point or points. The rotate means *p = q = 0*.::

    trans.transform([0, 0])
    trans.transform([[0, 0], [1, 1]])
    point = [0, 0]
    trans.transform_inv(point)
    trans.rotate(point)
    trans.rotate_inv(point)