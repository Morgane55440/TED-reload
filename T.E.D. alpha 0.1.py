      #Projet d'ISN
from tkinter import *
from random import randint
from math import floor
from tkinter.messagebox import *
import socket
import threading
import json

tile_y_size = 32
tile_x_size = 32
outside_tile = tile(tile_type(False, None, None, None), None, None, self.canvas, 0)

class game:
      def __init__(self, world_map):
            self.world_map = world_map
            
            
 class game_map:
      def __init__(self, map_file, canvas):
            self.canvas = canvas
            with open("map.json",mode='r')as map_list:
                  self.t_types = [tile_type(t[0], t[1], t[2], t[3]) fo t in map_list[0]]
                  self.world_map = [[tile(self.t_types[tile[0]], x * tile_x_size + 1, y * tile_y_size + 1, self.canvas, tile[1]) for x, tile in enumerate(col)] for y, col in enumerate(map_list[1])]
            self.x_size = len(self.world_map[0])
            self.y_size = len(self.world_map)
      def tile_get(self, x, y):
            if x < 0 || x >= self.x_size || y < 0 || y >= self.y_size:
                  return outside_tile
            return self.world_map[x][y]
            
            
class tile_type:
      def __init__(self, filename, iswalkable, health_var, mana_var):
            self.iswalkable = iswalkable
            self.health_var = health_var
            self.mana_var = mana_var
            self.texture= PhotoImage(file=filename)
            
class renderable:
      def __init__(self, xpos, ypos, sprite, canvas, shown = False):
            self.sprite = sprite
            self.xpos = xpos
            self.ypos = ypos
            self.canvas = canvas
            self.render = None
            if shown:
                  self.show()
      def show(self):
            if !self.is_rendered():
                  self.render = self.canvas.create_image(self.xpos, self.ypos, image=self.sprite, anchor = "nw")
      def hide(self):
            if self.is_rendered():
                  self.canvas.delete(self.render)
      def is_rendered(self):
            return self.render != None
      def move(self, **pos):
            self.xpos, self.ypos = pos.get("x", self.xpos), pos.get("y", self.ypos)
            if self.is_rendered():
                  self.canvas.coord(self.render, self.xpos, self.ypos)
            
class tile(renderable):
      def __init__(self, t_type, xcoord, ycoord, canvas, availability):
            self.t_type = t_type
            renderable.__init__(xpos, ypos, self.t_type.texture, canvas, True)
            self.availability = availability
            
            
class player(renderable):
      def __init__(self, world_map, class_file):
            with open(class_file,mode='r')as class:
                  gvalue[4][0]=json.load(server_class)
                  
                  
class stat:
      def __init__(self, init_value, **kwargs):
            self.max = kwargs.get("max", None)
            self.change_rate = kwargs.get("change_rate", 0)
            self.can_go_negative = kwargs.get("negative", False)
            self.value = init_value if self.negative else max(init_value, 0)
      def add(self, change):
            self.value += change
            if self.value < 0 and !self.can_go_negative:
                  self.value = 0
            else if self.value > self.max:
                  self.value = self.max
      def sub(self, change):
            self.add(-change)
      def update(self):
            self.add(self.change_rate)
      def is_zero(self):
            return self.value == 0
      def is_max(self):
            return self.max != None and self.value == self.max
       

def deplacement(target,x,y):
    #print(type(gvalue[4][target][7]),gvalue[4][target][7])
    gvalue[2].coords(gvalue[4][target][7],x*32,y*32)
    #fenhg.update()
    gvalue[4][target][1][3]+=gvalue[1][0][gvalue[1][1][x][y][0]][2]
    gvalue[4][target][2][3]+=gvalue[1][0][gvalue[1][1][x][y][0]][3]
    statupdate()

def dep_bas(target):
    success=False
    if gvalue[4][target][5][1]!=20:
        if gvalue[1][0][gvalue[1][1][gvalue[4][target][5][0]][gvalue[4][target][5][1]+1][0]][1] and (gvalue[4][target][5][0],gvalue[4][target][5][1]+1)!=(gvalue[4][(target-1)**2][5][0],gvalue[4][(target-1)**2][5][1]):
            gvalue[4][target][5][1]+=1
            deplacement(target,gvalue[4][target][5][0],gvalue[4][target][5][1])
            success=True
    return success
        
