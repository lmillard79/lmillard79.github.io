---
layout: single
title: "Projects & Open Source"
permalink: /projects/
author_profile: true
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/pano1.jpg
classes: wide
---

<div class="intro text-center" style="max-width: 800px; margin: 0 auto 2rem auto; color: #cbd5e1;">
  <p>Alongside consulting practice, I build and contribute to open-source tools for the Australian hydrology and hydraulic modelling community. Below are my active public repositories and selected technical contributions.</p>
</div>

---

## <i class="fab fa-github"></i> Open Source Repositories

<div style="background: rgba(255,255,255,0.04); border-left: 4px solid #2e8bc0; border-radius: 6px; padding: 1.2rem 1.5rem; margin-bottom: 1.5rem;">
  <h3 style="margin-bottom: 0.3rem;">
    <a href="https://github.com/lmillard79/pyextremes/tree/ARR2019_Book3" target="_blank" rel="noopener">pyextremes — ARR2019_Book3</a>
    <span style="font-size: 0.75rem; background: #2e8bc0; color: white; padding: 0.2rem 0.5rem; border-radius: 4px; margin-left: 0.5rem;">Python</span>
    <span style="font-size: 0.75rem; background: rgba(255,255,255,0.1); color: #94a3b8; padding: 0.2rem 0.5rem; border-radius: 4px; margin-left: 0.3rem;">Active Fork</span>
  </h3>
  <p style="font-size: 0.85rem; color: #94a3b8; margin-bottom: 0.8rem;">Fork of Georgy Bocharnikov's pyextremes — extended for ARR 2019 Book 3 and USGS Bulletin 17C at-site flood frequency analysis.</p>
  <p>Adds native <strong>Log-Pearson Type III (LP3)</strong> distribution fitting, the <strong>Multiple Grubbs-Beck Test</strong> for Potentially Influential Low Flood (PILF) identification, <strong>Two-Component Extreme Value (TCEV)</strong> distribution support, and <strong>LH-moments</strong> (h=1,2,3) for robust parameter estimation in Australian catchments where the "separation effect" affects standard L-moment fits.</p>
  <p>The branch is functional and testable. I'm actively developing it and welcome <strong>user feedback and bug reports</strong> via GitHub Issues — this is genuinely useful for Australian practitioners who need a pure-Python ARR 2019–compliant FFA workflow.</p>
  <p style="margin-top: 0.8rem;">
    <a href="https://github.com/lmillard79/pyextremes/blob/ARR2019_Book3/docs/user-guide/15-flood-frequency-analysis.md" target="_blank" rel="noopener" style="margin-right: 1rem;">📄 User Guide</a>
    <a href="/2026/03/22/pyextremes-arr2019-flood-frequency-python/" style="margin-right: 1rem;">📝 Insights Post</a>
    <a href="https://github.com/lmillard79/pyextremes/tree/ARR2019_Book3" target="_blank" rel="noopener">⭐ View on GitHub</a>
  </p>
</div>

<div style="background: rgba(255,255,255,0.04); border-left: 4px solid #2e8bc0; border-radius: 6px; padding: 1.2rem 1.5rem; margin-bottom: 1.5rem;">
  <h3 style="margin-bottom: 0.3rem;">
    <a href="https://github.com/lmillard79/tuflow-vscode" target="_blank" rel="noopener">tuflow-vscode</a>
    <span style="font-size: 0.75rem; background: #3178c6; color: white; padding: 0.2rem 0.5rem; border-radius: 4px; margin-left: 0.5rem;">TypeScript</span>
  </h3>
  <p style="font-size: 0.85rem; color: #94a3b8; margin-bottom: 0.8rem;">VS Code extension for TUFLOW hydraulic model files.</p>
  <p>Syntax highlighting, keyword IntelliSense, and file navigation for TUFLOW control files (.tcf, .tbc, .tgc, .tef). Reduces friction in the model development workflow — particularly useful when managing large, multi-file TUFLOW configurations. Available on the VS Code Marketplace.</p>
  <p style="margin-top: 0.8rem;">
    <a href="https://github.com/lmillard79/tuflow-vscode" target="_blank" rel="noopener">⭐ View on GitHub</a>
  </p>
</div>

