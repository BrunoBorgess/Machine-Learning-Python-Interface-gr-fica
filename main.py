import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import customtkinter as ctk
from tkinter import *
from PIL import Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import pandas as pd

'''
tranformar tdos os dados em funções,  criar entrys para coletar os dados digitados pelo usuário, após isso, colocar essas váriaveis que coletaram os dados
dentro dos meses e valores, após elaborador toda essa lógica, devera ser feito todo o algoritmo para plotar os gráficos utilizando matplotlib e plotar eles
na interface gráfica customtkinter - com isso, iremos ter uma aplicação com machine learning IA que irá fazer previsão de vendas baseada nos valores que 
forem passados dos ultimos meses.
OBS: 
 - Colocar apenas 5 meses como parametro de verificação - pois quanto menos o numéro para percorrer, mais preciso será a previsão
'''


'''meses = np.array([1, 2, 3, 4, 5])
valores = np.array([100, 95, 105, 102, 98])


df = pd.DataFrame({'Mês': meses, 'Valores': valores})

modelo = LinearRegression()
modelo.fit(df[['Mês']], df['Valores'])

# Preveja o valor para o proximo mes
mes_seguinte = np.array([6])
previsao = modelo.predict(mes_seguinte.reshape(-1, 1))

# Limitando a previsão a duas casas decimais
previsao_formatada = round(previsao[0], 2)

# Adicione o valor previsto á array original para plotar no gráfico
meses = np.concatenate([meses, mes_seguinte])
valores = np.concatenate([valores, previsao])

print(f"Previsão do valor para o mês seguinte R${previsao_formatada}")

# Criar o gráfico
plt.scatter(meses, valores, color='b', label='Dados da previsão')
plt.plot(meses, valores, 'r-')
plt.xlabel('Mês')
plt.ylabel('Valores')
plt.legend()
plt.show()'''

'''([self.entry_v1, self.entry_v2, self.entry_v3, self.entry_v4, self.entry_v5])'''

class BackEnd():
    # Pegando os valores das entrys com o método get()
    def funcs_machine(self):
        self.entry_name_entry = self.entry_name.get()
        # Pegando os valores das entrys mes
        self.entry_m1 = self.entry_mes1.get()
        self.entry_m2 = self.entry_mes2.get()
        self.entry_m3 = self.entry_mes3.get()
        self.entry_m4 = self.entry_mes4.get()
        self.entry_m5 = self.entry_mes5.get()
        #pegando os valores das entrys valores
        self.entry_v1 = self.entry_valor1.get()
        self.entry_v2 = self.entry_valor2.get()
        self.entry_v3 = self.entry_valor3.get()
        self.entry_v4 = self.entry_valor4.get()
        self.entry_v5 = self.entry_valor5.get()
        
        # Criando as regras de machine learning com sklern

        self.meses = np.array([1, 2, 3, 4, 5])
        self.valores = np.array([self.entry_v1, self.entry_v2 , self.entry_v3, self.entry_v4 ,self.entry_v5])

        self.df = pd.DataFrame({'Mês': self.meses, 'Valores': self.valores})

        self.modelo = LinearRegression()
        self.modelo.fit(self.df[['Mês']], self.df['Valores'])

        # Preveja o valor para o proximo mes
        self.mes_seguinte = np.array([6])
        self.previsao = self.modelo.predict(self.mes_seguinte.reshape(-1, 1))

        # Limitando a previsão a duas casas decimais
        self.previsao_formatada = round(self.previsao[0], 2)

        # Adicionando o valor previsto no array original para plotar no gráfico
        self.meses = np.concatenate([self.meses, self.mes_seguinte])
        self.valores = np.concatenate([self.valores, self.previsao])
        self.lb_resultado.configure(text=f"{self.entry_name_entry} , baseado nos valores dos meses {self.entry_m1}, {self.entry_m2}, {self.entry_m3}, {self.entry_m4}, {self.entry_m5} a previsão do valor para o mês seguinte R${self.previsao_formatada}")

        # Criando o gráfico com matplotlib o gráfico
        self.fig, self.ax = plt.subplots()
        plt.scatter(self.meses, self.valores, color='c', label='Dados da previsão')
        plt.plot(self.meses, self.valores, 'r-')
        plt.xlabel('Mês')
        plt.ylabel('Valores')
        plt.legend()


        # Tranformando o gráfico em figura com FigureCanvasTkAgg, para depois colocalo dentro do frame
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.scroll)
        self.canvas.draw()
        # Posicionando o gráfico dentro do frame
        self.canvas.get_tk_widget().pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)
        # Evita a abertura de uma nova janela no gráfico
        plt.close(self.fig)

    def limpar_entrys(self):
        # Limpando entry nome do projeto com o método delete, inicializando em 0 e com o argumento END para deletar até o final do que estiver dentro das entrys
        self.entry_name.delete(0, END)
        # Limpando entrys dos meses
        self.entry_mes1.delete(0, END)
        self.entry_mes2.delete(0, END)
        self.entry_mes3.delete(0, END)
        self.entry_mes4.delete(0, END)
        self.entry_mes5.delete(0, END)
        # limpando entrys de valores
        self.entry_valor1.delete(0, END)
        self.entry_valor2.delete(0, END)
        self.entry_valor3.delete(0, END)
        self.entry_valor4.delete(0, END)
        self.entry_valor5.delete(0, END)



