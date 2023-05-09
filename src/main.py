import requests
import tkinter
from PIL import ImageTk, Image
class Window():
    """ <a target="_blank" href="https://icons8.com/icon/B66tBXIKOwR9/chuck-norris">Chuck Norris</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>."""
    def __init__(self):
        self.fp = "ChuckNorris.png"
        self.initUI()
    def initUI(self):
        self.master = tkinter.Tk()
        self.master.title("Chuck Norris Facts")
        self.master.geometry("170x280")
        self.image = ImageTk.PhotoImage(Image.open(self.fp))
        self.norris_image = tkinter.Label(
                                        self.master, 
                                        image=self.image)
        self.norris_image.pack(side=tkinter.TOP)
        self.fact_label = tkinter.Message(self.master)
        self.fact_label.pack(side=tkinter.TOP)
        buttons_frame = tkinter.Frame(self.master)
        buttons_frame.pack(side=tkinter.BOTTOM, padx=10, pady=10)
        closeButton = tkinter.Button(buttons_frame, text="Close", command=self.master.quit)
        closeButton.pack(side=tkinter.RIGHT, padx=(10, 0))       
        newButton = tkinter.Button(buttons_frame, text="New", command= lambda : self.settext(get_fact()))
        newButton.pack(side=tkinter.LEFT, padx=(0, 10))     
        self.master.mainloop()  
    def settext(self, text):
        self.fact_label.config(text=text)
def get_fact():
    response = requests.get("https://api.chucknorris.io/jokes/random").json()
    return response["value"]
if __name__=="__main__":
    Window()
