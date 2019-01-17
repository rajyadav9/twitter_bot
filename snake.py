
#importing predefined modules
import random,sys,pygame,time

#check for errors in game
check_errors=pygame.init() #check_errors[0,7]
if check_errors[1]>0:
    print("have zero initializing errors,exiting. . . ".format(check_errors[1]))
    sys.exit(-1)
else:
     print("(+)pygame successfully initialized")

#surface of playing
playSurface=pygame.display.set_mode((720,460))
pygame.display.set_caption('naagin game')

#setting colos fo elemnts
red=pygame.Color(255,0,0) #signal gamee over
green=pygame.Color(0,255,0)#snake color
black=pygame.Color(0,0,0)#score
brown=pygame.Color(160,45,45)#background
white=pygame.Color(255,255,255)#food that snakes eat

#fpscontroller
fpsController=pygame.time.Clock()#frames per sec

#setting imp variables
snakePos=[100,50] # starting position
snakeBody=[[100,50],[90,50],[80,50]]  #snake body having 3 blocks


foodPos=[random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn=True

direction='RIGHT'
changeto =direction

score=0

#function to game over
def gameOver():
    myFont=pygame.font.SysFont('monaco',72)# system fonts is used ,72 desc size
    gosurf=myFont.render("GAME OVER.!!",True,red)#text,true or1,font color 
    gorect=gosurf.get_rect()#to get rectangullar conponent of gosurf
    gorect.midtop=(360,15)# where to display msg of game over give x and y coordinates
    playSurface.blit(gosurf,gorect)# to place on play surface.rect is placed on surface
    showScore(0)
    pygame.display.flip()#to update the fps
   
    time.sleep(4)
    pygame.quit()#pygame exit
    sys.exit()# console exit
  
#fun to show score
def showScore(choice=1):
    sfont=pygame.font.SysFont('monaco',24)
    ssruf=sfont.render('Score : {0}'.format(score),True,black)
    srect=ssruf.get_rect()
    if choice==1:
        srect.midtop=(80,10)
    else:
         srect.midtop=(360,120)
    playSurface.blit(ssruf,srect)
    


#main logic of game
while True:
      for event in pygame.event.get(): #TO GET EVENT
        if event.type == pygame.QUIT:  #IF EVENT TYPE IS QUIT THEN QUIT
            pygame.quit()
            sys.quit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT or event.key==ord('d'):
                changeto='RIGHT'
            if event.key==pygame.K_LEFT or event.key==ord('a'):
                 changeto='LEFT' 
            if event.key==pygame.K_UP or event.key==ord('w'):
                 changeto='UP'
            if event.key==pygame.K_DOWN or event.key==ord('s'):
                 changeto='DOWN'
            if event.key==pygame.K_ESCAPE:
                 pygame.event.post(pyagme.event.Event(pygame.QUIT))#POST AN EVENT TO QUIT
 # set directions
      if changeto =='RIGHT' and not direction =='LEFT':
            direction='RIGHT'            
      if changeto =='LEFT' and not direction =='RIGHT':
            direction='LEFT'  
      if changeto=='UP' and not direction=='DOWN':
            direction='UP'  
      if  changeto=='DOWN' and not direction=='UP':
            direction='DOWN' 
 #UPDATING SBAKE POS SNAKEPOS[X Y]
      if direction =='RIGHT':
          snakePos[0]+=10
      if direction =='LEFT':
          snakePos[0]-=10
      if direction =='UP':
          snakePos[1]-=10
      if direction =='DOWN':
          snakePos[1]+=10
      # SNAKE BODY UPDATION MECHANISM
      snakeBody.insert(0,list(snakePos))
      if snakePos[0]==foodPos[0] and snakePos[1]==foodPos[1]:
          score+=5
          foodSpawn=False
      else:
            snakeBody.pop()
      #foodspawn
      if foodSpawn==False:
         foodPos=[random.randrange(1,72)*10,random.randrange(1,46)*10]
      foodSpawn=True
      #drw snake body
      playSurface.fill(white)
      for pos in snakeBody:
          pygame.draw.rect(playSurface,green,
          pygame.Rect(pos[0],pos[1],10,10))
          
      pygame.draw.rect(playSurface,brown,
      pygame.Rect(foodPos[0],foodPos[1],10,10))

      # setting boundaries
      if snakePos[0]>710 or snakePos[0]<0:
          gameOver()
      
      if snakePos[1]>450 or snakePos[1]<0:
          gameOver()


 #head and body coliision
      for block in snakeBody[1:]:
            if snakePos[0]==block[0] and snakePos[1]==block[1]:
                gameOver()
      showScore()
      pygame.display.flip() 
    
      fpsController.tick(14)#no of ticks or frames per sec
       
