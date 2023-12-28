import pygame


import random
import subprocess
import sys
#functions

def give_pos(k):
    a=k
    c=k/8
    if(c==int(c)):
        b=c-1
    else:
        b=int(c)
    while(a>8):
        a=a-8
    x=50+100*(a-1)
    y=50+100*(b)
    return (x,y)
def give_nb(k):
    lv1=[i for i in range(10,57) if i%8==1]
    lv2=[i for i in range(9,57) if i%8==0]
    if k==1:
        return (2,9)
    elif k==8:
        return (7,16)
    elif k==9:
        return (10,17)
    elif k==2:
        return (3,10)
    elif k==64:
        return (63,56)
    elif k==57:
        return (58,49)
    elif k in range(3,8):
        k1=k-1
        k2=k+1
        k3=k+8
        return (k1,k2,k3)
    # 1st vertical row
    elif k in lv1:
        k1=k-8
        k2=k+1
        k3=k+8
        return (k1,k2,k3)
    elif k in range(58,64):
        k1=k+1
        k2=k-1
        k3=k-8
        return (k1,k2,k3)
    elif k in lv2:
        k1=k-1
        k2=k-8
        k3=k+8
        return (k1,k2,k3)
    else:
        return(k+1,k-1,k+8,k-8)
def blit_img_nb(l,url):
    if(len(l))==1:
        j1=pygame.image.load(url) 
        j11=j1.get_rect()
        j11.center=give_pos(l)
        ds.blit(j1,j11)
         
    elif len(l)==2:
        j1=pygame.image.load(url) 
        j11=j1.get_rect()
        j11.center=give_pos(l[0])
        ds.blit(j1,j11) 
        j2=pygame.image.load(url) 
        j22=j2.get_rect()
        j22.center=give_pos(l[1])
        ds.blit(j2,j22) 
    elif len(l)==3:
        j1=pygame.image.load(url) 
        j11=j1.get_rect()
        j11.center=give_pos(l[0])
        ds.blit(j1,j11) 
        j2=pygame.image.load(url) 
        j22=j2.get_rect()
        j22.center=give_pos(l[1])
        ds.blit(j2,j22)              
        j3=pygame.image.load(url) 
        j33=j3.get_rect()
        j33.center=give_pos(l[2])
        ds.blit(j3,j33)    
    elif len(l)==4:
        j1=pygame.image.load(url) 
        j11=j1.get_rect()
        j11.center=give_pos(l[0])
        ds.blit(j1,j11) 
        j2=pygame.image.load(url) 
        j22=j2.get_rect()
        j22.center=give_pos(l[1])
        ds.blit(j2,j22)              
        j3=pygame.image.load(url) 
        j33=j3.get_rect()
        j33.center=give_pos(l[2])
        ds.blit(j3,j33)        
        j4=pygame.image.load(url) 
        j44=j4.get_rect()
        j44.center=give_pos(l[3])
        ds.blit(j4,j44)  
def give_rc(pos):
    x=pos[0]
    y=pos[1]
    a=1+(x-50)/100
    b=1+(y-50)/100
    return (a,b)
def give_bno(rc):
    r=rc[0]
    c=rc[1]
    xx=8*(c-1)+r
    return xx
def arrow_cond(k):
    rowcol=give_rc(pos)
    block=give_bno(rowcol)
    lv1=[i for i in range(10,57) if i%8==1]
    lv2=[i for i in range(9,57) if i%8==0]

    if k==8:
        if block==7 and imgdir=='r':
            return 1
        if block==16 and imgdir=='u':
            return 1
    elif k==9:
        if block==10 and imgdir=='l':
            return 1
        if block==17 and imgdir=='u':
            return 1
    elif k==2:
        if block==3 and imgdir=='l':
            return 1
        if block==10 and imgdir=='u':
            return 1
    elif k==64:
        if block==63 and imgdir=='r':
            return 1
        if block==56 and imgdir=='d':
            return 1
    elif k==57:
        if block==58 and imgdir=='l':
            return 1
        if block==49 and imgdir=='d':
            return 1
    elif k in range(3,8):
        k1=k-1
        k2=k+1
        k3=k+8
        if block==k1 and imgdir=='r':
            return 1
        if block==k2 and imgdir=='l':
            return 1
        if block==k3 and imgdir=='u':
            return 1
    # 1st vertical row
    elif k in lv1:
        k1=k-8
        k2=k+1
        k3=k+8
        if block==k1 and imgdir=='d':
            return 1
        if block==k2 and imgdir=='l':
            return 1
        if block==k3 and imgdir=='u':
            return 1
    elif k in range(58,64):
        k1=k+1
        k2=k-1
        k3=k-8
        if block==k1 and imgdir=='l':
            return 1
        if block==k2 and imgdir=='r':
            return 1
        if block==k3 and imgdir=='d':
            return 1
    elif k in lv2:
        k1=k-1
        k2=k-8
        k3=k+8
        if block==k1 and imgdir=='r':
            return 1
        if block==k2 and imgdir=='d':
            return 1
        if block==k3 and imgdir=='u':
            return 1
    else:
        if block==k+1 and imgdir=='l':
            return 1
        if block==k-1 and imgdir=='r':
            return 1
        if block==k+8 and imgdir=='u':
            return 1        
        if block==k-8 and imgdir=='d':
            return 1      
