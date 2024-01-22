from customtkinter  import *
from PIL import ImageTk, Image

app = CTk()

app.geometry("1920x1080")
set_appearance_mode("system")
app.title('Chatbot Python')

my_image = ImageTk.PhotoImage(Image.open("ok.jpg"))
l1 = customtkinter.CTkLabel(master=app, image=my_image  )
##button = CTkButton(app, text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",)
##button.place(relx=0.5,rely=0.5, anchor="center",)

app.mainloop()