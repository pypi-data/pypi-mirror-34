# NADCON5-ng

Tweaks and Updates to US National Geodetic Survey `NADCON5` Tool. Used to calculate transformation between various US Datums, including: US Standard Datum (`USSD`) used  prior to `NAD27`, North American Datum of 1927 (`NAD27`), and various realizations of the North American Datum of 1983 `NAD83`

Build the dataset with one command

    make


[Link To Doxygen Documentation Website](http://docs.nc5ng.org/latest)

## Introduction

The intent of this project is to adapt the existing tool to be accessible to more users, through the implementation of additional interfaces and workflows on top of the existing NADCON5 Code Base and Data 

> **NOTE**: This project is a private project that is not in any way affiliated with the US Government, NOAA, or the National Geodetic Survey

**Derivative Work:** Additions and Modifications to NADCON5 code, documentation source files, and the source code of `nc5ng-core` python package  are released explicitly into Public Domain where applicable, with no rights reserved in perpetuity. However, certain published outputs associated with this project, e.g. builds and compiled documentation may be release under other licenses, Please see Licensing Section below.

[![Creative Commons License](https://licensebuttons.net/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)


## Project Status

This project is new, feature requests and development will be driven through issues filed in github.

At the time of this README was updated, the following was true

1. **GNU Make Pipeline:** The existing processing pipeline has been offloaded to GNU Make to eliminate in-source builds
2. **Documentation:** Documentation generation via Doxygen is functioning
  - Doxygen was bootstrapped on top of the NADCON5 code to create compiled documentation
  - Fortran source files were modified, superficially, to export documentation in a doxygen format
  - hosted online at url: https://docs.nc5ng.org/latest
3. Python package: Initial Framework for a python glue library
  - Functioning f2py submodules and functions
  - Data Inspection library and bundled source data
  - install with `pip install nc5ng-core` (Requirements: `gfortran`)
  - Rudimentary GMT/Python integration
  - Plotting NADCON5 input and output data directly through python wrapper
  


On the Immediate Roadmap

1. Remove build dependence on proprietary Oracle Fortran `f95`
  - Requires mapping build options to `gfortran` and correcting where necessary
  - Biggest issue is compiler specific handling of I/O and certain convenience extensions, not the math
  - `n5ng-core` already uses gfortran for `f2py`
2. Take over the "batch" programs (e.g. makework() , makeplotfiles01 , etc.) so that individual conversions can be done as needed, through Make or `nc5ng-core`


---
## What is NADCON5?


[NGS NADCON5 Front Page](https://www.ngs.noaa.gov/NADCON5/index.shtml)

[NGS NADCON5 Website](https://beta.ngs.noaa.gov/gtkweb)

The Following Information is Reproduced from the NADCON5 Webpage from NGS

### What is NADCON 5.0?

NADCON 5.0 performs three-dimensional (latitude, longitude, ellipsoid height) coordinate transformations for a wide range of datums and regions in the National Spatial Reference System. NADCON 5.0 is the replacement for all previous versions of the following tools:

- NADCON, which transformed coordinates between the North American Datum of 1927 (NAD 27) and early realizations of the North American Datum of 1983 (NAD 83), and
- GEOCON, which transformed coordinates between various latter realizations of NAD 83.

### How do I use NADCON 5.0?

NADCON 5.0 is functionally implemented in NGS’s Coordinate Conversion and Transformation Tool. Unlike earlier versions of NADCON and GEOCON, NADCON 5.0 is not a stand-alone tool.

Visit the NADCON 5.0 Digital Archive to access raw transformation data that make up NADCON 5.0 (e.g., grids, images, software).

### How can I learn more about NADCON 5.0?
[NOAA Technical Report NOS NGS 63 (PDF, 17 MB)](https://www.ngs.noaa.gov/PUBS_LIB/NOAA_TR_NOS_NGS_63.pdf) provides detailed information on NADCON 5.0, and the digital archive includes plots and data.




## Building `NADCON5-ng` 

Build simply with

    make

Which will build the initial tools and generate conversion output and images for the configured conversion 


### Dependencies

1. [Generic Mapping Tools](http://gmt.soest.hawaii.edu/) `**GMT**`
   - Tested with 5.2.1
   - Install on Debian Systems with `sudo apt-get install gmt gmt-dcw gmt-gshhg`

2. Oracle Fortran (`f95`) available for free (as in money, but not freedom) in [Oracle Developer Studio](https://www.oracle.com/tools/developerstudio/index.html)
   - Set `f95` path with environment variable `FC` (Per [GNU Conventions](https://www.gnu.org/software/make/manual/html_node/Implicit-Variables.html))

3. GNU Make



### Build Options

The configurable options for the build steps are

1. `OLD_DATUM`   - source datum (default: `ussd`)
2. `NEW_DATUM`   - target datum (default: `nad27`)
3. `REGION`      - geographical region (default: `conus`)
4. `GRIDSPACING` - Grid Spacing in arc-seconds (default: `900`)
5. `MAP_LEVEL`   - Map Resolution Flag (default: `0`)

These can be set as environment variables or directly on the command line

    export OLD_DATUM=nad27
    export NEW_DATUM=nad83
    make
    # Equivalent
    OLD_DATUM=ussd NEW_DATUM=nad27 make
    # Third Option
    make OLD_DATUM=ussd NEW_DATUM=nad27

### Targets

The Upstream build sequence can be simulated by using the targets `doit` `doit2` `doit3` `doit4`, as in

    make doit
    make doit2
    make doit3
    make doit4

This can be useful to compare results from the vanilla `NADCON`

Additionally, for the intermediate scripts `gmtbat0X` convenience targets are provided to manually step through the asset compilation

    make gmtbat01
    make gmtbat02
    make gmtbat03
    make gmtbat04
    make gmtbat05
    make gmtbat06
    make gmtbat07


Cleaning up is easy

Delete only the current configured build 

    make clean

Delete all compiled output (deletes build directory)

    make mrclean



## Licensing {#s-license}

A work of the US Government, the original NADCON5 Source Code and Data is considered in the public domain within the United States of America. Elsewhere, the US Government may reserve copyright and license this material. The licensing status of the `NADCON5.0` source material outside of the US  is not clear to the authors of `NADCON5-ng` . The authors and contributors cannot offer advice in this regard.


The licenses governing the derivative works provided by `nc5ng.org` and its contributors are enumerated below.

### Public Domain

New contributions, including:

 - Any modifications to National Geodetic Survey  `NADCON5.0` source code or data by `nc5ng` contributors
 - Makefile and build system
 - Documentation files and new documentation embedded in source files
 - Source code for python packages `nc5ng.core` and `nc5ng.nc5data`

Are released explicitly into the public domain in the United States and internationally as much as is allowed by law. The license file [LICENSE](LICENSE) states the terms of the Creative-Commons CC0 public domain disclaimer.

[![Creative Commons License](https://licensebuttons.net/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

### Fallback License

The fallback MIT License should be used in all cases where public domain release is not recognized or not applicable. A copy is provided with the distribution in the file [LICENSE-MIT](LICENSE-MIT)

### Compiled Assets generated by nc5ng.org and contributors

Compiled assets are published works generated using `NADCON5-ng` or in association with the project and usually published seperately from the public domain source code. For example, to promote the project or support the user base.

Compiled works are occasionally released in association with this project, This includes:

  - Pre-compiled HTML and PDF documentation and live webpages
  - Printed documentation provided by `nc5ng.org` 
  - Pre-compiled and pre-processed  output data provided by `nc5ng.org`
  - Websites, bug reports, project planning pages, and related project pages.
  
Compiled  assets published by `nc5ng.org` are provided with rights reserved and will default to a Creative Commons Attribution 4.0 International License, unless a different license is specified in the work.

[![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)


