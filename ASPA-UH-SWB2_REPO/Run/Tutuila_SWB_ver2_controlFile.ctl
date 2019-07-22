GRID 350.0 200.0 515000. 8409000. 100.0 

!                   Lower LH Corner              Grid 
!                 |_________________________|    Cell 
!       NX     NY       X0       Y0              Size 


# Input file for swb2, Samoa Test Case 
# Base projection: UTM Zone 2 South 
# (comment characters: !#$%*()-[] ) 
-------------------------------------

(0) PROJECT GRID DEFINITION 
--------------------------- 
 

 
BASE_PROJECTION_DEFINITION +proj=utm +zone=2 +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs 
 
 
 
 
 (1) MODULE SPECIFICATION 
------------------------- 
 
INTERCEPTION_METHOD              GASH 
EVAPOTRANSPIRATION_METHOD        MONTHLY_GRID 
RUNOFF_METHOD                    RUNOFF_RATIO 
SOIL_MOISTURE_METHOD             FAO-56 
PRECIPITATION_METHOD             METHOD_OF_FRAGMENTS 
FOG_METHOD                       NONE 
FLOW_ROUTING_METHOD              D8 
IRRIGATION_METHOD                NONE  
CROP_COEFFICIENT_METHOD          FAO-56 
DIRECT_NET_INFILTRATION_METHOD   GRIDDED 
DIRECT_SOIL_MOISTURE_METHOD      TABULAR 
SOIL_STORAGE_MAX_METHOD          GRIDDED 


(2) Initial conditions for soil moisture, snow 
----------------------------------------------- 
 
INITIAL_PERCENT_SOIL_MOISTURE    CONSTANT 75.0 
INITIAL_SNOW_COVER_STORAGE       CONSTANT 0.0 





(3) Daily rainfall-related grids and data 
------------------------------------------ 
 
PRECIPITATION ARC_GRID ../input/Gridded_rain/prism_ppt_tutuila_30yr_normal_%0m.asc 
PRECIPITATION_GRID_PROJECTION_DEFINITION +proj=utm +zone=2 +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs 


FRAGMENTS_DAILY_FILE ../dynamic_inputs/Rainfall_fragments/Rainfall_fragments_3.prn
FRAGMENTS_SEQUENCE_FILE ../dynamic_inputs/Rainfall_fragments/Sequence_file_3.prn
FRAGMENTS_SEQUENCE_SIMULATION_NUMBER 1

RAINFALL_ZONE ARC_GRID ../input/Rain_stations/tp_grid.asc
RAINFALL_ZONE_PROJECTION_DEFINITION +proj=utm +zone=2 +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs 

RAINFALL_ADJUST_FACTOR ARC_GRID ../input/RF_adj_grids/rfadj_%b.asc
RAINFALL_ADJUST_FACTOR_PROJECTION_DEFINITION  +proj=utm +zone=2 +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs 
RAINFALL_ADJUST_FACTOR_MONTHNAMES_LOWERCASE 


(4) Monthly air temperature grids 
---------------------------------- 
 
TMAX ARC_GRID ../input/Gridded_temps/prism_tmax_tutuila_30yr_normal_%0m.asc
TMAX_GRID_PROJECTION_DEFINITION +proj=utm +zone=2 +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs
TMAX_SCALE_FACTOR                 1.8 
TMAX_ADD_OFFSET                  32.0 
TMAX_MISSING_VALUES_CODE      -9999.0 
TMAX_MISSING_VALUES_OPERATOR      <= 
TMAX_MISSING_VALUES_ACTION       mean 
 
TMIN ARC_GRID ../input/Gridded_temps/prism_tmin_tutuila_30yr_normal_%0m.asc
TMIN_GRID_PROJECTION_DEFINITION +proj=utm +zone=2 +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs 
TMIN_SCALE_FACTOR                 1.8 
TMIN_ADD_OFFSET                  32.0 
TMIN_MISSING_VALUES_CODE      -9999.0 
TMIN_MISSING_VALUES_OPERATOR      <= 
TMIN_MISSING_VALUES_ACTION       mean 
 



(5) Continuous Frozen-Ground Index initial value and parameters 
--------------------------------------------------------------- 
 
INITIAL_CONTINUOUS_FROZEN_GROUND_INDEX CONSTANT 0.0 
 
UPPER_LIMIT_CFGI 83. 
LOWER_LIMIT_CFGI 55.



 
(6) "standard" GIS input grids: hydrologic soils group, available water capacity, soils, and flow direction 
----------------------------------------------------------------------------------------------------------- 
 
