#Finally I am author of somethin'

__author__ = "Andrei Necsulea"

#Import all the libraries for our project
import webbrowser
# Tkinter normal widgets
import tkinter as tk
#tkinter fonts 
import tkinter.font as font
# importing PIL for the bg img of the main window
from PIL import ImageTk , Image
#importing graph library
from matplotlib import pyplot as plt
# importing ttk cause we need comboboxes
from tkinter import Button, PhotoImage, ttk

from numpy import double, empty

#Creating the main window

window = tk.Tk()
# Setting the geometry 
window.geometry("960x540")
# Setting the title
window.title("A.N. Charts 1.0")


window.iconbitmap("main.ico")


#Setting maximizing and minimizing to false
window.resizable(0,0)

#Adding bg img
canv = tk.Canvas(master=window)
canv.place(x=0, y=0  , width = 960, height = 540)

img = ImageTk.PhotoImage(Image.open("img.jpg")) 

canv.create_image(0, 0, image=img, anchor='nw')

#Function for creating new Button 
#x_1 , y_1 from place

#Function for button 'New Graph' from main window

def New_Graph():
    # Button_1 is created to save time , making buttons instantly 
    def Button_1(window , text_1 , width_1 , height_1 , fg_1 , bg_1 , bd_1 , font_1 , command_1 , font_size , ancora , relx_1  , rely_1 ):
      myFont = font.Font(family=font_1 , size = font_size)
      btn = tk.Button(window , text = text_1 , width = width_1 , height = height_1 ,fg = fg_1 , bg = bg_1 , bd = bd_1 , command = command_1 )
      btn['font'] = myFont
      btn.place( relx = relx_1, rely = rely_1  , anchor=ancora )
      return btn
     # Second window from new graph 
    global new_window_2
    new_window_2 = tk.Tk()
    new_window_2['bg'] = "#4b6cb7"


    new_window_2.iconbitmap("n2.ico")


    new_window_2.geometry("650x400")
    new_window_2.title("Data for the graph")
    new_window_2.resizable(0,0)
    Label_1 = tk.Label(new_window_2 , text = " Number of points for the graph : ")
    Label_1.place(relx = 0.5 , rely = 0.3 , anchor = "center")
    label_font = font.Font(family = "Times" , size = 14)
    Label_1['bg'] = "#4b6cb7"
    Label_1['font'] = label_font
    Entry_1 = tk.Entry(new_window_2 )
    Entry_1.place(relx = 0.5 , rely = 0.5 , anchor = "center" , width = 320 , height = 25)
    Entry_1_font = font.Font(family = "Times" , size = 14)
    Entry_1['font'] = Entry_1_font
    
