import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

fig, ax = plt.subplots()

# Page options for the app
ui.page_opts(title = "Interactive Histogram App", fillable=True)

# Create a slidebar and input select for color changes
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of bins", 10, 100, 20,
                    step=5, animate=True)
    ui.input_select(  
        "select_color",  
        "Change the color of the histogram bins",  
        choices=["Green","Blue","Red"],
        selected=["Green"])
    ui.input_radio_buttons(  
        "select_bin_border",  
        "Change the color of the bin borders",  
        choices=["Black", "Grey", "White"],
        selected=["Black"])

# Render a histogram
@render.plot(alt="A histogram")
def histogram():
    count_of_points: int = 437
    np.random.seed(3)
    random_data_array = 100 + 15 * np.random.randn(count_of_points)
    ax.set_facecolor("Grey")
    plt.hist(random_data_array, input.selected_number_of_bins(),
             density=True, color = input.select_color(), ec=input.select_bin_border())
    plt.xlabel("X Axis Label")
    plt.ylabel("Y Axis Label")
