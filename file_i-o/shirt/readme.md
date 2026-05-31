### What the code does
Reads an input image, resizes it, overlays `shirt.png` on top, and saves the final edited image.

### How to test
- `python shirt.py input.jpg output.jpg`
- test invalid file names
- test mismatched extensions (`.jpg` → `.png`)

### Key idea
Use Pillow:
- `Image.open()` to open images
- `ImageOps.fit()` to resize
- `paste()` to overlay
- `save()` to write final image