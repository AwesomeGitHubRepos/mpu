mpu.units
=========

Module contents
---------------

.. automodule:: mpu.units
    :members:
    :undoc-members:
    :show-inheritance:

Allowed operations with Money
-----------------------------
Here you can see which operations are allowed by two Money objects of
currencies (A and B):

+---------+----------------------+----------+---------+---------------+
| Money A | Operator             | Money A  | Money B | int, Fraction |
+=========+======================+==========+=========+===============+
|         | `+` , `-`            | Money A  | N/A     | N/A           |
+---------+----------------------+----------+---------+---------------+
|         | `*`                  | N/A      | N/A     | Money A       |
+---------+----------------------+----------+---------+---------------+
|         | `/`                  | N/A      | N/A     | N/A           |
+---------+----------------------+----------+---------+---------------+
|         | `//`                 | Fraction | N/A     | Money A       |
+---------+----------------------+----------+---------+---------------+
|         | `>`, `>=`, `<`, `<=` | Bool     | N/A     | N/A           |
+---------+----------------------+----------+---------+---------------+
|         | ==                   | Bool     | False   | False         |
+---------+----------------------+----------+---------+---------------+
