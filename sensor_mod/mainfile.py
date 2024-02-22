"""
@author: Pola Polańska, modified by Dominik Cedro
@resources:
    tkinter docs: https://docs.python.org/3/library/tkinter.html

"""
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from hr_heartrate_monitor import HeartRateMonitor
from calculate_age_hr import calculate_opinion
import time
import argparse

parser = argparse.ArgumentParser(description="Read and print data from MAX30102")
parser.add_argument("-r", "--raw", action="store_true",
                    help="print raw data instead of calculation result")
parser.add_argument("-t", "--time", type=int, default=30,
                    help="duration in seconds to read from sensor, default 30")
args = parser.parse_args()

# hrm = HeartRateMonitor(print_raw=args.raw, print_result=(not args.raw))

def start_sensor():
    """ start sensor, disable start button and instructions label, wait 15 sec and stop sensor

    :return:
    """
    # create instance of HeartRateMonitor class and start sensor
    # hrm.start_sensor()
    start_button.config(state='disabled')
    # remove instructions label when sensor is running
    instructions_label.grid_remove()
    time.sleep(args.time)
    stop_sensor()

def stop_sensor():
    """
    Stop sensor, display result and enable start button
    """
    global fig
    global result
    # result, fig = hrm.stop_sensor()
    pulse_label.config(text=f"Your pulse is {result} bpm")

def show_graph():
    """
    Display graph in tkinter window
    """
    global fig
    global result

    age = age_entry.get()
    age_label.config(text=f"Age: {age}")
    graph = FigureCanvasTkAgg(fig, master=frame)
    canvas = graph.get_tk_widget()
    canvas.grid(row=5, column=0)
    opinion="Your heart rate for your age is accurate"
    pulse_label.config(text=opinion)


# GUI window based on tkinter framework
# implements start button, instructions, age entry, graph and pulse label


window = tk.Tk()
window.title("Raspberry Pulse Sensor Program")

window.geometry("800x600")
background_label = tk.Label(window, bg='#F9F7F7')
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(window, bg='#DBE2EF')  # Frame color
frame.pack(expand=True)

welcome_label = tk.Label(frame, text=" Welcome to Raspberry Pulse Sensor Program ", bg='#DBE2EF', fg='#112D4E', font=('Arial', 22, 'bold'))
welcome_label.grid(row=0, column=0)

instructions_label = tk.Label(frame, text="Instructions:\n1. Insert finger in the pulsometer\n2. Enter your age\n3. Click 'start sensor' button\n4. Wait 15 sec\n5. Click 'show graph' to examine your pulse\n", bg='#DBE2EF', fg='#112D4E', font=('Arial', 16), anchor='w')
instructions_label.grid(row=1, column=0, padx=20)

age_entry = tk.Entry(frame, font=('Arial', 12), bg='#F9F7F7', fg='#DBE2EF')
age_entry.grid(row=3, column=0)

spacer_label2 = tk.Label(frame, text="", bg='#DBE2EF', font=('Arial', 16, 'bold'))
spacer_label2.grid(row=4, column=0)

button = tk.Button(frame, text="Show Graph", command=show_graph, font=('Arial', 16, 'bold'), bg='#3F72AF', fg='#DBE2EF')
button.grid(row=5, column=0)

spacer_label = tk.Label(frame, text="", bg='#DBE2EF', font=('Arial', 16, 'bold'))
spacer_label.grid(row=6, column=0)

pulse_label = tk.Label(frame, text="", bg='#DBE2EF', fg='white', font=('Arial', 16, 'bold'))
pulse_label.grid(row=7, column=0)

start_button = tk.Button(window, text="Start Sensor", command=start_sensor, font=('Arial', 16, 'bold'), bg='#3F72AF', fg='white', width=20, height=3)



window.mainloop()