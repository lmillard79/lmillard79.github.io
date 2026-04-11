# Data — Baseflow Separation

## Required input

Daily streamflow data for a BOM gauge in CSV format.

### Format

```
Date,Flow_ML_day
1990-01-01,12.3
1990-01-02,15.7
...
```

### Source

Download daily streamflow data from the [BOM Water Data Online](http://www.bom.gov.au/waterdata/) portal:

1. Navigate to Water Data Online
2. Search for your gauge (e.g. Brisbane River at Gregors Creek — 143009A)
3. Select "Daily Mean Streamflow"
4. Export as CSV

Place the downloaded file in this directory and update the filename reference in the notebook.

## Sample data

A sample 10-year record for a Queensland gauge is provided for demonstration purposes (not included in this repository — download from BOM Water Data Online).
