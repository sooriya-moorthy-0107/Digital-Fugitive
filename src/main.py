import pygame
import sys
import os

from agent import MinesweeperAI
from config import *
from city import CityGrid, get_heat_color

def scale_bg(img, target_width, target_height):
    """
    Scales the background image to fill the target dimensions 
    while preserving aspect ratio.
    """
    img_rect = img.get_rect()
    scale_w = target_width / img_rect.width
    scale_h = target_height / img_rect.height
    scale_factor = max(scale_w, scale_h) # Fill the screen
    
    new_w = int(img_rect.width * scale_factor)
    new_h = int(img_rect.height * scale_factor)
    scaled_img = pygame.transform.smoothscale(img, (new_w, new_h))
    
    bg_surface = pygame.Surface((target_width, target_height))
    bg_rect = bg_surface.get_rect()
    scaled_rect = scaled_img.get_rect(center=bg_rect.center)
    bg_surface.blit(scaled_img, scaled_rect)
    return bg_surface

def main():
    pygame.init()
    pygame.mixer.init() 
    
    screen_width = WIDTH * CELL_SIZE + 100
    screen_height = HEIGHT * CELL_SIZE + 150
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("AI Police - Hot & Cold Radar (Upgraded UI)")
    
    font_header = pygame.font.SysFont("arial", 24, bold=True)
    font_cell = pygame.font.SysFont("arial", 16, bold=True)
    font_small = pygame.font.SysFont("arial", 10, bold=True)

    city = CityGrid()
    ai = MinesweeperAI(height=HEIGHT, width=WIDTH)

    revealed = set()
    lost = False
    setup_mode = True 
    
    offset_x = 50
    offset_y = 100

    # --- LOAD ASSETS ---
    assets = {}
    # Get the directory of this script, then go up one level to the project root
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    image_files = [
        (os.path.join(base_dir, "assets", "images", "police_bg.jpg"), "bg"), 
        (os.path.join(base_dir, "assets", "images", "thief.png"), "thief"), 
        (os.path.join(base_dir, "assets", "images", "police.png"), "police"), 
        (os.path.join(base_dir, "assets", "images", "jail.png"), "jail")
    ]
    
    for filepath, key in image_files:
        try:
            if os.path.exists(filepath):
                img = pygame.image.load(filepath)
                if key == "bg":
                    assets[key] = scale_bg(img, screen_width, screen_height)
                else:
                    assets[key] = pygame.transform.smoothscale(img, (CELL_SIZE, CELL_SIZE))
        except Exception as e:
            print(f"Warning: Could not load image '{filepath}': {e}")

    try:
        audio_path = os.path.join(base_dir, "assets", "audio", "background_siren.wav")
        if os.path.exists(audio_path):
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.set_volume(0.6) 
            pygame.mixer.music.play(-1) 
            print("Audio: Siren background music started successfully!")
        else:
            print(f"Audio: '{audio_path}' not found.")
    except Exception as e:
        print(f"Warning: Could not play audio: {e}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and setup_mode:
                mx, my = pygame.mouse.get_pos()
                c = (mx - offset_x) // CELL_SIZE
                r = (my - offset_y) // CELL_SIZE
                if 0 <= r < HEIGHT and 0 <= c < WIDTH:
                    city.toggle_thief((r, c))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and setup_mode:
                    setup_mode = False
                    print("HOT/COLD RADAR ACTIVATED")

        if not setup_mode and not lost:
            pygame.time.delay(100) 
            
            move = ai.make_safe_move()
            if move is None:
                move = ai.make_random_move()

            if move:
                if move in city.thieves:
                    lost = True
                    print(f"AMBUSH! Officer hit at {move}")
                else:
                    intel = city.get_intel(move)
                    revealed.add(move)
                    ai.add_knowledge(move, intel)

        # Draw Background
        if 'bg' in assets:
            screen.blit(assets['bg'], (0, 0))
        else:
            screen.fill(BLACK)

        # Draw Headers
        if setup_mode:
            t1 = font_header.render("PHASE 1: SET TRAPS", True, THIEF_RED)
            t2 = font_small.render("Click grid to hide thieves. Press ENTER to start.", True, WHITE)
            screen.blit(t1, (offset_x, 20))
            screen.blit(t2, (offset_x, 60))
        elif lost:
            t1 = font_header.render("MISSION FAILED", True, THIEF_RED)
            screen.blit(t1, (offset_x, 30))
        else:
            t1 = font_header.render("PHASE 2: RADAR TRACKING", True, WARM_COLOR)
            screen.blit(t1, (offset_x, 30))

        # Draw Grid
        for r in range(HEIGHT):
            for c in range(WIDTH):
                rect = pygame.Rect(offset_x + c*CELL_SIZE, offset_y + r*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                
                color = HOUSE_UNKNOWN
                text = ""
                txt_col = TEXT_COLOR
                img_to_draw = None

                if setup_mode:
                    if (r,c) in city.thieves:
                        color = THIEF_RED
                        img_to_draw = assets.get('thief')
                        if not img_to_draw:
                            text = "T"
                            txt_col = WHITE
                    else:
                        color = (200, 200, 200)
                
                else:
                    if (r,c) in ai.mines: 
                        color = THIEF_RED
                        img_to_draw = assets.get('jail') 
                        if not img_to_draw:
                            text = "BUSTED"
                            txt_col = WHITE
                    elif (r,c) in ai.safes and (r,c) not in revealed:
                        color = POLICE_BLUE 
                        img_to_draw = assets.get('police') 
                    elif (r,c) in revealed:
                        color = get_heat_color((r, c), city.thieves)
                        intel = city.get_intel((r,c))
                        if intel > 0: text = str(intel)
                    
                    if lost and (r,c) in city.thieves:
                        color = (100, 0, 0)
                        img_to_draw = assets.get('thief')
                        if not img_to_draw:
                            text = "T"
                            txt_col = WHITE

                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, GRID_LINE, rect, 2)
                
                if img_to_draw:
                    screen.blit(img_to_draw, rect.topleft)
                elif text:
                    f = font_small if text == "BUSTED" else font_cell
                    txt_surf = f.render(text, True, txt_col)
                    txt_rect = txt_surf.get_rect(center=rect.center)
                    screen.blit(txt_surf, txt_rect)

        pygame.display.flip()

if __name__ == "__main__":
    main()
