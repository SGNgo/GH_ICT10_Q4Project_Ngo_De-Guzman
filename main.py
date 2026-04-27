from pyscript import display, document  # allows us to show output and access HTML inputs

# class definition
class Classmate:
    def __init__(self, name, section, subject):
        self.name = name
        self.section = section
        self.fav_subject = subject

    def show(self):
        # display classmate info on the webpage
        display(f"My name is {self.name} from {self.section}. My favorite subject is {self.fav_subject}.", target="output")


# classmates (objects)
s1 = Classmate("Vito De Guzman", "10-Sapphire", "PE")
s2 = Classmate("Tax Rivera", "10-Sapphire", "Social Studies")
s3 = Classmate("Ishan Shrestha", "10-Sapphire", "Social Studies")
s4 = Classmate("Manuel Mergal", "10-Sapphire", "Math")
s5 = Classmate("Alonso Hizon", "10-Sapphire", "English")
s6 = Classmate("Anakin Batac", "10-Sapphire", "ICT")
s7 = Classmate("Seth Ngo", "10-Sapphire", "Filipino")

# stores classmates in a list
classmates = [s1, s2, s3, s4, s5, s6, s7]


def show_list(event):

    document.getElementById("output").innerHTML = ""

    # display classmates
    s1.show()
    s2.show()
    s3.show()
    s4.show()
    s5.show()
    s6.show()
    s7.show()


def add_classmate(event):
    # get input values
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    # create new classmate (object)
    new_s = Classmate(name, section, subject)

    # display new classmate
    new_s.show()

    # add to the list
    classmates.append(new_s)