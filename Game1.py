import pygame, simpleGE, random

class Tank(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Tank Green Base Idle.png")
        self.setSize(50, 30)
        self.accel = 0.05

        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.imageAngle +=2
        if self.isKeyPressed(pygame.K_RIGHT):
            self.imageAngle -= 2
        if self.isKeyPressed(pygame.K_UP):
            self.addForce(self.accel, self.imageAngle)
        if self.isKeyPressed(pygame.K_DOWN):
            self.addForce(-self.accel, self.imageAngle)
            
class Turret(simpleGE.Sprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.setImage("Tank Green Turret Idle.png")
        self.setSize(60, 40)
    
    def process(self):
        self.position = self.parent.position
        if self.isKeyPressed(pygame.K_a):
            self.imageAngle += 3
        if self.isKeyPressed(pygame.K_d):
            self.imageAngle -= 3
            
class Bullet(simpleGE.Sprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.colorRect("yellow", (3, 2))
        self.setBoundAction(self.HIDE)
        self.hide()
        
    def fire(self):
        self.show()
        self.position = self.parent.position
        self.moveAngle = self.parent.imageAngle
        self.speed = 10
    
    def reset(self):
        self.hide()
        
class Shell(simpleGE.Sprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.colorRect("white", (10, 4))
        self.setBoundAction(self.HIDE)
        self.hide()
        
    def fire(self):
        self.show()
        self.position = self.parent.position
        self.moveAngle = self.parent.imageAngle
        self.speed = 20
    
    def reset(self):
        self.hide()
    
class Target(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("red", (10, 10))
        self.reset()
        
    def reset(self):
        x = random.randint(0, self.screen.get_width())
        y = random.randint(0, self.screen.get_height())
        self.position = (x, y)

class TargetsHitLabel(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.fgColor ="black"
        self.bgColor = "white"
        self.text = "Targets Hit"
        self.clearBack = True
        self.center = (100, 30)
        self.size = (160, 40)
        
class TimerLabel(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time"
        self.center = (500, 30)
        self.size = (150, 40)
        self.clearBack = True
        self.fgColor = "black"
        self.bgColor = "white"
        
    

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.background.fill("gray")  
        self.tank = Tank(self)
        self.turret = Turret(self, self.tank)
        
        self.NUM_TARGETS = 10
        self.targets = []
        for i in range(self.NUM_TARGETS):
            self.targets.append(Target(self))
            
        self.NUM_BULLETS = 75
        self.currentBullet = 0
        self.bullets = []
        for i in range(self.NUM_BULLETS):
            self.bullets.append(Bullet(self, self.tank))
            
        self.NUM_SHELLS = 30
        self.currentShell = 0
        self.shells = []
        for i in range(self.NUM_SHELLS):
            self.shells.append(Shell(self, self.turret))
            
        self.targetsHitLabel = TargetsHitLabel()
        self.targetsHit = 0
        
        self.timerLabel = TimerLabel()
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 30
        
        self.sprites = [self.tank,
                        self.bullets,
                        self.turret,
                        self.shells,
                        self.targets,
                        self.targetsHitLabel,
                        self.timerLabel]
        
    def process(self):
        if self.isKeyPressed(pygame.K_SPACE):
            self.currentBullet += 1
            if self.currentBullet >= self.NUM_BULLETS:
                self.currentBullet = 0
            self.bullets[self.currentBullet].fire()
        for target in self.targets:
            if self.tank.collidesWith(target):
                target.reset()
                self.targetsHit += 1
                self.targetsHitLabel.text = f"Targets Hit {self.targetsHit}"
                
            for bullet in self.bullets:
                if bullet.collidesWith(target):
                    target.reset()
                    bullet.reset()
                    self.targetsHit += 1
                    self.targetsHitLabel.text = f"Targets Hit {self.targetsHit}"
                    
            for shell in self.shells:
                if shell.collidesWith(target):
                    target.reset()
                    shell.reset()
                    self.targetsHit += 1
                    self.targetsHitLabel.text = f"Targets Hit {self.targetsHit}"
            
            timeLeft = self.timer.getTimeLeft()
            self.timerLabel.text = f"Time left: {timeLeft: .2f}"
            if timeLeft < 0:
                self.stop()
            
    def processEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                self.currentShell += 1
                if self.currentShell >= self.NUM_SHELLS:
                    self.currentShell = 0
                self.shells[self.currentShell].fire()
                
class StartScreen(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.instructionsLabel = simpleGE.MultiLabel()
        self.instructionsLabel.center = (320, 240)
        self.instructionsLabel.size = (500, 400)
        self.instructionsLabel.textLines = [
            "Welcome to Tank Shooting Mayhem!",
            "Move the tank with the arrow keys",
            "Move the turret with the \"a\" and \"d\" keys",
            "Fire the machine gun with the spacebar",
            "Fire the main turret with the \"e\" key",
            "Shoot or run over as many targets before",
            "your time runs out.",
            ""
            "Click to begin."
        ]
        
        self.sprites = [self.instructionsLabel]
        
    def processEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.stop()
            
class GameFinished(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
        self.targetsHit = 0
        self.targetsHitLabel = simpleGE.Label()
        self.targetsHitLabel.text = f"Targets Hit: {self.targetsHit}"
        self.targetsHitLabel.center = (300, 150)
        
        self.playAgainButton = simpleGE.Button()
        self.playAgainButton.text = "Play Again!"
        self.playAgainButton.center = (175, 300)
        
        self.quitButton = simpleGE.Button()
        self.quitButton.text = "Quit :("
        self.quitButton.center = (475, 300)
        
        self.sprites = [self.targetsHitLabel, self.playAgainButton, self.quitButton]
        
    def setTargetsHit(self, targetsHit):
        self.targetsHit = targetsHit
        self.targetsHitLabel.text = f"Targets Hit: {self.targetsHit}"
    
    def process(self):
        if self.playAgainButton.clicked:
            self.next = "again"
            self.stop()
        
        if self.quitButton.clicked:
            self.next = "quit"
            self.stop()
                
        
            
        
def main():
    
    stillPlaying = True
    while(stillPlaying):
        startScreen = StartScreen()
        startScreen.start()
        
        game = Game()
        game.start()
        
        gameFinished = GameFinished()
        gameFinished.setTargetsHit(game.targetsHit)
        gameFinished.start()
        
        if gameFinished.next == "quit":
            stillPlaying = False
    
if __name__ == "__main__":
    main()
        