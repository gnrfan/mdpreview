#!/usr/bin/env python

import sys
import gtk
import gtkmozembed
import markdown2

class MarkdownPreviewer(object):

    DEFAULT_WINDOW_WIDTH = 700
    DEFAULT_WINDOW_HEIGHT = 550

    def __init__(self):
        # Parameter checking
        self.check_params()
        # Building GTK+ Window with embedded Gecko
        self.moz = gtkmozembed.MozEmbed()
        win = gtk.Window()
        win.add(self.moz)
        # Setting the title
        win.set_title(self.get_filename())
        # Setting a proper size for the window
        win.set_size_request(
            self.DEFAULT_WINDOW_WIDTH, 
            self.DEFAULT_WINDOW_HEIGHT)
        # Centering the window
        win.set_position(gtk.WIN_POS_CENTER)
        # Connecting a signal needed to quit the application
        # when the window is closed
        win.connect("destroy", gtk.main_quit)
        # Showing the window
        win.show_all()
        # Generating HTML
        data = self.generate_html()
        # Rendering the generated HTML
        self.moz.render_data(data, long(len(data)), 'file:///', 'text/html')

    def check_params(self):
        # Only one parameter must be passed from the command line: 
        # the path to the Markdown file.
        if len(sys.argv) != 2:
            self.print_usage()
            sys.exit()

    def print_usage(self):
        # Print usage information
        print "Usage: %s file.md" % self.get_scriptname()

    def get_filepath(self):
        return sys.argv[1]

    def get_filename(self):
        filepath = self.get_filepath()
        return filepath.split('/')[-1]

    def get_scriptname(self):
        return sys.argv[0].split('/')[-1]

    def generate_html(self):
        filepath = self.get_filepath()
        markdown_as_html = markdown2.markdown(open(filepath, "r").read())
        return '\n'.join([
            '<html>',
            '<head>',
            '<title>%s</title>' % (self.get_filename()),
            '<style type="text/css">',
            '  body { font-family: Arial, Helvetica, Sans-Serif }',
            '  pre { ',
            '     border: solid 1px #aaaaaa; ',
            '     background-color: #eeeeee; ',
            '     padding: 10px; ',
            '  }',
            '  code { font-family: Consolas, "DejaVu Sans Mono", "Droid Sans Mono", Courier, "Courier New"; }',
            '</style>',
            '<body>',
            markdown_as_html,
            '</body>',
            '</html>'
        ])

if __name__ == '__main__':
  MarkdownPreviewer()
  gtk.main()
