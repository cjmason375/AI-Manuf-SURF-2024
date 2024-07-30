# ***"Real-time manufacturing machine monitoring in edge analytics using electrical current consumption: Case study of plasma etcher operation and condition prediction"***

Technical Summary of work performed by Everett "CJ" Mason, Jr. at Purdue University's 2024 Summer Undergraduate Research Fellowship (SURF). <br> <br>
Feel free to contact me at *jemason@purdue.edu* or *everettmasonjr23@gmail.com*

View [abstract](https://github.com/cjmason375/AI-in-Manuf-SURF-2024/blob/main/Abstract.md) here.

View [Summer Research Symposium Presentation]() here.

<br>



## **1) INTRODUCTION/BACKGROUND**

[Industry 4.0](https://www.ibm.com/topics/industry-4-0) is an ongoing shift for factories towards utilizing smart manufacturing means in modern manufacturing processes. Traditionally, factories operated on the standard of *[preventative maintenance](https://www.ibm.com/topics/what-is-preventive-maintenance#:~:text=Preventive%20maintenance%20is%20the%20act,fixing%20things%20before%20they%20break)*, in which regular checks would occur for maintenance tasks to prevent unexpected future failures. However, the precautionary nature of this method would result in higher costs, increased waste as tools were  replaced before reaching their full lifespan, and increased labor. Industry 4.0 sees the ***shift from preventative maintenance to [predictive maintenance](https://www.ibm.com/topics/predictive-maintenance)***. This digitalization of the industrial world uses Artificial Intelligence (AI) and Machine Learning (ML) for automated real-time decision-making, optimizing productivity means, and reducing production costs. By intelligently predicting the failures of machines or tool parts, many drawbacks of preventative maintenance can be greatly reduced.

[***Annotated Literature Review***](https://github.com/cjmason375/AI-in-Manuf-SURF-2024/blob/main/Annotated%20Literature%20Review) <br>

*The NSF AI in Manufacturing project seeks to innovate standard industrial processes by incorporating emerging Machine Learning (ML) and Artificial Intelligence (AI) practices for smart detection. This specific branch of the project focuses on the use of [Edge Analytics](https://www.ibm.com/blog/analytics-at-the-edge/) and the [Industrial Internet of Things](https://www.iberdrola.com/innovation/what-is-iiot#:~:text=The%20Industrial%20Internet%20of%20Things%20(IIoT)%20is%20the%20collection%20of,the%20internet%20to%20industrial%20applications.) (IIoT) for implementing a real-time machine monitoring framework on a machine.*

To effectively implement AI and ML into the industrial scene, collecting and analyzing data is essential for creating accurate and efficient models. The [Internet of Things (IoT)](https://www.oracle.com/internet-of-things/what-is-iot/) has become increasingly important in this field, as IoT devices can connect and transfer data over the internet. For industrial purposes, IIoT encompasses a multitude of sensors and instruments that can be used to collect significant data about machine operation. Some primary data collection fields on machines are electrical consumption, motion/vibration, environment, sound, and vision. This collected data can then be used to train an ML model to track or make decisions based on a machine's operation state, the type of operation that a machine is running, abnormal behavior of the machine, or other parameters. 

With an ML model created, optimizing the speed at which the model can make decisions is crucial. Traditional ML methods rely on cloud computing, which incorporates multiple aspects that can slow decision-making, such as increased bandwidth, power consumption, and latency. [Edge computing](https://www.ibm.com/topics/edge-computing) is an effective solution as it prioritizes computing that performs within short proximity to the target device. In the case of IIoT, this means incorporating edge computing devices as close to the machine as possible.

<img width="600" alt="Screenshot 2024-07-29 at 6 59 20 PM" src="https://github.com/user-attachments/assets/b1fe2163-dd5d-4169-ab72-4149245bf94f"> <br>

*Defined objectives for the project.*

The Purdue SURF Project revolves around the case study of implementing ***real-time multi-sensor machine monitoring of operation state and condition prediction*** on a plasma etcher machine within the Semiconductor Cleanroom at Purdue University's Birck Nanotechnology Center (BNC). The machine has multiple components contributing to the overall current consumption: the main chamber, loading chamber, chiller, and turbo pump (high vacuum). There is also a gas pipeline, vacuum pump (low vacuum), and control PC, but these components do not significantly contribute to the measured current consumption. When not in operation, the chiller and turbo pump periodically operate to maintain a constant temperature and pressure within the chamber.

Using four (4) IoT current sensors connected through the IO-Link protocol, data was collected on the machine's three active wires and neutral wire over a month. This data was then cleaned and pattern-matched with time-series data to create an ML algorithm based on the periodic trend of the machine's idle state and the magnitude increase/decrease in current data observed when the machine operates a recipe. This model was then implemented onto an edge computing device to track machine current and power usage information and execute the three steps of the model: 1) accessing the machine state, 2) tracking the "recipe" (operation) executed, and 3) detecting anomalies in the machine's behavior.





<br>

## **2)  METHODOLOGY**

<img width="600" alt="Proposed Methodology Pipeline" src="https://github.com/cjmason375/AI-in-Manuf-SURF-2024/assets/107148984/9b08e460-c3d7-4495-80a6-98e8302898ff">
<br>

*This 3-step ML framework was formed based on background readings and previous work of the Purdue team.*

### ***2.1) Data Collection*** <br>

<img width="600" alt="Screenshot 2024-07-29 at 7 04 29 PM" src="https://github.com/user-attachments/assets/3746d4d8-72df-4cce-8bf3-dd022d75c779">

*Overview of setup for data collection from BNC plasma etching machine*

Before the SURF project began, BNC staff installed four ***ifm*** current transformer (CT) sensors in the circuit breaker box to monitor and collect current consumption data on the Plasma-Therm Apex machine's *3-phase, 4-wire 208 Volt Wye (Y) Configuration electric power plug*, which includes three active wires and one neutral wire.

<img width="600" alt="Screenshot 2024-07-03 at 4 18 25 PM" src="https://github.com/cjmason375/AI-in-Manuf-SURF-2024/assets/107148984/b7e601fe-6f16-439f-ade8-159db856c784">

*Detailed diagram view of 3-phase, 4-wire setup of plasma etching machine.*

A laptop computer was installed near the breaker box, and the sensors were connected to the laptop through an ifm IO-Link Master and the IO-Link network communications protocol for measuring current using Analog-to-Digital Conversion (ADC). This laptop will not only serve as the edge computer for the project, but can also be remotely accessed for data collection as the Cleanroom requires strict Personal Protective Equipment guidelines and is not easily accessible.

After the sensors were installed, the plasma etcher machine continued to be operated as usual by the staff within BNC's Cleanroom. The laptop continuously collected current data from May 16, 2024, to June 14, 2024, for the three-phase wires (named "Phase A," "Phase B," and "Phase C") and a neutral wire. The control PC connected to the plasma etching machine also kept track of the machine operation status log, which will be used to pattern-match with the current data from the time series and verify operation start times with the collected current data.

#### ***Real-world installation images:***

<img width="600" alt="Screenshot 2024-07-29 at 7 53 34 PM" src="https://github.com/user-attachments/assets/650dcfb5-7e55-4696-96a1-5a9a0edd1d6a">

*Labeled images of significant data collection components.*



### *2.2) Database & Visualization:* cleaning, organizing, and visualizing data <br>

#### *2.2.1) Extracting raw data* <br>

The "*moneo*" software served as an application software produced by ifm that directly integrated with the ifm sensors and visualized the collected current data. 

<img width="600" alt="Screenshot of Moneo data" src="https://github.com/cjmason375/AI-in-Manuf-SURF-2024/assets/107148984/76aedc9c-b18c-4fd1-b384-63099893c345"> <br>
*Snippet of moeno visualization graph for all four wires.*

Current consumption data for the three phases and neutral wire was **collected every second (1-second intervals) over the month-long span**. However, *moneo* displays data points averaged from 10-20 minutes of data collection, which the team determined would not be sufficient for research purposes or creating the most accurate Machine Learning model as small changes in the data would not be accurately represented. Therefore, my mentor extracted raw data from the ***InfluxDB*** database without the post-processing averaging that *moneo* performed.

Extracting the data for each phase resulted in a database with 2,699,013 data points for each of the four sensors - Phases A, B, C, and Neutral.

#### *2.2.2) Formatting current data* <br>

Cleaning and organizing data was essential to analyzing and visualizing the current data. Below is a screenshot of the original data collected in a comma-separated value (CSV) file.

<img width="600" alt="Screenshot 2024-07-04 at 1 23 38 AM" src="https://github.com/cjmason375/AI-in-Manuf-SURF-2024/assets/107148984/80b5a857-9a31-4ccc-bf58-11c8c1ce764c"> <br>
*Snippet of original exported Phase A current data*

There were two significant issues with the raw current data that prevented immediate analysis of the current data:

  1. **Timestamp formatting errors**: The timezone needed to be converted from Coordinated Universal Time (UTC) to Eastern Standard Time (EST), needed the "T" and "Z" characters removed from the timestamps, and required the inclusion of microseconds into each timestamp to ensure standardized data points.
  2. **Conversion of ADC values**: The original current values, listed under the "value" column, were measured from the current transformers, but they were not actual current values. Therefore, conversion was needed to change the measured ADC values to actual values, measured in Amps. The necessary equation was determined to be:

$$\scriptstyle Amps(A)\ = \frac{25}{8}\ \times\ (x-4)$$

***Python Script to convert timestamps and ADC current values***: [**raw_format.py**](https://github.com/cjmason375/AI-in-Manuf-SURF-2024/blob/main/raw_format.py)


#### *2.2.2) Merging current data* <br>

After initial processing, timestamps were aligned for all collected data, and current consumption values for each phase were combined into a central CSV file to be used as the project's primary time-series current value database. My mentor also calculated the accumulated time since the beginning of data collection (*"accum_time"*) and the time since the last recording (*"time_diff"*). Other collected data, such as "name," "max," "min," and "psid," were excluded from the merged file as they were deemed unnecessary for further data analytics.

<img width="600" alt="Screenshot 2024-07-04 at 6 24 29 PM" src="https://github.com/cjmason375/AI-in-Manuf-SURF-2024/assets/107148984/01d4cc9b-7b2d-494c-b34c-7b606e6b7db2">

***[Merged post-processing database for current and time data](https://app.box.com/s/krpmk6wtmzolxtw43c7wiemmswiylmyj)***

*Snippet of final merged current data CSV file for all four wires.*



#### *2.2.3) Adjusting operation status log* <br>

The operation status log was collected on the Control PC connected to the plasma etching machine. It provided information on the machine's operation start times, operation status, operating recipes, and users. However, the PC lacked a built-in functionality to export collected status data to a CSV file, so an Excel file was manually created based on photos of the operation status log.

The Control PC was discovered to be offset by 25 minutes and 57 seconds from the correct time, so all original time values were adjusted to add that difference.

<img width="600" alt="Screenshot 2024-07-29 at 8 16 17 PM" src="https://github.com/user-attachments/assets/3e900513-afac-4fec-b0b2-aa6e4c63e6af">

*Snippet of adjusted status log data.*



#### *2.2.4) Analyzing operation status log* <br>

With the operation status log formatted and processed, analysis was performed on the operation status log to determine the most common recipes, the total number of unique recipes, and the total occurrence number of each status. This analysis was performed by sorting in Excel. Results of the top most common recipes and all other data are shown below:

<img width="600" alt="Screenshot 2024-07-05 at 8 19 46 AM" src="https://github.com/cjmason375/AI-in-Manuf-SURF-2024/assets/107148984/0384eb48-768c-4165-8fa5-5f651c780ae8">

*Snippet displaying total recipes, total occurrences, total occurrences by status, and the most often occurring recipes.*

After discussion with a manager of the Cleanroom and the plasma machine, the status color of each recipe was determined to relate to the following insights:

<img width="600" alt="Screenshot 2024-07-29 at 8 34 20 PM" src="https://github.com/user-attachments/assets/4abf24f4-fe1f-4e8d-9ff0-9016d1abddb2">

Later, the team decided to conduct further analytics, seeking to learn more about each of the unique recipes. Therefore, the following information was found: the number of red, yellow, and green status occurrences for each recipe; the success rate, based on the number of green occurrences divided by the number of total occurrences (per recipe); and the longest and shortest instance for each recipe.

As we sought not to analyze "bad" data, we excluded yellow and red instances from the success rate and longest/shortest instance calculations. Recipes with only one (1) occurrence had that single occurrence labeled as the "longest instance" and "n/a" for the "shortest instance".

<img width="800" alt="Screenshot 2024-07-29 at 8 37 16 PM" src="https://github.com/user-attachments/assets/5e24c337-0f2a-4571-add8-32126268dee5"> <br>
*Snippet of further calculated analytics on Operation Status Log.*



#### *2.2.5) Calculating total power consumption from current data* <br>

A primary project goal is to give operators and administration insight into the plasma etcher's operation information, so the team decided to calculate the machine's power consumption values.

As current and power are directly proportional and closely related, the power consumption could be calculated from the collected current data. As we could not determine the active or reactive power in our system with the provided information, the power consumption values for each wire was based on ***apparent power values*** through the following equation:

$$\scriptstyle Apparent Power (VA)\ = \scriptstyle line voltage (V)\ \times\ \scriptstyle line current (A)\$$

<br>

$$\scriptstyle Apparent Power (VA)\ = \scriptstyle  120 V\ \times\ \scriptstyle current (A)\$$

The total power consumption was also calculated by adding each of the phases together.

<img width="600" alt="Screenshot 2024-07-29 at 9 03 59 PM" src="https://github.com/user-attachments/assets/009fa568-aa82-49c0-a5a2-cf3ff3900432">



#### *2.2.6) Pattern-matching current data with operation status log* <br>

By pattern-matching the start times of operations from the status log to the post-processed current data, the team aimed to verify that the increases in magnitude in the current data correlated to operations being performed on the plasma etcher machine. This would also verify that the general periodic nature of the current data correlated to an idle state within the machine.

A MATLAB script was written to read and plot both sets of processed data. The current data was to be plotted as four seperate line graphs, each with a different color and line-style to represent each phase of current data. The status log data was to be plotted as vertical color-coded lines with the unique recipe name attached, as to represent the beginning of recipe and its associated status.

***[MATLAB Script to plot current and status log data](https://github.com/cjmason375/AI-in-Manuf-SURF-2024/blob/main/MultiPhase_Graph.m)*** (*MultiPhase_Graph.m*)

<img width="1136" alt="Screenshot 2024-07-05 at 8 37 54 AM" src="https://github.com/cjmason375/AI-in-Manuf-SURF-2024/assets/107148984/c3e0831c-a612-4bd6-a267-2e84820fc472">

*MATLAB graph snippet, displaying operations from June 5, 2024*









### *2.3) Machine Learning:* training AI and ML model, implementing to edge computer, and real-time recognition  <br>


