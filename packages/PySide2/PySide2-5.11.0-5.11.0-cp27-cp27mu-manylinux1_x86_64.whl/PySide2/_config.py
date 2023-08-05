built_modules = list(name for name in
    "Core;Gui;Widgets;PrintSupport;Sql;Network;Test;Concurrent;X11Extras;Xml;XmlPatterns;Help;Multimedia;MultimediaWidgets;OpenGL;Positioning;Location;Qml;Quick;QuickWidgets;Scxml;Sensors;TextToSpeech;Charts;Svg;DataVisualization;UiTools;WebChannel;WebEngineCore;WebEngine;WebEngineWidgets;WebSockets;3DCore;3DRender;3DInput;3DLogic;3DAnimation;3DExtras"
    .split(";"))

shiboken_library_soversion = str(5.11)
pyside_library_soversion = str(5.11)

version = "5.11.0"
version_info = (5, 11, 0, "", "")

__build_date__ = '2018-06-11T22:02:21+00:00'




# Timestamp used for snapshot build, which is part of snapshot package version.
__setup_py_package_timestamp__ = ''
