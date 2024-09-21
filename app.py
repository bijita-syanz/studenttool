import os 
import appreq as appreq
import tkinter
import ttkbootstrap as ttk 
from tkinter import messagebox , filedialog
import webbrowser

file_opend = False
file_runing = False
def get_relative_path(path) :
    lenpath = len(path)
    for i in range (1,lenpath):
        char = path[(lenpath-i):((lenpath-i)+1)]
        if char == "/" :
            return path[lenpath-i+1 : lenpath]
        

def get_relative_path_from_directory(path , directory_path):
    path = path[len(directory_path)+1:len(path)]
    return path

def open_file():
        global file_path
        file_path = filedialog.askopenfilename(defaultextension=".html",
                                               filetypes=[("HTML files", "*.html"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                textairia.delete(index1="1.0" , index2="end")
                textairia.insert("end", content)
        if len(get_relative_path(file_path)) > 22 :
            rl_file_path = f"{get_relative_path(file_path)[0:22]}..."
        else :
            rl_file_path = get_relative_path(file_path)
        add_page_label.configure(text=rl_file_path)
        global file_opend
        file_opend = True
        
def update_file():
        if file_path :
            with open(file_path, 'r') as file:
                content = file.read()
                textairia.delete(index1="1.0" , index2="end")
                textairia.insert("end", content)
        else :
            print("error ther is no opend file")
            messagebox.showerror("error" , "error : ther is no opend file ! " )

        
def add_page() :

    filename = new_file_entry.get()
    titel = titel_entry.get()
    if filename == '' or titel== '' :
        print("error ther is a empty entry")
        messagebox.showerror("error" , "error : ther is an empty entry ! " )
        return False
    htmlfile = f"{filename}.html"
    with open(htmlfile , "+a") as htmlfile1:
        htmlfile1.write(appreq.Titel(titel))
    file_path = htmlfile
    if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                textairia.delete(index1="1.0" , index2="end")
                textairia.insert("end", content)
    if len(filename) > 22 :
        filename = f"{filename[0:20]}..."
    else :
        filename = f"{filename}.html"
    add_page_label.configure(text=f"{filename}")
    global file_opend
    file_opend = True

def add_post():
    
    htmlfile = file_path
    titel = post_titel_entry.get()
    if htmlfile == '' or titel =='' :
        print("error : ther is an empty entry ")
        messagebox.showerror("error" , "error : ther is an empty entry " )
        return False
    else :
        pass
    with open(htmlfile ,"+a") as file :
        file.write(appreq.media.add_post_titel(titel))
    update_file()

def add_cours():
    htmlfile = file_path
    name = cour_titel_entry.get()
    file = add_file_entry.get()
    if htmlfile == "" or name == "" :
        print("ther is an empty entry :")
        messagebox.showerror("error" , "error : ther is an empty entry " )
        return False 
    else :
        pass
    if htmlfile[len(htmlfile)-5 : len(htmlfile)] == ".html":
        pass
    else :
        htmlfile = f"{htmlfile}.html"
        
    file = f"2bac_cours\{file}"

    with open(htmlfile , "+a") as htmlfile :
        htmlfile.write(appreq.media.add_cour_in_post(file , name))
    update_file()

def close_post():
    file =  file_path
    if file == "" :
        print("error :ther is an empty entry ")
        messagebox.showerror("error" , "error : ther is an empty entry " )
        return False
    else :
        pass
    if file[len(file)-5 : len(file)] == ".html":
        pass
    else :
        file = f"{file}.html"
    with open(file , "+a") as html :
        html.write(appreq.media.colse_post())
    update_file()

def save_to_new():
    saving_file_path = new_file_entry.get()
    if saving_file_path:
            with open(file_path, 'w') as file:
                content = textairia.get(1.0, ttk.END)
                file.write(content)

    return messagebox.showinfo("alert" , f"file saved seccesfully to {file_path}")

def browse_new_file():
    saving_file_path = filedialog.askopenfilename(defaultextension=".html",
                                               filetypes=[("HTML files", "*.html"), ("All files", "*.*")])
    if saving_file_path:
            with open(file_path, 'w') as file:
                content = textairia.get(1.0, ttk.END)
                file.write(content)

    return messagebox.showinfo("alert" , f"file saved seccesfully to {file_path}")

def save_file():

    

    #file_path1 = filedialog.asksaveasfilename(defaultextension=".html",
    #                                        filetypes=[("HTML files", "*.html"), ("All files", "*.*")])
    if file_opend == True:
        with open(file_path, 'w') as file:
            content = textairia.get(1.0, ttk.END)
            file.write(content)
        messagebox.showinfo("alert" , f"file saved seccesfully to {file_path}")
    elif file_opend == False :
        save_window = ttk.Window(themename="darkly")
        save_window.geometry("300x40")
        new_file_frame = ttk.Frame(master=save_window)
        new_file_frame.grid(column=0 , row=0)
        browse_file_fram = ttk.Frame(master=save_window)
        browse_file_fram.grid(column=1 , row=0)
        entry = ttk.Entry(master=new_file_frame ,width=20)
        saving_button = ttk.Button(master=new_file_frame , text="save" , command=save_to_new)
        entry.grid(column=0 , row=0 )
        saving_button.grid(column=1 , row=0)

        browse_botton = ttk.Button(master=browse_file_fram , text="browse" , command=browse_new_file )
        browse_botton.grid(column=0 , row=0)

        while main_runing == True:
            save_window.mainloop()
            


def preview_file():
    if file_path :
        
        webbrowser.open(f'file://{os.path.abspath(temp_file)}')
    else :
        html_content = textairia.get(1.0, ttk.END)
        temp_file = 'temp_preview.html'
        with open(temp_file, 'w') as file:
            file.write(html_content)
        webbrowser.open(f'file://{os.path.abspath(temp_file)}')

#view :
def change_theme() :
    theme = selected_option.get()
    if theme == "NoN" :
        pass 
    elif theme == "darck":
        with open("setings.txt"  , "w") as stfile:
            stfile.write('darkly')
    elif theme == "light" :
        with open("setings.txt"  , "w") as stfile:
            stfile.write('')
    return True


def change_view():

    global selected_option

    change_view_window = ttk.Window()
    change_view_window.geometry("360x240")
    selected_option = ttk.StringVar()
    selected_option.set("NoN") 
    options = ["normal", "darck" , "light" ]
    new_theme = ttk.OptionMenu(change_view_window , selected_option, *options)
    new_theme.pack( pady=10)
    set_button = ttk.Button(master=change_view_window , text="set theme" , command=appreq.chnage_them)
    set_button.pack( pady=10)



#window :
with open("setings.txt" , "r") as  stfile :
    them =stfile.readline(6)
main = ttk.Window(themename="darkly")
main.title("html IDE")
#add page part
nav_bar = ttk.Frame(main )

nav_bar.grid(column=0 , row=0)
add_page_label = ttk.Label(master=nav_bar , text="add page" , font="calibri 15 bold" , justify="left")
add_page_label.grid(column=0 , row=0)
adding_frame = ttk.Frame(main )
adding_frame.grid(column=0 , row=1)
new_file_label = ttk.Label(adding_frame , text="creat html file" , font="calibri 10 bold")
new_file_entry = ttk.Entry(adding_frame , width=30)
new_file_label.grid(column=1 , row=0 , padx=3)
new_file_entry.grid(column=1 , row=1 , padx=3)
titel_label = ttk.Label(adding_frame , text="titel" , font="calibri 10 bold")
titel_entry = ttk.Entry(adding_frame , width=30)
titel_label.grid(column=2 , row=0 , padx=3)
titel_entry.grid(column=2 , row=1 , padx=3)
render_button = ttk.Button(adding_frame , text="creat " , command=add_page , width=20)
render_button.grid(column=3 , row=1 , padx=3)

#add post part
post_titel_label = ttk.Label(adding_frame , text='post titel' , font="clibri 10 bold")
post_titel_label.grid(column=1 , row=2 ,padx=3)
post_titel_entry = ttk.Entry(adding_frame , width=30)
post_titel_entry.grid(column=1 , row=3, padx=3)
add_post_button = ttk.Button(master=adding_frame , text="add post"  , command=add_post , width=20)
add_post_button.grid(column=2 , row=3 , padx=13)
close_post_buttom = ttk.Button(master=adding_frame , text="close post" , command=close_post , width=20)
close_post_buttom.grid(column=3 , row=3)

# add post contente
cour_titel_label = ttk.Label(adding_frame , text='cour titel' , font="clibri 10 bold")
cour_titel_label.grid(column=1 , row=4 ,padx=3)
cour_titel_entry = ttk.Entry(adding_frame , width=30)
cour_titel_entry.grid(column=1 , row=5, padx=3)
add_file_label = ttk.Label(adding_frame , text="add file" , font="calibri 10 bold")
add_file_entry = ttk.Entry(adding_frame , width=30)
add_file_label.grid(column=2 , row=4 , )
add_file_entry.grid(column=2 , row=5 , padx=3)
add_cour_button = ttk.Button(master=adding_frame , text="add cours"  , command=add_cours , width=20)
add_cour_button.grid(column=3 , row=5 , padx=3)

#terminale :
textairia = ttk.ScrolledText(main, wrap='word', undo=True, height=35, width=100)
textairia.grid(column=1 , row=1)
render_html_form = ttk.Frame(main)
render_html_form.grid(column=1 , row=0)
save_button =   ttk.Button(master=nav_bar , text="save file"    , command=save_file )
open_button =   ttk.Button(master=nav_bar , text="open file"    , command=open_file )
run__button =   ttk.Button(master=nav_bar , text="run file "    , command=preview_file )
update_button = ttk.Button(master=nav_bar , text="update file " , command=update_file )
view_menu = ttk.Menubutton(master=nav_bar , text="view" )
chose_them = ttk.Button(master=view_menu , text="chnage theme" , command=change_view)

open_button.grid(column=1 , row=0 , padx=4)
save_button.grid(column=2 , row=0 , padx=4)
run__button.grid(column=3 , row=0 , padx=4)
update_button.grid(column=4 , row=0 , padx=4)
view_menu.grid(column=5 , row=0 , padx=4)
chose_them.pack()
main_runing = True
main.mainloop()
main_runing = False
