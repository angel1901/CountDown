from tkinter import *
import time
from datetime import datetime
from tkinter import filedialog
import xlrd


class Digital_clock():
    def __init__(self):
        input_msg_1 = ""
        self.input_hor_1 = ["18:01", "08:15", "10:00", "11:45"]
        self.ventana = Tk()
        self.ventana.geometry("720x480")
        self.ventana.title('Reloj')
        self.texto = Label(self.ventana, text="Ingrese el Archivo que desea subir", font=('Lato Bold', 15))
        self.texto.grid(column=0, row=0, sticky=W, padx=5, pady=5)
        self.mensajes = {}
        self.input_msg_1 = StringVar()
        self.r1_v = StringVar()
        self.actual = ""
        
        def leer_archivo():
            ruta_file=filedialog.askopenfilename(title = "Select file")
            importar_archivo(ruta_file)
            
        def importar_archivo(ruta):
            wb = xlrd.open_workbook(ruta) 
            #wb = xlrd.open_workbook('C:/Users/Angel Ramirez/Downloads/vigilia2.xlsx') 
            hoja = wb.sheet_by_index(0) 
            for x in range(hoja.nrows):
                val_x = hoja.cell_value(x, 0)
                val_y = hoja.cell_value(x, 1)
                self.mensajes[val_x] = val_y
            
        # def horarios():
        #     input_dara = self.r1_v.get()
        #     if input_dara == 0:
        #         print(str(self.input_hor_1))
        #         self.horario_0.configure(text="Domingo")    
        #         self.ventana.update()
        #         self.ventana.mainloop()
        #     elif input_dara == 1:
        #         self.horario_1.configure(text="Otro")    
        #         self.ventana.update()
        #         self.ventana.mainloop()
        #     print(input_dara)
            
        self.horario_1 = Button(text="Importar Archivo",bg="salmon",command=leer_archivo)
        self.horario_1.grid(column=0, row=1, sticky=W, padx=5, pady=5)
        self.horario_1 = Button(text="Crear Reloj",bg="salmon",command=self.crear_ventana_reloj)
        self.horario_1.grid(column=0, row=2, sticky=W, padx=5, pady=5)

        # self.label_mensaje = Label(self.ventana, text="Hora de Inicio", font=('Lato', 12))
        # self.label_mensaje.grid(column=0, row=4, sticky=W, padx=5, pady=5)
        # r1 = Radiobutton(self.ventana, text='Domingo', value='0', variable=self.r1_v, command=horarios)
        # r1.grid(row=5,column=0, sticky=W) 
        # r2 = Radiobutton(self.ventana, text='Otro', value='1', variable=self.r1_v, command=horarios)
        # r2.grid(row=7,column=0, sticky=W)

        # self.msg_1 = Entry(self.ventana, width="30", textvariable=self.input_msg_1)
        # self.msg_1.grid(column=1, row=2, sticky=W, padx=5, pady=5)

        self.horario_0 = Label(self.ventana, text="", font=('Lato', 12))
        self.horario_0.grid(column=0, row=6, sticky=W, padx=5, pady=5)
        self.horario_1 = Label(self.ventana, text="", font=('Lato', 12))
        self.horario_1.grid(column=0, row=8, sticky=W, padx=5, pady=5)

        self.label_mensaje = Label(self.ventana, text="Mensaje Personalizado", font=('Lato', 12))
        self.label_mensaje.grid(column=1, row=0, sticky=W, padx=5, pady=5)
        self.msg_1 = Entry(self.ventana, width="30", textvariable=self.input_msg_1)
        self.msg_1.grid(column=1, row=1, sticky=W, padx=5, pady=5)
        self.horario_1 = Button(text="Enviar Mensaje",bg="salmon",command=self.envio_personalizado)
        self.horario_1.grid(column=1, row=2, sticky=W, padx=5, pady=5)
        self.horario_1 = Button(text="Ocultar Mensaje",bg="salmon",command=self.clearMsg)
        self.horario_1.grid(column=1, row=3, sticky=W, padx=5, pady=5)

        # self.msg_1.grid(column=0, row=2, sticky=W)
        # username_entry = Entry(self.ventana, width="30", textvariable=input_hor_1)
        # username_entry.grid(column=1, row=2, sticky=W, padx=5, pady=5)
        self.ventana.mainloop()


    def crear_ventana_reloj(self):
        self.ventana_full = Toplevel()
        self.ventana_full.attributes("-fullscreen", True)
        self.ventana_full.title('Reloj')
        self.ventana_full.configure(bg='black')
        self.ventana_full.columnconfigure(0, weight=1)
        self.ventana_full.rowconfigure(0, weight=2)
        self.ventana_full.rowconfigure(1, weight=5)
        self.ventana_full.rowconfigure(2, weight=2)
        self.hora = Label(self.ventana_full, text=str(time.strftime('%H:%M:%S')), font=('Lato', 150), fg='white')
        self.hora.grid(column=0, row=0, sticky=N, padx=5, pady=5)
        self.hora.config(bg="black")
        self.msg = Label(self.ventana_full, text="", font=('Lato', 120), fg='white', wraplength=1900)
        self.msg.grid(column=0, row=1, sticky=EW, padx=5, pady=5)
        self.msg.config(bg="black")
        self.countdown = Label(self.ventana_full, text=str(time.strftime('%H:%M:%S')), font=('Lato', 150), fg='white')
        self.countdown.grid(column=0, row=2, sticky=S, padx=5, pady=5)
        self.countdown.config(bg="black")
        self.update_reloj()
        self.update_msg()
        self.ventana_full.mainloop()
    
    def update_reloj(self):
        self.ahora = time.strftime('%H:%M:%S')
        for z in self.input_hor_1:
            if self.ahora > z:
                self.start = 0
            else:
                self.start = 1

        self.hora.configure(text=self.ahora)    
        self.ventana_full.after(1000, self.update_reloj)
        self.ventana_full.update()
        
    
    def update_msg(self):
        print("Actualizacion Imagen")
        print(self.ahora)
        hora = self.ahora
        self.actual = ""
        for x in self.mensajes:
            self.destello()
            num_of_secs = int(self.mensajes[x] * 60)
            self.msg.configure(text=x)
            self.actual = x
            while num_of_secs:
                m, s = divmod(num_of_secs, 60)
                h = 0
                if m >60:
                    h,m = divmod(m, 60)
                self.min_sec_format = '{:02d}:{:02d}:{:02d}'.format(h, m, s)
                self.countdown.configure(text=self.min_sec_format)    
                self.ventana_full.update()
                self.ventana_full.configure(bg='black')
                self.hora.config(bg="black")
                self.msg.config(bg="black")
                self.countdown.config(bg="black")
                time.sleep(1)
                num_of_secs -= 1

    def destello(self):
        self.ventana_full.configure(bg='green')
        self.hora.config(bg="green")
        self.msg.config(bg="green")
        self.countdown.config(bg="green")

    def envio_personalizado(self):
        self.destello()
        input_dara = self.input_msg_1.get()
        self.msg.configure(text=input_dara)

    def clearMsg(self):
        self.destello()
        self.msg.configure(text=self.actual)
        print()


if __name__ == "__main__":
    app = Digital_clock()