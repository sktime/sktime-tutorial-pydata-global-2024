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


def plot_multivariate_time_series(df):
    plot_df = (
        df.stack()
        .reset_index()
        .rename({"level_0": "index", "level_1": "variable", 0: "value"}, axis=1)
    )
    fig = px.line(plot_df, x="index", y="value", facet_row="variable")
    return fig


def add_changepoint_vlines(fig, changepoints):
    fig = copy.deepcopy(fig)
    for changepoint in changepoints:
        fig.add_vline(x=changepoint, line_dash="dash", line_color="red")
    return fig


def add_segmentation_vrects(fig, segments, colors=px.colors.qualitative.Alphabet):
    fig = copy.deepcopy(fig)
    for i, segment in enumerate(segments):
        color = colors[i % len(colors)]
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