#Function for entry
    def new_Entry_function():
        aux = Entry_1.get()
        if aux == "":
            tk.messagebox.showerror("Error" ,  "The entry is empty !\nPlease insert a number !")
            new_window_2.destroy()
        else:
             if (aux.isnumeric()) == True :
                    aux = int(aux)

                    def make_window(): 

                        new_window_2.destroy()
                        global new_window_3
                        new_window_3 = tk.Tk()
                        new_window_3['bg'] = "#4b6cb7"
                        #new_window_3.geometry("650x400")
                        new_window_3.state('zoomed')
                        new_window_3.title("Data for the graph")


                        new_window_3.iconbitmap("n3.ico")


                        #new_window_3.resizable(0,0)
                        global string_i
                        global string_i_minus_1
                        list_aux = list()
                        list_entries = list()
                        string_i = 1
                        string_i_minus_1 = 1
                        string_i = str(string_i)
                        string_i_minus_1 = str(string_i_minus_1)

                        
                        for i in range(0,aux,1):
                                #if i%2 == 0:
                                           label_x = tk.Label(new_window_3 , text = " Please insert coordinates for point " + string_i + " : " + " " + "   x =")
                                           label_x.grid(column = 2 , row = i  , columnspan = 3)
                                           
                                           label_x_font = font.Font(family = "Times" , size = 14 )
                                
                                           label_x['font'] = label_font
                               
                                           label_x['bg'] = "#4b6cb7"
                                           string_i = int(string_i)
                                           string_i+=1
                                           string_i = str(string_i)
                                           en_x = tk.Entry(new_window_3 , width = 10)
                                           list_entries.append(en_x)

                                           en_x.grid(column = 5 , row = i , columnspan = 1)
                                           
                                           

                                #else
                                           label_y = tk.Label(new_window_3 , text = "    y = ")
                                           label_y.grid(column = 7 ,  row = i  )
                                           
                                           label_y_font = font.Font(family = "Times" , size = 14)
                                
                                           label_y['font'] = label_font
                               
                                           label_y['bg'] = "#4b6cb7"
                                           
                                           en_y = tk.Entry(new_window_3 , width = 10)
                                           list_entries.append(en_y)
                                           en_y.grid(column = 9 , row = i )
                                          
                       #Trebuie creata functie pentru copierea textului din entry aici :
                        def entry_copy(entry):

                          x = entry.get()
                          list_aux.append(x)

                        label_s = tk.Label(new_window_3 , text = "      Color for the points :")
                       
                        label_s['bg'] = "#4b6cb7"
                       #label_s.place(relx = 0.5 , rely = 0.6 , anchor = "nw")
                        label_s.grid(column = 2 , row = i+1 , pady = 50)
                        label_s_font = font.Font(family = "Times" , size = 12)
                        label_s['font'] = label_s_font 
                       
                       
                        ceva = tk.StringVar()
                        combobox_1 = ttk.Combobox(new_window_3  , width = 20 , state = "readonly" )
                      
                        
                        combobox_1['textvariable'] = ceva
                        combobox_1['values'] = ('red' , 'green' , 'blue' , 'cyan' , 'magenta' , 'yellow' , 'black' , 'white')
                        combobox_1.grid(column = 4 , row = i+1 )
                        combobox_1.current(0)
                       

                        combobox = ttk.Combobox(new_window_3 , width = 20 ,  state="readonly")
                        combobox['values'] = ('red' , 'green' , 'blue' , 'cyan' , 'magenta' , 'yellow' , 'black' , "white")
                        combobox.grid(column = 12 , row = i+1 )
                        combobox.current(0)
                       
                        
                        def combobox_1_f(event):
                           global c_1_f
                           c_1_f = combobox_1.get()
                        combobox_1.bind("<<ComboboxSelected>>" , combobox_1_f)
                       
                        
                        def combobox_f(event):
                         global c_f
                         c_f = combobox.get()
                        combobox.bind("<<ComboboxSelected>>" , combobox_f)
                      
                       

                        label_color_line = tk.Label(new_window_3 , text = " Color for the line :")
                       
                        label_color_line['bg'] = "#4b6cb7"
                        #label_s.place(relx = 0.5 , rely = 0.6 , anchor = "nw")
                        label_color_line.grid(column = 10 , row = i+1 )
                        label_color_line_font = font.Font(family = "Times" , size = 12)
                        label_color_line['font'] = label_color_line_font 
                       
                       

                       #label_s_d = tk.Label(new_window_3 , text = "Note : If you see contents of the window blocking each other , maximize window !\nAllowed colors : red , green , blue , cyan , magenta , yellow , black , white")
                       #label_s_d['bg'] = "#4b6cb7"
                       #label_s_d['fg'] = "yellow"
                       #label_s_d.place(relx = 0.5 ,rely = 0.7 , anchor = "sw")
                       #label_s_d_font = font.Font(family = "Times" , size = 9)
                       #label_s_d['font'] = label_s_d_font
                       
                      
                        def combine_funcs(*funcs):
                           def combined_func(*args, **kwargs):
                             for f in funcs:
                              f(*args, **kwargs)
                           return combined_func
                       
                       

                        global aux_c_1_f
                        global aux_c_f

                        def verify_and_create_graph():
                            
                         


                         for i in range(0,len(list_entries),1):
                             entry_copy(list_entries[i])
                            
                         ok = 1
                         list_copy = list()

                         def verify_float(s):
                          try:
                                float(s)
                                return True
                          except ValueError:
                                return False

                         for i in range(0,len(list_aux),1):
                             list_aux[i] = str(list_aux[i])
                             if (verify_float(list_aux[i]))==False:
                                                                 ok = 0
                             else:
                                  if (verify_float(list_aux[i]))==True:
                                       list_aux_int = float(list_aux[i])
                                       list_copy.append(list_aux_int)

                             
                         if (ok == 0 and len(list_copy) != len(list_aux)) or len(list_copy)==0:
                             tk.messagebox.showerror("Error" , "One or more of the inputs places contains letters or is empty !\nPlease insert a number !")
                             new_window_3.destroy()
                         x_list = list()
                         y_list = list()
                         
            
                         if ok == 1 and len(list_copy) == len(list_aux):
                            
                             
                             aux_c_1_f = c_1_f
                             aux_c_f = c_f

                             new_window_3.destroy()
                             for i in range(0,len(list_copy),1):
                                 if i%2==0:
                                            x = list_copy[i]
                                            x_list.append(x)
                                            y = list_copy[i+1]
                                            y_list.append(y)
                         
                         
                         
                        
                         combobox_list_values = ('red' , 'green' , 'blue' , 'cyan' , 'magenta' , 'yellow' , 'black' , 'white')
                         combobox_1_list_values = ('red' , 'green' , 'blue' , 'cyan' , 'magenta' , 'yellow' , 'black' , 'white')

                         if aux_c_1_f in combobox_list_values and aux_c_f in combobox_1_list_values :

                          plt.plot(x_list , y_list , marker = "o"  , mec = aux_c_1_f , mfc = aux_c_1_f , color = aux_c_f)
                          aux_c_1_f = ""
                          aux_c_f = ""
                          plt.show()
                         else:
                           tk.messagebox.showerror("Error" , "You must select colors for both comboboxes !")
                   

                       
                               

                               
                        
                                 
                            
                       
                       
                        btn = tk.Button(new_window_3 ,    text = "Create Graph" , width=50 , height = 2 , fg = "blue" , bg = "lightblue" , bd = 3 , command =verify_and_create_graph)
                        btn_font = font.Font(family = "Times" , size = 14)
                        btn['font'] = btn_font
                        btn.place(relx = 0.5 , rely = 0.92 , anchor = "n")


                    def make_window_1():

                        new_window_2.destroy()
                        global new_window_3
                        new_window_3 = tk.Tk()
                        new_window_3['bg'] = "#4b6cb7"
                        #new_window_3.geometry("650x400")
                        new_window_3.state('zoomed')
                        new_window_3.title("Data for the graph")


                        new_window_3.iconbitmap("n3.ico")


                        #new_window_3.resizable(0,0)
                        global string_i
                        global string_i_minus_1
                        list_aux = list()
                        list_entries = list()
                        string_i = 1
                        string_i_minus_1 = 1
                        string_i = str(string_i)
                        string_i_minus_1 = str(string_i_minus_1)

                       
                        for i in range(0,aux,1):
                                #if i%2 == 0:
                                           label_x = tk.Label(new_window_3 , text = " Please insert coordinates for point " + string_i + " : " + " " + "   x =")
                                           label_x.grid(column = 2 , row = i  , columnspan = 3)
                                           
                                           label_x_font = font.Font(family = "Times" , size = 14 )
                                
                                           label_x['font'] = label_font
                               
                                           label_x['bg'] = "#4b6cb7"
                                           string_i = int(string_i)
                                           string_i+=1
                                           string_i = str(string_i)
                                           en_x = tk.Entry(new_window_3 , width = 10)
                                           list_entries.append(en_x)

                                           en_x.grid(column = 5 , row = i , columnspan = 1)
                                           
                                           

                                #else
                                           label_y = tk.Label(new_window_3 , text = "    y = ")
                                           label_y.grid(column = 7 ,  row = i  )
                                           
                                           label_y_font = font.Font(family = "Times" , size = 14)
                                
                                           label_y['font'] = label_font
                               
                                           label_y['bg'] = "#4b6cb7"
                                           
                                           en_y = tk.Entry(new_window_3 , width = 10)
                                           list_entries.append(en_y)
                                           en_y.grid(column = 9 , row = i )
                                          
                       #Trebuie creata functie pentru copierea textului din entry aici :
                        def entry_copy(entry):
                          x = entry.get()
                          list_aux.append(x)

                        label_s = tk.Label(new_window_3 , text = "      Color for the points :")
                       
                        label_s['bg'] = "#4b6cb7"
                       #label_s.place(relx = 0.5 , rely = 0.6 , anchor = "nw")
                        label_s.grid(column = 2 , row = i+1 , pady = 50)
                        label_s_font = font.Font(family = "Times" , size = 12)
                        label_s['font'] = label_s_font 
                       
                       
                        ceva = tk.StringVar()
                        combobox_1 = ttk.Combobox(new_window_3  , width = 20 , state = "readonly" )
                      
                        
                        combobox_1['textvariable'] = ceva
                        combobox_1['values'] = ('red' , 'green' , 'blue' , 'cyan' , 'magenta' , 'yellow' , 'black' , 'white')
                        combobox_1.grid(column = 4 , row = i+1 )
                        combobox_1.current(0)
                       

                        
                        
                        
                        def combobox_1_f(event):
                           global c_1_f
                           c_1_f = combobox_1.get()
                        combobox_1.bind("<<ComboboxSelected>>" , combobox_1_f)
                       
                       
                                            
                                                                    

                       #label_s_d = tk.Label(new_window_3 , text = "Note : If you see contents of the window blocking each other , maximize window !\nAllowed colors : red , green , blue , cyan , magenta , yellow , black , white")
                       #label_s_d['bg'] = "#4b6cb7"
                       #label_s_d['fg'] = "yellow"
                       #label_s_d.place(relx = 0.5 ,rely = 0.7 , anchor = "sw")
                       #label_s_d_font = font.Font(family = "Times" , size = 9)
                       #label_s_d['font'] = label_s_d_font
                       
                      
                        def combine_funcs(*funcs):
                           def combined_func(*args, **kwargs):
                             for f in funcs:
                              f(*args, **kwargs)
                           return combined_func
                       
                       

                        global aux_c_1_f
                        global aux_c_f
                        def verify_and_create_graph():
                            
                         


                         for i in range(0,len(list_entries),1):
                             entry_copy(list_entries[i])

                         def is_number(s):
                            try:
                                float(s)
                                return True
                            except ValueError:
                                return False

                         ok = 1
                         list_copy = list()
                         for i in range(0,len(list_aux),1):
                             list_aux[i] = str(list_aux[i])
                             if (is_number(list_aux[i]))==False:
                                                                 ok = 0
                             else:
                                  if(is_number(list_aux[i]))==True:
                                       list_aux_int = float(list_aux[i])
                                       list_copy.append(list_aux_int)

                             
                         if (ok == 0 and len(list_copy) != len(list_aux)) or len(list_copy)==0:
                             tk.messagebox.showerror("Error" , "One or more of the inputs places contains letters or is empty !\nPlease insert a number !")
                             new_window_3.destroy()
                         x_list = list()
                         y_list = list()
                         
            
                         if ok == 1 and len(list_copy) == len(list_aux):
                            
                             
                             aux_c_1_f = c_1_f
                            
                             new_window_3.destroy()
                             for i in range(0,len(list_copy),1):
                                 if i%2==0:
                                            x = list_copy[i]
                                            x_list.append(x)
                                            y = list_copy[i+1]
                                            y_list.append(y)
                         
                         
                         
                         
                         combobox_list_values = ('red' , 'green' , 'blue' , 'cyan' , 'magenta' , 'yellow' , 'black' , 'white')
                         
                         if aux_c_1_f in combobox_list_values :

                          plt.plot(x_list , y_list , marker = "o"  , mec = aux_c_1_f , mfc = aux_c_1_f )
                          aux_c_1_f = ""
                          plt.show()
                         else:
                           tk.messagebox.showerror("Error" , "You must select color for the combobox !")
                       
                            
                       
                       
                        btn = tk.Button(new_window_3 ,    text = "Create Graph" , width=50 , height = 2 , fg = "blue" , bg = "lightblue" , bd = 3 , command =verify_and_create_graph)
                        btn_font = font.Font(family = "Times" , size = 14)
                        btn['font'] = btn_font
                        btn.place(relx = 0.5 , rely = 0.92 , anchor = "n")

                    if aux > 1 :
                      make_window()
                    else :
                      make_window_1()

                    

             else:
                  if (aux.isalpha())==True or (aux.isalnum())==True:
                    tk.messagebox.showerror("Error" ,  "The entry must contain only numbers!\nPlease insert a number !")
                    new_window_2.destroy()
    
    Button_1(new_window_2 , "Insert coordinates" , 30 , 2 , "blue" , "lightblue" , 3 , "Times" , new_Entry_function , 14 , "center" , 0.5 , 0.7 )

    new_window_2.mainloop()
