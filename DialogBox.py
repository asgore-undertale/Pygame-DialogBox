import keyboard, pygame, time
pygame.init()

# use it in another thread

class DialogBox():
    def __init__(self, win, x=0, y=0, boxW=0, boxH=0, boxC=(0, (255, 255, 255)), borderS=0, sleepT=0, textC=(255, 255, 255), fontP='', fontS=0, perline=0, RTL=False):
        super(DialogBox, self).__init__()
        
        self.win = win
        self.x = x
        self.y = y
        self.boxW = boxW
        self.boxH = boxH
        self.boxC = boxC
        self.textC = textC
        self.borderS = borderS
        self.sleepT = sleepT
        self.perline = perline
        self.fontS = fontS
        self.surface = pygame.Surface((self.boxW, self.boxH))
        self.font = pygame.font.Font(fontP, fontS)
        self.RTL = RTL
    
    def update(self):
        self.win.blit(self.surface, (self.x, self.y))
        pygame.display.update()
    
    def open(self):
        self.surface.set_alpha(255)
        self.draw()
        self.update()
    
    def close(self):
        self.surface.set_alpha(0)
        self.update()
    
    def draw(self):
        pygame.draw.rect(self.surface, self.boxC[0], (self.x, self.y, self.boxW, self.boxH))
        pygame.draw.rect(self.surface, self.boxC[1], (self.x, self.y, self.boxW, self.boxH), self.borderS)
    
    def type(self, text):
        self.open()
        
        _x, _y = (self.borderS * (not self.RTL)) + ((self.boxW - self.borderS) * self.RTL), self.borderS
        x, y = _x, _y
        
        for char in text:
            if char == '\n':
                y += self.fontS + self.perline
                x = _x
                continue
            
            charimg = self.font.render(char, True, self.textC)
            charW, charH = charimg.get_size()
            
            if self.RTL: x -= charW
            self.surface.blit(charimg, (x, y))
            #pygame.draw.rect(self.surface, (0, 0, 255), (x, y, charW, charH), 1) # charbox
            if not self.RTL: x += charW
            
            self.update()
            time.sleep(self.sleepT)
        
        keyboard.wait('enter')
        self.close()


#################> To Test <#################
# boxWidth, boxHeight, borderThick = 240, 80, 10

# WindowSize = (boxWidth, boxHeight)
# pygame.display.set_caption('DialogBox')
# textbox = pygame.display.set_mode(WindowSize)

# pygame.display.update()
# dialogbox = DialogBox(textbox, 0, 0, boxWidth, boxHeight, (0, (255, 255, 255)), borderThick, 0, (255, 255, 255), 'AMARIYA-BOLD.ttf', 24, 5, False)
# dialogbox.type('hello\nﻡﻼﺴﻟﺍ')

# while True:
    # for event in pygame.event.get():
        # if event.type is pygame.QUIT: 
            # pygame.quit()