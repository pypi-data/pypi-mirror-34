#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
import timeit
import itertools
import math
import subprocess
import json
import warnings
import enum
import plotly
from . import utils
from . import ipython_utils
from . import plotly_utils
from . import _validators


try:
    if utils.is_interactive():
        from tqdm import tqdm_notebook as tqdm
    else:
        from tqdm import tqdm

except ImportError:
    tqdm = lambda x: x


def _autorange(timer, is_ns_timer=False):
    '''Return the number of loops so that total time >= 0.2.'''
    THRESHOLD = int(0.2 * 1.0e+9) if is_ns_timer else 0.2
    i = 1
    while True:
        for j in 1, 2, 5:
            number = i * j
            time_taken = timer.timeit(number=number)
            if time_taken >= THRESHOLD:
                return number
        i *= 10


def _bench(
        datasets,
        dataset_sizes,
        kernels,
        repeat=0,
        number=0,
        disable_tqdm=False
):
    try:
        timer = time.perf_counter_ns  # python >= 3.7
        is_ns_timer = True
    except AttributeError:
        timer = time.perf_counter
        is_ns_timer = False

    if repeat == 0:
        default_repeat = 7 if timeit.default_repeat < 7 else timeit.default_repeat
        repeat = default_repeat

    shape = (len(kernels), len(datasets))
    res = utils.create_empty_array_of_shape(shape)
    for i, j in itertools.product(range(shape[0]), range(shape[1])):
        res[i][j] = []

    for i, dataset in enumerate(tqdm(datasets, disable=disable_tqdm)):
        dataset_stmt = dataset.stmt
        for j, dataset_size in enumerate(tqdm(dataset_sizes, disable=disable_tqdm)):
            data = dataset_stmt(dataset_size)
            for k, kernel in enumerate(kernels):
                kernel_stmt = kernel.stmt
                t = timeit.Timer(stmt=lambda: kernel_stmt(data), timer=timer)
                loops = number if number > 0 else _autorange(timer=t, is_ns_timer=is_ns_timer)
                all_runs = t.repeat(repeat=repeat, number=loops)
                if is_ns_timer:
                    all_runs = [value * 1.0e-9 for value in all_runs]

                res[k][i].append(
                    ipython_utils.TimeitResult(
                        loops=loops,
                        repeat=repeat,
                        all_runs=all_runs,
                        precision=4
                    )
                )

    return res


class NotReadyError(Exception):
    '''Raised when a resource is not prepared.'''
    pass


class Dataset(object):
    '''Dataset class.

    Args:
        stmt (function):
        title (str):
    '''
    def __init__(self, *, stmt, title=None):
        self._stmt = stmt
        self._title = '' if title is None else title

    @property
    def stmt(self):
        return self._stmt

    @property
    def title(self):
        return self._title


class Kernel(object):
    '''Kernel class.

    Args:
        stmt (function):
        label (str):
    '''
    def __init__(self, *, stmt, label=None):
        self._stmt = stmt
        self._label = '' if label is None else label

    @property
    def stmt(self):
        return self._stmt

    @property
    def label(self):
        return self._label


class LayoutSize(object):
    '''LayoutSize class.

    Args:
        width (int):
        height (int):
        label (str):
    '''

    def __init__(self, *, width=None, height=None, label=None):
        if (width is None) or (width > 0):
            self._width = width
        else:
            raise ValueError('`width` must be greater than 0.')

        if (height is None) or (height > 0):
            self._height = height
        else:
            raise ValueError('`height` must be greater than 0.')

        self._label = '' if label is None else label

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def label(self):
        return self._label


class MeasurementMode(enum.Enum):
    '''Measurement mode.'''
    STANDARD = 1  #: Perform minimum value based measurements.
    STATISTICS = 2  #: Perform statistics based measurements.


