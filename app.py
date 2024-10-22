from shiny import App, render, ui

# Import modules for plot rendering
import numpy as np
import matplotlib.pyplot as plt

#Import Palmer Penguins Data
from palmerpenguins import load_penguins

#Import seaborn package
import seaborn as sns


app_ui = ui.page_fluid(
    #Add a page Title
    ui.panel_title("My pyShiny App with Plot"),
    #Add string ID, string label, and integers to represent min, max and initial value
    ui.input_slider("selected_number_of_bins", "Number of bins", 0,100, 20), 
    ui.output_plot("plot"),
    ui.output_plot("MyPlot")
)

def server(input, output, session):
    @output
    @render.plot(alt = "A histogram")
    def plot():
        np.random.seed(19680801)
        x= 100 + 15 * np.random.randn(437)
        plt.hist(x, input.selected_number_of_bins(), density=True)
        plt.xlabel("Number of Bins")
        plt.ylabel("Frequency")
    @render.plot(alt="My Plot Chart")
    def MyPlot():
        penguins=load_penguins()
        g=sns.lmplot(
            x="flipper_length_mm",
            y="body_mass_g",
            hue="species",
            height=7,
            data=penguins,
            palette=["#D8D822","#DE4AE2","#19CDAF"]
        )
        g.set_xlabels("Flipper Length")
        g.set_ylabels("Body Mass")
        return g


app = App(app_ui,server,debug=True)
