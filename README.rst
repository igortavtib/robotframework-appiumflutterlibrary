AppiumFlutterLibrary
====================

.. image:: https://img.shields.io/pypi/v/robotframework-appiumflutterlibrary?color=blue
    :target: https://pypi.python.org/pypi/robotframework-appiumflutterlibrary/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/robotframework-appiumflutterlibrary
    :target: https://pypi.python.org/pypi/robotframework-appiumflutterlibrary/
    :alt: Number of PyPI downloads

`AppiumFlutterLibrary`_ is a library for testing Flutter apps with `Robot Framework`_.

The project uses the `FlutterDriver`_ test tools integrated to `Appium`_ as a `Robot Framework`_ library.

Installation
------------

The recommended installation method is using
`pip <http://pip-installer.org>`__::

    pip install --upgrade robotframework-appiumflutterlibrary


See `Robot Framework installation instructions`_ for detailed information
about installing Python and Robot Framework itself.

Keyword documentation
---------------------

AppiumFlutterLibrary has a complete `Keyword Documentation`_.

Flutter setup
-------------

To use AppiumFlutterLibrary you will need to make a simple setup in your Flutter project.
 
At first, include flutter_driver package to your dev dependencies at *pubspec.yaml*:
 
.. code:: yaml

 dev_dependencies:
   flutter_test:
     sdk: flutter
   flutter_driver:
     sdk: flutter


Then go to your `main.dart` file and add enableFlutterDriverExtension() to your main function before runApp()
 
.. code:: dart

  import 'package:flutter/material.dart';
  import 'package:flutter_driver/driver_extension.dart';

  void main() {
    enableFlutterDriverExtension();
    runApp(const MyApp());
  }

  ... 


.. _AppiumFlutterLibrary: https://github.com/igortavtib/robotframework-appiumflutterlibrary
.. _FlutterDriver: https://flutter.dev/docs/cookbook/testing/integration/introduction
.. _Robot Framework: https://robotframework.org
.. _Appium: https://appium.io/
.. _Keyword Documentation: http://igortavtib.github.io/robotframework-appiumflutterlibrary/AppiumFlutterLibrary.html
.. _PyPI: https://pypi.org/project/robotframework-appiumflutterlibrary/
.. _Robot Framework installation instructions: https://github.com/robotframework/robotframework/blob/master/INSTALL.rst
.. _Appium Driver Setup Guide: http://appium.io/docs/en/about-appium/getting-started/?lang=en
.. _sample project: https://github.com/serhatbolsu/robotframework-appium-sample