class Benchmark(object):
    '''This class measures execution speed of given code snippets.

    Args:
        datasets (list(:class:`Dataset`)):
        dataset_sizes (list(int)):
        kernels (list(:class:`Kernel`)):
        repeat (int): Number of times the measurement is repeated.
            When zero, this value is determined automatically.
        number (int): Number of loops to execute per measurement.
            When zero, this value is determined automatically.
        measurement_mode (:class:`MeasurementMode`):
        xlabel (str): The text for a x-axis label.
        title (str): The title for a figure.
        layout_sizes (list(:class:`LayoutSize`)):
    '''
    def __init__(
            self, *,
            datasets,
            dataset_sizes,
            kernels,
            repeat=0,
            number=0,
            measurement_mode=MeasurementMode.STANDARD,
            xlabel=None,
            title=None,
            layout_sizes=None
    ):
        self._datasets = datasets

        self._dataset_sizes = dataset_sizes
        _validators.validate_dataset_sizes(self._dataset_sizes)

        self._kernels = kernels

        if repeat >= 0:
            self._repeat = repeat
        else:
            raise ValueError('`repeat` must be greater than or equal to 0.')

        if number >= 0:
            self._number = number
        else:
            raise ValueError('`number` must be greater than or equal to 0.')

        self._xlabel = '' if xlabel is None else xlabel
        self._title = '' if title is None else title

        self._layout_sizes = None
        if layout_sizes is not None:
            self._layout_sizes = [LayoutSize(label='auto')] + layout_sizes

        self._measurement_mode = measurement_mode
        self._figure = None

    def run(self, *, disable_tqdm=False):
        results = _bench(
            datasets=self._datasets,
            dataset_sizes=self._dataset_sizes,
            kernels=self._kernels,
            repeat=self._repeat,
            number=self._number,
            disable_tqdm=disable_tqdm
        )
        self._figure = self._create_figure(benchmark_results=results)

    @classmethod
    def _default_colors(cls):
        return plotly.colors.DEFAULT_PLOTLY_COLORS

    @classmethod
    def _color(cls, *, index):
        colors = cls._default_colors()
        return colors[index % len(colors)]

    @staticmethod
    def _axis_range(sequence, use_log_scale=False):
        ar = [min(sequence), max(sequence)]
        if use_log_scale:
            ar[0] = math.log10(ar[0])
            ar[1] = math.log10(ar[1])
        return ar

    @staticmethod
    def _label_rgba(colors):
        return 'rgba({}, {}, {}, {})'.format(colors[0], colors[1], colors[2], colors[3])

    @staticmethod
    def _calc_filled_line(x, y, delta):
        x_rev = x[::-1]
        y_upper = [a + b for a, b in zip(y, delta)]
        y_lower = [a - b for a, b in zip(y, delta)]
        y_lower = y_lower[::-1]
        return x+x_rev, y_upper+y_lower

    @staticmethod
    def _create_update_menus(
            layout,
            layout_sizes=None,
            has_multiple_subplots=False
    ):
        updatemenus = []
        pos_x = 0.0

        if layout_sizes is not None:
            updatemenus.append(
                dict(
                    active=0,
                    buttons=plotly_utils.make_layout_size_buttons(layout_sizes=layout_sizes),
                    direction='down',
                    showactive=True,
                    x=pos_x,
                    xanchor='left',
                    y=1.2,
                    yanchor='top'
                )
            )
            pos_x += 0.1

        updatemenus.append(
            dict(
                active=3,
                buttons=plotly_utils.make_scale_buttons(layout=layout),
                direction='down',
                showactive=True,
                x=pos_x,
                xanchor='left',
                y=1.2,
                yanchor='top'
            )
        )
        pos_x += 0.1

        if has_multiple_subplots:
            updatemenus.append(
                dict(
                    active=0,
                    buttons=plotly_utils.make_subplot_buttons(layout=layout),
                    direction='down',
                    showactive=True,
                    x=pos_x,
                    xanchor='left',
                    y=1.2,
                    yanchor='top'
                )
            )

        return updatemenus

    def _add_standard_traces(self, *, figure, benchmark_results):
        '''Add standard traces.'''
        ndatasets = len(self._datasets)
        for i, result in enumerate(benchmark_results):
            legendgroup = str(i)
            name = self._kernels[i].label
            color = self._color(index=i)
            for j, item in enumerate(result):
                index = j + 1
                x = self._dataset_sizes
                y = [tres.best for tres in item]

                if ndatasets > 1:
                    title = self._datasets[j].title
                    suffix = ' - ' + title if title else ''
                else:
                    suffix = ''

                trace = plotly.graph_objs.Scatter(
                    x=x,
                    y=y,
                    name=name + suffix,
                    text=[tres.standard_report() for tres in item],
                    hoverinfo='x+text+name',
                    showlegend=True,
                    legendgroup=legendgroup,
                    line=dict(color=color),
                )
                figure.add_trace(trace, row=index, col=1)

    def _add_statistical_traces(self, *, figure, benchmark_results):
        '''Add statistical traces.'''
        ndatasets = len(self._datasets)
        for i, result in enumerate(benchmark_results):
            legendgroup = str(i)
            name = self._kernels[i].label
            color = self._color(index=i)
            error_color = self._label_rgba(colors=plotly.colors.unlabel_rgb(color) + (0.5,))
            for j, item in enumerate(result):
                index = j + 1
                x = self._dataset_sizes
                y = [tres.average for tres in item]

                if ndatasets > 1:
                    title = self._datasets[j].title
                    suffix = ' - ' + title if title else ''
                else:
                    suffix = ''

                trace = plotly.graph_objs.Scatter(
                    x=x,
                    y=y,
                    name=name + suffix,
                    text=[tres.statistical_report() for tres in item],
                    hoverinfo='x+text+name',
                    showlegend=True,
                    legendgroup=legendgroup,
                    line=dict(color=color),
                    error_y=dict(
                        type='data',
                        array=[tres.stdev for tres in item],
                        visible=True,
                        color=error_color
                    )
                )
                figure.add_trace(trace, row=index, col=1)

    def _add_average_traces(self, *, figure, benchmark_results):
        '''Add average_traces.'''
        ndatasets = len(self._datasets)
        for i, result in enumerate(benchmark_results):
            legendgroup = str(i)
            name = self._kernels[i].label
            color = self._color(index=i)
            for j, item in enumerate(result):
                index = j + 1
                x = self._dataset_sizes
                y = [tres.average for tres in item]

                if ndatasets > 1:
                    title = self._datasets[j].title
                    suffix = ' - ' + title if title else ''
                else:
                    suffix = ''

                trace = plotly.graph_objs.Scatter(
                    x=x,
                    y=y,
                    name=name + suffix,
                    text=[tres.__str__() for tres in item],
                    hoverinfo='x+text+name',
                    showlegend=True,
                    legendgroup=legendgroup,
                    line=dict(color=color),
                )
                figure.add_trace(trace, row=index, col=1)

    def _add_stdev_traces(self, *, figure, benchmark_results):
        '''Add stdev traces.'''
        for i, result in enumerate(benchmark_results):
            legendgroup = str(i)
            color = self._color(index=i)
            for j, item in enumerate(result):
                index = j + 1
                x = self._dataset_sizes
                y = [tres.average for tres in item]
                fillcolor = self._label_rgba(colors=plotly.colors.unlabel_rgb(color) + (0.1,))
                fx, fy = self._calc_filled_line(x=x, y=y, delta=[tres.stdev for tres in item])
                trace = plotly.graph_objs.Scatter(
                    x=fx,
                    y=fy,
                    hoverinfo='x',
                    showlegend=False,
                    legendgroup=legendgroup,
                    line=dict(color='rgba(255,255,255,0)'),
                    fill='tozerox',
                    fillcolor=fillcolor
                )
                figure.add_trace(trace, row=index, col=1)

    def _create_figure(self, *, benchmark_results):
        '''Create a figure with multiple subplots.'''
        ndatasets = len(self._datasets)
        subplots = plotly.tools.make_subplots(
            rows=ndatasets,
            cols=1,
            shared_xaxes=True,
            subplot_titles=[dataset.title for dataset in self._datasets],
            print_grid=False
        )
        fig = plotly.graph_objs.FigureWidget(subplots)

        if self._measurement_mode == MeasurementMode.STANDARD:
            self._add_standard_traces(figure=fig, benchmark_results=benchmark_results)
        else:
            self._add_statistical_traces(figure=fig, benchmark_results=benchmark_results)
            #self._add_average_traces(figure=fig, benchmark_results=benchmark_results)
            #self._add_stdev_traces(figure=fig, benchmark_results=benchmark_results)

        # update the layout.
        layout = fig.layout

        layout.xaxis1.update(
            title=self._xlabel,
            type='log',
            autorange=True
        )
        for i, _ in enumerate(self._datasets):
            yaxis = 'yaxis' + str(i + 1)
            layout[yaxis].update(
                title='processing time',
                type='log',
                autorange=True
            )

        layout.title = self._title
        layout.updatemenus = self._create_update_menus(
            layout=layout,
            layout_sizes=self._layout_sizes,
            has_multiple_subplots=ndatasets > 1
        )

        return fig

    def plot(self, *, auto_open=True):
        '''Create a graph locally as an HTML document.

        Args:
            auto_open (bool): If True, open the saved file in a web browser after saving.
        '''
        if self._figure is None:
            raise NotReadyError('Benchmark results are not ready yet.')

        if utils.is_interactive():
            plotly.offline.init_notebook_mode()
            plotly.offline.iplot(self._figure, show_link=False)
        else:
            plotly.offline.plot(self._figure, show_link=False, auto_open=auto_open)

    def save_as_html(self, *, filepath='temp-plot.html'):
        '''Save as a html.

        Args:
            filepath (str): The local filepath to save the outputted chart to.
                If the filepath already exists, it will be overwritten.
        '''
        if self._figure is None:
            raise NotReadyError('Benchmark results are not ready yet.')

        plotly.offline.plot(self._figure, show_link=False, auto_open=False, filename=filepath)

    def save_as_png(self, *, filepath='plot_image.png', width=1280, height=960):
        '''Save as a png.

        Args:
            filepath (str): The local filepath to save the image to.
            width (int): Specifies the width of the image in `px`.
            height (int): Specifies the height of the image in `px`.

        Returns:
            bool: True if successful, false otherwise.
        '''
        if not utils.cmd_exists('orca'):
            warnings.warn('`orca` is not installed, this function can not be used.')
            return False

        dirpath, filename = os.path.split(filepath)
        if not dirpath:
            dirpath = '.'

        if self._figure is None:
            raise NotReadyError('Benchmark results are not ready yet.')

        dumps = json.dumps(self._figure, cls=plotly.utils.PlotlyJSONEncoder)
        try:
            subprocess.check_call([
                'orca',
                'graph', dumps,
                '-d', dirpath,
                '-o', filename,
                '--width', str(width),
                '--height', str(height)
            ])
            return True
        except subprocess.CalledProcessError:
            return False
