"""Draw the Better Structures pack icon: a stone keep on a grassy hill, flying the Modkeel pennant.

    python packs/better-structures/icon.py      # -> packs/better-structures/icon.png (512x512)

Same pixel style and palette as the Companion icon (companion/listing/icon.py).
"""
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
N = 32

BG, BG_EDGE = (27, 38, 52), (17, 25, 35)
SKY_STAR = (60, 78, 100)
OUTLINE = (30, 30, 36)
STONE, STONE_DARK, STONE_LIGHT = (128, 128, 136), (92, 92, 102), (160, 160, 168)
MOSS = (86, 120, 60)
GRASS, GRASS_DARK, DIRT = (92, 150, 62), (70, 118, 48), (120, 84, 54)
DOOR, WINDOW = (58, 40, 26), (255, 184, 110)
MAST = (95, 66, 40)
FLAG, FLAG_DARK = (240, 138, 60), (178, 90, 34)

TOWER = (10, 21)        # keep walls, x range
TOP, BASE = 11, 25      # wall rows
MERLONS = (10, 11, 13, 14, 17, 18, 20, 21)  # battlement teeth (start, end pairs); mast in the gap


def draw() -> Image.Image:
    img = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    px = img.load()

    def inside(x: int, y: int) -> bool:
        r = 4
        cx = min(max(x, r), N - 1 - r)
        cy = min(max(y, r), N - 1 - r)
        return (x - cx) ** 2 + (y - cy) ** 2 <= r * r + 1

    for y in range(N):
        for x in range(N):
            if inside(x, y):
                edge = not all(inside(x + dx, y + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))
                px[x, y] = BG_EDGE if edge else BG
    for x, y in ((5, 6), (26, 10), (4, 13), (27, 4)):
        px[x, y] = SKY_STAR

    def put(x: int, y: int, c: tuple) -> None:
        if inside(x, y) and px[x, y] != BG_EDGE:
            px[x, y] = c

    # stone bricks: staggered joints like Minecraft stone bricks, light top edge per course
    a, b = TOWER
    for y in range(TOP, BASE + 1):
        course = (y - TOP) // 2
        for x in range(a, b + 1):
            joint = (x - a + (course % 2) * 2) % 4 == 0 and (y - TOP) % 2 == 0
            c = STONE_DARK if joint or (y - TOP) % 2 == 1 and x == b else STONE
            if (y - TOP) % 2 == 0 and not joint:
                c = STONE_LIGHT if x < (a + b) // 2 else STONE
            put(x, y, c)
    # battlements: teeth two rows tall on top of the wall
    for i in range(0, len(MERLONS) - 1, 2):
        for x in range(MERLONS[i], MERLONS[i + 1] + 1):
            for y in (TOP - 2, TOP - 1):
                put(x, y, STONE_LIGHT if y == TOP - 2 else STONE)
    # outline
    for y in range(TOP, BASE + 1):
        put(a - 1, y, OUTLINE)
        put(b + 1, y, OUTLINE)
    for x in range(a - 1, b + 2):
        if px[x, TOP - 2][:3] in (BG, SKY_STAR) and px[x, TOP - 1][:3] in (BG, SKY_STAR):
            put(x, TOP - 1, OUTLINE)
    for i in range(0, len(MERLONS) - 1, 2):
        for x in range(MERLONS[i], MERLONS[i + 1] + 1):
            put(x, TOP - 3, OUTLINE)
    # moss creeping up the left wall
    for x, y in ((10, 22), (10, 23), (11, 23), (10, 24), (11, 24), (12, 24), (13, 25)):
        put(x, y, MOSS)

    # arched door and two lit windows
    for y in range(20, BASE + 1):
        for x in (15, 16):
            put(x, y, DOOR)
    for x in (14, 17):
        for y in range(21, BASE + 1):
            put(x, y, DOOR)
    for x, y in ((14, 20), (17, 20)):
        put(x, y, OUTLINE)
    for x, y in ((12, 14), (12, 15), (19, 14), (19, 15)):
        put(x, y, WINDOW)

    # mast and the Modkeel pennant
    for y in range(2, TOP - 2):
        put(16, y, MAST)
    for y, (s, e) in zip(range(2, 7), [(17, 18), (17, 21), (17, 23), (17, 20), (17, 18)]):
        for x in range(s, e + 1):
            put(x, y, FLAG if y < 5 else FLAG_DARK)

    # grassy hill under the keep
    for y in range(BASE + 1, N):
        for x in range(N):
            put(x, y, GRASS if y == BASE + 1 else DIRT if y > BASE + 2 else GRASS_DARK)
    for x in range(3, 29):
        if x < a - 1 or x > b + 1:
            put(x, BASE, GRASS if x % 3 else GRASS_DARK)
    for x in (4, 7, 24, 27):
        put(x, BASE - 1, GRASS)
    return img


def main() -> None:
    draw().resize((512, 512), Image.NEAREST).save(HERE / "icon.png")
    print(HERE / "icon.png")


if __name__ == "__main__":
    main()
