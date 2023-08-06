
python-dispatch
===============

Lightweight event handling for Python


.. image:: https://travis-ci.org/nocarryr/python-dispatch.svg?branch=master
   :target: https://travis-ci.org/nocarryr/python-dispatch
   :alt: Build Status

.. image:: https://coveralls.io/repos/github/nocarryr/python-dispatch/badge.svg?branch=master
   :target: https://coveralls.io/github/nocarryr/python-dispatch?branch=master
   :alt: Coverage Status

.. image:: https://badge.fury.io/py/python-dispatch.svg
   :target: https://badge.fury.io/py/python-dispatch
   :alt: PyPI version

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/nocarryr/python-dispatch/master/LICENSE.txt
   :alt: GitHub license


Description
-----------

This is an implementation of the "Observer Pattern" with inspiration from the
`Kivy <kivy.org>`_ framework. Many of the features though are intentionally
stripped down and more generalized. The goal is to have a simple drop-in
library with no dependencies that stays out of the programmer's way.

Installation
------------

.. code-block::

   pip install python-dispatch

Links
-----

.. list-table::
   :header-rows: 1

   * - 
     - 
   * - Project Home
     - https://github.com/nocarryr/python-dispatch
   * - PyPI
     - https://pypi.python.org/pypi/python-dispatch
   * - Documentation
     - https://nocarryr.github.io/python-dispatch


Usage
-----

Events
^^^^^^

.. code-block:: python

   from pydispatch import Dispatcher

   class MyEmitter(Dispatcher):
       # Events are defined in classes and subclasses with the '_events_' attribute
       _events_ = ['on_state', 'new_data']
       def do_some_stuff(self):
           # do stuff that makes new data
           data = self.get_some_data()
           # Then emit the change with optional positional and keyword arguments
           self.emit('new_data', data=data)

   # An observer - could inherit from Dispatcher or any other class
   class MyListener(object):
       def on_new_data(self, *args, **kwargs):
           data = kwargs.get('data')
           print('I got data: {}'.format(data))
       def on_emitter_state(self, *args, **kwargs):
           print('emitter state changed')

   emitter = MyEmitter()
   listener = MyListener()

   emitter.bind(on_state=listener.on_emitter_state)
   emitter.bind(new_data=listener.on_new_data)

   emitter.do_some_stuff()
   # >>> I got data: ...

   emitter.emit('on_state')
   # >>> emitter state changed

Properties
^^^^^^^^^^

.. code-block:: python

   from pydispatch import Dispatcher, Property

   class MyEmitter(Dispatcher):
       # Property objects are defined and named at the class level.
       # They will become instance attributes that will emit events when their values change
       name = Property()
       value = Property()

   class MyListener(object):
       def on_name(self, instance, value, **kwargs):
           print('emitter name is {}'.format(value))
       def on_value(self, instance, value, **kwargs):
           print('emitter value is {}'.format(value))

   emitter = MyEmitter()
   listener = MyListener()

   emitter.bind(name=listener.on_name, value=listener.on_value)

   emitter.name = 'foo'
   # >>> emitter name is foo
   emitter.value = 42
   # >>> emitter value is 42
