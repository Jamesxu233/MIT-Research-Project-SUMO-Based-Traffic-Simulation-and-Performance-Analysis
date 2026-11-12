#!/usr/bin/env python3
"""Reshape the project's original wide-format Excel result files into tidy CSV."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "results" / "raw"
PROCESSED = ROOT / "results" / "processed"

MODELS = [
    ("Model 1", "RCC", "X-shaped central-cross roundabout"),
    ("Model 2", "RCCS_46s", "Central-cross roundabout with 46-second signal timing"),
    ("Model 3", "RCCS_26s", "Central-cross roundabout with 26-second signal timing"),
    ("Model 4", "RS", "Roundabout with signalized junctions"),
    ("Model 5", "BR", "Basic two-lane roundabout"),
    ("Model 6", "SI", "Signalized intersection"),
]
FIELDS = [
    "begin", "end", "id", "meanTravelTime", "TotalTravelTime",
    "meanOverlapTravelTime", "meanSpeed", "meanHaltsPerVehicle",
    "meanTimeLoss", "vehicleSum", "cum_vehicleSum", "meanSpeedWithin",
    "meanHaltsPerVehicleWithin", "meanDurationWithin", "vehicleSumWithin",
    "meanIntervalSpeedWithin", "meanIntervalHaltsPerVehicleWithin",
    "meanIntervalDurationWithin", "meanTimeLossWithin",
]

def convert_workbook(source: Path, scenario: str) -> pd.DataFrame:
    wide = pd.read_excel(source)
    frames = []
    for index, (model_id, code, description) in enumerate(MODELS):
        # Six 19-column data blocks are separated by one blank column.
        block = wide.iloc[:, index * 20:index * 20 + 19].copy()
        if block.shape[1] != len(FIELDS):
            raise ValueError(f"Unexpected column count for {model_id}: {block.shape[1]}")
        block.columns = FIELDS
        block = block.dropna(how="all", subset=["begin", "end", "id"])
        block.insert(0, "model_description", description)
        block.insert(0, "model_code", code)
        block.insert(0, "model_id", model_id)
        block.insert(0, "scenario", scenario)
        frames.append(block)
    return pd.concat(frames, ignore_index=True)

def main():
    PROCESSED.mkdir(parents=True, exist_ok=True)
    summaries = []
    for scenario, filename in [
        ("heavy", "heavy_traffic_metrics_original.xlsx"),
        ("low", "low_traffic_metrics_original.xlsx"),
    ]:
        source = RAW / filename
        tidy = convert_workbook(source, scenario)
        tidy.to_csv(PROCESSED / f"{scenario}_traffic_metrics_long.csv", index=False)
        for model_id, code, description in MODELS:
            subset = tidy[tidy["model_code"] == code]
            cumulative = subset["cum_vehicleSum"].dropna()
            summaries.append({
                "scenario": scenario,
                "model_id": model_id,
                "model_code": code,
                "model_description": description,
                "last_recorded_cumulative_vehicle_count":
                    int(cumulative.iloc[-1]) if not cumulative.empty else None,
                "available_time_intervals": int(len(cumulative)),
            })
    pd.DataFrame(summaries).to_csv(
        PROCESSED / "scenario_model_summary.csv", index=False
    )
    print("Processed source workbooks into results/processed/")

if __name__ == "__main__":
    main()
