import math
import os
from PIL import Image, ImageDraw, ImageFont

# Canvas dimensions
WIDTH = 800
HEIGHT = 320
NUM_FRAMES = 30
DURATION = 45 # ms per frame (~22 fps)

frames = []

for frame_idx in range(NUM_FRAMES):
    t = frame_idx / NUM_FRAMES  # Normalized 0.0 to 1.0
    cycle = math.sin(t * 2 * math.pi)

    img = Image.new("RGBA", (WIDTH, HEIGHT), (11, 15, 25, 255))
    draw = ImageDraw.Draw(img)

    # 1. Draw Background Grid Lines
    for y in (60, 120, 180):
        draw.line([(0, y), (WIDTH, y)], fill=(30, 41, 59, 255), width=1)

    # 2. Draw Stars / Sparkles
    star_positions = [(100, 50, 0), (450, 40, 0.33), (720, 60, 0.66)]
    for sx, sy, phase in star_positions:
        s_scale = 1 + 0.3 * math.sin((t + phase) * 2 * math.pi)
        r = int(3 * s_scale)
        color = (241, 196, 15, 255) if phase == 0 else ((0, 229, 255, 255) if phase < 0.5 else (255, 0, 85, 255))
        draw.ellipse([sx - r, sy - r, sx + r, sy + r], fill=color)

    # 3. Ground Platform & Moving Road Lines
    draw.rectangle([0, 240, WIDTH, HEIGHT], fill=(15, 23, 42, 255))
    draw.line([(0, 240), (WIDTH, 240)], fill=(0, 229, 255, 255), width=3)

    # Animated road dashes
    dash_offset = (frame_idx * 12) % 40
    for x in range(-40 + dash_offset, WIDTH + 40, 40):
        draw.line([(x, 270), (x + 20, 270)], fill=(0, 229, 255, 180), width=4)

    # Air speed lines
    speed_offset = (frame_idx * 25) % 60
    for y_line, col in [(150, (0, 229, 255, 60)), (190, (255, 0, 85, 50))]:
        for sx in range(-60 + speed_offset, WIDTH + 60, 120):
            draw.line([(sx, y_line), (sx + 40, y_line)], fill=col, width=2)

    # --- 4. UNDER CONSTRUCTION BANNER (LEFT) ---
    banner_wave = math.sin(t * 2 * math.pi) * 4
    bx, by = 40, 115 + banner_wave

    # Connection rope to Police
    draw.line([(bx + 210, by + 40), (bx + 310, by + 45)], fill=(241, 196, 15, 200), width=2)

    # Banner Shadow & Main Box
    draw.rounded_rectangle([bx + 5, by + 25, bx + 225, by + 85], radius=12, fill=(0, 0, 0, 80))
    draw.rounded_rectangle([bx, by + 20, bx + 220, by + 80], radius=12, fill=(30, 41, 59, 255), outline=(241, 196, 15, 255), width=3)

    # Hazard Stripes Bars
    draw.rectangle([bx + 3, by + 23, bx + 217, by + 30], fill=(241, 196, 15, 255))
    draw.rectangle([bx + 3, by + 70, bx + 217, by + 77], fill=(241, 196, 15, 255))
    for s_x in range(int(bx + 10), int(bx + 210), 16):
        draw.polygon([(s_x, by + 23), (s_x + 6, by + 23), (s_x, by + 30)], fill=(44, 62, 80, 255))
        draw.polygon([(s_x, by + 70), (s_x + 6, by + 70), (s_x, by + 77)], fill=(44, 62, 80, 255))

    # Traffic Cones Left & Right
    for cone_x in (bx - 5, bx + 205):
        draw.polygon([(cone_x + 10, by + 65), (cone_x + 22, by + 65), (cone_x + 18, by + 38), (cone_x + 14, by + 38)], fill=(255, 85, 0, 255))
        draw.polygon([(cone_x + 12, by + 53), (cone_x + 20, by + 53), (cone_x + 18, by + 47), (cone_x + 14, by + 47)], fill=(255, 255, 255, 255))
        draw.rectangle([cone_x + 7, by + 65, cone_x + 25, by + 69], fill=(230, 81, 0, 255))

    # Banner Text
    try:
        font = ImageFont.truetype("arialbd.ttf", 14)
    except:
        font = ImageFont.load_default()
    draw.text((bx + 110, by + 50), "UNDER CONSTRUCTION", fill=(241, 196, 15, 255), font=font, anchor="mm")

    # --- 5. CUTE POLICE OFFICER (MIDDLE) ---
    police_bob = math.sin(t * 4 * math.pi) * 4
    px, py = 370, 135 + police_bob

    # Dust puff
    dust_r = int(6 + 4 * (frame_idx % 5) / 5)
    draw.ellipse([px - 20 - dust_r, 235 - dust_r, px - 20 + dust_r, 235 + dust_r], fill=(148, 163, 184, int(150 * (1 - (frame_idx % 5)/5))))

    # Running legs & arms angles
    leg_angle = cycle * 25
    arm_angle = -cycle * 30

    # Back Leg
    bl_x = px + 25 + math.sin(math.radians(-leg_angle)) * 20
    draw.line([(px + 25, py + 75), (bl_x, py + 105)], fill=(30, 41, 59, 255), width=10)
    draw.ellipse([bl_x - 7, py + 101, bl_x + 7, py + 109], fill=(15, 23, 42, 255))

    # Front Leg
    fl_x = px + 35 + math.sin(math.radians(leg_angle)) * 20
    draw.line([(px + 35, py + 75), (fl_x, py + 105)], fill=(37, 99, 235, 255), width=10)
    draw.ellipse([fl_x - 7, py + 101, fl_x + 7, py + 109], fill=(15, 23, 42, 255))

    # Police Body Uniform
    draw.rounded_rectangle([px + 20, py + 40, px + 50, py + 78], radius=8, fill=(37, 99, 235, 255))
    draw.rectangle([px + 20, py + 68, px + 50, py + 73], fill=(15, 23, 42, 255))
    draw.ellipse([px + 33, py + 48, px + 39, py + 54], fill=(241, 196, 15, 255)) # Badge

    # Front Arm (Holding Whistle)
    fa_x = px + 40 + math.sin(math.radians(-arm_angle)) * 18
    draw.line([(px + 38, py + 48), (fa_x, py + 70)], fill=(37, 99, 235, 255), width=8)
    draw.ellipse([fa_x - 4, py + 67, fa_x + 4, py + 75], fill=(255, 223, 196, 255))
    draw.rectangle([fa_x, py + 68, fa_x + 8, py + 72], fill=(203, 213, 225, 255)) # Whistle

    # Head
    hx, hy = px + 35, py + 25
    draw.ellipse([hx - 18, hy - 18, hx + 18, hy + 18], fill=(255, 223, 196, 255))

    # Eyes & Sparkles
    draw.ellipse([hx + 2, hy - 4, hx + 8, hy + 3], fill=(15, 23, 42, 255))
    draw.ellipse([hx + 5, hy - 3, hx + 7, hy - 1], fill=(255, 255, 255, 255))
    draw.ellipse([hx - 10, hy - 4, hx - 4, hy + 3], fill=(15, 23, 42, 255))
    draw.ellipse([hx - 7, hy - 3, hx - 5, hy - 1], fill=(255, 255, 255, 255))

    # Rosy Cheeks & Open Mouth
    draw.ellipse([hx + 7, hy + 2, hx + 12, hy + 6], fill=(255, 138, 138, 160))
    draw.ellipse([hx - 12, hy + 2, hx - 7, hy + 6], fill=(255, 138, 138, 160))
    draw.arc([hx - 3, hy + 3, hx + 5, hy + 11], 0, 180, fill=(153, 27, 27, 255), width=2)

    # Police Cap
    draw.chord([hx - 20, hy - 25, hx + 20, hy], 180, 360, fill=(30, 58, 138, 255))
    draw.line([(hx, hy - 7), (hx + 20, hy - 3)], fill=(15, 23, 42, 255), width=3) # Visor
    draw.line([(hx - 18, hy - 10), (hx + 18, hy - 10)], fill=(241, 196, 15, 255), width=3)

    # Siren Flashing Light on Cap
    siren_col1 = (255, 0, 85, 255) if cycle > 0 else (0, 229, 255, 255)
    siren_col2 = (0, 229, 255, 255) if cycle > 0 else (255, 0, 85, 255)
    draw.ellipse([hx - 6, hy - 33, hx, hy - 25], fill=siren_col1)
    draw.ellipse([hx, hy - 33, hx + 6, hy - 25], fill=siren_col2)

    # --- 6. CUTE THIEF AGENT (RIGHT) ---
    thief_bob = math.cos(t * 4 * math.pi) * 4
    tx, ty = 580, 130 + thief_bob

    # Flying Sweat Droplets
    sweat_x = tx - 10 - (frame_idx * 5) % 20
    sweat_y = ty + 10 - (frame_idx * 3) % 15
    draw.ellipse([sweat_x - 3, sweat_y - 4, sweat_x + 3, sweat_y + 4], fill=(0, 229, 255, 220))

    # Thief Legs
    t_leg_angle = -cycle * 25
    tbl_x = tx + 25 + math.sin(math.radians(-t_leg_angle)) * 20
    draw.line([(tx + 25, ty + 75), (tbl_x, ty + 105)], fill=(30, 41, 59, 255), width=10)
    draw.ellipse([tbl_x - 7, ty + 101, tbl_x + 7, ty + 109], fill=(239, 68, 68, 255))

    tfl_x = tx + 35 + math.sin(math.radians(t_leg_angle)) * 20
    draw.line([(tx + 35, ty + 75), (tfl_x, ty + 105)], fill=(51, 65, 85, 255), width=10)
    draw.ellipse([tfl_x - 7, ty + 101, tfl_x + 7, ty + 109], fill=(239, 68, 68, 255))

    # Body / Striped Outfit
    draw.rounded_rectangle([tx + 20, ty + 40, tx + 50, ty + 78], radius=8, fill=(239, 68, 68, 255))
    draw.rectangle([tx + 20, ty + 47, tx + 50, ty + 52], fill=(255, 255, 255, 255))
    draw.rectangle([tx + 20, ty + 58, tx + 50, ty + 63], fill=(255, 255, 255, 255))
    draw.rectangle([tx + 20, ty + 69, tx + 50, ty + 74], fill=(255, 255, 255, 255))

    # Money Swag Sack Bag
    draw.ellipse([tx - 5, ty + 45, tx + 18, ty + 72], fill=(217, 119, 6, 255), outline=(146, 64, 14, 255), width=2)
    draw.text((tx + 6, ty + 58), "$", fill=(241, 196, 15, 255), font=font, anchor="mm")

    # Front Arm
    tfa_x = tx + 38 + math.sin(math.radians(t_leg_angle)) * 18
    draw.line([(tx + 35, ty + 48), (tfa_x, ty + 70)], fill=(239, 68, 68, 255), width=8)
    draw.ellipse([tfa_x - 4, ty + 67, tfa_x + 4, ty + 75], fill=(255, 223, 196, 255))

    # Head & Thief Mask
    thx, thy = tx + 35, ty + 25
    draw.ellipse([thx - 18, thy - 18, thx + 18, thy + 18], fill=(255, 223, 196, 255))

    # Bandit Mask
    draw.rounded_rectangle([thx - 18, thy - 6, thx + 18, thy + 5], radius=4, fill=(15, 23, 42, 255))

    # Wide Panicked Eyes
    draw.ellipse([thx + 3, thy - 4, thx + 10, thy + 3], fill=(255, 255, 255, 255))
    draw.ellipse([thx + 5, thy - 3, thx + 9, thy + 2], fill=(15, 23, 42, 255))
    draw.ellipse([thx - 10, thy - 4, thx - 3, thy + 3], fill=(255, 255, 255, 255))
    draw.ellipse([thx - 8, thy - 3, thx - 4, thy + 2], fill=(15, 23, 42, 255))

    # Beanie Cap & Red Pom-Pom
    draw.chord([thx - 20, thy - 25, thx + 20, thy - 2], 180, 360, fill=(15, 23, 42, 255))
    draw.rectangle([thx - 20, thy - 6, thx + 20, thy - 1], fill=(30, 41, 59, 255))
    draw.ellipse([thx - 4, thy - 28, thx + 4, thy - 20], fill=(239, 68, 68, 255))

    # Surprised Mouth
    draw.ellipse([thx - 2, thy + 8, thx + 4, thy + 15], fill=(153, 27, 27, 255))

    frames.append(img.convert("RGB"))

# Save as animated GIF
out_path = r"d:\projects\Digital-Fugitive\assets\images\under_construction.gif"
frames[0].save(
    out_path,
    save_all=True,
    append_images=frames[1:],
    duration=DURATION,
    loop=0
)

print(f"SUCCESS: Generated animated GIF at {out_path} with {NUM_FRAMES} frames!")
