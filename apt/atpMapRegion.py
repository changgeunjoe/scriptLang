from tkinter import *
import tkintermapview


class mapWidget(tkintermapview.TkinterMapView):
    def __init__(self, window, regionAddress):
        super().__init__(window, width=800, height=500, corner_radius=0)
        super().pack()
        marker_1 = self.set_address(regionAddress, marker=True)
        self.set_zoom(15) # 0~19 (19 is the highest zoom level) 

