Tomorrow
========

Magic decorator syntax for asynchronous code in Python

Installation
------------

LightConfig is conveniently available via pip:

::

    pip install lightconfig

Usage
-----

The LightConfig library enables you to get a easy way to create or read 
config file.


sample
-----------------

.. code:: python

    from lightconfig import LightConfig
    cfg = LightConfig("config.ini")
    cfg.section1.option1 = "value1"
    print(cfg.section1.option1)  #expect 'value1'


