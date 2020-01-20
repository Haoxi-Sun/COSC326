# Elsie Sun
#
# learn how to update the shape of widgets drawn on the Canvas from:
# https://stackoverflow.com/questions/22835289/how-to-get-tkinter-canvas-to-dynamically-resize-to-window-width/22835732
# 
# The program will display the order n hilbert curve
# n is a number that a client enters 
from tkinter import *

# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        global width, height
        # determine the ratio of old width/height to new width/height
        scale_x = float(event.width)/self.width
        scale_y = float(event.height) / self.height
        self.width = event.width
        self.height = event.height
        width = self.width
        height = self.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all", 0, 0, scale_x, scale_y)

# show a picture of the order n
# n is a number you input
def show():
    if order_text.get() != '':
        # before drawing new curve,
        # clear the canvas.
        canvas.delete(ALL)
        order_num = int(order_text.get())
        global seg_x_length, seg_y_length
        seg_x_length = (width - 2 * margin) / (2 ** order_num - 1)
        seg_y_length = (height - 2 * margin) / (2 ** order_num - 1)
        hilbert_curve(order_num, 1, 10, 10)


def hilbert_curve(order, shape, pos_x, pos_y):
    # stop this recursive
    if order == 0:
        return

    # the starting position in order-1 curve
    pos_x_change = pos_x + 2 ** (order - 1) * seg_x_length
    pos_y_change = pos_y + 2 ** (order - 1) * seg_y_length

    # the bias of line in create_line function
    half_bias_start_x = (2 ** (order - 1) - 1) * seg_x_length
    half_bias_end_x = 2 ** (order - 1) * seg_x_length
    bias_x = (2 ** order - 1) * seg_x_length

    half_bias_start_y = (2 ** (order - 1) - 1) * seg_y_length
    half_bias_end_y = 2 ** (order - 1) * seg_y_length
    bias_y = (2 ** order - 1) * seg_y_length

    # define direction of up, left, down and right
    # as 1, 2, 3, 4 respectively
    # suppose the direction of order curve is up
    if shape == 1:
        # first plot the left order-1 curve with the
        # same starting point as order curve
        hilbert_curve(order-1, 2, pos_x, pos_y)
        # just draw the joint line
        canvas.create_line(pos_x, pos_y + half_bias_start_y, pos_x, pos_y + half_bias_end_y)
        # second plot the top order-1 curve with the
        # same starting x position and different y position
        hilbert_curve(order-1, 1, pos_x, pos_y_change)
        # just draw the joint line
        canvas.create_line(pos_x + half_bias_start_x, pos_y + half_bias_end_y,
                           pos_x + half_bias_end_x, pos_y + half_bias_end_y)
        # third plot the top order-1 curve
        hilbert_curve(order-1, 1, pos_x_change, pos_y_change)
        # just draw the joint line
        canvas.create_line(pos_x + bias_x, pos_y + half_bias_start_y, pos_x + bias_x, pos_y + half_bias_end_y)
        # last plot the right order-1 curve
        hilbert_curve(order-1, 4, pos_x_change, pos_y)
    
    # suppose the direction of order curve is left
    elif shape == 2:
        # first plot the up order-1 curve
        hilbert_curve(order - 1, 1, pos_x, pos_y)
        canvas.create_line(pos_x + half_bias_start_x, pos_y, pos_x + half_bias_end_x, pos_y)
        # canvas.create_line
        # second plot the left order-1 curve
        hilbert_curve(order - 1, 2, pos_x_change, pos_y)
        canvas.create_line(pos_x + half_bias_end_x, pos_y + half_bias_start_y,
                           pos_x + half_bias_end_x, pos_y + half_bias_end_y)
        # third plot the left order-1 curve
        hilbert_curve(order - 1, 2, pos_x_change, pos_y_change)
        canvas.create_line(pos_x + half_bias_start_x, pos_y + bias_y, pos_x + half_bias_end_x, pos_y + bias_y)
        # last plot the down order-1 curve
        hilbert_curve(order - 1, 3, pos_x, pos_y_change)
    # suppose the direction of order curve is down
    elif shape == 3:
        # first plot the left order-1 curve
        hilbert_curve(order - 1, 2, pos_x, pos_y_change)
        canvas.create_line(pos_x, pos_y + half_bias_start_y, pos_x, pos_y + half_bias_end_y)
        # second plot the top order-1 curve
        hilbert_curve(order - 1, 3, pos_x, pos_y)
        canvas.create_line(pos_x + half_bias_start_x, pos_y + half_bias_start_y,
                           pos_x + half_bias_end_x, pos_y + half_bias_start_y)
        # third plot the top order-1 curve
        hilbert_curve(order - 1, 3, pos_x_change, pos_y)
        canvas.create_line(pos_x + bias_x, pos_y + half_bias_start_y, pos_x + bias_x, pos_y + half_bias_end_y)
        # last plot the right order-1 curve
        hilbert_curve(order - 1, 4, pos_x_change, pos_y_change)
    # suppose the direction of order curve is right
    else:
        # first plot the left order-1 curve
        hilbert_curve(order - 1, 1, pos_x_change, pos_y)
        canvas.create_line(pos_x + half_bias_start_x, pos_y, pos_x + half_bias_end_x, pos_y)
        # second plot the top order-1 curve
        hilbert_curve(order - 1, 4, pos_x, pos_y)
        canvas.create_line(pos_x + half_bias_start_x, pos_y + half_bias_start_y,
                           pos_x + half_bias_start_x, pos_y + half_bias_end_y)
        # third plot the top order-1 curve
        hilbert_curve(order - 1, 4, pos_x, pos_y_change)
        canvas.create_line(pos_x + half_bias_start_x, pos_y + bias_y, pos_x + half_bias_end_x, pos_y + bias_y)
        # last plot the right order-1 curve
        hilbert_curve(order - 1, 3, pos_x_change, pos_y_change)


# width and height of the display canvas
width = height = 600

# margin between curve border and canvas border
margin = 10

seg_x_length = 0
seg_y_length = 0

window = Tk()
window.title('Hilbert Curve Plotting Tool')

frame = Frame(window)
frame.pack()
label = Label(frame, text='Please input order')
label.pack(side=LEFT)
order_text = StringVar()
entry = Entry(frame, textvariable=order_text, width=10)
entry.pack(side=LEFT)
button = Button(frame, text='Show', command=show)
button.pack(side=LEFT)

frame = Frame(window)
frame.pack(fill=BOTH, expand=YES)
canvas = ResizingCanvas(frame, width=width, height=height, bg="white", highlightthickness=0)
canvas.pack(fill=BOTH, expand=YES)
window.mainloop()