#Function for button 'New Pie Chart' from main window
def New_Pie_Chart():
  def Button_1(window , text_1 , width_1 , height_1 , fg_1 , bg_1 , bd_1 , font_1 , command_1 , font_size , ancora , relx_1  , rely_1 ):
      myFont = font.Font(family=font_1 , size = font_size)
      btn = tk.Button(window , text = text_1 , width = width_1 , height = height_1 ,fg = fg_1 , bg = bg_1 , bd = bd_1 , command = command_1 )
      btn['font'] = myFont
      btn.place( relx = relx_1, rely = rely_1  , anchor=ancora )
      return btn
  new_window_1 = tk.Tk()
  new_window_1["bg"] = "#4b6cb7"
  new_window_1.geometry("650x400")
  new_window_1.title("Data for the charts")


  new_window_1.iconbitmap("n1pie.ico")


  new_window_1.resizable(0,0)

  label_color_line = tk.Label(new_window_1 , text = "                                   Number of labels : ")
                       
  label_color_line['bg'] = "#4b6cb7"
  #label_s.place(relx = 0.5 , rely = 0.6 , anchor = "nw")
  label_color_line.grid(column = 10 , row = 5 )
  label_color_line_font = font.Font(family = "Times" , size = 10)
  label_color_line['font'] = label_color_line_font 

  inp = tk.Entry(new_window_1 , width = 3)
  inp.grid(column=15 , row=5)
  

