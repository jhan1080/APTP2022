try:
    import Tkinter as tk
except:
    import tkinter as tk


class SampleApp(tk.Tk):
    def __init__(win):
        tk.Tk.__init__(win)
        win._frame = None
        win.switch_frame(StartPage)

    def switch_frame(win, frame_class):
        new_frame = frame_class(win)
        if win._frame is not None:
            win._frame.destroy()
        win._frame = new_frame
        win._frame.pack()


class StartPage(tk.Frame):
    def __init__(win, master):
        tk.Frame.__init__(win, master)
        win.width=450
        win.height=750
        background1 = tk.PhotoImage(file="background1.png")
        tk.Button(win, text="Go to page one",
                  command=lambda: master.switch_frame(PageOne)).pack()
        tk.Button(win, text="Go to page two",
                  command=lambda: master.switch_frame(PageTwo)).pack()


class PageOne(tk.Frame):
    def __init__(win, master):
        tk.Frame.__init__(win, master)
        tk.Frame.configure(win, bg='blue')
        tk.Label(win, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(win, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()


class PageTwo(tk.Frame):
    def __init__(win, master):
        tk.Frame.__init__(win, master)
        tk.Frame.configure(win, bg='red')
        tk.Label(win, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(win, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()



app = SampleApp()
app.mainloop()