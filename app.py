from shiny import App, render, ui
import numpy as np
import matplotlib.pyplot as plt

app_ui = ui.page_fluid(
    ui.input_slider("num_bins", "Number of Bins for Histogram", min=1, max=50, value=10),
    ui.output_plot("hist_plot"),
    ui.output_plot("scatter_plot"),
)

def server(input, output, session):
    @output
    @render.plot
    def hist_plot():
        np.random.seed(0)
        data = np.random.randn(1000)
        fig, ax = plt.subplots()
        ax.hist(data, bins=input.num_bins(), color='skyblue')
        plt.title("Histogram")
        return fig

    @output
    @render.plot
    def scatter_plot():
        np.random.seed(1)  # Ensure the scatter plot data is consistent
        x = np.random.rand(50)
        y = np.random.rand(50)
        fig, ax = plt.subplots()
        ax.scatter(x, y, color='red')
        plt.title("Scatter Plot")
        return fig

app = App(app_ui, server)