def dep_haut(target):
    success=False
    if gvalue[4][target][5][1]!=0:
        if gvalue[1][0][gvalue[1][1][gvalue[4][target][5][0]][gvalue[4][target][5][1]-1][0]][1] and (gvalue[4][target][5][0],gvalue[4][target][5][1]-1)!=(gvalue[4][(target-1)**2][5][0],gvalue[4][(target-1)**2][5][1]):
            gvalue[4][target][5][1]+=-1
            deplacement(target,gvalue[4][target][5][0],gvalue[4][target][5][1])
            success=True
    return success

def dep_gauche(target):
    success=False
    if gvalue[4][target][5][0]!=0:
        if gvalue[1][0][gvalue[1][1][gvalue[4][target][5][0]-1][gvalue[4][target][5][1]][0]][1] and (gvalue[4][target][5][0]-1,gvalue[4][target][5][1])!=(gvalue[4][(target-1)**2][5][0],gvalue[4][(target-1)**2][5][1]):
            gvalue[4][target][5][0]+=-1
            deplacement(target,gvalue[4][target][5][0],gvalue[4][target][5][1])
            success=True
    return success
  
def dep_droite(target):
    success=False
    if gvalue[4][target][5][0]!=39:
        if gvalue[1][0][gvalue[1][1][gvalue[4][target][5][0]+1][gvalue[4][target][5][1]][0]][1] and (gvalue[4][target][5][0]+1,gvalue[4][target][5][1])!=(gvalue[4][(target-1)**2][5][0],gvalue[4][(target-1)**2][5][1]):
            gvalue[4][target][5][0]+=1
            deplacement(target,gvalue[4][target][5][0],gvalue[4][target][5][1])
            success=True
    return success
    
def skill(user,target,cost,attack):
    gvalue[4][user][2][3]+=cost
    if attack<=0:
        if gvalue[4][target][3][0]<=-attack:
            attack+=gvalue[4][target][3][0]
        else:
            attack=0
    gvalue[4][target][1][3]+=attack
    statupdate()

def endturn(target):
    gvalue[4][target][1][3]+=gvalue[4][target][1][2]
    gvalue[4][target][2][3]+=gvalue[4][target][2][2]
    gvalue[4][target][3][3]=gvalue[4][target][3][1]
    statupdate()
    
def no_attack_input_treatment(action,user,user_turn):
    if action=="up" or action=="down" or action=="right" or action=="left":
        if gvalue[4][user][3][3]!=0:
            if action=="up":
                if dep_haut(user):
                    print_if_true("déplacement effectué",user_turn)
                    gvalue[4][user][3][3]+=-1
                else:
                    print_if_true("déplacement impossible",user_turn)
            if action=="down":
                if dep_bas(user):
                    print_if_true("déplacement effectué",user_turn)
                    gvalue[4][user][3][3]+=-1
                else:
                    print_if_true("déplacement impossible",user_turn)
            if action=="right":
                if dep_droite(user):
                    print_if_true("déplacement effectué",user_turn)
                    gvalue[4][user][3][3]+=-1
                else:
                    print_if_true("déplacement impossible",user_turn)
            if action=="left":
                if dep_gauche(user):
                    print_if_true("déplacement effectué",user_turn)
                    gvalue[4][user][3][3]+=-1
                else:
                    print_if_true("déplacement impossible",user_turn)
        else:
            print_if_true("vous avez dépensé tous vos points de mouvements",user_turn)
    if action=="surrender":
        print_if_true("vous avez abandonné",user_turn)
        gvalue[5]=True
        if gvalue[0]==2:
            gvalue[6]=2-user
    if action=="end":
        endturn(user)
        print("fin de tour")
        gvalue[5]=True
        
def print_if_true(txt,printingorder):
    if printingorder:
        print(txt)

def classloading(server_file,client_file):
    with open(server_file,mode='r')as server_class:
        gvalue[4][0]=json.load(server_class)
    with open(client_file,mode='r')as client_class:
        gvalue[4][1]=json.load(client_class)
        
