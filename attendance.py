from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt
import logging

logging.getLogger('matplotlib').setLevel(logging.ERROR)

absences = np.array([0, 0, 0, 0, 0])
days = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])

def generate_graph(e):
    day = int(document.getElementById("day").value)
    value = int(document.getElementById("absences").value or 0)

    absences[day] = value
    document.getElementById("absences").value = ""

    plt.figure()
    plt.bar(days, absences)
    plt.title("10-Sapphire Weekly Absences")

    display(plt, target="output")
    display(f"Total Absences: {np.sum(absences)}", target="output")

def reset_graph(e):
    global absences
    absences = np.array([0, 0, 0, 0, 0])

    document.getElementById("absences").value = ""
    document.getElementById("day").value = "0"

    display("", target="output", append=False)