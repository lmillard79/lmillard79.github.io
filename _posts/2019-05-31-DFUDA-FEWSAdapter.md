---
title: "Delft-FEWS Model Adapter Development"
date: 2019-05-31
permalink: /blog/delft-fews-adapter/
layout: single
header:
  image: "/images/pano1.jpg"
  caption: "Creating custom model adapters for Delft-FEWS"
author_profile: true
tags: ['Delft-FEWS', 'Hydrology', 'Python']
categories: ['Hydrology', 'Software Development']
---
# Delft FEWS Proof of Concept Model adapter

Often we have legacy models which we'd like to use with Delft-FEWS but an adapter does exist or the current adapter is out of date with the latest model release.
Examples of models that can use the following code are RORB, GoldSim, MIKE1D, HEC-RAS 5.0 and many others. 


<iframe src="//www.slideshare.net/slideshow/embed_code/key/13I30pDti4SjJx" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/LindsayMillard/python-the-lingua-franca-of-fews" title="Python the lingua franca of FEWS" target="_blank">Python the lingua franca of FEWS</a> </strong> from <strong><a href="//www.slideshare.net/LindsayMillard" target="_blank">Lindsay Millard</a></strong> </div>

## Pre-Adapter - XML to generic model input
Here is the Python Code Block:
```python

   from xml.etree.ElementTree import *  # Import everything 

import time
from datetime import datetime
import csv
import os

import numpy as np
import pandas as pd  ## Abbreviate it using the convention
pd.options.display.date_dayfirst=True  # Important to some assumptions below

# Check what version of the module you are running, lets check Pandas.
pd.__version__

# It is a good idea to put your variables up front
fewsNamespace="http://www.wldelft.nl/fews/PI"
regionHome = r'C:\Users\Lindsay\Documents\GitHub\DFUDA_2019_Adapter/'

XMLs = ['importState','import']

for xml in XMLs:
    fin = os.path.join(regionHome,'1_Input',xml+'.xml')    
    FEWS_Export = fin   #  regionHome+'1_Input/importState.xml'

    parameterNames = ['HNPD_OUT','Reservoir.inflow.forecast', 'Reservoir.outflow.forecast', 'Gate.setting.forecast',]
    spreadsheetNames = {'Reservoir.inflow.forecast':'LakeInflows', 'Reservoir.outflow.forecast':'RegulatorFlows', 'Gate.setting.forecast':'Gates', 'HNPD_OUT':'LakeLevels'}

    for parametername in parameterNames:                   
        ParList=[]
        par =[]
        locId=[]
        i = 0    
        
        with open(FEWS_Export, "r") as file:
            tree = parse(file)
            PItimeSeries = tree.getroot()
            Parameters=PItimeSeries.findall('.//{' + fewsNamespace + '}parameterId')
            for param in Parameters:
                ParList.append(param.text)
                
            missingvalue = PItimeSeries.findall('.//{' + fewsNamespace + '}missVal')
            series = PItimeSeries.findall('.//{' + fewsNamespace + '}series')

            # determine size of aray needed. all series MUST be the same length
            parCount=0
            for S in series:
                events = S.findall('.//{' + fewsNamespace + '}event')
                ArrayDates = np.zeros((len(events)),dtype='datetime64[ns]')
                
                par = S.find('.//{' + fewsNamespace + '}parameterId').text
                if par==parametername:
                    parCount = parCount + 1
            
            ArrayValues = np.zeros((len(events), parCount))
            j = 0

            DateList = []
            for S in series:
                par = S.find('.//{' + fewsNamespace + '}parameterId').text
                
                if par!=parametername:
                    pass
                
                else:            
                    events = S.findall('.//{' + fewsNamespace + '}event')
                    locs = S.findall('.//{' + fewsNamespace + '}locationId')
                    i=0
                    for l in locs:
                        locId.append(l.text)        
                
                    for ev in events:
                        if ev.attrib['value'] == S.find('.//{' + fewsNamespace + '}missVal').text:
                            ArrayValues[i,j] = float(0)
                        else:
                            ArrayValues[i,j] = float(ev.attrib['value'])
                        
                        strucTime_Tuple = datetime.strptime(ev.attrib['date'] + " " + ev.attrib['time'],"%Y-%m-%d %H:%M:%S")
                        ArrayDates[i] = strucTime_Tuple

                        i += 1
                    j +=  1
            row = i
            col = j

            DFd = pd.DataFrame(ArrayDates) 
            DFd.columns = ['DateTime']
            DFv = pd.DataFrame(ArrayValues) 
            DFv.columns = locId

            DF = pd.concat([DFd,DFv],axis=1)
                
            
        if xml == 'importState' and parametername == 'HNPD_OUT':
            GoldSIMSpreadSheet = regionHome+'2_Model/'+spreadsheetNames[parametername]+'.xlsx'
            DF.to_excel(GoldSIMSpreadSheet,sheet_name='FEWS_Export')
        
        elif parametername != 'HNPD_OUT':
            GoldSIMSpreadSheet = regionHome+'2_Model/'+spreadsheetNames[parametername]+'.xlsx'
            DF.to_excel(GoldSIMSpreadSheet,sheet_name='FEWS_Export')

```


## Post Adapter - Model output back to XML Timeseries

