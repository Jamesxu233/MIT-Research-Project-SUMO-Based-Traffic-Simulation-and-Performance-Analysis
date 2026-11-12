# Model Inventory and Run Notes

This document describes the files extracted from the supplied archive. It distinguishes files that were present in the archive from curated run configurations added for this repository package.

## 1. Extracted model folders

| Repository folder | Original archive folder | Main files |
|---|---|---|
| `x_cross_roundabout/` | `X交叉环岛/` | `model_test.net.xml`, `model_test.rou.xml`, `model_test.add.xml`, `model_test.tl.xml`, `model_test.tl2.xml` |
| `basic_two_lane_roundabout/` | `双车道环岛/` | `initial model.net.xml`, `initial model.rou.xml`, `initial model.add.xml` |
| `signalized_two_lane_roundabout/` | `双车道环岛加交通灯/` | `roundabout with tl.net.xml`, `.rou.xml`, `.add.xml`, `.trl1.xml` |
| `signalized_intersection/` | `交叉路口/` | `model1.net.xml`, `.rou.xml`, `.add.xml`, `model1TLS.xml` |

The original model PNG diagrams are copied to `assets/`.

## 2. Curated SUMO configurations

The repository package adds configurations with relative paths:

- `x_cross_roundabout/rcc_baseline.sumocfg`
- `basic_two_lane_roundabout/basic_roundabout.sumocfg`
- `signalized_two_lane_roundabout/signalized_roundabout.sumocfg`
- `signalized_intersection/signalized_intersection.sumocfg`

For the two signalized cases, the curated configuration explicitly references the supplied traffic-light logic file in addition to detector definitions.

The original SUMO configuration files are preserved for traceability.

## 3. RCCS signal-logic caution

The archive contains `model_test.tl.xml` and `model_test.tl2.xml` for the X-shaped central-cross network. They contain traffic-light logic records, but their mapping to the paper's two RCCS variants should be verified against the target network's traffic-light IDs and the stated cycle definitions before using them as a reproduction of Model 2 or Model 3.

Do not assume that a file name or phase duration alone proves the exact model mapping.

## 4. Detector XML files

The archive also contains files named `e3_system*.xml` outside the model folders. These are retained in `results/raw/` because they contain detector-related records. The `*.add.xml` files inside each model folder define E3 detectors and their entry/exit points for use during simulation.

## 5. Version compatibility

The XML comments indicate that some network files were generated with SUMO 1.4.0 and some traffic-light definitions with NetEdit 1.12.0. The curated configuration files use relative paths, but no compatibility run was performed during this documentation update. Verify each model in the SUMO version installed on your machine.
