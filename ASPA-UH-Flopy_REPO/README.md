# ASPA-UH-Flopy_model


Please note that calibration and validation of this groundwater modeling component remains ongoing as of this writing. Any results presented here are not necessarily accurate or representative of reality, due to the need for additional constraint on many of the model
parameters. This is an ongoing process and will continue to evolve

The MODFLOW model input is structured into a discrete set of required and optional
packages, and each are represented by separate input files. Required packages include the
basic package (.bas), the discretization package (.dis), and the output control package (.oc).
While these files are generally human-readable text or ascii grid files that can be modified by
hand, FloPy contains highly useful data formatting functionality to easily take shapefile- or
raster-based input data and generate the MODFLOW package files in required formats.
Implementation of the Tutuila groundwater modeling framework accomplished all pre-
processing steps using FloPy or other Python modules within a dedicated Jupyter Notebook.
FloPy also provides functionality to run the MODFLOW code. this exe should be included in the repository, but if your browser prevets you from opening it, you can download this zip file: (https://water.usgs.gov/water-resources/software/MODFLOW-2005/MF2005.1_12.zip). and find the mf2005.exe file in the bin directory. 

FloPy runs MODFLOW as a sub-process and prints output directly to
the notebook cell. Once the MODFLOW code is run and output files are saved, these can be
accessed within the notebook for post-processing routines that display model output or conduct
statistical analysis. The Tutuila groundwater model workflow currently includes definition of the
required MODFLOW packages as well as those representing boundary conditions (.ghb),
hydraulic conductivity zones (.lpf), head observations (.obs), spatially-resampled recharge rates
(.rch) derived directly from SWB2, and salt-water interface predictions


<!-- blank line -->
<figure class="video_container">
  <iframe src='https://www.mapchannels.com/mc5/27562/27562-testsuccess.htm?v=20190807113007' frameborder="0" allowfullscreen="true"></iframe>
</figure>
<!-- blank line -->
