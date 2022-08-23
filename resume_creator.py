from tkinter import *
from tkinter import ttk
from handlers.file_writer import analysis_reporter, write_resume

# def ajd():
#     try:
#         meters.set('It so totally completely\n worked \tas \n\n\n\expected!')
#     except ValueError:
#         pass
#
# output_path = './output/'
#
# root = Tk()
# root.title("Resume Tailor")
#
# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
# 
# resume_file = StringVar()
# resume_file_entry = ttk.Entry(mainframe, width=15, textvariable=resume_file)
# resume_file_entry.grid(column=2, row=1, sticky=(W, E))
#
# input_path = './input/jds/'
#
# ttk.Label(mainframe, text=input_path).grid(column=2, row=2, sticky=(W, E))
#
# ttk.Button(mainframe, text="Write Resume", command=write_resume(input_path)).grid(column=3, row=3, sticky=W)
# ttk.Button(mainframe, text="Analyze Job Posts", command=ajd).grid(column=1, row=3, sticky=W)
#
# ttk.Label(mainframe, text="Input file path:").grid(column=1, row=2, sticky=W)
#
# for child in mainframe.winfo_children():
#     child.grid_configure(padx=5, pady=5)
#
# resume_file_entry.focus()
# root.bind("<Return>", write_resume)
#
# root.mainloop()
