Hey Matt, 

In making the data processing routine, the following things will make data uploads go smoothly. Mahalo!

#### 1) Naming files: 
- Files should always start with a code consising of the well field abbreviation then with no spaces the well number
- Wellfield options include Malaeimi = MMI, Malaeloa = MOA, Iliili = ILI, Tafuna = TAF. 
- Other parts of the name should be separated with an underscore (_) and can include whatever identifying infor you want. 
e.g. MMI4_09-15-2019.csv or TAF33_download_from-Friday.csv

#### 2) Units for pressure need to be in PSI. 

#### 3) Units for temp in F.

#### 4) Date in its own column, 

#### 5) Time in its own column. 

For example: 

| Date      | Time | Abs Pres (psi)     | Temp (°F) |
| ----------- | ----------- | ----------- | ----------- |
| 04/06/17      | 9:30:00       | 14.6387      | 77.923       |
| 04/06/17   | 9:45:00        | 14.6366      | 76.181       |



Thanks!