def open_second_window():
    subprocess.Popen(["python", "C:/Users/datta/OneDrive/Desktop/sw.py"])


pygame.init()
ds=pygame.display.set_mode((1140,800))
pygame.display.set_caption("WUMPUS COLLECTOR")
# colors
black=(0,0,0)
white=(255,255,255)
lightgreen=(144,238,144)
ds.fill(lightgreen)
#game variables
arrows=5
goldleft=5
ss1=pygame.mixer.Sound("E:/Python games/Tutorial/sss1.wav")
ss2=pygame.mixer.Sound("E:/Python games/Tutorial/ss2.wav")
ss3=pygame.mixer.Sound("C:/Users/datta/Downloads/sound.wav")
l=[i for i in range(3,65)]
l.remove(9)
pygame.draw.line(ds,white,(1140,0),(1140,800),5)
pygame.draw.line(ds,white,(800,0),(1140,0),5)
pygame.draw.line(ds,white,(800,100),(1140,100),5)
pygame.draw.line(ds,white,(800,200),(1140,200),5)
pygame.draw.line(ds,white,(800,300),(1140,300),5)
pygame.draw.line(ds,white,(800,800),(1140,800),5)
danger=[]
#images
i1=pygame.image.load("C:/Users/datta/Downloads/Microsoft-Fluentui-Emoji-Flat-Man-Zombie-Flat.512.png")
i11=i1.get_rect()
i2=pygame.image.load("C:/Users/datta/Downloads/Microsoft-Fluentui-Emoji-Flat-Man-Zombie-Flat.512.png")
i22=i2.get_rect()
t=pygame.font.SysFont('calibri',72)
t2=pygame.font.SysFont('Arial Black',22)

t4=t.render("GAME OVER",True,(white),(10,50,10))
t44=t4.get_rect()
t1=t.render("CONGRAGULATIONS",True,(white),(10,50,10))
t11=t1.get_rect()
t11.center=(400,400)
t3=t2.render("ARROWS LEFT : "+str(arrows),True,(black),(lightgreen))
t33=t3.get_rect()
t6=t2.render("GOLD LEFT : "+str(goldleft),True,(black),(lightgreen))
t66=t6.get_rect()
t33.topleft=(860,30)
t66.topleft=(860,130)

tr=t2.render("PRESS R FOR RULES",True,(black),(lightgreen))
tr1=tr.get_rect()
tr1.topleft=(840,230)
ds.blit(tr,tr1)
h=random.sample(l,2)
imgzh1=h[0]
imgzh2=h[1]
zbl=[imgzh1,imgzh2]

l.remove(h[0])
l.remove(h[1])
i11.center=give_pos(h[0])
i22.center=give_pos(h[1])
n1=list(give_nb(h[0]))
n2=list(give_nb(h[1]))
l=[i for i in l if i not in n1]
l=[i for i in l if i not in n2]
n1=[i for i in n1 if i!=imgzh2 ]
n2=[i for i in n2 if i!=imgzh1 ]
blit_img_nb(n1,"C:/Users/datta/Downloads/s.png")
blit_img_nb(n2,"C:/Users/datta/Downloads/s.png")


h=random.sample(l,2)

l.remove(h[0])
l.remove(h[1])
imgzh3=h[0]
imgzh4=h[1]
k1=pygame.image.load("C:/Users/datta/Downloads/hole.png")
k2=pygame.image.load("C:/Users/datta/Downloads/hole.png")
k11=k1.get_rect()
k22=k2.get_rect()
k11.center=give_pos(h[0])
k22.center=give_pos(h[1])
n3=list(give_nb(h[0]))
n4=list(give_nb(h[1]))
n3=[i for i in n3 if i!=imgzh4 ]
n4=[i for i in n4 if i!=imgzh3 ]
n12=list(set(n1+n2))
n34=list(set(n3+n4))
nboth=[i for i in n12 if i in n34] 



blit_img_nb(n3,"C:/Users/datta/Downloads/h.png")
blit_img_nb(n4,"C:/Users/datta/Downloads/h.png")
if(nboth!=[]):
    for i in range(len(nboth)):
        p1=pygame.image.load("C:/Users/datta/Downloads/b.png")
        p11=p1.get_rect()
        p11.center=give_pos(nboth[i])
        ds.blit(p1,p11)
l=[i for i in l if i not in n3]
l=[i for i in l if i not in n4]



g=random.sample(l,5)

gold=len(g)
for i in g:
    p1=pygame.image.load("C:/Users/datta/Downloads/gold.png")
    p11=p1.get_rect()
    p11.center=give_pos(i)
    ds.blit(p1,p11)

for i in range(9):
    k=100*i
    pygame.draw.line(ds,white,(0,k),(800,k),5)
for j in range(9):
    k=100*j
    pygame.draw.line(ds,white,(k,0),(k,800),5)
ds.blit(i1,i11)
ds.blit(i2,i22)
ds.blit(k1,k11)
ds.blit(k2,k22)



