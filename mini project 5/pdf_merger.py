import os
import tkinter as tk

# tkinter is a built-in library in Python for creating GUI applications.
# It provides a set of tools and widgets to build graphical user interfaces.
from tkinter import filedialog, messagebox
from pypdf import PdfWriter

selected_files = []


def merge_pdfs(pdf_paths, output_path):
    merger = PdfWriter()
    for pdf in pdf_paths:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()


def select_pdfs():
    files = filedialog.askopenfilenames(
        title="Select PDF files",
        filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")),
    )
    if not files:
        return

    selected_files.clear()
    selected_files.extend(files)

    listbox.delete(
        0, tk.END
    )  # tk.END is to clear the previous listbox content before adding new files
    for file_path in files:
        listbox.insert(tk.END, os.path.basename(file_path))

    status_var.set(f"{len(files)} file(s) selected")


def merge_files():
    if not selected_files:
        messagebox.showwarning(
            "No files selected", "Please select at least one PDF file."
        )
        return

    default_name = "merged.pdf"
    if selected_files:
        default_name = (
            os.path.splitext(os.path.basename(selected_files[0]))[0] + "_merged.pdf"
        )

    output_path = filedialog.asksaveasfilename(
        initialfile=default_name,
        defaultextension=".pdf",
        filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")),
    )

    if not output_path:
        return

    try:
        merge_pdfs(selected_files, output_path)
        messagebox.showinfo(
            "Success", f"PDF files merged successfully.\nSaved to:\n{output_path}"
        )
    except Exception as exc:
        messagebox.showerror("Error", f"Something went wrong:\n{exc}")


# created window
root = tk.Tk()
root.title("PDF Merger")
root.geometry("500x300")
root.resizable(True, True)


# giving widgets
select_btn = tk.Button(root, text="Select PDFs", width=20, command=select_pdfs)
# pady is the vertical paading, padx is the horizontal padding
select_btn.pack(pady=(20, 10))

listbox = tk.Listbox(root, width=100, height=10)
listbox.pack(padx=20, pady=5)

status_var = tk.StringVar(value="No file selected")
status_label = tk.Label(root, textvariable=status_var, fg="black")
status_label.pack(pady=10)

merge_btn = tk.Button(
    root, text="Merge PDFs", width=20, command=merge_files, bg="blue", fg="white"
)
merge_btn.pack(pady=5)

# run the main loop
root.mainloop()
