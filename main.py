import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()  # this is like int main in c++

canvas = tk.Canvas(root,width = 600, height = 300)
canvas.grid(columnspan = 3,rowspan = 3)

#keeping the logo
logo = Image.open('D:\projects\Tkinter\PDFextract_text\starterFiles\logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column = 1,row = 0)

#instructions
instructions = tk.Label(root, text = "Select a PDF file to extract")
instructions.grid(columnspan = 3,column = 0,row = 1)

def open_pdf():
    browse_text.set("Loading...")
    file = askopenfile(parent = root,mode = 'rb',title = "Choose a file",filetype = [("Pdf file","*.pdf")])
    if file:
        readpdf = PyPDF2.PdfFileReader(file)
        page = readpdf.getPage(0)
        page_content = page.extractText()
        
        #print in a textbox
        textbox = tk.Text(root,height = 10,width = 50,padx = 15,pady = 15)
        textbox.insert(1.0,page_content)
        # textbox.tag_configure("center",justify = "center")
        # textbox.tag_add("center",1.0,"end")
        textbox.grid(column = 1,row = 3)

        browse_text.set("Browse")

#button
browse_text = tk.StringVar()
browse_button = tk.Button(root,textvariable = browse_text,command = lambda:open_pdf())
browse_text.set("Browse")
browse_button.grid(column = 1,row = 2)

canvas = tk.Canvas(root,width = 600, height = 300)
canvas.grid(columnspan = 3)

root.mainloop() #this is like return 0; in c++ i.e, end of the main fxn