# ASPA-UH_Integrated_Modeling_Framework

A framework for, and a case study of a small scale, vertically integrated, collaborative groundwater modeling process that attepts to
merge the fields of data-science and hydrology. This modeling framework applies an open-source, cloud-based, and process oriented paradigm to make modeling more accessible, transparent, reproducible, and stakeholder driven.


We refer to this framework as vertically integrated because it includes a diverse chain of modular components extending from the direct collection and processing of basic hydrologic parameters, through to the development of a dynamic regional groundwater model.

The framework has four descrete components: 

1: ASPA-UH_Wx_Sub-REPO contains data and code for processing and QA/Qc-ing raw weather station data

2: ASPA-UH_Stream_Sub-REPO contains data and code for processing, QA/Qc-ing, and automatically developing and updating rating curves from raw streamflow data

3: ASPA-UH-SWB2_REPO contains the needed data and code to run the Tutuila SWB2 water budget model

4: ASPA-UH-Flopy_REPO contains files and code to run MODFLOW based groundwater models using the data generated within other components of this framework

.............................................................................................................................................................................................................................................

<p align="center">
  <img width="650" height="325" src=Docs/Framework_Schematic1.jpg >
</p>




Schematic of data and modeling workflow for the ASPA-UH-WRRC collaborative modeling framework. Datasets or geospatial layer components are shown in quadrilaterals, code-based processes are contained in ovals, and external model executables are contained in triangles, which are themselves within ovals since they are run as Python sub-processes.


By: 
Christopher K. Shuler, Matamua Katrina E. Mariner, Aly El-Kadi
1. Water Resources Research Center and Department of Geology and Geophysics, University of Hawaii at Manoa
2. American Samoa Power Authority, American Samoa USA


We are working on a website too:
https://integratedmodelingframework.weebly.com/