def statupdate():
    for k in range (2):
        for i in range (1,3):
            if gvalue[4][k][i][3]>=gvalue[4][k][i][1]:
                gvalue[4][k][i][3]=gvalue[4][k][i][1]
            elif gvalue[4][k][i][3]<=0:
                gvalue[4][k][i][3]=0
                if gvalue[0]==2 and i==1:
                    gvalue[6]=2-k
    gvalue[3][0][2]=(gvalue[4][gvalue[0]-2][1][3])/gvalue[4][gvalue[0]-2][1][1]
    gvalue[3][1][2]=(gvalue[4][gvalue[0]-2][2][3])/gvalue[4][gvalue[0]-2][2][1]
    gvalue[3][0][3]=gvalue[4][gvalue[0]-2][1][0]," : ",floor(gvalue[3][0][2]*100),"percents"
    gvalue[3][1][3]=gvalue[4][gvalue[0]-2][2][0]," : ",floor(gvalue[3][1][2]*100),"percents"
    gvalue[2].coords(gvalue[3][0][0],32,32*21.5,32+320*gvalue[3][0][2],32*22.25)
    gvalue[2].coords(gvalue[3][1][0],32,32*22.75,32+320*gvalue[3][1][2],32*23.5)
    gvalue[2].itemconfig(gvalue[3][0][1], text=gvalue[3][0][3])
    gvalue[2].itemconfig(gvalue[3][1][1], text=gvalue[3][1][3])
    fenhg.update

def close():
    if askyesno("Quit","Do you really want to quit the game ?"):
            fen.destroy()

def hostgame():
    global c
    gvalue[0]=2
    s = socket.socket()         
    host = socket.gethostbyname(socket.gethostname())
    print(host) 
    port = 52860            
    s.bind((host, port))        
    s.listen(5)
    c, addr = s.accept()
    fen.destroy()
    server_file=input("donnez le nom du fichier de votre personnage")
    client_file=c.recv(64)
    client_file=client_file.decode()
    c.send(bytes(server_file,encoding='utf-8'))
    classloading(server_file,client_file)
    
    fenhg=Tk()
    gvalue[2] = Canvas(fenhg,height = 32*25,width = 32*40,bg="ivory")

    for casetype in gvalue[1][0]:
        casetype[4]=PhotoImage(file=casetype[0])

    for k in range (2):
        gvalue[4][k][6]=PhotoImage(file=gvalue[4][k][0])
    
    
    for k in range (40):
        for i in range(21):
            gvalue[2].create_image(32*k,32*i,image=gvalue[1][0][gvalue[1][1][k][i][0]][4],anchor='nw')  
    for k in range (22):
        gvalue[2].create_line(0,k*32,32*40,k*32) #lignes horizontales
    for k in range (40):
        gvalue[2].create_line(k*32,0,k*32,32*21) #lignes verticales

    gvalue[3][0][3]=gvalue[4][gvalue[0]-2][1][0]," : ",floor(gvalue[3][0][2]*100),"percents"
    gvalue[3][1][3]=gvalue[4][gvalue[0]-2][2][0]," : ",floor(gvalue[3][1][2]*100),"percents"
    gvalue[2].create_rectangle(32,32*21.5,352,32*22.25)                                 #Barre
    gvalue[3][0][0]=gvalue[2].create_rectangle(32,32*21.5,32+320*gvalue[3][0][2],32*22.25,fill="red")       #de
    gvalue[3][0][1]=gvalue[2].create_text(192,32*21.875,text=gvalue[3][0][3],font="Arial 14 italic",fill="black")  #vie
    gvalue[2].create_rectangle(32,32*22.75,352,32*23.5)                                 #Barre
    gvalue[3][1][0]=gvalue[2].create_rectangle(32,32*22.75,32+320*gvalue[3][1][2],32*23.5,fill="blue")      #de
    gvalue[3][1][1]=gvalue[2].create_text(192,32*23.15,text=gvalue[3][1][3],font="Arial 14 italic",fill="black")   #mana
    gvalue[2].grid()

    not_done=True
    while not_done:
        x,y=randint(0,39),randint(0,20)
        if gvalue[1][1][x][y][1]==1:
            gvalue[4][0][5][0],gvalue[4][0][5][1]=x,y
            not_done=False
    for k in range(2):
        posclient=c.recv(16)
        gvalue[4][1][5][k]=int.from_bytes(posclient, byteorder='big')
    x=x.to_bytes(16, byteorder="big")
    y=y.to_bytes(16, byteorder="big")
    c.send(x)
    c.send(y)
    for k in range(2):
        gvalue[4][k][7]=gvalue[2].create_image(32*gvalue[4][k][5][0],32*gvalue[4][k][5][1],image=gvalue[4][k][6],anchor='nw')    
    global fenhg
    thread_play=threading.Thread(target=play_server).start()
    fenhg.mainloop()

