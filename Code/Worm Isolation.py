from tkinter import *
from tkinter import ttk
import networkx as nx
from edge_list import *
import matplotlib.pyplot as plt
from deletion_no import *




global graph
graph = nx.Graph()
global i
i=0
global j
j=0
global nodes_list_x
nodes_list_x = []
global nodes_list_y
nodes_list_y = []
global edges_li
edges_li = []
class creation:
    def __init__(self):
        self.root = Tk()
        self.root.title("Worm Isolation")
        self.root.minsize(1200,900)
        self.canvas = Canvas(self.root, width=1200, height=900, borderwidth=0, highlightthickness=0, bg="black")
        self.canvas.place(x=0, y=0, in_=self.root)
        self.labelTop = Label(self.root, text = "Choose")
        self.labelTop.place(x=0,y=0,in_=self.root)
        self.my_choice = StringVar()
        self.commbox = ttk.Combobox(self.root, width=15, textvariable = self.my_choice)
        self.commbox['values'] = ("Nodes Creation", "Edges Creation", "Worm Attack")
        self.commbox.place(x=80, y=0, in_=self.root)
        self.button = ttk.Button(self.root, text = "Click Me", command = self.chosen)
        self.button.place(x=240,y=0,in_=self.root)
        self.button  = []
        self.lines = []
        self.root.mainloop()
    def nodes_creation(self,event):
        global i
        i = i+1
        print("node created at", event.x, event.y)
        self.button.append(self.canvas.create_oval(event.x, event.y, event.x+50, event.y+50, fill="blue"))
        self.canvas.create_text((event.x+25), (event.y+25), fill="white", font=("Pursia",20), text=i)
        global nodes_list_x
        m = int(event.x)+25
        nodes_list_x.append(m)
        global nodes_list_y
        n = int(event.y)+25
        nodes_list_y.append(n)
        print(nodes_list_x,nodes_list_y)
        global graph
        graph.add_node(i)
        print(graph.nodes())

    def edges_creation(self):
        for i in range(len(self.button)):
            self.canvas.tag_bind(self.button[i],"<1>", func_list[i])
        if(len(edges_list)==0):
            pass
        else:
            if(len(edges_list)%2==0):
                while(True):
                    global j
                    global edges_li
                    try:
                        edges_li.append((edges_list[j],edges_list[j+1]))
                    except:
                        pass
                    
                    if(j<len(edges_list)):
                        j=j+2
                        
                    else:
                        break

                global graph
                graph.add_edges_from(edges_li)
                print(nx.edges(graph))
                
                i = 0
                while(True):
                    print(len(edges_li))
                    global nodes_list_x
                    global nodes_list_y
                    try:
                        self.lines.append(self.canvas.create_line(nodes_list_x[edges_list[i]-1], nodes_list_y[edges_list[i]-1], nodes_list_x[edges_list[i+1]-1], nodes_list_y[edges_list[i+1]-1], fill="white"))
                    except:
                        pass
                   
                    if(i<len(edges_list)):
                        i=i+2
                    else:
                        break

            else:
                pass

    def worm_attack(self):
        for i in range(len(self.button)):
            self.canvas.tag_bind(self.button[i],"<1>", func_list1[i])

        for k in range(len(deletion_nodes)):
            
            neighbors = list(graph.neighbors(deletion_nodes[k]))
            print(neighbors)
            for i in range(len(neighbors)):
                global nodes_list_x
                global nodes_list_y
                graph.remove_edge(deletion_nodes[k],neighbors[i])
                self.canvas.create_line(nodes_list_x[deletion_nodes[k]-1], nodes_list_y[deletion_nodes[k]-1], nodes_list_x[neighbors[i]-1], nodes_list_y[neighbors[i]-1],fill="red")    
                if(len(neighbors)>1):
                    graph.add_edge(neighbors[i],neighbors[i+1])
                    self.canvas.create_line(nodes_list_x[neighbors[i]-1], nodes_list_y[neighbors[i]-1], nodes_list_x[neighbors[i+1]-1], nodes_list_y[neighbors[i+1]-1], fill = "white")
        
    def chosen(self):
        if(self.my_choice.get()=="Nodes Creation"):
            self.canvas.unbind("<Button-1>")
            self.canvas.bind("<Button-1>", self.nodes_creation)

        if(self.my_choice.get()=="Edges Creation"):
            self.canvas.unbind("<Button-1>")
            self.edges_creation()

        if(self.my_choice.get()=="Worm Attack"):
            self.canvas.unbind("<Button-1>")
            self.worm_attack()

C1 = creation()


