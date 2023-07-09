import tkinter as tk
import webbrowser
ques = ""
def Gui():
    course = course_entry.get()
    source = source_var.get()

   
    source_urls = {
        
        "YouTube ": "https://www.youtube.com/"
    }

    if source in source_urls:
        url = source_urls[source]
        webbrowser.open_new(url)
    else:
        print("Invalid source selected")

window = tk.Tk()
window.title("Course Enquiry Form")

course_label = tk.Label(window, text= "question")
course_label.pack()
course_entry = tk.Entry(window)
course_entry.pack()

source_label = tk.Label(window, text="Source:")
source_label.pack()

f=open("backend.txt","+a")
f.writelines(["Question ",ques])

source_var = tk.StringVar()

youtube_radio = tk.Radiobutton(window, text="YouTube ", variable=source_var, value="YouTube ")
youtube_radio.pack()

submit_button = tk.Button(window, text="Submit", command=Gui)
submit_button.pack()

window.mainloop()
