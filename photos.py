from pyscript import display, HTML  # HTML allows formatted display

# images and captions
images = [
    ("Intrams.JPG", "Intramurals Upper Division"),
    ("Xmas.JPG", "Yearly Christmas Party"),
    ("Last Day.JPG", "Goodbyes"),
    ("Minimart.JPG", "Minimart Fair")
]

# loop through each image
for img, caption in images:
    display(HTML(f"""
        <div class='photo'>
        <img src='{img}'>
        <p>{caption}</p>
        </div>
"""), target="gallery")
