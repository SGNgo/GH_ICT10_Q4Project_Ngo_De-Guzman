from pyscript import display, document

class Classmate:
    def __init__(self, name, section, subject):
        self.name = name
        self.section = section
        self.fav_subject = subject

    def show(self):
        display(f"My name is {self.name} from {self.section}. My favorite subject is {self.fav_subject}.", target="output")

s1 = Classmate("Vito De Guzman", "10-Sapphire", "PE")
s2 = Classmate("Tax Rivera", "10-Sapphire", "Social Studies")
s3 = Classmate("Ishan Shrestha", "10-Sapphire", "Social Studies")
s4 = Classmate("Manuel Mergal", "10-Sapphire", "Math")
s5 = Classmate("Alonso Hizon", "10-Sapphire", "English")
s6 = Classmate("Anakin Batac", "10-Sapphire", "ICT")
s7 = Classmate("Seth Ngo", "10-Sapphire", "Filipino")

classmates = [s1, s2, s3, s4, s5, s6, s7]

def show_list(event):
    document.getElementById("output").innerHTML = ""
    for c in classmates:
        c.show()

def add_classmate(event):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    new_s = Classmate(name, section, subject)
    classmates.append(new_s)
    new_s.show()