from typing import Tuple

import copy
import pandas as pd
import plotly.express as px


def load_stallion(as_period=False) -> Tuple[pd.DataFrame, pd.DataFrame]:
    data = pd.read_csv("data/stallion_data.csv")
    data["date"] = pd.to_datetime(data["date"])
    if as_period:
        data["date"] = data["date"].dt.to_period("M")
    data = data.set_index(["agency", "sku", "date"])
    y = data[["volume"]]
    X = data.drop(columns="volume")
    return X, y


def plot_multivariate_time_series(df, color=None):
    plot_df = (
        df.stack()
        .reset_index()
        .rename({"level_0": df.index.name, "level_1": "variable", 0: "value"}, axis=1)
    )
    fig = px.line(
        plot_df, x=df.index.name, y="value", facet_row="variable", color=color
    )
    return fig


def add_changepoint_vlines(fig, changepoints):
    fig = copy.deepcopy(fig)
    for changepoint in changepoints:
        fig.add_vline(x=changepoint, line_dash="dash", line_color="red")
    return fig


def add_segmentation_vrects(
    fig, segments, segment_labels=None, colors=px.colors.qualitative.Alphabet
):
    fig = copy.deepcopy(fig)
    if segment_labels is None:
        segment_labels = pd.RangeIndex(len(segments))

    if len(segments) != len(segment_labels):
        raise ValueError("segments and segment_labels must be the same length")

    if segment_labels.dtype != int:
        raise ValueError("segment_labels must be of type int")

    for segment, segment_label in zip(segments.values, segment_labels.values):
        color = colors[segment_label % len(colors)]
        fig.add_vrect(
            x0=segment.left,
            x1=segment.right,
            fillcolor=color,
            opacity=0.2,
            line_width=0,
            layer="below",
        )
    return fig


def add_subset_segment_anomaly_vrects(fig, subset_anomalies):
    fig = copy.deepcopy(fig)
    n_vars = len(fig.data)
    for row in subset_anomalies.itertuples():
        columns = row.anomaly_columns
        for col in columns:
            fig.add_vrect(
                x0=row.anomaly_interval.left,
                x1=row.anomaly_interval.right,
                fillcolor="red",
                opacity=0.2,
                line_width=0,
                layer="below",
                row=n_vars
                - col,  # plotly rows are 1-indexed and we want to reverse the order
                col=1,
            )
    return fig


def to_time_intervals(intervals: pd.Series, times: pd.Index) -> pd.Series:
    time_intervals = pd.Series(
        [
            pd.Interval(
                times[interval.left],
                times[interval.right - 1] + pd.Timedelta("10min"),
                closed="left",
            )
            for interval in intervals
        ],
        name="interval",
    )
    return time_intervals


def plot_changepoint_illustration(df, cpts):
    cpt_fig = plot_multivariate_time_series(df)
    cpt_fig = add_changepoint_vlines(cpt_fig, cpts)
    for i, cpt in enumerate(cpts):
        cpt_fig.add_annotation(
            x=cpt,
            y=1.2,
            text=f"change point {i+1}",
            showarrow=False,
            yshift=-10,
            font=dict(size=16),
            xref="x",
            yref="paper",
        )
    cpt_fig.update_layout(showlegend=False, xaxis_title=None)
    return cpt_fig


def plot_segmentation_illustration(df, segments, segment_labels):
    cpts = segments.iloc[1:].array.left
    segment_fig = plot_changepoint_illustration(df, cpts)
    segment_fig = add_segmentation_vrects(segment_fig, segments, segment_labels)
    for i, segment in enumerate(segments):
        segment_fig.add_annotation(
            x=segment.mid,
            y=-0.22,
            text=f"segment {i}<br> label {segment_labels[i]}",
            showarrow=False,
            yshift=-10,
            font=dict(size=16),
            xref="x",
            yref="paper",
        )
    segment_fig.update_layout(showlegend=False, xaxis_title=None)
    return segment_fig


def plot_point_anomaly_illustration(df, point_anomalies):
    outlier_plot = plot_multivariate_time_series(df)
    outlier_plot.add_scatter(
        x=point_anomalies,
        y=df.iloc[point_anomalies, 0],
        mode="markers",
        marker=dict(symbol="x", size=10, color="red"),
        name="Point anomaly",
    )
    return outlier_plot


def plot_segment_anomaly_illustration(df, anomaly_segments):
    anomaly_plot = plot_multivariate_time_series(df)
    anomaly_plot = add_segmentation_vrects(
        anomaly_plot, anomaly_segments, colors=["red"]
    )
    for i, segment in enumerate(anomaly_segments):
        anomaly_plot.add_annotation(
            x=segment.mid,
            y=-0.13,
            text=f"Segment anomaly {i+1}",
            showarrow=False,
            yshift=-10,
            font=dict(size=16),
            xref="x",
            yref="paper",
        )
    anomaly_plot.update_layout(showlegend=False, xaxis_title=None)
    return anomaly_plot
