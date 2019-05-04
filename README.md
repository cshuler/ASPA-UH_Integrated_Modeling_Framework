# ASPA-UH_Integrated_Modeling_Framework


Christopher K. Shuler1,* and Matamua Katrina E. Mariner2
1. Water Resources Research Center and Department of Geology and Geophysics, University of Hawaii at Manoa,
1680 East West Road, HI 96822, USA
2. American Samoa Power Authority, American Samoa USA


A framework for, and a case study of a small scale, vertically integrated, collaborative groundwater modeling process that attepts to
merge the fields of data-science and hydrology. This modeling framework applies an open-source, cloud-based, and process oriented paradigm to make modeling more accessible, transparent, reproducible, and stakeholder driven.


We refer to this framework as vertically integrated because it includes a diverse chain of modular components extending from the direct collection and processing of basic hydrologic parameters, through to the development of a dynamic regional groundwater model.

The framework has four descrete components: 

1: ASPA-UH_Wx_Sub-REPO contains data and code for processing and QA/Qc-ing raw weather station data
2: ASPA-UH_Stream_Sub-REPO contains data and code for processing, QA/Qc-ing, and automatically developing and updating rating curves from raw streamflow data

3: ASPA-UH-SWB2_REPO contains the needed data and code to run the Tutuila SWB2 water budget model

4: ASPA-UH-Flopy_REPO contains files and code to run MODFLOW based groundwater models using the data generated within other components of this framework

........................................................................................................................................................................................


![alt text](https://github.com/cshuler/ASPA-UH_Integrated_Modeling_Framework/blob/master/Framework_Schematic1.jpg)

Scematic of the collaborative modeling framework coponents
