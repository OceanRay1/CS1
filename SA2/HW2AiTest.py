# Author: Roshan Shivnani
# Date: 09/18/2026
# Purpose: Testing A.I. "DartmouthChat" if it can correctly use cs1lib to draw an image 

import SA2.cs1lib as cs1lib                              

WIDTH, HEIGHT = 800, 600                    

# --------------------------------------------------------------
# Helper – convert 0‑255 RGB values to the 0‑1 floats that this
# version of cs1lib expects.
# --------------------------------------------------------------
def rgb(r, g, b):
    """
    Convert three integers in the range 0‑255 to a tuple of three floats
    in the range 0‑1, which is what cs1lib.set_fill_color expects.
    Example:  rgb(255, 0, 0)  ->  (1.0, 0.0, 0.0)
    """
    return (r / 255.0, g / 255.0, b / 255.0)


# --------------------------------------------------------------
# Drawing helpers – only the API that is guaranteed to exist
# --------------------------------------------------------------
def draw_sky():
    """Light‑blue sky that fills the top half of the window."""
    cs1lib.set_fill_color(*rgb(135, 206, 235))   # sky‑blue
    cs1lib.draw_rectangle(0, 0, WIDTH, HEIGHT / 2)


def draw_grass():
    """Green lawn that occupies the bottom half."""
    cs1lib.set_fill_color(*rgb(34, 139, 34))     # forest‑green
    cs1lib.draw_rectangle(0, HEIGHT / 2,
                          WIDTH, HEIGHT / 2)


def draw_sun():
    """Bright yellow sun in the upper‑right corner."""
    cx, cy, r = WIDTH - 100, 100, 70
    cs1lib.set_fill_color(*rgb(255, 223, 0))     # sunshine yellow
    cs1lib.draw_circle(cx, cy, r)


def draw_cloud(x, y, w, h):
    """A fluffy cloud made from three overlapping ellipses."""
    cs1lib.set_fill_color(*rgb(255, 255, 255))   # pure white
    cs1lib.draw_ellipse(x, y, w, h)
    cs1lib.draw_ellipse(x - w * 0.4, y + h * 0.2, w, h)
    cs1lib.draw_ellipse(x + w * 0.4, y + h * 0.2, w, h)


def draw_clouds():
    """Scatter a few clouds across the sky."""
    draw_cloud(200, 100, 40, 30)
    draw_cloud(300,  80, 50, 35)
    draw_cloud(550, 120, 45, 32)
    draw_cloud(630,  90, 38, 27)


def draw_pond():
    """A calm blue pond on the left side of the grass."""
    cx, cy, rw, rh = 150, HEIGHT * 0.65, 120, 80
    cs1lib.set_fill_color(*rgb(64, 164, 223))    # water‑blue
    cs1lib.draw_ellipse(cx, cy, rw, rh)


def draw_path():
    """Winding dirt path (two rectangles + a simple polygon)."""
    cs1lib.set_fill_color(*rgb(139, 69, 19))     # saddle‑brown (dirt)

    # straight segment
    cs1lib.draw_rectangle(WIDTH * 0.45, HEIGHT / 2,
                          WIDTH * 0.1, HEIGHT * 0.25)

    # curved segment – a four‑point polygon that suggests a turn
    cs1lib.draw_polygon([
        (WIDTH * 0.45, HEIGHT * 0.75),
        (WIDTH * 0.55, HEIGHT * 0.75),
        (WIDTH * 0.57, HEIGHT * 0.85),
        (WIDTH * 0.43, HEIGHT * 0.85)
    ])


def draw_tree(base_x, ground_y,
              trunk_w=30, trunk_h=120, crown_r=70):
    """Simple tree: brown trunk + three green circles for the crown."""
    # trunk
    cs1lib.set_fill_color(*rgb(101, 67, 33))    # dark brown
    cs1lib.draw_rectangle(base_x,
                          ground_y - trunk_h,
                          trunk_w,
                          trunk_h)

    # crown (three overlapping circles)
    cs1lib.set_fill_color(*rgb(34, 139, 34))    # forest‑green
    cx = base_x + trunk_w / 2
    cy = ground_y - trunk_h
    cs1lib.draw_circle(cx, cy, crown_r)
    offset = crown_r * 0.6
    cs1lib.draw_circle(cx - offset, cy + offset, crown_r)
    cs1lib.draw_circle(cx + offset, cy + offset, crown_r)


def draw_bench(base_x, ground_y,
               bench_w=120, bench_h=30):
    """Very simple wooden bench (seat, back‑rest, four legs)."""
    # seat
    cs1lib.set_fill_color(*rgb(160, 82, 45))    # sienna / wood tone
    cs1lib.draw_rectangle(base_x,
                          ground_y - bench_h,
                          bench_w,
                          bench_h)

    # backrest
    cs1lib.draw_rectangle(base_x,
                          ground_y - bench_h - 30,
                          bench_w,
                          10)

    # legs – four tiny brown rectangles
    cs1lib.set_fill_color(*rgb(101, 67, 33))    # same brown as trunk
    leg_w, leg_h = 6, 30
    # front‑left
    cs1lib.draw_rectangle(base_x + 5,
                          ground_y,
                          leg_w,
                          leg_h)
    # front‑right
    cs1lib.draw_rectangle(base_x + bench_w - 5 - leg_w,
                          ground_y,
                          leg_w,
                          leg_h)
    # rear‑left
    cs1lib.draw_rectangle(base_x + 5,
                          ground_y - bench_h,
                          leg_w,
                          leg_h)
    # rear‑right
    cs1lib.draw_rectangle(base_x + bench_w - 5 - leg_w,
                          ground_y - bench_h,
                          leg_w,
                          leg_h)


# --------------------------------------------------------------
# Main drawing routine – called once per frame by cs1lib
# --------------------------------------------------------------
def main():
    """Draw everything, back‑to‑front."""
    # ----- background ------------------------------------------------
    draw_sky()
    draw_grass()

    # ----- mid‑ground (objects that should appear behind the bench/trees)
    # -----------------------------------------------------------------
    draw_sun()
    draw_clouds()
    draw_pond()
    draw_path()

    # ----- foreground (draw last so they sit on top) ----------------
    ground_y = HEIGHT / 2               # y‑coordinate of the grass line
    draw_tree(100, ground_y)            # left tree
    draw_tree(600, ground_y)            # right tree
    draw_bench(340, ground_y + 10)      # bench on the grass


# --------------------------------------------------------------
# Run the program
# --------------------------------------------------------------
if __name__ == "__main__":
    # start_graphics creates the window and repeatedly calls `main`
    cs1lib.start_graphics(main,
                          width=WIDTH,
                          height=HEIGHT,
                          title="Simple Park Scene (0‑1 colours)")