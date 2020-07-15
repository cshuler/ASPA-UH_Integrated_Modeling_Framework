[![DOI](https://zenodo.org/badge/181068976.svg)](https://zenodo.org/badge/latestdoi/181068976)


# ASPA-UH WRRC Integrated Modeling Framework


Developed By: 
Christopher K. Shuler (1), Matamua Katrina E. Mariner (2), Aly El-Kadi (1)
###### (1) Water Resources Research Center and Department of Geology and Geophysics, University of Hawaii at Manoa  (2) American Samoa Power Authority, American Samoa USA

A framework for, and a case study of a small scale, vertically integrated, collaborative groundwater modeling process that merges the fields of data-science and hydrology. This modeling framework applies an open-source, cloud-based, and process oriented paradigm to make modeling more accessible, transparent, reproducible, and stakeholder driven. We refer to this framework as vertically integrated because it includes a diverse chain of modular components extending from the direct collection and processing of basic hydrologic parameters, through to the development of a dynamic regional groundwater model.

## Getting Started  
This framework provides data, code, and documentation for a reseach scale hydrological modeling project. In genral, input data folders are kept separate from results (output data) folders, and code used to generate the outputs is developed within Jupyter Notebooks. Thus, when exploring this repository, all models and data processing routines can be found by searching for **.ipynb** files. If you are new to GitHub also consider exploring [This Website](https://integratedmodelingframework.weebly.com/) to learn more about what we are doing here.
# 


The framework has four descrete components: 

#### 1: ASPA-UH_Wx_Sub-REPO contains data and code for processing and QA/QC-ing raw weather station data

[Download Processed Weather Station Data (click "view raw")](ASPA-UH_Wx_REPO/workspace/QA_All_merged.csv)

#### 2: ASPA-UH_Stream_Sub-REPO contains data and code for processing, QA/QC-ing, and automatically developing and updating rating curves from raw streamflow data

[Download Processed Streamflow Data](ASPA-UH_Stream_REPO/workspace)

#### 3: ASPA-UH-SWB2_REPO contains the needed data and code to run the Tutuila SWB2 water budget model

[See Maps of Recharge and other Water Budget Components](ASPA-UH-SWB2_REPO/output/Figures)

#### 4: ASPA-UH-Flopy_REPO contains files and code to run MODFLOW based groundwater models using the data generated within other components of this framework

[Check Out Different Groundwater Model Notebooks](ASPA-UH-Flopy_REPO/Models)

&nbsp;

### How it all fits together

<p align="center">
  <img width="650" height="325" src=Docs/Figures/Framework_Schematic1.jpg >
</p>




Schematic of data and modeling workflow for the ASPA-UH-WRRC collaborative modeling framework. The SWB2 model is a water budget model originally developed by the USGS used to produce spatially distributed groundwater recharge data, and FloPy is a Python based MODFLOW groundwater model compiler used to predict groundwater heads and salinities on a regional scale.  Datasets or geospatial layer components are shown in quadrilaterals, code-based processes are contained in ovals, and external model executables are contained in triangles, which are themselves within ovals since they are run as Python sub-processes. All components, meaning all raw data, all modelign code, all model executables, and the most recent versions of results are included in this repository.


#### Don't forget to check out our website!
https://integratedmodelingframework.weebly.com/

&nbsp;

#### Additionally our recent open-access article, *"Collaborative groundwater modeling: Open-source, cloud-based, applied science at a small-island water utility scale"* published in Environmental Modeling and Software can be found [Here!](https://www.sciencedirect.com/science/article/pii/S136481521930934X)
or download the pdf from this repository [here](Docs/1-s2.0-S136481521930934X-main.pdf)


&nbsp;

### Disclaimer
This work is provided as open-source software on the condition that its authors, the UH Water Resource Research Center, or the American Samoa Power authority shall be held liable for any damages resulting from the authorized or unauthorized use of the information. No warranty, expressed or implied, is made by the authors as to the accuracy and functioning of the program and related program material nor shall the fact of distribution constitute any such warranty and no responsibility is assumed by the authors in connection therewith. This information is preliminary or provisional and is subject to revision. This software is provided "AS IS." Note that sensitive information, or datasets that are not publically available, are not posted in raw forms. The model code is licensed under the GNU General Public License v3.0 which is an open-access license designed to explicitly affirm any user’s unlimited permission to run, copy, and use the unmodified code from this repository. Please note that some raw datasets used in this work are not owned by the authors and may be subject to other licenses or conditions.

This is a work in progress and is is subject to change, revision, or removal at the developers discression. No guarentee is made regarding the quality or accuracy of these data. While QA QC procedures have been applied to some data these procedures are still under development and subject to revision and any use of this data should be understood in this context.


#### These projects are supported by
- The University of Hawaii Water Resources Research Center through The National Institutes for Water Resources grant numbers: 2015AS443B, 2015AS445B, 2018AS488B
- U.S. Environmental Protection Agency Region IX through  The American Samoa Environmental Protection Agency grant number: C00543
- Pacific Regional Integrated Sciences and Assessments (Pacific RISA) program grant number: NA15OAR4310146
- and The American Samoa Power Authority through ratepayer supported funds

