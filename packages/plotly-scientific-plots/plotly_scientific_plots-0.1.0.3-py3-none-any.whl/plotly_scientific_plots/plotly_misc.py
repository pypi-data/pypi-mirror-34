### Plotly misc

def plotOut(fig, plot):
    """ Standard code snippet to decide whether to return plotly fig object or plot """
    if plot:
        plotfunc = pyo.iplot if in_notebook() else pyo.plot
        plotfunc(fig)
        return None
    else:
        return fig

def in_notebook():
    """
    Returns ``True`` if the module is running in IPython kernel,
    ``False`` if in IPython shell or other Python shell.
    """
    try:
        return get_ipython().__class__.__name__ == 'ZMQInteractiveShell'
    except:
        return False

