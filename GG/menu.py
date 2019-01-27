import tkinter as tk
from GlassesGang import liveFilters, stillFilters

def run():
    root = tk.Tk()

    root.title("Glasses Gang")

    v  = tk.IntVar()
    v2 = tk.StringVar(root)
    v3 = tk.StringVar(root)

    filepath = {
        "Orange Sunglasses" : "Costumes/glasses.png",
        "Heart Sunglasses" : "Costumes/hearts.png",
        "Mad Goggles" : "Costumes/madgoggles.png",
        "Top Hat" : "Costumes/tophat.png",
        "Party Hat" : "Costumes/partyhat.png",
        "Star" : "Costumes/starhat.png",
        "Green Mohawk" : "Costumes/hair.png",
        "Bunny Ears" : "Costumes/bunnyears.png",
        "None" : "Costumes/null.png",
        }

    def Output():    
        if v.get() == 1:
            liveFilters(
                v3.get() != "None", v2.get() != "None", filepath.get(v3.get()), filepath.get(v2.get()))
        else:
            stillFilters(
                v3.get() != "None", v2.get() != "None", filepath.get(v3.get()), filepath.get(v2.get()), filePathE.get())


    tk.Label(root,text="File path of image:").grid(row=2,column=0)
    filePathE = tk.Entry(root)
    filePathE.grid(row=2,column=1,sticky=tk.W)

    v.set(0)

    tk.Label(root,text="Choose Live or Still photo:").grid(row=0,column=0,sticky=tk.W)
    liveButton = tk.Radiobutton(root,text="Live",variable=v,value=1,command=lambda:filePathE.config(state='disabled')).grid(row=1,column=0)
    stillButton = tk.Radiobutton(root,text="Still",variable=v,value=2,command=lambda:filePathE.config(state='normal')).grid(row=1,column=1,sticky=tk.W)

    v2.set("Orange Sunglasses")

    tk.Label(root,text="Choose Sunglasses:").grid(row=3,column=0,sticky=tk.W)
    Hat = tk.OptionMenu(root,v2,"Orange Sunglasses","Heart Sunglasses","Mad Goggles","None")
    Hat.grid(row=3,column=1, sticky=tk.W)

    v3.set("Top Hat")

    tk.Label(root,text="Choose Hat:").grid(row=4,column=0,sticky=tk.W)
    Sunglasses = tk.OptionMenu(root,v3,"Top Hat","Party Hat","Star","Green Mohawk","Bunny Ears" ,"None")
    Sunglasses.grid(row=4,column=1, sticky=tk.W)


    tk.Label(root,text="If Live Pic is selected, then press esc key to stop program, press P key to take photo").grid(row=8,sticky=tk.SW)
    quitButton = tk.Button(root,text="Quit",command=root.destroy).grid(row=7,column=3,sticky=tk.W)
    okButton = tk.Button(root,text="Ok",command=Output).place(x=240,y=129)


    root.mainloop()
        
if __name__ == "__main__":
    run()
