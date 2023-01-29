import pygame
pygame.init()

class Game():
    def __init__(self):
        pygame.display.set_caption("Mystical Mineshaft")
        self.screen = pygame.display.set_mode((1400, 750))
        self.clock = pygame.time.Clock()
        self.mini_map_surf = pygame.Surface((150, 150))
        
        self.backgr_surf = pygame.image.load("C:/Users/eran rotem/Desktop/repo/MysticalMineshaft/8BitPNG/8BitMinerBG2.png").convert()
        # self.backgr_surf = pygame.Surface((900, 500))
        # self.backgr_surf.fill("#1b6e3b")
        
        self.player_surf = pygame.image.load("C:/Users/eran rotem/Desktop/repo/MysticalMineshaft/8BitPNG/8BitMinerV4.png").convert_alpha()
        # self.player_surf = pygame.Surface((18, 32))
        player_rect = self.player_surf.get_rect(midbottom = (100, 550))

        self.mini_map_surf.fill("#e9f09c")
        gravity = 0


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    # print(keys)
                    if event.key == pygame.K_SPACE and player_rect.bottom >= 550:
                        gravity = -15
                    # if event.key == pygame.K_d:
                    # if event.key == pygame.K_a:
                    if keys[pygame.K_a]:                    
                        self.player_surf = pygame.image.load("C:/Users/eran rotem/Desktop/repo/MysticalMineshaft/8BitPNG/8BitMinerFlip.png").convert_alpha()
                        player_rect.x -= 20
                    if keys[pygame.K_d]:
                        self.player_surf = pygame.image.load("C:/Users/eran rotem/Desktop/repo/MysticalMineshaft/8BitPNG/8BitMinerV4.png").convert_alpha()
                        player_rect.x += 20
                                
            self.screen.blit(self.backgr_surf, (0, 0))
            self.screen.blit(self.player_surf, player_rect)
            self.screen.blit(self.mini_map_surf, (1230, 580))
            
            gravity += 1
            player_rect.y += gravity
            if player_rect.bottom >= 550:
                player_rect.bottom = 550
            
            pygame.display.update() 
            self.clock.tick(60)

Game()