```python

from xml.etree.ElementTree import *  # Import everything 

import time
from datetime import datetime
import csv
import os

## from xlsxwriter.workbook import Workbook

import numpy as np
import pandas as pd  ## Abbreviate it using the convention
pd.options.display.date_dayfirst=True  # Important to some assumptions below


## Worker Function for checking currency
def newest(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)

# It is a good idea to put your variables up front
fewsNamespace="http://www.wldelft.nl/fews/PI"

regionHome = r'C:\Users\Lindsay\Documents\GitHub\DFUDA_2019_Adapter/'

ExportXML = '3_Output/Export_fromGoldSim.xml'

# populate the xml file
def xml(parameter, location, eventValues, dT64, unit):
    #sd = str(dateTime[0])
    sd = dateTime[0].strftime("%Y-%m-%d")
    st = dateTime[0].strftime("%H:%M:%S")
    ed = dateTime[-1].strftime("%Y-%m-%d")
    et = dateTime[-1].strftime("%H:%M:%S")
    DTtimeStep = dateTime[1]-dateTime[0]
    timeStep = int(DTtimeStep.total_seconds())
    
    # write XML output timeseries
    with open(regionHome+ExportXML,'a') as xf:    # 'a+b'
        
        ## Write Header for each Series 
        
        xf.write('    <series>\n')
        xf.write('        <header>\n')
        xf.write('            <type>instantaneous</type>\n')        
        
        loc_text = str('            <locationId>%s</locationId>\n') % (location)
        xf.write(loc_text)        
        
        par_text = str('            <parameterId>%s</parameterId>\n') % (parameter)
        xf.write(par_text)
        
        timestep_text = str('            <timeStep unit="second" multiplier="%s"/>\n') %(timeStep)
        xf.write(timestep_text)   
        
        sd_text = str('            <startDate date="%s" time="%s"/>\n') % (sd, st)
        xf.write(sd_text)
        
        ed_text = str('            <endDate date="%s" time="%s"/>\n') % (ed, et)
        xf.write(ed_text)
        
        xf.write('            <missVal>-999.0</missVal>\n')
        xf.write('            <stationName>Hydro Gauge 1</stationName>\n')        
        
        unit_text = str('            <units>%s</units>\n') %(unit)
        xf.write(unit_text) 
        
        xf.write('        </header>\n')
        
        
        ## Write all the event values for each  timestamp in the series
        for i in range(len(eventValues)):
            event_date = str('        <event date="%s"') % (dateTime[i].strftime("%Y-%m-%d"))
            event_time = str(' time="%s"') % (dateTime[i].strftime("%H:%M:%S"))
            event_value = str(' value="%s"') % eventValues[i][0].round(2)
            event_flag = str(' flag="0"/>\n')
            
            event = str(event_date+event_time+event_value+event_flag)
            xf.write(event)
            
        xf.write('    </series>\n')
        
        

GoldSimOutputs = ['RoutedFlows.txt','RoutedLevels.txt']

DF = pd.DataFrame()

# write XML output header, once
with open(ExportXML,'w') as xf:
    xf.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    xf.write('<TimeSeries xmlns="http://www.wldelft.nl/fews/PI" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.wldelft.nl/fews/PI http://fews.wldelft.nl/schemas/version1.0/pi-schemas/pi_timeseries.xsd" version="1.2">\n')
    xf.write('    <timeZone>10.0</timeZone>\n')

for GS in GoldSimOutputs:
    fin = os.path.join(regionHome,'2_Model',GS)

    with open(fin,'r') as f:
        lines = f.readlines()
        parameter = lines[11].split()[1]
        unit = lines[12].split()[1]

    df = pd.read_table(fin,skiprows=14,header=None,names=['DateTime',parameter+'_'+unit,'Blank'],index_col=0,
                       parse_dates=True,dayfirst=True)

    df = df.drop(['Blank'],axis=1)   
    DF = pd.concat([DF,df],axis=1)
    
    locn = 'NPD'
    dateTime = df.index.to_pydatetime()
    xml(parameter,locn,df.values,dateTime,unit)

with open(ExportXML,'a') as xf:
    xf.write('</TimeSeries>\n') 

ax=DF.iloc[:,0].plot(legend=True)
DF.iloc[:,1].plot(secondary_y=True,
                  ax=ax,legend=True)
ax.set_ylabel(DF.columns[0])
ax.set_xlim('09-01-2011','13-01-2011')
ax.grid(which='both')

fig = ax.get_figure()
fig.savefig('GoldSim_TS.png',dpi=300)

        

```


## Batch File to control all of the steps

```

echo on

C:

:: Initialise the Executables
set PYEXE="C:\Python27\python.exe"
set EXE=GSPlayer.exe
set RUN=Start /wait %EXE%

:: Housekeeping
set regionHome=C:\Users\Lindsay\Documents\GitHub\DFUDA_2019_Adapter

:: Pre-Adapter - Grab the FEWS_Export.xml from URBS turn into GoldSim XLSX
%PYEXE% %regionHome%\01_Pre_Adapter.py

:: Runtime - Go Do some GoldSim modelling 
CD "C:\Program Files (x86)\GTG\GoldSim Player 12.1"
%RUN% -r  -x %regionHome%\2_Model\NPD_Routing_v8_simplified.gsp

:: Probably need to do this
CD %regionHome%

:: Post-Adapter - Turn the GoldSim XLSX into a FEWS_Import.xml 
%PYEXE% %regionHome%\03_Post_Adapter.py

:: Have a look at the results as a plot
%SystemRoot%\System32\rundll32.exe "%ProgramFiles%\Windows Photo Viewer\PhotoViewer.dll", ImageView_Fullscreen %regionHome%\GoldSim_TS.png


```