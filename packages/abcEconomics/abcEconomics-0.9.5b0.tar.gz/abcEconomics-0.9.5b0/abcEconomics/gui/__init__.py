""" abcEconomics can be started with a gui or provide visual data output """
from .webtext import abcEconomicsdescription
from .plot_with_plotly import ppl
from .gui_with_dash import dashgui


def gui(parameter_mask, names=None, header=None, story=None,
        title="Agent-Based Computational Economics",
        texts=None, pages=None, histograms=None,
        serve=False, runtime='browser-X', truncate_rounds=0,
        hostname='0.0.0.0', port=80, pypy=None):
    """ gui is a decorator that can be used to add a graphical user interface
    to your simulation.

    Args:

        parameter_mask:
            a dictionary with the parameter name as key and an example value
            as value. Instead of the example value you can also put a tuple:
            (min, default, max)

            parameters can be:
                - float:
                    {'exponent': (0.0, 0.5, 1.1)}

                - int:
                    {'num_firms': (0, 100, 100000)}

                - dict or list, which should be strings of a dict or a
                  list (see example):
                    {'list_to_edit': "['brd', 'mlk', 'add']"}

                - a list of options:
                    {'several_options': ['opt_1', 'opt_2', 'opt_3']}

                - a string:
                    {'name': '2x2'}

        names (optional):
            a dictionary with the parameter name as key and an alternative
            text to be displayed instead.

        title:
            a string with the name of the simulation.

        header:
            html string for a bar on the top

        story:
            a dictionary with text to be displayed alongeside the graphs.
            Key must be the graphs title, value can be text or html.

        pages:
            A dictinoary with title as key and links to external websites
            as values, which are displayed on the right hand side.

        truncate_rounds:
            Does not display the initial x rounds, in the result graphs

        runtime:
            webbrowser to start the simulation in, can be 'xui' or python's
            webbrowser module's webrowser string.

        histograms:
            specifies in which round histograms are generated. If it is
            not specified rounds from the menu is used. Alternatively you can
            create 'histogram' parameter in parameter_mask.

        serve:
            If you run this on your local machine serve must be False.
            If used as a web server must be True

        hostname:
            Hostname if serve is active, defaults to '0.0.0.0'

        port:
            Port if serve is active, defaults to 80

        pypy:
            Name of the pypy interpreter to run abcEconomics super fast. e.G. 'pypy' or
            'pypy3'. The mainfile needs to be run with cpython e.G.:
            :code:`python3 start.py`

    Example::

        parameter_mask = {'name': 'name',
                          'random_seed': None,
                          'rounds': 40,
                          'num_firms': (0, 100, 100000),
                          'num_households': (0, 100, 100000),
                          'exponent': (0.0, 0.5, 1.1),
                          'several_options': ['opt_1', 'opt_2', 'opt_3']
                          'list_to_edit': "['brd', 'mlk', 'add']",
                          'dictionary_to_edit': "{'v1': 1, 'v2': 2}"}

        names = {'num_firms': 'Number of Firms'}

        @gui(parameter_mask, names,
             title="Agent-Based Computational Economics",
             serve=False)
        def main(simulation_parameters):
            parameter_list = eval(simulation_parameters['list_to_edit'])
            simulation = Simulation()
            firms = simulation.build_agents(Firm,
                simulation_parameters['num_firms'])
            households = simulation.build_agents(Household,
                simulation_parameters['num_households'])

            for r in range(simulation_parameters['rounds']):
                simulation.advance_round(r)
                firms.work()
                households.buy()

        if __name__ == '__main__':
            main(simulation_parameters)
    """
    parameter_mask = ({} if parameter_mask is None else parameter_mask)
    names = ({} if names is None else names)
    story = ({} if story is None else story)
    texts = ([abcEconomicsdescription] if texts is None else texts)
    pages = ([] if pages is None else pages)

    def inner(simulation):
        dashgui(simulation, parameter_mask, names, title, header, truncate_rounds, texts, pages)
        return lambda _: None
    return inner


def graph(path, parameter_mask=None, names=None):
    """ After the simulation simulation.graphs displays all logged data,
    this can not be use in conjuncture with @gui.

    Args:

        parameter_mask (optional):
            simulation parameters to display
        names (optional):
            a dictionary with the parameter name as key and an alternative
            text to be displayed instead.
    """
    names = ({} if names is None else names)

    ppl(path)
