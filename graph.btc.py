import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk

import urllib
import json

import pandas as pd
import numpy as np

from matplotlib import pyplot as plt

LARGE_FONT=("Verdana",12)
style.use("ggplot")

f= Figure()
a=f.add_subplot(111)


def animate(i):
	pd.options.mode.chained_assignment = None
	datalink="https://api.bitfinex.com/v1/trades/BTCUSD?limit_trades=5000"
	data=urllib.request.urlopen(datalink)
	data=data.read().decode("utf-8")
	data=json.loads(data)
	data=pd.DataFrame(data)
	
	buys=data[(data["type"]=="buy")] # changed to match the api response bid is now buy 
	buys["datestamp"]=np.array(buys["timestamp"]).astype("datetime64[s]")
	buyDates=(buys["datestamp"]).tolist()
	
	sells=data[(data["type"]=="sell")] # changed to match the api response bid is now buy 
	sells["datestamp"]=np.array(sells["timestamp"]).astype("datetime64[s]")
	sellDates=(sells["datestamp"]).tolist()
	
	
	a.clear()
	
	a.plot_date(buyDates,buys["price"],"#00A3E0",label="buys")
	a.plot_date(sellDates,sells["price"],"#183A54",label="sells")
	
	a.legend(bbox_to_anchor=(0,1.02,1,.102),loc=3,ncol=2,borderaxespad=0)
	
	title="BTCUSD Prices\nLast Price: " +str(data["price"][0])
	a.set_title(title)
	
	
	

class SeaofBTCapp(tk.Tk):
	
	def __init__(self,*args,**kwargs):
		
		tk.Tk.__init__(self,*args,**kwargs)
		
		tk.Tk.iconbitmap(self,default="dragon5.ico")
		tk.Tk.wm_title(self,"Dragon Claw client")
		
		container=tk.Frame(self)
		container.pack(side="top",fill="both",expand=True)
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)
		
		menubar=tk.Menu(container)
		filemenu=tk.Menu(menubar,tearoff=0)
		filemenu.add_command(label="Save settings",command=lambda:popupmsg("Not supported just yet!"))
		filemenu.add_separator()
		filemenu.add_command(label="Exit",command=quit)
		menubar.add_cascade(label="File",menu=filemenu)
		
		tk.Tk.config(self,menu=menubar)
		
		self.frames={}
		
		for F in (StartPage,PageOne,BTCE_page):
			
			frame = F(container,self)
			
			self.frames[F]=frame
			
			frame.grid(row=0,column=0,sticky="nsew")

		self.show_frame(StartPage)
		
	def show_frame(self,cont):
		
		frame=self.frames[cont]
		frame.tkraise()
		
def qf(param):
	print(param)

class StartPage(tk.Frame):
	
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label=ttk.Label(self,text=("ALPHA Bitcoin trading application - use at your own risk. There is no warranty"), font=LARGE_FONT)
		label.pack(pady=10,padx=10)
		
		button1 = ttk.Button(self,text="Agree",command=lambda:controller.show_frame(BTCE_page))
		button1.pack()
		
		button2 = ttk.Button(self,text="Disagree",command = quit)
		button2.pack()
		
		
		
class PageOne(tk.Frame):
	
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label=ttk.Label(self,text="Page 1", font=LARGE_FONT)
		label.pack(pady=10,padx=10)
		button1 = ttk.Button(self,text="Back to Home",command=lambda:controller.show_frame(StartPage))
		button1.pack()
		

		
class BTCE_page(tk.Frame):
	
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label=ttk.Label(self,text="Graph Page", font=LARGE_FONT)
		label.pack(pady=10,padx=10)
		button1 = ttk.Button(self,text="Back to Home",command=lambda:controller.show_frame(StartPage))
		button1.pack()
		

		
		canvas=FigureCanvasTkAgg(f,self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand = True)
		
		toolbar=NavigationToolbar2TkAgg(canvas,self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand = True)
		
		
		
app =SeaofBTCapp()
app.geometry("1280x720")
ani=animation.FuncAnimation(f,animate,interval=5000)
app.mainloop()



		
	