pos=[50,50]
right=pygame.image.load("C:/Users/datta/Downloads/right.png")
right1=right.get_rect()
right1.center=tuple(pos)
ds.blit(right,right1)
down=pygame.image.load("C:/Users/datta/Downloads/down.png")
down1=down.get_rect()
down1.center=tuple(pos)
left=pygame.image.load("C:/Users/datta/Downloads/left.png")
left1=left.get_rect()
left1.center=tuple(pos)
up=pygame.image.load("C:/Users/datta/Downloads/up.png")

up1=up.get_rect()
up1.center=tuple(pos)
imgdir='r'
danger.append(imgzh1)
danger.append(imgzh2)
danger.append(imgzh3)
danger.append(imgzh4)
ds.blit(t3,t33)
ds.blit(t6,t66)
blacklist=[i for i in range(2,65)]
for i in blacklist:
    op=give_pos(i)
    oi=pygame.image.load("C:/Users/datta/Downloads/black square.png")
    oi1=oi.get_rect()
    oi1.center=(op)
    ds.blit(oi,oi1)




run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            sys.exit()

        if event.type==pygame.KEYDOWN:

                if event.key==pygame.K_DOWN:
                    ss1.play()
                    try:
                        ds.fill(lightgreen)

                        for i in range(9):
                            k=100*i
                            pygame.draw.line(ds,white,(0,k),(800,k),5)
                        for j in range(9):
                            k=100*j
                            pygame.draw.line(ds,white,(k,0),(k,800),5)  

                        ds.blit(k1,k11)
                        ds.blit(k2,k22)  
                        
                        blit_img_nb(n3,"C:/Users/datta/Downloads/h.png")
                        blit_img_nb(n4,"C:/Users/datta/Downloads/h.png")            
    
                        i1=pygame.image.load("C:/Users/datta/Downloads/Microsoft-Fluentui-Emoji-Flat-Man-Zombie-Flat.512.png")
                        i11=i1.get_rect()
                        for i in zbl:
                            j=give_pos(i)
                            i11.center=j
                            ds.blit(i1,i11)
                            n=give_nb(i)
                            blit_img_nb(n,"C:/Users/datta/Downloads/s.png")
                                        
                        if(nboth!=[]):
                            for i in range(len(nboth)):
                                p1=pygame.image.load("C:/Users/datta/Downloads/b.png")
                                p11=p1.get_rect()
                                p11.center=give_pos(nboth[i])
                                ds.blit(p1,p11)   
                        for i in g:
                            p1=pygame.image.load("C:/Users/datta/Downloads/gold.png")
                            p11=p1.get_rect()
                            p11.center=give_pos(i)
                            ds.blit(p1,p11)  
                        imgdir='d'      
                        ds.blit(down,down1) 
                        ds.blit(t3,t33)
                        ds.blit(t6,t66)
                        ds.blit(tr,tr1)
                        pygame.draw.line(ds,white,(1140,0),(1140,800),10)
                        pygame.draw.line(ds,white,(800,0),(1140,0),5)
                        pygame.draw.line(ds,white,(800,100),(1140,100),5)
                        pygame.draw.line(ds,white,(800,200),(1140,200),5)
                        pygame.draw.line(ds,white,(800,300),(1140,300),5)
                        pygame.draw.line(ds,white,(800,800),(1140,800),5)
                        for i in blacklist:
                            op=give_pos(i)
                            oi=pygame.image.load("C:/Users/datta/Downloads/black square.png")
                            oi1=oi.get_rect()
                            oi1.center=(op)
                            ds.blit(oi,oi1)                                                 
                    except:
                        ds.fill(lightgreen)
                        for i in range(9):
                            k=100*i
                            pygame.draw.line(ds,white,(0,k),(800,k),5)
                        for j in range(9):
                            k=100*j
                            pygame.draw.line(ds,white,(k,0),(k,800),5) 
                            
                        ds.blit(t4,t44)                                      
                if event.key==pygame.K_LEFT:
                    ss1.play()
                    try:
                        ds.fill(lightgreen)
                        
                        for i in range(9):
                            k=100*i
                            pygame.draw.line(ds,white,(0,k),(800,k),5)
                        for j in range(9):
                            k=100*j
                            pygame.draw.line(ds,white,(k,0),(k,800),5)  

                        ds.blit(k1,k11)
                        ds.blit(k2,k22)  
                        
                        blit_img_nb(n3,"C:/Users/datta/Downloads/h.png")
                        blit_img_nb(n4,"C:/Users/datta/Downloads/h.png")            
                        for i in zbl:
                            j=give_pos(i)
                            i11.center=j
                            ds.blit(i1,i11)
                            n=give_nb(i)
                            blit_img_nb(n,"C:/Users/datta/Downloads/s.png")               
                        if(nboth!=[]):
                            for i in range(len(nboth)):
                                p1=pygame.image.load("C:/Users/datta/Downloads/b.png")
                                p11=p1.get_rect()
                                p11.center=give_pos(nboth[i])
                                ds.blit(p1,p11)   
                        for i in g:
                            p1=pygame.image.load("C:/Users/datta/Downloads/gold.png")
                            p11=p1.get_rect()
                            p11.center=give_pos(i)
                            ds.blit(p1,p11) 
                        imgdir='l'
                        ds.blit(left,left1)
                        ds.blit(t3,t33)
                        ds.blit(t6,t66)
                        ds.blit(tr,tr1)
                        pygame.draw.line(ds,white,(1140,0),(1140,800),10)
                        pygame.draw.line(ds,white,(800,0),(1140,0),5)
                        pygame.draw.line(ds,white,(800,100),(1140,100),5)
                        pygame.draw.line(ds,white,(800,200),(1140,200),5)
                        pygame.draw.line(ds,white,(800,300),(1140,300),5)
                        pygame.draw.line(ds,white,(800,800),(1140,800),5)           
                        for i in blacklist:
                            op=give_pos(i)
                            oi=pygame.image.load("C:/Users/datta/Downloads/black square.png")
                            oi1=oi.get_rect()
                            oi1.center=(op)
                            ds.blit(oi,oi1)                
                    except:
                        ds.fill(lightgreen)
                        for i in range(9):
                            k=100*i
                            pygame.draw.line(ds,white,(0,k),(800,k),5)
                        for j in range(9):
                            k=100*j
                            pygame.draw.line(ds,white,(k,0),(k,800),5)  
                        ds.blit(t4,t44) 
                if event.key==pygame.K_RIGHT:
                    ss1.play()
                    try:
                        ds.fill(lightgreen)
                        
                        for i in range(9):
                            k=100*i
                            pygame.draw.line(ds,white,(0,k),(800,k),5)
                        for j in range(9):
                            k=100*j
                            pygame.draw.line(ds,white,(k,0),(k,800),5)  

                        ds.blit(k1,k11)
                        ds.blit(k2,k22)  
                        
                        blit_img_nb(n3,"C:/Users/datta/Downloads/h.png")
                        blit_img_nb(n4,"C:/Users/datta/Downloads/h.png")            
                        for i in zbl:
                            j=give_pos(i)
                            i11.center=j
                            ds.blit(i1,i11)
                            n=give_nb(i)
                            blit_img_nb(n,"C:/Users/datta/Downloads/s.png")              
                        if(nboth!=[]):
                            for i in range(len(nboth)):
                                p1=pygame.image.load("C:/Users/datta/Downloads/b.png")
                                p11=p1.get_rect()
                                p11.center=give_pos(nboth[i])
                                ds.blit(p1,p11)   
                        for i in g:
                            p1=pygame.image.load("C:/Users/datta/Downloads/gold.png")
                            p11=p1.get_rect()
                            p11.center=give_pos(i)
                            ds.blit(p1,p11) 
                        imgdir='r'
                        ds.blit(right,right1)
                        ds.blit(t3,t33)
                        ds.blit(t6,t66)
                        ds.blit(tr,tr1)
                        pygame.draw.line(ds,white,(1140,0),(1140,800),10)
                        pygame.draw.line(ds,white,(800,0),(1140,0),5)
                        pygame.draw.line(ds,white,(800,100),(1140,100),5)
                        pygame.draw.line(ds,white,(800,200),(1140,200),5)
                        pygame.draw.line(ds,white,(800,300),(1140,300),5)
                        pygame.draw.line(ds,white,(800,800),(1140,800),5)           
                        for i in blacklist:
                            op=give_pos(i)
                            oi=pygame.image.load("C:/Users/datta/Downloads/black square.png")
                            oi1=oi.get_rect()
                            oi1.center=(op)
                            ds.blit(oi,oi1)                
                    except:
                        ds.fill(lightgreen)
                        for i in range(9):
                            k=100*i
                            pygame.draw.line(ds,white,(0,k),(800,k),5)
                        for j in range(9):
                            k=100*j
                            pygame.draw.line(ds,white,(k,0),(k,800),5)  
                        ds.blit(t4,t44) 
                if event.key==pygame.K_UP:
                    ss1.play()
                    try:
                        ds.fill(lightgreen)
                        
                        for i in range(9):
                            k=100*i
                            pygame.draw.line(ds,white,(0,k),(800,k),5)
                        for j in range(9):
                            k=100*j
                            pygame.draw.line(ds,white,(k,0),(k,800),5)  

                        ds.blit(k1,k11)
                        ds.blit(k2,k22)  
                        ds.blit(tr,tr1)
                        blit_img_nb(n3,"C:/Users/datta/Downloads/h.png")
                        blit_img_nb(n4,"C:/Users/datta/Downloads/h.png")            
                        for i in zbl:
                            j=give_pos(i)
                            i11.center=j
                            ds.blit(i1,i11)
                            n=give_nb(i)
                            blit_img_nb(n,"C:/Users/datta/Downloads/s.png")               
                        if(nboth!=[]):
                            for i in range(len(nboth)):
                                p1=pygame.image.load("C:/Users/datta/Downloads/b.png")
                                p11=p1.get_rect()
                                p11.center=give_pos(nboth[i])
                                ds.blit(p1,p11)   
                        for i in g:
                            p1=pygame.image.load("C:/Users/datta/Downloads/gold.png")
                            p11=p1.get_rect()
                            p11.center=give_pos(i)
                            ds.blit(p1,p11) 
                        imgdir='u'
                        ds.blit(up,up1)
                        ds.blit(t3,t33)
                        ds.blit(t6,t66)
                        pygame.draw.line(ds,white,(1140,0),(1140,800),10)
                        pygame.draw.line(ds,white,(800,0),(1140,0),5)
                        pygame.draw.line(ds,white,(800,100),(1140,100),5)
                        pygame.draw.line(ds,white,(800,200),(1140,200),5)
                        pygame.draw.line(ds,white,(800,300),(1140,300),5)
                        pygame.draw.line(ds,white,(800,800),(1140,800),5)           
                        for i in blacklist:
                            op=give_pos(i)
                            oi=pygame.image.load("C:/Users/datta/Downloads/black square.png")
                            oi1=oi.get_rect()
                            oi1.center=(op)
                            ds.blit(oi,oi1)                
                    except:
                        ds.fill(lightgreen)
                        for i in range(9):
                            k=100*i
                            pygame.draw.line(ds,white,(0,k),(800,k),5)
                        for j in range(9):
                            k=100*j
                            pygame.draw.line(ds,white,(k,0),(k,800),5)  
                        ds.blit(t4,t44) 
                if event.key==pygame.K_y:
                    ss1.play()
                    try:
                        if imgdir=='r' and right1.centerx<700:
                            cur_rc=give_rc(pos)
                            cur_bno=give_bno(cur_rc)
                            if (cur_bno+1) in blacklist:
                                blacklist.remove(cur_bno+1)
                            pos[0]+=100
                            right1.center=pos
                            up1.center=pos
                            down1.center=pos
                            left1.center=pos
                            ds.fill(lightgreen)
                            for i in range(9):
                                k=100*i
                                pygame.draw.line(ds,white,(0,k),(800,k),5)
                            for j in range(9):
                                k=100*j
                                pygame.draw.line(ds,white,(k,0),(k,800),5)  

                            ds.blit(k1,k11)
                            ds.blit(k2,k22)  
                            
                            blit_img_nb(n3,"C:/Users/datta/Downloads/h.png")
                            blit_img_nb(n4,"C:/Users/datta/Downloads/h.png")            
                            for i in zbl:
                                j=give_pos(i)
                                i11.center=j
                                ds.blit(i1,i11)
                                n=give_nb(i)
                                blit_img_nb(n,"C:/Users/datta/Downloads/s.png")               
                            if(nboth!=[]):
                                for i in range(len(nboth)):
                                    p1=pygame.image.load("C:/Users/datta/Downloads/b.png")
                                    p11=p1.get_rect()
                                    p11.center=give_pos(nboth[i])
                                    ds.blit(p1,p11)   
                            for i in g:
                                p1=pygame.image.load("C:/Users/datta/Downloads/gold.png")
                                p11=p1.get_rect()
                                p11.center=give_pos(i)
                                ds.blit(p1,p11) 
                                ds.blit(right,right1)
                            ds.blit(t3,t33)
                            ds.blit(t6,t66)
                            ds.blit(tr,tr1)
                            pygame.draw.line(ds,white,(1140,0),(1140,800),10)
                            pygame.draw.line(ds,white,(800,0),(1140,0),5)
                            pygame.draw.line(ds,white,(800,100),(1140,100),5)
                            pygame.draw.line(ds,white,(800,200),(1140,200),5)
                            pygame.draw.line(ds,white,(800,300),(1140,300),5)
                            pygame.draw.line(ds,white,(800,800),(1140,800),5)                                       
                            for i in blacklist:
                                op=give_pos(i)
                                oi=pygame.image.load("C:/Users/datta/Downloads/black square.png")
                                oi1=oi.get_rect()
                                oi1.center=(op)
                                ds.blit(oi,oi1)  
                        if imgdir=='l' and right1.centerx>100:
                            cur_rc=give_rc(pos)
                            cur_bno=give_bno(cur_rc)
                            if (cur_bno-1) in blacklist:
                                blacklist.remove(cur_bno-1)  
                            pos[0]-=100
                            right1.center=pos
                            up1.center=pos
                            down1.center=pos
                            left1.center=pos
                            ds.fill(lightgreen)
                          
                            for i in range(9):
                                k=100*i
                                pygame.draw.line(ds,white,(0,k),(800,k),5)
                            for j in range(9):
                                k=100*j
                                pygame.draw.line(ds,white,(k,0),(k,800),5)  

                            ds.blit(k1,k11)
                            ds.blit(k2,k22)  
                            
                            blit_img_nb(n3,"C:/Users/datta/Downloads/h.png")
                            blit_img_nb(n4,"C:/Users/datta/Downloads/h.png")            
                            for i in zbl:
                                j=give_pos(i)
                                i11.center=j
                                ds.blit(i1,i11)
                                n=give_nb(i)
                                blit_img_nb(n,"C:/Users/datta/Downloads/s.png")               
                            if(nboth!=[]):
                                for i in range(len(nboth)):
                                    p1=pygame.image.load("C:/Users/datta/Downloads/b.png")
                                    p11=p1.get_rect()
                                    p11.center=give_pos(nboth[i])
                                    ds.blit(p1,p11)   
                            for i in g:
                                p1=pygame.image.load("C:/Users/datta/Downloads/gold.png")
                                p11=p1.get_rect()
                                p11.center=give_pos(i)
                                ds.blit(p1,p11) 
                                ds.blit(left,left1)
                            ds.blit(t3,t33)
                            ds.blit(t6,t66) 
                            ds.blit(tr,tr1)                               
                            pygame.draw.line(ds,white,(1140,0),(1140,800),10)
                            pygame.draw.line(ds,white,(800,0),(1140,0),5)
                            pygame.draw.line(ds,white,(800,100),(1140,100),5)
                            pygame.draw.line(ds,white,(800,200),(1140,200),5)
                            pygame.draw.line(ds,white,(800,300),(1140,300),5)
                            pygame.draw.line(ds,white,(800,800),(1140,800),5)       
                            for i in blacklist:
                                op=give_pos(i)
                                oi=pygame.image.load("C:/Users/datta/Downloads/black square.png")
                                oi1=oi.get_rect()
                                oi1.center=(op)
                                ds.blit(oi,oi1)  
                        if imgdir=='u' and right1.centery>100:
                            cur_rc=give_rc(pos)
                            cur_bno=give_bno(cur_rc)
                            if (cur_bno-8) in blacklist:
                                blacklist.remove(cur_bno-8) 
                            pos[1]-=100
                            right1.center=pos
                            up1.center=pos
                            down1.center=pos
                            left1.center=pos
                            ds.fill(lightgreen)
                            for i in range(9):
                                k=100*i
                                pygame.draw.line(ds,white,(0,k),(800,k),5)
                            for j in range(9):
                                k=100*j
                                pygame.draw.line(ds,white,(k,0),(k,800),5)  

                            ds.blit(k1,k11)
                            ds.blit(k2,k22)  
                            
                            blit_img_nb(n3,"C:/Users/datta/Downloads/h.png")
                            blit_img_nb(n4,"C:/Users/datta/Downloads/h.png")            
                            for i in zbl:
                                j=give_pos(i)
                                i11.center=j
                                ds.blit(i1,i11)
                                n=give_nb(i)
                                blit_img_nb(n,"C:/Users/datta/Downloads/s.png")                
                            if(nboth!=[]):
                                for i in range(len(nboth)):
                                    p1=pygame.image.load("C:/Users/datta/Downloads/b.png")
                                    p11=p1.get_rect()
                                    p11.center=give_pos(nboth[i])
                                    ds.blit(p1,p11)   
                            for i in g:
                                p1=pygame.image.load("C:/Users/datta/Downloads/gold.png")
                                p11=p1.get_rect()
                                p11.center=give_pos(i)
                                ds.blit(p1,p11) 
                                ds.blit(up,up1)
      
                            ds.blit(t6,t66)
                            ds.blit(t3,t33)
                            ds.blit(tr,tr1)
                            pygame.draw.line(ds,white,(1140,0),(1140,800),10)
                            pygame.draw.line(ds,white,(800,0),(1140,0),5)
                            pygame.draw.line(ds,white,(800,100),(1140,100),5)
                            pygame.draw.line(ds,white,(800,200),(1140,200),5)
                            pygame.draw.line(ds,white,(800,300),(1140,300),5)
                            pygame.draw.line(ds,white,(800,800),(1140,800),5)       
                            for i in blacklist:
                                op=give_pos(i)
                                oi=pygame.image.load("C:/Users/datta/Downloads/black square.png")
                                oi1=oi.get_rect()
                                oi1.center=(op)
                                ds.blit(oi,oi1)  
                        if imgdir=='d' and right1.centery<700:
                            cur_rc=give_rc(pos)
                            cur_bno=give_bno(cur_rc)
                            if (cur_bno+8) in blacklist:
                                blacklist.remove(cur_bno+8) 
                            pos[1]+=100
                            right1.center=pos
                            up1.center=pos
                            down1.center=pos
                            left1.center=pos
                            ds.fill(lightgreen)
                            for i in range(9):
                                k=100*i
                                pygame.draw.line(ds,white,(0,k),(800,k),5)
                            for j in range(9):
                                k=100*j
                                pygame.draw.line(ds,white,(k,0),(k,800),5)  

                            ds.blit(k1,k11)
                            ds.blit(k2,k22)  
                            
                            blit_img_nb(n3,"C:/Users/datta/Downloads/h.png")
                            blit_img_nb(n4,"C:/Users/datta/Downloads/h.png")            
                            for i in zbl:
                                j=give_pos(i)
                                i11.center=j
                                ds.blit(i1,i11)
                                n=give_nb(i)
                                blit_img_nb(n,"C:/Users/datta/Downloads/s.png")              
                            if(nboth!=[]):
                                for i in range(len(nboth)):
                                    p1=pygame.image.load("C:/Users/datta/Downloads/b.png")
                                    p11=p1.get_rect()
                                    p11.center=give_pos(nboth[i])
                                    ds.blit(p1,p11)   
                            for i in g:
                                p1=pygame.image.load("C:/Users/datta/Downloads/gold.png")
                                p11=p1.get_rect()
                                p11.center=give_pos(i)
                                ds.blit(p1,p11) 
                                ds.blit(down,down1)
                            for i in blacklist:
                                op=give_pos(i)
                                oi=pygame.image.load("C:/Users/datta/Downloads/black square.png")
                                oi1=oi.get_rect()
                                oi1.center=(op)
                                ds.blit(oi,oi1)  
                            ds.blit(t3,t33)
                            ds.blit(t6,t66)
                            ds.blit(tr,tr1)

                            pygame.draw.line(ds,white,(1140,0),(1140,800),10)
                            pygame.draw.line(ds,white,(800,0),(1140,0),5)
                            pygame.draw.line(ds,white,(800,100),(1140,100),5)
                            pygame.draw.line(ds,white,(800,200),(1140,200),5)
                            pygame.draw.line(ds,white,(800,300),(1140,300),5)
                            pygame.draw.line(ds,white,(800,800),(1140,800),5)                                   
                        rowcol=give_rc(pos)
                        block=give_bno(rowcol)
                        if block in danger:
                            ss2.play()
                            ds.fill(lightgreen)
                            for i in range(9):
                                k=100*i
                                pygame.draw.line(ds,white,(0,k),(800,k),5)
                            for j in range(9):
                                k=100*j
                                pygame.draw.line(ds,white,(k,0),(k,800),5)
                            
                            del up
                            del right
                            del left
                            del down

                            t44.center=((400,400))
                            ds.blit(t4,t44)
                          
                            


                    except:
                        ds.fill(lightgreen)
                        for i in range(9):
                            k=100*i
                            pygame.draw.line(ds,white,(0,k),(800,k),5)
                        for j in range(9):
                            k=100*j
                            pygame.draw.line(ds,white,(k,0),(k,800),5)  
                            pygame.draw.line(ds,white,(1140,0),(1140,800),10)
                            pygame.draw.line(ds,white,(800,0),(1140,0),5)
                            pygame.draw.line(ds,white,(800,100),(1140,100),5)
                            pygame.draw.line(ds,white,(800,200),(1140,200),5)
                            pygame.draw.line(ds,white,(800,300),(1140,300),5)
                            pygame.draw.line(ds,white,(800,800),(1140,800),5)  
                        t44.center=(400,400)     
                        ds.blit(t4,t44) 
                if event.key==pygame.K_RETURN:
                    ss1.play()
                    if gold!=0:
                        rowcol=give_rc(pos)
                        block=give_bno(rowcol)
                        if block in g:
                            goldleft-=1
                            t6=t2.render("GOLD LEFT : "+str(goldleft),True,(black),(lightgreen))
                            g.remove(block)
                            ds.fill(lightgreen)
                            for i in range(9):
                                k=100*i
                                pygame.draw.line(ds,white,(0,k),(800,k),5)
                            for j in range(9):
                                k=100*j
                                pygame.draw.line(ds,white,(k,0),(k,800),5)  

                            ds.blit(k1,k11)
                            ds.blit(k2,k22)  
                            
                            blit_img_nb(n3,"C:/Users/datta/Downloads/h.png")
                            blit_img_nb(n4,"C:/Users/datta/Downloads/h.png")            
                            for i in zbl:
                                j=give_pos(i)
                                i11.center=j
                                ds.blit(i1,i11)
                                n=give_nb(i)
                                blit_img_nb(n,"C:/Users/datta/Downloads/s.png")               
                            if(nboth!=[]):
                                for i in range(len(nboth)):
                                    p1=pygame.image.load("C:/Users/datta/Downloads/b.png")
                                    p11=p1.get_rect()
                                    p11.center=give_pos(nboth[i])
                                    ds.blit(p1,p11)   
                            for i in g:
                                p1=pygame.image.load("C:/Users/datta/Downloads/gold.png")
                                p11=p1.get_rect()
                                p11.center=give_pos(i)
                                ds.blit(p1,p11) 
                            if imgdir=='r':
                                ds.blit(right,right1)
                            elif imgdir=='u':
                                ds.blit(up,up1)
                            elif imgdir=='d':
                                ds.blit(down,down1)                      
                            elif imgdir=='l':
                                ds.blit(left,left1)
                    ds.blit(t3,t33)
                    ds.blit(t6,t66)
                    ds.blit(tr,tr1)
                    pygame.draw.line(ds,white,(1140,0),(1140,800),10)
                    pygame.draw.line(ds,white,(800,0),(1140,0),5)
                    pygame.draw.line(ds,white,(800,100),(1140,100),5)
                    pygame.draw.line(ds,white,(800,200),(1140,200),5)
                    pygame.draw.line(ds,white,(800,300),(1140,300),5)
                    pygame.draw.line(ds,white,(800,800),(1140,800),5)                           
                    for i in blacklist:
                        op=give_pos(i)
                        oi=pygame.image.load("C:/Users/datta/Downloads/black square.png")
                        oi1=oi.get_rect()
                        oi1.center=(op)
                        ds.blit(oi,oi1)  
                if event.key==pygame.K_SPACE:
                    ss3.play()
                    if arrows>0:
                        arrows-=1

                    t3=t2.render("ARROWS LEFT : "+str(arrows),True,(black),(lightgreen))
                    ds.blit(t3,t33)
                    if(arrow_cond(imgzh1) and arrows>0):
                        if imgzh1 in danger:
                            danger.remove(imgzh1)
                            zbl.remove(imgzh1)
                        ds.fill(lightgreen)
                        for i in range(9):
                            k=100*i
                            pygame.draw.line(ds,white,(0,k),(800,k),5)
                        for j in range(9):
                            k=100*j
                            pygame.draw.line(ds,white,(k,0),(k,800),5)                     

                        ds.blit(k1,k11)
                        ds.blit(k2,k22)  
                        
                        blit_img_nb(n3,"C:/Users/datta/Downloads/h.png")
                        blit_img_nb(n4,"C:/Users/datta/Downloads/h.png")            
                        for i in zbl:
                            j=give_pos(i)
                            i11.center=j
                            ds.blit(i1,i11)
                            n=give_nb(i)
                            blit_img_nb(n,"C:/Users/datta/Downloads/s.png")                     
                        if(nboth!=[]):
                            for i in range(len(nboth)):
                                p1=pygame.image.load("C:/Users/datta/Downloads/b.png")
                                p11=p1.get_rect()
                                p11.center=give_pos(nboth[i])
                                ds.blit(p1,p11)   
                        for i in g:
                            p1=pygame.image.load("C:/Users/datta/Downloads/gold.png")
                            p11=p1.get_rect()
                            p11.center=give_pos(i)
                            ds.blit(p1,p11) 
                        if imgdir=='r':
                            ds.blit(right,right1)
                        elif imgdir=='u':
                            ds.blit(up,up1)
                        elif imgdir=='d':
                            ds.blit(down,down1)                      
                        elif imgdir=='l':
                            ds.blit(left,left1)
                        ds.blit(t3,t33)
                        ds.blit(t6,t66)
                        ds.blit(tr,tr1)
                        
                        pygame.draw.line(ds,white,(1140,0),(1140,800),10)
                        pygame.draw.line(ds,white,(800,0),(1140,0),5)
                        pygame.draw.line(ds,white,(800,100),(1140,100),5)
                        pygame.draw.line(ds,white,(800,200),(1140,200),5)
                        pygame.draw.line(ds,white,(800,300),(1140,300),5)
                        pygame.draw.line(ds,white,(800,800),(1140,800),5)                               
                        for i in blacklist:
                            op=give_pos(i)
                            oi=pygame.image.load("C:/Users/datta/Downloads/black square.png")
                            oi1=oi.get_rect()
                            oi1.center=(op)
                            ds.blit(oi,oi1)  
                    if(arrow_cond(imgzh2) and arrows>0):
                        if imgzh2 in danger:
                            danger.remove(imgzh2)
                            zbl.remove(imgzh2)
                        ds.fill(lightgreen)
                        for i in range(9):
                            k=100*i
                            pygame.draw.line(ds,white,(0,k),(800,k),5)
                        for j in range(9):
                            k=100*j
                            pygame.draw.line(ds,white,(k,0),(k,800),5)                     

                        ds.blit(k1,k11)
                        ds.blit(k2,k22)  
                        
                        blit_img_nb(n3,"C:/Users/datta/Downloads/h.png")
                        blit_img_nb(n4,"C:/Users/datta/Downloads/h.png")            
                        for i in zbl:
                            j=give_pos(i)
                            i11.center=j
                            ds.blit(i1,i11)
                            n=give_nb(i)
                            blit_img_nb(n,"C:/Users/datta/Downloads/s.png")                      
                        if(nboth!=[]):
                            for i in range(len(nboth)):
                                p1=pygame.image.load("C:/Users/datta/Downloads/b.png")
                                p11=p1.get_rect()
                                p11.center=give_pos(nboth[i])
                                ds.blit(p1,p11)   
                        for i in g:
                            p1=pygame.image.load("C:/Users/datta/Downloads/gold.png")
                            p11=p1.get_rect()
                            p11.center=give_pos(i)
                            ds.blit(p1,p11)                     
                        if imgdir=='r':
                            ds.blit(right,right1)
                        elif imgdir=='u':
                            ds.blit(up,up1)
                        elif imgdir=='d':
                            ds.blit(down,down1)                      
                        elif imgdir=='l':
                            ds.blit(left,left1)
                        ds.blit(t3,t33)
                        ds.blit(t6,t66)
                        ds.blit(tr,tr1)
                        pygame.draw.line(ds,white,(1140,0),(1140,800),10)
                        pygame.draw.line(ds,white,(800,0),(1140,0),5)
                        pygame.draw.line(ds,white,(800,100),(1140,100),5)
                        pygame.draw.line(ds,white,(800,200),(1140,200),5)
                        pygame.draw.line(ds,white,(800,300),(1140,300),5)
                        pygame.draw.line(ds,white,(800,800),(1140,800),5)       
                        for i in blacklist:
                            op=give_pos(i)
                            oi=pygame.image.load("C:/Users/datta/Downloads/black square.png")
                            oi1=oi.get_rect()
                            oi1.center=(op)
                            ds.blit(oi,oi1)  
                if event.key==pygame.K_r:
                    ss1.play()
                    open_second_window()
        if(goldleft==0):
            ds.fill(lightgreen)
            for i in range(9):
                k=100*i
                pygame.draw.line(ds,white,(0,k),(800,k),5)
            for j in range(9):
                k=100*j
                pygame.draw.line(ds,white,(k,0),(k,800),5)  
            ds.blit(t1,t11)    


    pygame.display.update()

pygame.quit()