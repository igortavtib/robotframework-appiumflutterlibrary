# AppiumFlutterLibrary

![PyPI](https://img.shields.io/pypi/v/robotframework-appiumflutterlibrary?color=blue)
![PyPI - Downloads](https://img.shields.io/pypi/dm/robotframework-appiumflutterlibrary)

AppiumFlutterLibrary is a library for testing Flutter apps with [RobotFramework](https://robotframework.org/).

The project uses the [Flutter Driver](https://flutter.dev/docs/cookbook/testing/integration/introduction) test tools integrated to [Appium](https://appium.io/) as a RobotFramework library.

## Installation

Install using [pip](https://pypi.org/project/robotframework-appiumflutterlibrary/)

```bash
pip install --upgrade robotframework-appiumflutterlibrary
```

## Keyword documentation

AppiumFlutterLibrary has a complete [Keyword Documentation](https://igortavtib.github.io/robotframework-appiumflutterlibrary/AppiumFlutterLibrary.html).

## Flutter setup

 To use AppiumFlutterLibrary you will need to make a simple setup in your Flutter project.
 
 At first, include flutter_driver package to your dev dependencies at *pubspec.yaml*:
 
 ```yaml
 
dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_driver:
    sdk: flutter

 ```
 
 Then go to your *main.dart* file and add **enableFlutterDriverExtension()** to your main function before **runApp()**
 
 ```dart
import 'package:flutter/material.dart';
import 'package:flutter_driver/driver_extension.dart';

void main() {
  enableFlutterDriverExtension();
  runApp(const MyApp());
}

... 
 ```
