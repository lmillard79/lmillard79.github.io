# Data — Model Performance Metrics

## Synthetic URBS outputs

The notebook generates synthetic observed and modelled hydrographs internally to illustrate metric behaviour. No external data download is required for the demonstration.

## Using your own URBS outputs

To apply the metrics to real URBS calibration results, place your parsed URBS output CSV here:

```
data/
└── urbs_calibration_[event_name].csv
```

Expected format:

```csv
datetime,observed_m3s,modelled_m3s
2011-01-10 00:00,0.0,0.0
2011-01-10 01:00,12.3,14.1
...
```

The notebook includes a section demonstrating how to load and process this format.
