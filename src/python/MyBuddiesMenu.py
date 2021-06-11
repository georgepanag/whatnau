#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Jun 01, 2021 02:52:46 PM EEST  platform: Windows NT

import sys
from PIL import ImageTk,Image

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import MyBuddiesMenu_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = MyBuddiesToplevel (root)
    MyBuddiesMenu_support.init(root, top)
    root.mainloop()

w = None
def create_MyBuddiesToplevel(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_MyBuddiesToplevel(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = MyBuddiesToplevel (w)
    MyBuddiesMenu_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_MyBuddiesToplevel():
    global w
    w.destroy()
    w = None

def show_Buddies(userID,button):
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="pasatempo64",database="whatnau") 
    mycursor = mydb.cursor()
    val=(userID)
    mycursor.execute("select usrname from _user,(select buddy from buddies where buddies.userID=%s) as b where b.buddy=_user.userID",val)#+str(userID))
    myresult = mycursor.fetchall()
           
    rows = len(myresult)

    for i in myresult:
        button.insert("end", i)
    
    

   

class MyBuddiesToplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+660+210")
        top.minsize(148, 1)
        top.maxsize(4804, 1325)
        top.resizable(1,  1)
        top.title("All Contacts")
        top.configure(background="#d9d9d9")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.017, rely=0.111, relheight=0.318
                , relwidth=0.272)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")
        img=Image.open('avatar.png')
        self.Canvas1.image=ImageTk.PhotoImage(img)
        self.Canvas1.create_image(0,0,image=self.Canvas1.image,anchor='nw')



        

        self.SearchInContactsEntry = tk.Entry(top)
        self.SearchInContactsEntry.place(relx=0.267, rely=0.022, height=24
                , relwidth=0.707)
        self.SearchInContactsEntry.configure(background="white")
        self.SearchInContactsEntry.configure(disabledforeground="#a3a3a3")
        self.SearchInContactsEntry.configure(font="TkFixedFont")
        self.SearchInContactsEntry.configure(foreground="#000000")
        self.SearchInContactsEntry.configure(insertbackground="black")
        self.SearchInContactsEntry.configure(readonlybackground="#f0f0f0f0f0f0")

        self.SearchInContactsButton = tk.Button(top)
        self.SearchInContactsButton.place(relx=0.033, rely=0.022, height=33
                , width=136)
        self.SearchInContactsButton.configure(activebackground="#ececec")
        self.SearchInContactsButton.configure(activeforeground="#000000")
        self.SearchInContactsButton.configure(background="#d9d9d9")
        self.SearchInContactsButton.configure(disabledforeground="#a3a3a3")
        self.SearchInContactsButton.configure(foreground="#000000")
        self.SearchInContactsButton.configure(highlightbackground="#d9d9d9")
        self.SearchInContactsButton.configure(highlightcolor="black")
        self.SearchInContactsButton.configure(pady="0")
        self.SearchInContactsButton.configure(text='''Search In Contacts''')

        self.Scrolledlistbox1 = ScrolledListBox(top)
        self.Scrolledlistbox1.place(relx=0.017, rely=0.467, relheight=0.482
                , relwidth=0.642)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(cursor="xterm")
        self.Scrolledlistbox1.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(foreground="black")
        self.Scrolledlistbox1.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="blue")
        self.Scrolledlistbox1.configure(selectforeground="white")
        listOfCompanies=['john5','bobHarley','FredFRaud21']
        show_Buddies(userID,self.Scrolledlistbox1)
        

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Listbox widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def size_(self):
        sz = tk.Listbox.size(self)
        return sz

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





