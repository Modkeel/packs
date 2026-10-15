"""Cut the KEEL letters out of their lime and magenta shots (a pixel that is the same on both walls
is letter) and lay them on backgrounds made from the pack's own gallery shots.

    python icon_cut.py <shots dir> <out dir>
"""
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageEnhance, ImageFilter

HERE = Path(__file__).parent
GALLERY = HERE.parent / "gallery"
SIZE = 512


def cutout(shots: Path, layout: str) -> Image.Image:
    lime = Image.open(shots / f"icon-keel-{layout}-lime.png").convert("RGB")
    magenta = Image.open(shots / f"icon-keel-{layout}-magenta.png").convert("RGB")
    diff = ImageChops.difference(lime, magenta).convert("L")
    alpha = diff.point(lambda d: 255 if d < 12 else 0)
    # the letters sit in the middle; a corner of sky past the wall is the same on both shots
    w, h = alpha.size
    middle = Image.new("L", alpha.size, 0)
    middle.paste(255, (w // 4, h // 8, w * 3 // 4, h * 7 // 8))
    alpha = ImageChops.multiply(alpha, middle)
    r, g, b = lime.split()
    sky = Image.eval(ImageChops.subtract(b, r), lambda d: 0 if d > 60 else 255)
    alpha = ImageChops.multiply(alpha, sky)
    letters = lime.convert("RGBA")
    letters.putalpha(alpha)
    return letters.crop(alpha.getbbox())


def background(name: str) -> Image.Image:
    if name == "night":
        bg = Image.new("RGB", (SIZE, SIZE))
        px = bg.load()
        for y in range(SIZE):
            for x in range(SIZE):
                t = y / SIZE
                px[x, y] = (int(14 + 20 * t), int(22 + 34 * t), int(38 + 30 * t))
        return bg
    shot = Image.open(GALLERY / f"{name}.jpg").convert("RGB")
    side = min(shot.size)
    left = (shot.width - side) // 2
    bg = shot.crop((left, 0, left + side, side)).resize((SIZE, SIZE), Image.LANCZOS)
    bg = bg.filter(ImageFilter.GaussianBlur(6))
    return ImageEnhance.Brightness(bg).enhance(0.55)


def compose(letters: Image.Image, bg: Image.Image, fill: float) -> Image.Image:
    scale = SIZE * fill / max(letters.size)
    lt = letters.resize((round(letters.width * scale), round(letters.height * scale)),
                        Image.NEAREST)
    out = bg.convert("RGBA")
    shadow = Image.new("RGBA", lt.size, (0, 0, 0, 170))
    shadow.putalpha(ImageChops.multiply(lt.getchannel("A"), shadow.getchannel("A")))
    x, y = (SIZE - lt.width) // 2, (SIZE - lt.height) // 2
    out.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(4)), (x + 6, y + 8))
    out.alpha_composite(lt, (x, y))
    return out.convert("RGB")


if __name__ == "__main__":
    shots, dest = Path(sys.argv[1]), Path(sys.argv[2])
    dest.mkdir(parents=True, exist_ok=True)
    made = []
    for layout, fill in (("row", 0.9), ("grid", 0.82)):
        letters = cutout(shots, layout)
        letters.save(dest / f"letters-{layout}.png")
        for bg in ("night", "mineshaft-oak-in", "stronghold-in"):
            icon = compose(letters, background(bg), fill)
            icon.save(dest / f"icon-{layout}-{bg}.png")
            made.append(icon)
    # how they look in Modrinth's search list (~96 px)
    sheet = Image.new("RGB", (len(made) * 104 + 8, 112), (33, 34, 38))
    for i, icon in enumerate(made):
        sheet.paste(icon.resize((96, 96), Image.LANCZOS), (8 + i * 104, 8))
    sheet.save(dest / "sheet-96.png")
    print(f"{len(made)} icons in {dest}")
