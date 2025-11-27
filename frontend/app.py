import gi
import subprocess
from gi.repository import Gtk, GLib

gi.require_version('Gtk', '4.0')

class TweaksApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id = "com.jeremygamer13.JbuntuTweaks")

    def do_activate(self):
        builder = Gtk.Builder.new_from_file("menu.glade")

        self.window = builder.get_object("window")
        self.button = builder.get_object("button")
        
        self.window.set_application(self)
        self.window.present()

