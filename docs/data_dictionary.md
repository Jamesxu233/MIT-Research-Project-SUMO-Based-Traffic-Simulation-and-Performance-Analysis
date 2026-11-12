# Data Dictionary

## 1. Source workbooks

| File | Scenario | Time rows in source workbook | Model blocks |
|---|---|---:|---:|
| `heavy_traffic_metrics_original.xlsx` | Heavy traffic | 45 | 6 |
| `low_traffic_metrics_original.xlsx` | Low traffic | 12 | 6 |

Each workbook stores six groups of 19 data columns, separated by blank columns. The included script reshapes these blocks into long-format CSV.

## 2. Model labels

The six groups are assigned in the order defined in the paper:

1. `RCC` — Model 1, X-shaped central-cross roundabout
2. `RCCS_46s` — Model 2, central-cross roundabout with 46-second signal timing
3. `RCCS_26s` — Model 3, central-cross roundabout with 26-second signal timing
4. `RS` — Model 4, roundabout with signalized junctions
5. `BR` — Model 5, basic two-lane roundabout
6. `SI` — Model 6, signalized intersection

The labels above identify the paper's model sequence; the precise signal-XML mapping for RCCS remains subject to validation.

## 3. Fields

| Field | Description |
|---|---|
| `scenario` | `heavy` or `low` traffic scenario |
| `model_id` | Paper model number |
| `model_code` | Short model identifier |
| `model_description` | Human-readable model description |
| `begin` | Start time of the interval |
| `end` | End time of the interval |
| `id` | Detector/system identifier from the workbook |
| `meanTravelTime` | Mean travel-time metric in source export |
| `TotalTravelTime` | Total travel-time metric in source export |
| `meanOverlapTravelTime` | Mean overlap travel-time metric in source export |
| `meanSpeed` | Mean speed in source export |
| `meanHaltsPerVehicle` | Mean halts per vehicle |
| `meanTimeLoss` | Mean time loss |
| `vehicleSum` | Vehicle count in the interval |
| `cum_vehicleSum` | Cumulative vehicle count |
| `meanSpeedWithin` | Mean speed within the monitored area |
| `meanHaltsPerVehicleWithin` | Mean halts per vehicle within the monitored area |
| `meanDurationWithin` | Mean duration within the monitored area |
| `vehicleSumWithin` | Vehicle count within the monitored area |
| `meanIntervalSpeedWithin` | Interval mean speed within the monitored area |
| `meanIntervalHaltsPerVehicleWithin` | Interval mean halts per vehicle within the monitored area |
| `meanIntervalDurationWithin` | Interval mean duration within the monitored area |
| `meanTimeLossWithin` | Mean time loss within the monitored area |

The source workbook uses SUMO-exported field names. Units and precise detector aggregation semantics should be confirmed against the original detector configuration and SUMO output documentation before downstream statistical interpretation.