class App(ctk.CTk, BackEnd):
    def __init__(self):
        super().__init__()
        self.tela()
        self.frame_1()
        self.frame_2()
        self.frame_3()
        self.frame_4()
    def tela(self):
        self.geometry('1000x550')
        self.title('Projec')
        self.resizable('False', 'False')
        self.iconbitmap('icon.ico')
        self._set_appearance_mode('Dark')
    def frame_1(self):
        self.frame1 = ctk.CTkFrame(self, width=250, height=548, fg_color='beige')
        self.frame1.place(x=1, y=1)
        
        self.entry_name = ctk.CTkEntry(self.frame1, placeholder_text='Digite o nome do projeto', width=210, border_width=1, corner_radius=5)
        self.entry_name.place(x=20, y=150)
        # Criando entradas de valores para serem analisadas
        self.entry_mes1 = ctk.CTkEntry(self.frame1, placeholder_text='Digite o mês', width=90, border_width=1, corner_radius=5)
        self.entry_mes1.place(x=20, y=200)
        self.entry_mes2 = ctk.CTkEntry(self.frame1, placeholder_text='Digite o mês', width=90, border_width=1, corner_radius=5)
        self.entry_mes2.place(x=20, y=230)
        self.entry_mes3 = ctk.CTkEntry(self.frame1, placeholder_text='Digite o mês', width=90, border_width=1, corner_radius=5)
        self.entry_mes3.place(x=20, y=260)
        self.entry_mes4 = ctk.CTkEntry(self.frame1, placeholder_text='Digite o mês', width=90, border_width=1, corner_radius=5)
        self.entry_mes4.place(x=20, y=290)
        self.entry_mes5 = ctk.CTkEntry(self.frame1, placeholder_text='Digite o mês', width=90, border_width=1, corner_radius=5)
        self.entry_mes5.place(x=20, y=320)

        # Criando as entradas de valores de vendas para serem analisados
        self.entry_valor1 = ctk.CTkEntry(self.frame1, placeholder_text='Digite o valor', width=90, border_width=1, corner_radius=5)
        self.entry_valor1.place(x=140, y=200)
        self.entry_valor2 = ctk.CTkEntry(self.frame1, placeholder_text='Digite o valor', width=90, border_width=1, corner_radius=5)
        self.entry_valor2.place(x=140, y=230)
        self.entry_valor3 = ctk.CTkEntry(self.frame1, placeholder_text='Digite o valor', width=90, border_width=1, corner_radius=5)
        self.entry_valor3.place(x=140, y=260)
        self.entry_valor4 = ctk.CTkEntry(self.frame1, placeholder_text='Digite o valor', width=90, border_width=1, corner_radius=5)
        self.entry_valor4.place(x=140, y=290)
        self.entry_valor5 = ctk.CTkEntry(self.frame1, placeholder_text='Digite o valor', width=90, border_width=1, corner_radius=5)
        self.entry_valor5.place(x=140, y=320)

        # Criando os buttons para realizar a previsão

        self.img_delet = ctk.CTkImage(light_image=Image.open('del.png'), size=(20, 20))
        self.img_load = ctk.CTkImage(light_image=Image.open('load.png'), size=(20, 20))
        self.bt_ok = ctk.CTkButton(self.frame1, text='Gerar previsão', border_width=1, image=self.img_load, command=self.funcs_machine)
        self.bt_ok.place(x=20, y=370)
        self.bt_limpar = ctk.CTkButton(self.frame1, text='Limpar tela', border_width=1, image=self.img_delet, command=self.limpar_entrys)
        self.bt_limpar.place(x=20, y=415)
    def frame_2(self):
        self.frame2 = ctk.CTkFrame(self, width=748, height=548, fg_color='beige')
        self.frame2.place(x=253, y=1)
        self.lb_resultado = ctk.CTkLabel(self.frame2,text='')
        self.lb_resultado.place(x=20, y=510)

    def frame_3(self):
        self.frame3 = ctk.CTkFrame(self.frame1, width=298, height=50, fg_color='beige')
        self.frame3.place(x=25, y=50)
        self.img_machine = ctk.CTkImage(light_image=Image.open('machine.png'), size=(40,40))
        self.label_machine = ctk.CTkLabel(self.frame1, image=self.img_machine, text='')
        self.label_machine.place(x=25, y=40)
        self.lb_frame3 = ctk.CTkLabel(self.frame3, text='Machine Learning')
        self.lb_frame3.place(x=50, y=5)
    

    def frame_4(self):
        self.scroll = ctk.CTkScrollableFrame(self.frame2, width=700, height=500, fg_color='beige')
        self.scroll.place(x= 1, y=5)


if __name__ == "__main__":
    App = App()
    App.mainloop()
