import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb


LARGE_FONT=("Verdana",12)

def callback():
	if mb.askyesno('Jura?', 'Tem certeza que você acha o dudu melhor no top?'):
		mb.showwarning('Yes', 'Você só pode ser o Dudu para achar isso, ou ser o namorado do dudu! Responda de novo')
	else:
		mb.showinfo('No', 'Voltou ao seu juízo')
def resposta():
	mb.showerror("Resposta", "Desculpe, mas o Igor é main na jungle! Você perdeu! Comece de novo!")
	quit()
def resposta2():
	mb.showerror("Resposta", "Desculpe, mas o Dudu é noob! Você perdeu! Comece de novo!")
	quit()
def resposta3():
	mb.showerror("Resposta", "Desculpe, mas o Igor carrega o Dudu de ADC! Você perdeu! Comece de novo!")
	quit()
def resposta4():
	mb.showerror("Você é um brincalhão", "Desculpe, mas nunca em toda a história do universo que o dudu vai conseguir superar o Igor de Sup! O Igor sempre carrega o adc noob do dudu!")
	quit()
	
def fimdejogo():
	mb.showinfo('Vencedor', 'Parabéns, você venceu o jogo! Realmente você deixou de ser um desiludido e assumiu a verdade: O Igor está anos-luz na frente do Dudu')
	quit()
	
	

class MelhorNoLol(tk.Tk):
	
	def __init__(self,*args,**kwargs):
		
		tk.Tk.__init__(self,*args,**kwargs)
		
		tk.Tk.iconbitmap(self,default="dragon5.ico")
		tk.Tk.wm_title(self,"Quem é melhor no LOL client")
		
		container=tk.Frame(self)
		container.pack(side="top",fill="both",expand=True)
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)
		
		menubar=tk.Menu(container)
		filemenu=tk.Menu(menubar,tearoff=0)
		filemenu.add_command(label="Dudu fraco",command=lambda:popupmsg("Not supported just yet!"))
		filemenu.add_separator()
		filemenu.add_command(label="Dudu não sabe jogar LOL",command=quit)
		menubar.add_cascade(label="File",menu=filemenu)
		
		tk.Tk.config(self,menu=menubar)
		
		self.frames={}
		
		for F in (StartPage,PageOne,PageTwo,PageThree,PageFour):
			
			frame = F(container,self)
			
			self.frames[F]=frame
			
			frame.grid(row=0,column=0,sticky="nsew")

		self.show_frame(StartPage)
		
	def show_frame(self,cont):
		
		frame=self.frames[cont]
		frame.tkraise()
		
class StartPage(tk.Frame):
	
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		#photo1=PhotoImage(file="cava2.gif")
		label=ttk.Label(self,text=("O Igor joga mais que o dudu no top?"), font=LARGE_FONT)
		label.pack(pady=10,padx=10)
		
		button1 = ttk.Button(self,text="Sim",command=lambda:controller.show_frame(PageOne))
		button1.pack()
		
		button2 = ttk.Button(self,text="Não",command = callback)
		button2.pack()
		

		
class PageOne(tk.Frame):
	
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		#photo1=PhotoImage(file="cava2.gif")
		label=ttk.Label(self,text=("O Igor joga mais que o dudu na jungle?"), font=LARGE_FONT)
		label.pack(pady=10,padx=10)
		

		
		button1 = ttk.Button(self,text="Sim",command=lambda:controller.show_frame(PageTwo))
		button1.pack()
		
		button2 = ttk.Button(self,text="Não",command = resposta)
		button2.pack()		

		
		
class PageTwo(tk.Frame):
	
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		#photo1=PhotoImage(file="cava2.gif")
		label=ttk.Label(self,text=("O Igor joga mais que o dudu no mid?"), font=LARGE_FONT)
		label.pack(pady=10,padx=10)
		

		
		button1 = ttk.Button(self,text="Sim",command=lambda:controller.show_frame(PageThree))
		button1.pack()
		
		button2 = ttk.Button(self,text="Não",command = resposta2)
		button2.pack()

class PageThree(tk.Frame):
	
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		#photo1=PhotoImage(file="cava2.gif")
		label=ttk.Label(self,text=("O Igor joga mais que o dudu de adc?"), font=LARGE_FONT)
		label.pack(pady=10,padx=10)
		

		
		button1 = ttk.Button(self,text="Sim",command=lambda:controller.show_frame(PageFour))
		button1.pack()
		
		button2 = ttk.Button(self,text="Não",command = resposta3)
		button2.pack()		

class PageFour(tk.Frame):
	
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		#photo1=PhotoImage(file="cava2.gif")
		label=ttk.Label(self,text=("O Igor joga mais que o dudu de sup?"), font=LARGE_FONT)
		label.pack(pady=10,padx=10)
		

		
		button1 = ttk.Button(self,text="Sim",command=fimdejogo)
		button1.pack()
		
		button2 = ttk.Button(self,text="Não",command = resposta4)
		button2.pack()	
		

		

		
app =MelhorNoLol()
app.geometry("400x200")
app.mainloop()