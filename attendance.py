from pyscript import display, document
import numpy as np                  # for array and math operations
import matplotlib.pyplot as plt    # for graph
import logging

logging.getLogger('matplotlib').setLevel(logging.ERROR)

# absences for each day
absences = np.array([0, 0, 0, 0, 0])

# days of the week
days = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])


def generate_graph(e):
    # get selected day
    day = int(document.getElementById("day").value)

    # get absence input
    value = int(document.getElementById("absences").value or 0)

    # store value
    absences[day] = value

    document.getElementById("absences").value = ""

    # create graph
    plt.figure()
    plt.bar(days, absences)
    plt.title("10-Sapphire Weekly Absences")

    # display graph
    display(plt, target="output")

    # display total absences
    display(f"Total Absences: {np.sum(absences)}", target="output")


def reset_graph(e):
    global absences  # allow modification of global variable

    # resets all values to 0
    absences = np.array([0, 0, 0, 0, 0])

    # resets inputs
    document.getElementById("absences").value = ""
    document.getElementById("day").value = "0"

    # clears graph/output
    display("", target="output", append=False)