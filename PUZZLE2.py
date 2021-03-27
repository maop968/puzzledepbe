import gi, PUZZLE1, threading, time, sys
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib, GObject



class MyWindow(Gtk.Window):
    logintext = "Please, login with your university card"
    
    def __init__(self):

        css_provider = Gtk.CssProvider()
        css_provider.load_from_path("stylescss/interfacestyle.css")
        context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        wind = Gtk.Window.__init__(self, title="rdfid_gtk.py")
        
        self.ready = True
        
        self.box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.add(self.box)
        self.evbox=Gtk.EventBox()
        self.label=Gtk.Label()
        self.label.set_text(self.logintext)
        self.label.get_style_context().add_class('login_label')
        self.label.set_size_request(400,100)
        self.evbox.add(self.label)


        self.button = Gtk.Button(label="Clear")
        self.button.connect("clicked", self.reset_button)
        self.box.pack_start(self.evbox, True, True, 0)
        self.box.pack_start(self.button, True, True, 0)

        thread = threading.Thread(target=self.get_uid)
        thread.setDaemon(True)
        thread.start()
        
    def get_uid(self):
        
        uid=PUZZLE1.Rfid().read_uid532()
        if uid is not None:
            self.label.get_style_context().remove_class('login_label')
            self.label.get_style_context().add_class('uid_label')
            self.label.set_text("uid: " + uid)
            self.ready=False
        return self.ready

    def example(self):
        GLib.idle_add(self.get_uid)
        
    def create_thread(self):
        thread = threading.Thread(target=self.example)
        thread.start()

    def reset_button(self, widget):
        
        self.label.set_text(self.logintext)
        self.label.get_style_context().add_class('login_label')
        if self.ready is False:
            self.ready = True
            self.create_thread()

if __name__ == "__main__":

    wind = MyWindow()
    wind.show_all()
    Gtk.main()
    wind.connect("destroy", Gtk.main_quit)
    
    
    