# for ul asta e important...trebuie pus cumva in functie

  
    

# pie_cmd is a command for create pie chart button 

  def pie_cmd():
     
     e_pie = inp.get()
     e_aux = inp.get()
     if e_aux.isdigit()==0:
       new_window_1.destroy()
       tk.messagebox.showerror("Error" , "Please insert a number !") 

     e_aux = int(e_aux)
     if e_pie.isdigit():
                        new_window_1.destroy()
                        new_window_inp = tk.Tk()
                        new_window_inp["bg"] = "#4b6cb7"
                        #new_window_inp.geometry("600x700")
                        new_window_inp.state("zoomed")
                        new_window_inp.title("Data for the pie charts")


                        new_window_inp.iconbitmap("mainpie.ico")


                        #new_window_inp.resizable(0,0)

                        list_inp_1_entry = list()
                        list_inp_entry_1 = list()
                        list_inp_names_entry = list()
                        list_inp_names_entry_1 = list()

                        for i_nou in range(0,e_aux,1):
                            copie_i = str(i_nou+1)

                            label_color_line_c = tk.Label(new_window_inp , text = "                                      Percent for label " + copie_i + " :   ")               
                            label_color_line_c['bg'] = "#4b6cb7"
                            #label_s.place(relx = 0.5 , rely = 0.6 , anchor = "nw")
                            label_color_line_c.grid(column = 13 , row = i_nou + 6 )
                            label_color_line_font_c = font.Font(family = "Times" , size = 8)
                            label_color_line_c['font'] = label_color_line_font_c 

                            inp_1 = tk.Entry(new_window_inp , width = 3)
                            inp_1.grid(column=17 , row=i_nou + 6)
                            list_inp_entry_1.append(inp_1)

                            label_names = tk.Label(new_window_inp , text = "   Name : " )
                            label_names['bg'] = "#4b6cb7"
                            label_names.grid(column = 20 , row = i_nou + 6 )
                            label_names_font = font.Font(family = "Times" , size = 8)
                            label_names['font'] = label_names_font

                            inp_names = tk.Entry(new_window_inp , width = 10)
                            inp_names.grid(column = 23 , row = i_nou + 6)
                            list_inp_names_entry.append(inp_names)

                            

                        def btn_inp_cmd():

                          def is_number_1(s):
                                  try:
                                      float(s)
                                      return True
                                  except ValueError:
                                      return False

                          ok = 1
                          for c in range(0,len(list_inp_entry_1),1):
                              inp_1_get = list_inp_entry_1[c].get()
                              if is_number_1(inp_1_get)==False or inp_1_get == "": 
                                      ok = 0 
                              if ok :
                               inp_1_get = float(inp_1_get)
                               list_inp_1_entry.append(inp_1_get)
                              else :
                                tk.messagebox.showerror("Error" , "One or more inputs are empty or have bad contents ! ")
                                new_window_inp.destroy()
                          
                          ok1 = 1
                          for d in range(0,len(list_inp_names_entry),1):
                              inp_names_get = list_inp_names_entry[d].get()
                              if inp_names_get.isalnum()==0 or inp_names_get == "":
                                    ok1 = 0 
                              if ok1 :
                               list_inp_names_entry_1.append(inp_names_get)
                              else :
                                tk.messagebox.showerror("Error" , "One or more inputs are empty or have bad contents ! ")
                                new_window_inp.destroy()


                          if ok and ok1 :
                           new_window_inp.destroy()
                           plt.pie(list_inp_1_entry , labels = list_inp_names_entry_1)
                           plt.show()

                          
                            

                        btn_inp = tk.Button(new_window_inp , text = "Create Pie Chart" , width = 25 , height = 1 , fg = "blue" , bg = "lightblue" , bd = 3 , command = btn_inp_cmd )
                        btn_inp['font'] = "Times"
                        btn_inp.place(relx = 0.4 , rely = 0.9)

     else:
         if e_pie == "":
           tk.messagebox.showerror("Error" , "Please insert a number !") 
           new_window_1.destroy()
         if e_pie.isalpha():
             tk.messagebox.showerror("Error" , "Please insert a number !") 
             new_window_1.destroy()
         if e_pie.isalnum():
             tk.messagebox.showerror("Error" , "Please insert a number !")
             new_window_1.destroy()

         
  
  Button_1(new_window_1 , "Insert percents" , 20 , 1 , "blue" , "lightblue" , 3 , "Times" , pie_cmd , 18 , "center" , 0.5 , 0.6 )

  new_window_1.mainloop()

