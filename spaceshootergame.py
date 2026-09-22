import pygame
import random
class Alieninvasion():
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        self.bullets=[]
        self.player=pygame.Rect(10,700,50,50)
        self.enemies=[]
        self.game_over=False
        self.deployed=0
        self.totalspawn=0
        #self.enemy_alive=True 
    def run(self):
        running = True
        
            
        while running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
            if self.player.x<0:
                self.player.x=0
            if self.player.x>1150:
                self.player.x=1150
            self.key=pygame.key.get_pressed()
            if self.key[pygame.K_LEFT]:
                self.player.x-=20   
            if self.key[pygame.K_RIGHT]:
                self.player.x+=20
            if self.key[pygame.K_SPACE]:
                bullet=pygame.Rect(0,0,5,5)
                bullet.centerx=self.player.centerx
                bullet.bottom=self.player.top
                self.bullets.append(bullet)
                #self.enemy=pygame.Rect(100,0,100,100)
            if random.randint(0,50)==1:
                enemy=pygame.Rect(random.randint(0,1150),-50,50,50)
                self.enemies.append(enemy)
                self.totalspawn+=1
                    
            
            self.screen.fill((0,0,0))
            #move enemies
            for enemy in self.enemies:
                enemy.y+=5
                pygame.draw.rect(self.screen,(225,0,0),(enemy.x,enemy.y,enemy.height,enemy.width))
                if enemy.y>850:
                    self.enemies.remove(enemy)
                
            for bullet in self.bullets:
                bullet.y-=10
                pygame.draw.rect(self.screen,(225,0,225),(bullet.x,bullet.y,bullet.height, bullet.width,))
                for enemy in self.enemies:

                    if bullet.colliderect(enemy):
                        #self.enemy_alive=False
                        enemy.x=random.randint(0,1100)
                        enemy.y=0
                        self.enemies.remove(enemy)#jab bullet hit toh vo enemy ko list se hi hata degi so enemy will disappear
                        self.deployed+=1
                        self.bullets.remove(bullet)
                        break
                        #self.enemy_alive=True
               # if self.enemy_alive:
            for enemy in self.enemies:   
                if self.player.colliderect(enemy):
                    self.game_over=True
                    break
                if self.game_over:  
                    running=False
                if enemy.y>800:
                    running=False
            clock=pygame.time.Clock()
            clock.tick(120)
                    
                                                
            
            pygame.draw.rect(self.screen,(0,0,225),(self.player.x,self.player.y,self.player.height,self.player.width))
            pygame.display.flip()

        pygame.quit()
        print("Game Over")
        print("your score:-",self.deployed)
        print("total spawned enemies",self.totalspawn)
if __name__=="__main__": #this is used so that a user can run this in this file only but lets say if user imports this file in another file then on import only this file may have got run if this might not be present thats why to avoid unnecessary running we use it 
    
    ai=Alieninvasion()  
    ai.run()

