from __future__ import annotations
import pandas as pd


chem = pd.DataFrame({
    "action_id": [10, 10, 10, 10, 11, 11, 11],
    "Mn": [1.0, 1.1, 2.5, 2.5, 0.2, 0.3, 1.0],
    "timestamp": [
        "11:30",
        "11:35",
        "12:00",
        "12:05",
        "23:00",
        "23:30",
        "00:10"]})
addings = pd.DataFrame({
    "action_id": [10, 10, 11],
    "Mn": [500, 100, 400],
    "timestamp": [
        "11:45",
        "12:00",
        "23:55"]})

result = pd.DataFrame({
    "action_id": [10, 11],
    "Mn_add": [600, 400],
    "Mn_befor": [1.1, 0.3],
    "Mn_after": [2.5, 1.0],
    "timestamp": [
        "11:45",
        "23:55"]})


def solution(chem, addings):
    """
    Написати програму що поверне змерджений датафрейм відповідно до прикладу:
    "action_id" - ід процессу
    "Mn_add" - масса внесеного
    "Mn_befor" - хім аналіз до внесення
    "Mn_after" - хім аналіз відразу після внесення
    "timestamp" - початок внесення речовини

    hint:
    you can return str(dataframe) to be sure that data types are ok
    """
    return None
