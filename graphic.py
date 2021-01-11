#! /usr/bin/env python3

from projet_telephonie import *
from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as st

B = 0.2

#On defini la matrice de Walsh ligne par ligne pour une capacite maximale de 8 utilisateurs
walsh1 = [1,1,1,1,1,1,1,1]
walsh2 = [1,-1,1,-1,1,-1,1,-1]
walsh3 = [1,1,-1,-1,1,1,-1,-1]
walsh4 = [1,-1,-1,1,1,-1,-1,1]
walsh5 = [1,1,1,1,-1,-1,-1,-1]
walsh6 = [1,-1,1,-1,-1,1,-1,1]
walsh7 = [1,1,-1,-1,-1,-1,1,1]
walsh8 = [1,-1,-1,1,-1,1,1,-1]

def choix():
    if (var.get()==1):
        # 1 utilisateur sans bruit
        def processing():
            message1 = entry1.get()
            binaire1 = text_to_bits(message1)
            stand_bin1 = standard(binaire1)
            ext_bin1 = extend_message(stand_bin1)
            code1 = coded_message(ext_bin1)
            volt1 = volt_representation(code1)
            mes_end1 = decode(volt1)
            bin_rec1 = mesRec(mes_end1)
            bin_traite1 = textelisible(bin_rec1)
            texte1 = text_from_bits(bin_traite1)
            text_area1.insert(INSERT,binaire1)
            text_area1.configure(state='disabled')
            text_area2.insert(INSERT,stand_bin1)
            text_area2.configure(state='disabled')
            text_area3.insert(INSERT,ext_bin1)
            text_area3.configure(state='disabled')
            text_area4.insert(INSERT,code1)
            text_area4.configure(state='disabled')
            text_area5.insert(INSERT,volt1)
            text_area5.configure(state='disabled')
            text_area6.insert(INSERT,mes_end1)
            text_area6.configure(state='disabled')
            text_area7.insert(INSERT, bin_rec1)
            text_area7.configure(state='disabled')
            text_area8.insert(INSERT,bin_traite1)
            text_area8.configure(state='disabled')
            text_area9.insert(INSERT,texte1)
            text_area9.configure(state='disabled')
        
        win2 = Tk()
        win2.geometry('675x600')
        win2.title("Un utilisateur sans bruit")
        frame = ttk.Frame(win2)
        canvas = Canvas(frame)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0,0),window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        label1 = Label(win2, text="Entrez le message a envoyer")
        label1.pack()
        entry1 = Entry(win2)
        entry1.pack()
        btn_send = Button(win2, text="\N{RIGHTWARDS BLACK ARROW}", command=processing)
        btn_send.pack()
        label2 = ttk.Label(scrollable_frame, text="Le message en binaire est:")
        label2.pack()
        text_area1 = st.ScrolledText(scrollable_frame,height = 3)
        text_area1.pack()
        label3 = ttk.Label(scrollable_frame, text='Le message en binaire standard(1 et -1) est:')
        label3.pack()
        text_area2 = st.ScrolledText(scrollable_frame,height = 3)
        text_area2.pack()
        label4 = ttk.Label(scrollable_frame, text="Le message dont chaque bit est etendu sur 8 bits est:")
        label4.pack()
        text_area3 = st.ScrolledText(scrollable_frame,height = 3)
        text_area3.pack()
        label5 = ttk.Label(scrollable_frame, text="Le message code avec le code de Walsh est:")
        label5.pack()
        text_area4 = st.ScrolledText(scrollable_frame,height = 3)
        text_area4.pack()
        label6 = ttk.Label(scrollable_frame, text="La representaion en volt sur le canal est")
        label6.pack()
        text_area5 = st.ScrolledText(scrollable_frame,height = 3)
        text_area5.pack()
        label7 = ttk.Label(scrollable_frame, text="Le message, recu et decode en binaire est")
        label7.pack()
        text_area6 = st.ScrolledText(scrollable_frame,height = 3)
        text_area6.pack()
        label8 = ttk.Label(scrollable_frame, text="Le message recu non etendu est")
        label8.pack()
        text_area7 = st.ScrolledText(scrollable_frame,height = 3)
        text_area7.pack()
        label9 = ttk.Label(scrollable_frame,text="Le message recu dans en binaire normal (0 et 1) est")
        label9.pack()
        text_area8 = st.ScrolledText(scrollable_frame,height = 3)
        text_area8.pack()
        label10 = ttk.Label(scrollable_frame, text="Le message recu en texte lisible est")
        label10.pack()
        text_area9 = st.ScrolledText(scrollable_frame,height = 3)
        text_area9.pack()
        frame.pack(fill='both',expand=True)
        canvas.pack(side='left',fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        win2.mainloop()
    elif(var.get()==2):
        # 2 utilisateurs sans bruit
        def processing():
            message1 = entry1.get()
            message2 = entry2.get()
            binaire1 = text_to_bits(message1)
            binaire2 = text_to_bits(message2)
            stand_binaire1 = standard(binaire1)
            stand_binaire2 = standard(binaire2)
            stand_bin1, stand_bin2 = equ_message(stand_binaire1,stand_binaire2)
            ext_bin1 = extend_message(stand_bin1)
            ext_bin2 = extend_message(stand_bin2)
            code1 = coded_message(ext_bin1,walsh2)
            code2 = coded_message(ext_bin2,walsh3)
            volt1 = volt_representation(code1)
            volt2 = volt_representation(code2)
            no_bruit = bruit_nul(len(ext_bin1))
            phys = multiplex_2users(volt1,volt2,no_bruit)
            mes_end1 = decode(phys,walsh2)
            mes_end2 = decode(phys,walsh3)
            bin_rec1 = mesRec(mes_end1)
            bin_rec2 = mesRec(mes_end2)
            bin_traite1 = textelisible(bin_rec1)
            bin_traite2 = textelisible(bin_rec2)
            texte1 = text_from_bits(bin_traite1)
            texte2 = text_from_bits(bin_traite2)
            
            text_area1.insert(INSERT,binaire1)
            text_area1.configure(state='disabled')
            text_area11.insert(INSERT,binaire2)
            text_area11.configure(state='disabled')
            text_area2.insert(INSERT,stand_bin1)
            text_area2.configure(state='disabled')
            text_area21.insert(INSERT,stand_bin2)
            text_area21.configure(state='disabled')
            text_area3.insert(INSERT,ext_bin1)
            text_area3.configure(state='disabled')
            text_area31.insert(INSERT,ext_bin2)
            text_area31.configure(state='disabled')
            text_area4.insert(INSERT,code1)
            text_area4.configure(state='disabled')
            text_area41.insert(INSERT,code2)
            text_area41.configure(state='disabled')
            text_area5.insert(INSERT,volt1)
            text_area5.configure(state='disabled')
            text_area51.insert(INSERT,volt2)
            text_area51.configure(state='disabled')
            text_area6.insert(INSERT,phys)
            text_area6.configure(state='disabled')
            text_area7.insert(INSERT,mes_end1)
            text_area7.configure(state='disabled')
            text_area71.insert(INSERT,mes_end2)
            text_area71.configure(state='disabled')
            text_area8.insert(INSERT,bin_rec1)
            text_area8.configure(state='disabled')
            text_area81.insert(INSERT,bin_rec2)
            text_area81.configure(state='disabled')
            text_area9.insert(INSERT,bin_traite1)
            text_area9.configure(state='disabled')
            text_area91.insert(INSERT,bin_traite2)
            text_area91.configure(state='disabled')
            text_area10.insert(INSERT,texte1)
            text_area10.configure(state='disabled')
            text_area101.insert(INSERT,texte2)
            text_area101.configure(state='disabled')
        
        win2 = Tk()
        win2.geometry('675x600')
        win2.title("Deux utilisateurs sans bruit")
        frame = ttk.Frame(win2)
        canvas = Canvas(frame)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0,0),window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        label1 = Label(win2, text="Entrez le message a envoyer")
        label1.pack()
        entry1 = Entry(win2)
        entry2 = Entry(win2)
        entry1.pack()
        entry2.pack()
        btn_send = Button(win2, text="\N{RIGHTWARDS BLACK ARROW}", command=processing)
        btn_send.pack()
        label2 = ttk.Label(scrollable_frame, text="Le premier message en binaire est:")
        label2.pack()
        text_area1 = st.ScrolledText(scrollable_frame,height = 3)
        text_area1.pack()
        label21 = ttk.Label(scrollable_frame, text="Le second message en binaire est:")
        label21.pack()
        text_area11 = st.ScrolledText(scrollable_frame,height = 3)
        text_area11.pack()
        label3 = ttk.Label(scrollable_frame, text='Le premier message en binaire standard(1 et -1) est:')
        label3.pack()
        text_area2 = st.ScrolledText(scrollable_frame,height = 3)
        text_area2.pack()
        label31 = ttk.Label(scrollable_frame, text='Le second message en binaire standard(1 et -1) est:')
        label31.pack()
        text_area21 = st.ScrolledText(scrollable_frame,height = 3)
        text_area21.pack()
        label4 = ttk.Label(scrollable_frame, text="Le premier message dont chaque bit est etendu sur 8 bits est:")
        label4.pack()
        text_area3 = st.ScrolledText(scrollable_frame,height = 3)
        text_area3.pack()
        label41 = ttk.Label(scrollable_frame, text="Le second message dont chaque bit est etendu sur 8 bits est:")
        label41.pack()
        text_area31 = st.ScrolledText(scrollable_frame,height = 3)
        text_area31.pack()
        label5 = ttk.Label(scrollable_frame, text="Le premier message code avec le code de Walsh est:")
        label5.pack()
        text_area4 = st.ScrolledText(scrollable_frame,height = 3)
        text_area4.pack()
        label51 = ttk.Label(scrollable_frame, text="Le second message code avec le code de Walsh est:")
        label51.pack()
        text_area41 = st.ScrolledText(scrollable_frame,height = 3)
        text_area41.pack()
        label6 = ttk.Label(scrollable_frame, text="La representaion en volt du premier message sur le canal est")
        label6.pack()
        text_area5 = st.ScrolledText(scrollable_frame,height = 3)
        text_area5.pack()
        label61 = ttk.Label(scrollable_frame, text="La representaion en volt du second message sur le canal est")
        label61.pack()
        text_area51 = st.ScrolledText(scrollable_frame,height = 3)
        text_area51.pack()
        label7 = ttk.Label(scrollable_frame, text="Le code multiplexe sur le canal est")
        label7.pack()
        text_area6 = st.ScrolledText(scrollable_frame,height = 3)
        text_area6.pack()
        label8 = ttk.Label(scrollable_frame, text="Le premier message recu et decode est")
        label8.pack()
        text_area7 = st.ScrolledText(scrollable_frame,height = 3)
        text_area7.pack()
        label81 = ttk.Label(scrollable_frame, text="Le second message recu et decode est")
        label81.pack()
        text_area71 = st.ScrolledText(scrollable_frame,height = 3)
        text_area71.pack()
        label9 = ttk.Label(scrollable_frame,text="Le premier message recu non etendu est")
        label9.pack()
        text_area8 = st.ScrolledText(scrollable_frame,height = 3)
        text_area8.pack()
        label91 = ttk.Label(scrollable_frame,text="Le second message recu non etendu est")
        label91.pack()
        text_area81 = st.ScrolledText(scrollable_frame,height = 3)
        text_area81.pack()
        label10 = ttk.Label(scrollable_frame, text="Le premier message recu en binaire normal (0 et 1) est")
        label10.pack()
        text_area9 = st.ScrolledText(scrollable_frame,height = 3)
        text_area9.pack()
        label101 = ttk.Label(scrollable_frame, text="Le second message recu en binaire normal (0 et 1) est")
        label101.pack()
        text_area91 = st.ScrolledText(scrollable_frame,height = 3)
        text_area91.pack()
        label11 = ttk.Label(scrollable_frame,text='Le premier message recu en texte lisible est')
        label11.pack()
        text_area10 = st.ScrolledText(scrollable_frame,height = 3)
        text_area10.pack()
        label111 = ttk.Label(scrollable_frame,text='Le second message recu en texte lisible est')
        label111.pack()
        text_area101 = st.ScrolledText(scrollable_frame,height = 3)
        text_area101.pack()
        frame.pack(fill='both',expand=True)
        canvas.pack(side='left',fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        win2.mainloop()
    elif(var.get()==3):
        # 1 utilisateur avec bruit
        def processing():
            message1 = entry1.get()
            binaire1 = text_to_bits(message1)
            stand_bin1 = standard(binaire1)
            ext_bin1 = extend_message(stand_bin1)
            code1 = coded_message(ext_bin1,walsh2)
            volt1 = volt_representation(code1)
            bruit = bruit_gen(len(ext_bin1))
            phys = multiplex_1user(volt1,bruit)
            mes_end1 = decode(phys,walsh2)
            bin_rec1 = mesRec(mes_end1)
            bin_traite1 = textelisible(bin_rec1)
            texte1 = text_from_bits(bin_traite1)
            
            text_area1.insert(INSERT,binaire1)
            text_area1.configure(state='disabled')
            text_area2.insert(INSERT,stand_bin1)
            text_area2.configure(state='disabled')
            text_area3.insert(INSERT,ext_bin1)
            text_area3.configure(state='disabled')
            text_area4.insert(INSERT,code1)
            text_area4.configure(state='disabled')
            text_area5.insert(INSERT,volt1)
            text_area5.configure(state='disabled')
            text_area6.insert(INSERT,phys)
            text_area6.configure(state='disabled')
            text_area7.insert(INSERT,mes_end1)
            text_area7.configure(state='disabled')
            text_area8.insert(INSERT,bin_rec1)
            text_area8.configure(state='disabled')
            text_area9.insert(INSERT,bin_traite1)
            text_area9.configure(state='disabled')
            text_area10.insert(INSERT,texte1)
            text_area10.configure(state='disabled')
        
        win2 = Tk()
        win2.geometry('675x600')
        win2.title("Un utilisateur avec bruit")
        frame = ttk.Frame(win2)
        canvas = Canvas(frame)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0,0),window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        label1 = Label(win2, text="Entrez le message a envoyer")
        label1.pack()
        entry1 = Entry(win2)
        entry1.pack()
        btn_send = Button(win2, text="\N{RIGHTWARDS BLACK ARROW}", command=processing)
        btn_send.pack()
        label2 = ttk.Label(scrollable_frame, text="Le message en binaire est:")
        label2.pack()
        text_area1 = st.ScrolledText(scrollable_frame,height = 3)
        text_area1.pack()
        label3 = ttk.Label(scrollable_frame, text='Le message en binaire standard(1 et -1) est:')
        label3.pack()
        text_area2 = st.ScrolledText(scrollable_frame,height = 3)
        text_area2.pack()
        label4 = ttk.Label(scrollable_frame, text="Le message dont chaque bit est etendu sur 8 bits est:")
        label4.pack()
        text_area3 = st.ScrolledText(scrollable_frame,height = 3)
        text_area3.pack()
        label5 = ttk.Label(scrollable_frame, text="Le message code avec le code de Walsh est:")
        label5.pack()
        text_area4 = st.ScrolledText(scrollable_frame,height = 3)
        text_area4.pack()
        label6 = ttk.Label(scrollable_frame, text="La representaion en volt du message sur le canal est")
        label6.pack()
        text_area5 = st.ScrolledText(scrollable_frame,height = 3)
        text_area5.pack()
        label7 = ttk.Label(scrollable_frame, text="Le code multiplexe (avec du bruit) sur le canal est")
        label7.pack()
        text_area6 = st.ScrolledText(scrollable_frame,height = 3)
        text_area6.pack()
        label8 = ttk.Label(scrollable_frame, text="Le message recu et decode est")
        label8.pack()
        text_area7 = st.ScrolledText(scrollable_frame,height = 3)
        text_area7.pack()
        label9 = ttk.Label(scrollable_frame,text="Le message recu non etendu est")
        label9.pack()
        text_area8 = st.ScrolledText(scrollable_frame,height = 3)
        text_area8.pack()
        label10 = ttk.Label(scrollable_frame, text="Le message recu en binaire normal (0 et 1) est")
        label10.pack()
        text_area9 = st.ScrolledText(scrollable_frame,height = 3)
        text_area9.pack()
        label11 = ttk.Label(scrollable_frame,text='Le message recu en texte lisible est')
        label11.pack()
        text_area10 = st.ScrolledText(scrollable_frame,height = 3)
        text_area10.pack()
        frame.pack(fill='both',expand=True)
        canvas.pack(side='left',fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        win2.mainloop()
    elif(var.get()==4):
        # 2 utilisateurs avec bruit
        def processing():
            message1 = entry1.get()
            message2 = entry2.get()
            binaire1 = text_to_bits(message1)
            binaire2 = text_to_bits(message2)
            stand_binaire1 = standard(binaire1)
            stand_binaire2 = standard(binaire2)
            stand_bin1, stand_bin2 = equ_message(stand_binaire1,stand_binaire2)
            ext_bin1 = extend_message(stand_bin1)
            ext_bin2 = extend_message(stand_bin2)
            code1 = coded_message(ext_bin1,walsh2)
            code2 = coded_message(ext_bin2,walsh3)
            volt1 = volt_representation(code1)
            volt2 = volt_representation(code2)
            bruit = bruit_gen(len(ext_bin1))
            phys = multiplex_2users(volt1,volt2,bruit)
            mes_end1 = decode(phys,walsh2)
            mes_end2 = decode(phys,walsh3)
            bin_rec1 = mesRec(mes_end1)
            bin_rec2 = mesRec(mes_end2)
            bin_traite1 = textelisible(bin_rec1)
            bin_traite2 = textelisible(bin_rec2)
            texte1 = text_from_bits(bin_traite1)
            texte2 = text_from_bits(bin_traite2)
            
            text_area1.insert(INSERT,binaire1)
            text_area1.configure(state='disabled')
            text_area11.insert(INSERT,binaire2)
            text_area11.configure(state='disabled')
            text_area2.insert(INSERT,stand_bin1)
            text_area2.configure(state='disabled')
            text_area21.insert(INSERT,stand_bin2)
            text_area21.configure(state='disabled')
            text_area3.insert(INSERT,ext_bin1)
            text_area3.configure(state='disabled')
            text_area31.insert(INSERT,ext_bin2)
            text_area31.configure(state='disabled')
            text_area4.insert(INSERT,code1)
            text_area4.configure(state='disabled')
            text_area41.insert(INSERT,code2)
            text_area41.configure(state='disabled')
            text_area5.insert(INSERT,volt1)
            text_area5.configure(state='disabled')
            text_area51.insert(INSERT,volt2)
            text_area51.configure(state='disabled')
            text_area6.insert(INSERT,phys)
            text_area6.configure(state='disabled')
            text_area7.insert(INSERT,mes_end1)
            text_area7.configure(state='disabled')
            text_area71.insert(INSERT,mes_end2)
            text_area71.configure(state='disabled')
            text_area8.insert(INSERT,bin_rec1)
            text_area8.configure(state='disabled')
            text_area81.insert(INSERT,bin_rec2)
            text_area81.configure(state='disabled')
            text_area9.insert(INSERT,bin_traite1)
            text_area9.configure(state='disabled')
            text_area91.insert(INSERT,bin_traite2)
            text_area91.configure(state='disabled')
            text_area10.insert(INSERT,texte1)
            text_area10.configure(state='disabled')
            text_area101.insert(INSERT,texte2)
            text_area101.configure(state='disabled')
        
        win2 = Tk()
        win2.geometry('675x600')
        win2.title("Deux utilisateurs avec bruit")
        frame = ttk.Frame(win2)
        canvas = Canvas(frame)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0,0),window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        label1 = Label(win2, text="Entrez le message a envoyer")
        label1.pack()
        entry1 = Entry(win2)
        entry2 = Entry(win2)
        entry1.pack()
        entry2.pack()
        btn_send = Button(win2, text="\N{RIGHTWARDS BLACK ARROW}", command=processing)
        btn_send.pack()
        label2 = ttk.Label(scrollable_frame, text="Le premier message en binaire est:")
        label2.pack()
        text_area1 = st.ScrolledText(scrollable_frame,height = 3)
        text_area1.pack()
        label21 = ttk.Label(scrollable_frame, text="Le second message en binaire est:")
        label21.pack()
        text_area11 = st.ScrolledText(scrollable_frame,height = 3)
        text_area11.pack()
        label3 = ttk.Label(scrollable_frame, text='Le premier message en binaire standard(1 et -1) est:')
        label3.pack()
        text_area2 = st.ScrolledText(scrollable_frame,height = 3)
        text_area2.pack()
        label31 = ttk.Label(scrollable_frame, text='Le second message en binaire standard(1 et -1) est:')
        label31.pack()
        text_area21 = st.ScrolledText(scrollable_frame,height = 3)
        text_area21.pack()
        label4 = ttk.Label(scrollable_frame, text="Le premier message dont chaque bit est etendu sur 8 bits est:")
        label4.pack()
        text_area3 = st.ScrolledText(scrollable_frame,height = 3)
        text_area3.pack()
        label41 = ttk.Label(scrollable_frame, text="Le second message dont chaque bit est etendu sur 8 bits est:")
        label41.pack()
        text_area31 = st.ScrolledText(scrollable_frame,height = 3)
        text_area31.pack()
        label5 = ttk.Label(scrollable_frame, text="Le premier message code avec le code de Walsh est:")
        label5.pack()
        text_area4 = st.ScrolledText(scrollable_frame,height = 3)
        text_area4.pack()
        label51 = ttk.Label(scrollable_frame, text="Le second message code avec le code de Walsh est:")
        label51.pack()
        text_area41 = st.ScrolledText(scrollable_frame,height = 3)
        text_area41.pack()
        label6 = ttk.Label(scrollable_frame, text="La representaion en volt du premier message sur le canal est")
        label6.pack()
        text_area5 = st.ScrolledText(scrollable_frame,height = 3)
        text_area5.pack()
        label61 = ttk.Label(scrollable_frame, text="La representaion en volt du second message sur le canal est")
        label61.pack()
        text_area51 = st.ScrolledText(scrollable_frame,height = 3)
        text_area51.pack()
        label7 = ttk.Label(scrollable_frame, text="Le code multiplexe sur le canal est")
        label7.pack()
        text_area6 = st.ScrolledText(scrollable_frame,height = 3)
        text_area6.pack()
        label8 = ttk.Label(scrollable_frame, text="Le premier message recu et decode est")
        label8.pack()
        text_area7 = st.ScrolledText(scrollable_frame,height = 3)
        text_area7.pack()
        label81 = ttk.Label(scrollable_frame, text="Le second message recu et decode est")
        label81.pack()
        text_area71 = st.ScrolledText(scrollable_frame,height = 3)
        text_area71.pack()
        label9 = ttk.Label(scrollable_frame,text="Le premier message recu non etendu est")
        label9.pack()
        text_area8 = st.ScrolledText(scrollable_frame,height = 3)
        text_area8.pack()
        label91 = ttk.Label(scrollable_frame,text="Le second message recu non etendu est")
        label91.pack()
        text_area81 = st.ScrolledText(scrollable_frame,height = 3)
        text_area81.pack()
        label10 = ttk.Label(scrollable_frame, text="Le premier message recu en binaire normal (0 et 1) est")
        label10.pack()
        text_area9 = st.ScrolledText(scrollable_frame,height = 3)
        text_area9.pack()
        label101 = ttk.Label(scrollable_frame, text="Le second message recu en binaire normal (0 et 1) est")
        label101.pack()
        text_area91 = st.ScrolledText(scrollable_frame,height = 3)
        text_area91.pack()
        label11 = ttk.Label(scrollable_frame,text='Le premier message recu en texte lisible est')
        label11.pack()
        text_area10 = st.ScrolledText(scrollable_frame,height = 3)
        text_area10.pack()
        label111 = ttk.Label(scrollable_frame,text='Le second message recu en texte lisible est')
        label111.pack()
        text_area101 = st.ScrolledText(scrollable_frame,height = 3)
        text_area101.pack()
        frame.pack(fill='both',expand=True)
        canvas.pack(side='left',fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        win2.mainloop()

win = Tk()
var = IntVar()

text1 = Label(text="Bienvenu sur le programme de simulation du CDMA, veuillez choisir votre mode de simulation!", fg="blue")
text1.pack()

r1 = Radiobutton(win, text="Un utilisateur sans bruit", variable=var, value=1, command=choix)
r1.pack()
r2 = Radiobutton(win, text="Deux utilisateur sans bruit", variable=var, value=2, command=choix)
r2.pack()
r3 = Radiobutton(win, text="Un utilisateur avec bruit", variable=var, value=3, command=choix)
r3.pack()
r4 = Radiobutton(win, text="Deux utilisateur avec bruit", variable=var, value=4, command=choix)
r4.pack()

win.mainloop()