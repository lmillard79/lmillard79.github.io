# Data — Monte Carlo Loss Sampling

## No external data required for the sampler

The IL/CL distribution parameters are taken directly from ARR 2019 Book 5, Table 5.3.13 and are hardcoded in the notebook.

## Generated outputs

The notebook writes IL/CL sample files to this directory:

```
data/
├── il_cl_samples_N100.csv      # 100-member ensemble (generated)
├── il_cl_samples_N500.csv      # 500-member ensemble (generated)
└── il_cl_samples_N1000.csv     # 1000-member ensemble (generated)
```

These files are ready for use as URBS batch input pre-processor inputs.

## Regional variation

If your project requires region-specific loss distributions rather than the national ARR defaults, place your regional IL/CL data here as:

```
data/
└── regional_losses_[region_name].csv
```
