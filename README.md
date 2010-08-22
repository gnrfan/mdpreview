MDPreview
=========

MDPreview is a Markdown previewer for the GNOME desktop writting using PyGTK and GtkMozEmbed. It is a very short Python script but a very handy aid specially for people hacking on stuff from sites like GitHub and using Linux on the desktop.

Installation
============

In Ubuntu you can install MDPreview like this:

    apt-get install python-gtk2 python-gtkmozembed python-markdown

Then, simply copy mdpreview.py to /usr/bin/mdpreview:

    sudo cp src/mdpreview.py /usr/bin/mdpreview

Using MDPreview
===============

From the command line simple call mdpreview with the name or full path to the Markdown file you want to preview like this:

    $ mdpreview README.md

Using Nautilus (GNOME's file manager) you can right-click on a file and choose to open it with MDPreview. Just browse to the location of the mdpreview script or enter /usr/bin/mdpreview as a custom command.

Screenshot
==========

![Screenshot of MDPreview](http://github.com/gnrfan/mdpreview/raw/master/media/mdpreview-01.png "MDPreview")

TODO
====

* Add an icon!!!
* Calculate window size based on the current screen size
* Maximize the window if the -m or --maximize-window parameter is used
* Use a custom stylesheet if the -s or --custom-stylesheet is used 

Ideas, patches and bug reports are welcomed. Please file an issue.

BSD License
===========

Copyright (c) 2010 Antonio Ognio
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. Neither the name of copyright holders nor the names of its
   contributors may be used to endorse or promote products derived
   from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL COPYRIGHT HOLDERS OR CONTRIBUTORS
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