def Button_1(window , text_1 , width_1 , height_1 , fg_1 , bg_1 , bd_1 , font_1 , command_1 , font_size , ancora , relx_1  , rely_1 ):
    myFont = font.Font(family=font_1 , size = font_size)
    btn = tk.Button(window , text = text_1 , width = width_1 , height = height_1 ,fg = fg_1 , bg = bg_1 , bd = bd_1 , command = command_1 )
    btn['font'] = myFont
    btn.place( relx = relx_1, rely = rely_1  , anchor=ancora )
    return btn

def help(): 
 res = tk.messagebox.askquestion("Confirm" , "Do you want to get documentation ? ")
 if res == "yes" :
   webbrowser.open('documentation.html', new=2)




photo = PhotoImage(file = "qm.png" )

photoimage_1 = photo.subsample(1,1)

help_btn = tk.Button(window , image = photoimage_1  , bd = 0 , command = help)
help_btn.place(relx = 0.96 , rely = 0.0093 )

Button_1(window , "New Graph" , 25 , 1  , "blue" , "lightblue" , 3 , "Times" , New_Graph , 18 , "center" , 0.5 , 0.3)

Button_1(window , "New Pie Chart" , 25 , 1 ,  "blue" , "lightblue" , 3 , "Times" , New_Pie_Chart , 18 , "center" , 0.5 , 0.5)



window.mainloop()