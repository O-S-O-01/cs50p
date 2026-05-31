### What This Program Does ###

---

***This program asks for a file name and outputs its media (MIME) type based on the file extension.***

- gif → image/gif
- jpg, .jpeg → image/jpeg
- png → image/png
- pdf → application/pdf
- txt → text/plain
- zip → application/zip
- Anything else → application/octet-stream

The check is case-insensitive.

### How to Test the Program ###

Run the program with python extensions.py
***expected response and the file type give***

photo.jpg      → image/jpeg

image.PNG      → image/png

document.pdf   → application/pdf

notes.txt      → text/plain

archive.zip    → application/zip


***Default Case***
file           → application/octet-stream
unknown.xyz    → application/octet-stream

---
> The program checks how the filename ends and maps extensions to their correct media types.