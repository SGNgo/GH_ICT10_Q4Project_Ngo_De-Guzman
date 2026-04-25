from pyscript import display, HTML

images = [
    ("Intrams.jpg", "Intramurals Upper Division"),
    ("Xmas.jpg", "Yearly Christmas Party"),
    ("Last Day.jpg", "Goodbyes"),
    ("Minimart.jpg", "Minimart Fair")
]

for img, caption in images:
    display(HTML(f"""
        <div class='photo'>
        <img src='{img}'>
        <p>{caption}</p>
        </div>
    """), target="gallery")