<div style="background: rgba(255,255,255,0.04); border-left: 4px solid #2e8bc0; border-radius: 6px; padding: 1.2rem 1.5rem; margin-bottom: 1.5rem;">
  <h3 style="margin-bottom: 0.3rem;">
    <a href="https://github.com/lmillard79/Billabong-QGIS-Plugin" target="_blank" rel="noopener">Billabong QGIS Plugin</a>
    <span style="font-size: 0.75rem; background: #4caf50; color: white; padding: 0.2rem 0.5rem; border-radius: 4px; margin-left: 0.5rem;">Python</span>
  </h3>
  <p style="font-size: 0.85rem; color: #94a3b8; margin-bottom: 0.8rem;">Python plugin for QGIS — hydrological data processing and analysis tools.</p>
  <p>A QGIS plugin providing hydrological analysis tools within the QGIS environment. Published to the QGIS Plugin Repository.</p>
  <p style="margin-top: 0.8rem;">
    <a href="https://github.com/lmillard79/Billabong-QGIS-Plugin" target="_blank" rel="noopener">⭐ View on GitHub</a>
  </p>
</div>

<div style="background: rgba(255,255,255,0.04); border-left: 4px solid #2e8bc0; border-radius: 6px; padding: 1.2rem 1.5rem; margin-bottom: 1.5rem;">
  <h3 style="margin-bottom: 0.3rem;">
    <a href="https://github.com/lmillard79/PyRomb_ModelBuilder" target="_blank" rel="noopener">PyRomb — URBS Model Builder</a>
    <span style="font-size: 0.75rem; background: #4caf50; color: white; padding: 0.2rem 0.5rem; border-radius: 4px; margin-left: 0.5rem;">Python</span>
    <span style="font-size: 0.75rem; background: rgba(255,255,255,0.1); color: #94a3b8; padding: 0.2rem 0.5rem; border-radius: 4px; margin-left: 0.3rem;">PR merged upstream</span>
  </h3>
  <p style="font-size: 0.85rem; color: #94a3b8; margin-bottom: 0.8rem;">URBS runoff model builder for QGIS — contribution merged into Tom Norman's PyRomb main repository.</p>
  <p>I wrote the URBS model builder component of PyRomb, submitted as a pull request to Tom Norman's main repository. The contribution was accepted upstream — URBS and RORB runoff models can now both be built directly within QGIS via the PyRomb plugin, removing the need to configure model files manually outside the GIS environment.</p>
  <p style="margin-top: 0.8rem;">
    <a href="https://github.com/lmillard79/PyRomb_ModelBuilder" target="_blank" rel="noopener">⭐ View on GitHub</a>
  </p>
</div>

---

## <i class="fas fa-code"></i> Technical Projects

<div style="background: rgba(255,255,255,0.04); border-left: 4px solid #64748b; border-radius: 6px; padding: 1.2rem 1.5rem; margin-bottom: 1.5rem;">
  <h3 style="margin-bottom: 0.3rem;">Delft-FEWS / GoldSim Model Adapter</h3>
  <p style="font-size: 0.85rem; color: #94a3b8; margin-bottom: 0.8rem;">Python · Seqwater / WRM Water & Environment · 2019</p>
  <p>A Python pre/post-adapter enabling GoldSim reservoir routing models to run natively within a Delft-FEWS real-time forecasting system. The adapter translates FEWS PI-XML time series to GoldSim spreadsheet inputs (pre-adapter) and converts GoldSim output back to PI-XML for FEWS import (post-adapter), triggered by a batch controller. Presented at the 2019 TUFLOW User Conference.</p>
  <p style="margin-top: 0.8rem;">
    <a href="/blog/delft-fews-adapter/" style="margin-right: 1rem;">📝 Technical Post</a>
  </p>
</div>

<div style="background: rgba(255,255,255,0.04); border-left: 4px solid #64748b; border-radius: 6px; padding: 1.2rem 1.5rem; margin-bottom: 1.5rem;">
  <h3 style="margin-bottom: 0.3rem;">Continuous Simulation for Long-Duration Flood Estimation</h3>
  <p style="font-size: 0.85rem; color: #94a3b8; margin-bottom: 0.8rem;">Python · URBS · Internal R&D</p>
  <p>Adapted the pyraingen stochastic rainfall generation framework (Dykman & Brady) for long-term URBS continuous simulation — generating synthetic rainfall sequences constrained to IFD design values for use in continuous simulation flood frequency analysis. Part of ongoing R&D into moving from design storm–based to continuous simulation–based design flood estimation.</p>
</div>

---

<div class="notice--info" style="margin-top: 2rem;">
  <p><strong><a href="https://github.com/lmillard79" target="_blank" rel="noopener">View all repositories on GitHub →</a></strong> &nbsp;|&nbsp; Questions or collaboration on any of the above: <a href="mailto:lindsay.milard@outlook.com.au">get in touch</a>.</p>
</div>