def clientgame():
    global s
    gvalue[0]=3
    s = socket.socket()         
    host = input("Host IP : ")
    port = 52860
    s.connect((host, port))

    fen.destroy()
    client_file=input("donnez le nom du fichier de votre personnage")
    s.send(bytes(client_file,encoding='utf-8'))
    server_file=s.recv(64)
    server_file=server_file.decode()
    classloading(server_file,client_file)
    fenhg=Tk()
    gvalue[2] = Canvas(fenhg,height = 32*25,width = 32*40,bg="ivory")

    

    for casetype in gvalue[1][0]:
        casetype[4]=PhotoImage(file=casetype[0])

    for k in range (2):
        gvalue[4][k][6]=PhotoImage(file=gvalue[4][k][0])
    
    
    for k in range (40):
        for i in range(21):
            gvalue[2].create_image(32*k,32*i,image=gvalue[1][0][gvalue[1][1][k][i][0]][4],anchor='nw')  
    for k in range (22):
        gvalue[2].create_line(0,k*32,32*40,k*32) #lignes horizontales
    for k in range (40):
        gvalue[2].create_line(k*32,0,k*32,32*21) #lignes verticales

    gvalue[3][0][3]=gvalue[4][gvalue[0]-2][1][0]," : ",floor(gvalue[3][0][2]*100),"percents"
    gvalue[3][1][3]=gvalue[4][gvalue[0]-2][2][0]," : ",floor(gvalue[3][1][2]*100),"percents"
    gvalue[2].create_rectangle(32,32*21.5,352,32*22.25)                                 #Barre
    gvalue[3][0][0]=gvalue[2].create_rectangle(32,32*21.5,32+320*gvalue[3][0][2],32*22.25,fill="red")       #de
    gvalue[3][0][1]=gvalue[2].create_text(192,32*21.875,text=gvalue[3][0][3],font="Arial 14 italic",fill="black")  #vie
    gvalue[2].create_rectangle(32,32*22.75,352,32*23.5)                                 #Barre
    gvalue[3][1][0]=gvalue[2].create_rectangle(32,32*22.75,32+320*gvalue[3][1][2],32*23.5,fill="blue")      #de
    gvalue[3][1][1]=gvalue[2].create_text(192,32*23.15,text=gvalue[3][1][3],font="Arial 14 italic",fill="black")   #mana
    gvalue[2].grid()

    not_done=True
    while not_done:
        x,y=randint(0,39),randint(0,20)
        if gvalue[1][1][x][y][1]==2:
            gvalue[4][1][5][0],gvalue[4][1][5][1]=x,y
            not_done=False
    x=x.to_bytes(16, byteorder="big")
    y=y.to_bytes(16, byteorder="big")
    s.send(x)
    s.send(y)
    for k in range(2):
        posclient=s.recv(16)
        gvalue[4][0][5][k]=int.from_bytes(posclient, byteorder='big')
    for k in range(2):
        gvalue[4][k][7]=gvalue[2].create_image(32*gvalue[4][k][5][0],32*gvalue[4][k][5][1],image=gvalue[4][k][6],anchor='nw')
    
    global fenhg

    thread_play=threading.Thread(target=play_client).start()
    fenhg.mainloop()
    
def play_server():
    global c
    server_playing=False
    if gvalue[4][0][3][2]>=gvalue[4][1][3][2]:
        server_playing=True
    while gvalue[6]==0:
        if server_playing:
            gvalue[5]=False
            c.send(bytes("serverturn",encoding='utf-8'))
            while not gvalue[5]:
                action=input("action : ")
                c.send(bytes(action,encoding='utf-8'))
                try:
                    action=int(action)
                    curattstats=gvalue[4][0][4][action]
                except:
                    no_attack_input_treatment(action,0,True)
                else:
                    if -curattstats[1]<=gvalue[4][0][2][3]:
                        print("coût : ",-curattstats[1]," ,dégats : ",-curattstats[0]," ,portée : ",curattstats[2])
                        target=input("self/ennemy/cancel : ")
                        c.send(bytes(target,encoding='utf-8'))
                        if target=="self":
                            skill(0,0,curattstats[1],curattstats[0])
                            print("action effectué")
                        if target=="ennemy":
                            if ((curattstats[2])**2)>=((gvalue[4][0][5][0]-gvalue[4][1][5][0])**2+(gvalue[4][0][5][1]-gvalue[4][1][5][1])**2):
                                skill(0,1,curattstats[1],curattstats[0])
                                print("action effectué")
                            else:
                                print("vous êtes trop loin")
                    else:
                        print("il ne reste plus assez de",gvalue[4][0][2][0])       
        if gvalue[6]==0:
            server_playing=False
                
        if not server_playing:
            gvalue[5]=False
            c.send(bytes("clientturn",encoding='utf-8'))
            while not gvalue[5]:
                action=c.recv(1024)
                action=action.decode()
                try:
                    action=int(action)
                    curattstats=gvalue[4][1][4][action]
                except:
                    no_attack_input_treatment(action,1,False)
                    c.send(bytes(action,encoding='utf-8'))
                else:
                    target=c.recv(1024)
                    target=target.decode()
                    c.send(bytes(target,encoding='utf-8'))
                    if target=="self":
                        skill(1,1,curattstats[1],curattstats[0])
                        print("l'ennemi a effectué une action")
                    if target=="ennemy":
                        if ((curattstats[2])**2)>=((gvalue[4][0][5][0]-gvalue[4][1][5][0])**2+(gvalue[4][0][5][1]-gvalue[4][1][5][1])**2):
                            skill(1,0,curattstats[1],curattstats[0])
                            print("l'ennemi a effectué une action")
        server_playing=True
    if gvalue[6]==1:
        c.send(bytes("serverwin",encoding='utf-8'))
        showerror('Victoire', "Vous avez gagné, appuyez sur ok pour quitter")
    if gvalue[6]==2:
        c.send(bytes("clientwin",encoding='utf-8'))
        showerror('Défaite', "Vous avez perdu, appuyez sur ok pour quitter")
    fenhg.destroy()
    start()