HYDROLOGIC_SOILS_GROUP ARC_GRID ../input/Land_use_Soils_data/h2ogp_grid.asc
HYDROLOGIC_SOILS_GROUP_PROJECTION_DEFINITION +proj=utm +zone=2 +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs 

LAND_USE ARC_GRID ../input/Land_use_Soils_data/lu_grid.asc
LAND_USE_PROJECTION_DEFINITION +proj=utm +zone=2 +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs  

SOILS_CODE CONSTANT 1 

SOIL_STORAGE_MAX ARC_GRID ../input/Land_use_Soils_data/soil_moist_cap_grid.asc
SOIL_STORAGE_MAX_PROJECTION_DEFINITION +proj=utm +zone=2 +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs 
SOIL_STORAGE_MAX_MISSING_VALUES_CODE          0.0 
SOIL_STORAGE_MAX_MISSING_VALUES_OPERATOR      < 
SOIL_STORAGE_MAX_MISSING_VALUES_ACTION       mean

(7) Other gridded datasets required for the Maui example 
-------------------------------------------------------- 
 
REFERENCE_ET0 ARC_GRID ../input/ET_Process/%b_et_clipped.asc
REFERENCE_ET0_PROJECTION_DEFINITION +proj=utm +zone=2 +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs 

## note also includes water line leakage and MFR too ##
CESSPOOL_LEAKAGE ARC_GRID ../input/Direct_infiltration/Total_inlf_in.asc
CESSPOOL_LEAKAGE_PROJECTION_DEFINITION +proj=utm +zone=2 +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs 


(8) Grids required for Gash Interception 
----------------------------------------- 
 
FRACTION_CANOPY_COVER ARC_GRID ../input/Land_use_Soils_data/cancovras.asc
FRACTION_CANOPY_COVER_PROJECTION_DEFINITION +proj=utm +zone=2 +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs 
 
EVAPORATION_TO_RAINFALL_RATIO ARC_GRID ../input/Evaporation/v_evp2pcp.asc
EVAPORATION_TO_RAINFALL_RATIO_PROJECTION_DEFINITION +proj=utm +zone=2 +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs 



(9) Runoff-related data and grid 
-------------------------------- 
 
RUNOFF_ZONE ARC_GRID ../input/Runoff_zones_WS/ro_rast.asc
RUNOFF_ZONE_PROJECTION_DEFINITION +proj=utm +zone=2 +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs 
 
RUNOFF_RATIO_MONTHLY_FILE ../dynamic_inputs/RO_Rf_Ratios_Dynamic/RO_Rf_ratios_Dynamic_monthly_2000_2011.txt

PERCENT_PERVIOUS_COVER ARC_GRID ../input/Land_use_Soils_data/ppervras.asc
PERCENT_PERVIOUS_COVER_PROJECTION_DEFINITION +proj=utm +zone=2 +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs 

FLOW_DIRECTION ARC_GRID ../input/DEM_Process/flow_direction.asc
FLOW_DIRECTION_PROJECTION_DEFINITION +proj=utm +zone=2 +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs 
 
(10) Output control 
—————————————— 
OUTPUT ENABLE gross_precipitation 
OUTPUT ENABLE rainfall 
OUTPUT ENABLE interception 
OUTPUT ENABLE runon 
OUTPUT ENABLE runoff 
OUTPUT ENABLE reference_ET0 
OUTPUT ENABLE actual_et 
OUTPUT ENABLE net_infiltration 
OUTPUT ENABLE rejected_net_infiltration 
OUTPUT ENABLE infiltration 
OUTPUT ENABLE irrigation 
OUTPUT ENABLE runoff_outside 
OUTPUT ENABLE crop_et 
 
OUTPUT ENABLE tmin 
OUTPUT ENABLE tmax 
OUTPUT ENABLE gdd 
 
OUTPUT ENABLE snow_storage 
OUTPUT ENABLE soil_storage 
OUTPUT ENABLE delta_soil_storage 
 
OUTPUT ENABLE snowmelt 
OUTPUT ENABLE snowfall 
 
OUTPUT ENABLE direct_net_infiltation 
OUTPUT ENABLE direct_soil_moisture 

(11) Lookup table(s) 
-------------------- 
  

LAND_USE_LOOKUP_TABLE ../input/Landuse_lookup_maui_mod5.txt


(12) Start and end date for simulation 
-------------------------------------- 
 
START_DATE 01/01/2000 
END_DATE 12/31/2000 