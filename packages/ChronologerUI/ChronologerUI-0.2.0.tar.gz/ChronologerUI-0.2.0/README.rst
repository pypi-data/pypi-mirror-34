==============
Chronologer UI
==============

.. figure:: https://bitbucket.org/saaj/chronologer/raw/53816c9dfba77791492438c0f7eb14fc96fae998/source/resource/clui/image/logo/logo240.png
   :alt: Chronologer

Chronologer UI is a `Qooxdoo`_ application written in ECMAScript 5.1.


.. _qooxdoo: http://www.qooxdoo.org/


Building frontend
=================
The frontend requires Qoodxoo 5 SDK which requires Python 2. The SDK can be installed like::

  wget -q -P /tmp https://github.com/qooxdoo/qooxdoo/releases/download/release_5_0_2/qooxdoo-5.0.2-sdk.zip
  mkdir -p /usr/share/javascript/qooxdoo
  unzip -q -d /usr/share/javascript/qooxdoo /tmp/qooxdoo-5.0.2-sdk.zip

To install dependencies::

  ./generate.py load-library

To make a source version and serve it locally::

  ./generate.py && ./generate.py source-server

To make a build version::

  ./generate.py build

Credits
=======
Logo is contributed by `lightypaints`_.


.. _lightypaints: https://www.behance.net/lightypaints