def play_client():
    global s
    #gvalue[14]=gvalue[2].create_rectangle(0,0,32,32,fill = "blue")
    while gvalue[6]==0:
        turn=s.recv(128)
        turn=turn.decode()
        if turn=="serverturn":
            gvalue[5]=False
            while not gvalue[5]:
                action=s.recv(1024)
                action=action.decode()
                try:
                    action=int(action)
                    curattstats=gvalue[4][0][4][action]
                except:
                    no_attack_input_treatment(action,0,False)
                else:
                    target=s.recv(1024)
                    target=target.decode()
                    if target=="self":
                        skill(0,0,curattstats[1],curattstats[0])
                        print("l'ennemi a effectué une action")
                    if target=="ennemy":
                        if ((curattstats[2])**2)>=((gvalue[4][0][5][0]-gvalue[4][1][5][0])**2+(gvalue[4][0][5][1]-gvalue[4][1][5][1])**2):
                            skill(0,1,curattstats[1],curattstats[0])
                            print("l'ennemi a effectué une action")
        if turn=="clientturn":
            gvalue[5]=False
            while not gvalue[5]:
                action=input("action : ")
                s.send(bytes(action,encoding='utf-8'))
                try:
                    action=int(action)
                    curattstats=gvalue[4][1][4][action]
                except:
                    action=s.recv(1024)
                    action=action.decode()
                    no_attack_input_treatment(action,1,False)
                else:
                    if -curattstats[1]<=gvalue[4][1][2][3]:
                        print("coût : ",-curattstats[1]," ,dégats : ",-curattstats[0]," ,portée : ",curattstats[2])
                        target=input("self/ennemy/cancel : ")
                        s.send(bytes(target,encoding='utf-8'))
                        target=s.recv(1024)
                        target=target.decode()
                        if target=="self":
                            skill(1,1,curattstats[1],curattstats[0])
                            print("action effectué")
                        if target=="ennemy":
                            if ((curattstats[2])**2)>=((gvalue[4][0][5][0]-gvalue[4][1][5][0])**2+(gvalue[4][0][5][1]-gvalue[4][1][5][1])**2):
                                skill(1,0,curattstats[1],curattstats[0])
                                print("action effectué")
                            else:
                                print("vous êtes trop loin")
                    else:
                        print("il ne reste plus assez de",gvalue[4][1][2][0])
        if turn=="serverwin":
            gvalue[6]=1
            showerror('Défaite', "Vous avez perdu, appuyez sur ok pour quitter")
        if turn=="clientwin":
            gvalue[6]=2
            showerror('Victoire', "Vous avez gagné, appuyez sur ok pour quitter")
    fenhg.destroy()
    start()

def start():
    fen=Tk()
    global fen
    hostbutton = Button(fen, text="HOST",command=hostgame).grid()
    clientbutton=Button(fen, text="CLIENT",command=clientgame).grid()
    quitbutton = Button(fen, text="QUIT GAME",command=close).grid()
    fen.mainloop()
    

gvalue=[0,0,0,[[0,0,1,0],[0,0,1,0]],[0,0],False,0]            #voir txt
with open("map.json",mode='r')as map_list:
        gvalue[1]=json.load(map_list)
start()

