import turtle

_t_=turtle.Turtle()

def reset():
    _t_.reset()

def penup():
    _t_.penup()

def pendown():
    _t_.pendown()

def speed(*args,**kwargs):
    _t_.speed(*args,**kwargs)

def pencolor(*args,**kwargs):
    _t_.pencolor(*args,**kwargs)

def forward(*args,**kwargs):
    _t_.forward(*args,**kwargs)

def backward(*args,**kwargs):
    _t_.backward(*args,**kwargs)

def right(*args,**kwargs):
    _t_.right(*args,**kwargs)

def left(*args,**kwargs):
    _t_.left(*args,**kwargs)

def goto(*args,**kwargs):
    _t_.goto(*args,**kwargs)

def done(*args,**kwargs):
    try:
        print("Interrupt Kernel to continue...",end="")
        turtle.mainloop()
    except KeyboardInterrupt:
        print("done.")

