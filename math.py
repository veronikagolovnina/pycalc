

def iCalc(source, side):
    storeObj = Frame(source, borderwidth = 1, bg = "powder blue")
    storeObj.pack(side=side, expand = YES, fill=BOTH)
    return storeObj

def button (source, size, text, command = None) :
    storeObj = Button(source, text = text, command = None)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')