from shiny import App, render, ui
import numpy as np
import matplotlib.pyplot as plt

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_slider("num_bins", "Number of Bins", min=1, max=50, value=10)
        ),
        ui.panel_main(
            ui.output_plot("hist_plot")
        )
    )
)

def server(input, output, session):
    @output
    @render.plot
    def hist_plot():
        np.random.seed(42)
        data = np.random.randn(1000)
        plt.hist(data, bins=input.num_bins(), color='blue', edgecolor='black')
        plt.title("Generated Histogram")
        plt.xlabel("Value")
        plt.ylabel("Frequency")

app = App(app_ui, server)
