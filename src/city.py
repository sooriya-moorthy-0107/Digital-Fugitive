from config import HEIGHT, WIDTH, HOT_COLOR, WARM_COLOR, COLD_COLOR, FROZEN_COLOR

def get_heat_color(cell, thieves):
    """Returns a Hot/Cold color based on distance to the nearest thief."""
    if not thieves:
        return (200, 200, 200) # Default grey if no thieves exist
        
    # Calculate Manhattan distance to the nearest thief
    min_dist = min(abs(cell[0] - t[0]) + abs(cell[1] - t[1]) for t in thieves)
    
    if min_dist <= 2:
        return HOT_COLOR
    elif min_dist <= 4:
        return WARM_COLOR
    elif min_dist <= 6:
        return COLD_COLOR
    else:
        return FROZEN_COLOR

class CityGrid:
    def __init__(self):
        self.thieves = set()

    def toggle_thief(self, cell):
        if cell in self.thieves:
            self.thieves.remove(cell)
        else:
            self.thieves.add(cell)

    def get_intel(self, cell):
        count = 0
        for i in range(cell[0]-1, cell[0]+2):
            for j in range(cell[1]-1, cell[1]+2):
                if (i, j) == cell: continue
                if 0 <= i < HEIGHT and 0 <= j < WIDTH:
                    if (i, j) in self.thieves:
                        count += 1
        return count
