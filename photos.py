from pyscript import display

images = [
    ("images/activity1.jpg", "Class Presentation Day"),
    ("images/activity2.jpg", "ICT Coding Session"),
    ("images/activity3.jpg", "Group Project Work")
]

for img, caption in images:
    display(f"<img src='{img}' width='300'><br><p>{caption}</p><br>", target="gallery")