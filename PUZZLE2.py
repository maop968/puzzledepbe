import gi, PUZZLE1, threading
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="rdfid_gtk.py")
        self.connect("destroy", Gtk.main_quit)
        self.label=Gtk.Label()
        self.label.set_text("pass your card")
        self.add(self.label)

        "creamos un thread"
        thread = threading.Thread(target=self.getUid)
        thread.setDaemon(True)
        thread.start()
        # self.button = Gtk.Button(label="Click Here")
        # self.button.connect("clicked", self.on_button_clicked)
        # self.add(self.button)
        self.show_all()
        Gtk.main()

    def getUid(self):
        Rf = PUZZLE1.Rfid()
        uid=Rf.read_uid532()
        self.label.set_text(uid)

wind = MyWindow()