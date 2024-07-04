# ***"Real-time manufacturing machine monitoring in edge analytics using electrical current consumption: Case study of plasma etcher operation and condition prediction"***

Technical Summary of work performed by Everett "CJ" Mason, Jr. at Purdue University's 2024 Summer Undergraduate Research Fellowship (SURF). <br> <br>
Feel free to contact me at *jemason@purdue.edu* or *everettmasonjr23@gmail.com*

View [abstract](https://github.com/cjmason375/AI-in-Manuf-SURF-2024/blob/main/Abstract.md) here.



<br>

## *INTRODUCTION/BACKGROUND*

#### *From Everett's [Annotated Literature Review](https://github.com/cjmason375/AI-in-Manuf-SURF-2024/blob/main/Annotated%20Literature%20Review):* <br>

*"The NSF AI in Manufacturing project seeks to innovate standard industrial processes by incorporating emerging Machine Learning (ML) and Artificial Intelligence (AI) practices for smart detection. Within this multi-university project, my team is focusing on the use of TinyML in the [Industrial Internet of Things](https://www.iberdrola.com/innovation/what-is-iiot#:~:text=The%20Industrial%20Internet%20of%20Things%20(IIoT)%20is%20the%20collection%20of,the%20internet%20to%20industrial%20applications.) (IIoT) and using multi-sensor analysis on machines for predictive maintenance and productivity monitoring."*

[Industry 4.0](https://www.ibm.com/topics/industry-4-0) is an ongoing shift for factories towards utilizing smart manufacturing means in modern manufacturing processes. Traditionally, factories operated on the standard of *[preventative maintenance](https://www.ibm.com/topics/what-is-preventive-maintenance#:~:text=Preventive%20maintenance%20is%20the%20act,fixing%20things%20before%20they%20break)*, in which regular checks would occur for maintenance tasks to prevent unexpected future failures. However, the precautionary nature of this method would result in higher costs, increased waste as tools were  replaced before reaching their full lifespan, and increased labor. Industry 4.0 sees the ***shift from preventative maintenance to [predictive maintenance](https://www.ibm.com/topics/predictive-maintenance)***. This digitalization of the industrial world uses Artificial Intelligence (AI) and Machine Learning (ML) for automated real-time decision-making, optimizing productivity means, and reducing production costs. By intelligently predicting the failures of machines or tool parts, many drawbacks of preventative maintenance can be greatly reduced.

To effectively implement AI and ML into the industrial scene, collecting and analyzing data is essential for creating accurate and efficient models. The [Internet of Things (IoT)](https://www.oracle.com/internet-of-things/what-is-iot/) has become increasingly important in this field, as IoT devices can connect and transfer data over the internet. For industrial purposes, IIoT encompasses a multitude of sensors and instruments that can be used to collect significant data about machine operation. Some primary data collection fields on machines are electrical consumption, motion/vibration, environment, sound, and vision. This collected data can then be used to train an ML model to track or make decisions based on a machine's operation state, the type of operation that a machine is running, abnormal behavior of the machine, or other parameters. 

With an ML model created, optimizing the speed at which the model can make decisions is crucial. Traditional ML methods rely on cloud computing, which incorporates multiple aspects that can slow decision-making, such as increased bandwidth, power consumption, and latency. [Edge computing](https://www.ibm.com/topics/edge-computing) is an effective solution as it prioritizes computing that performs within short proximity to the target device. In the case of IIoT, this means incorporating edge computing devices as close to the machine as possible.

The Purdue SURF Project revolves around the case study of implementing a ***multi-sensor analysis Machine Learning model*** on a plasma etcher machine within the Semiconductor Cleanroom at Purdue University's Birck Nanotechnology Center (BNC). The machine has multiple components contributing to the overall current consumption: the main chamber, loading chamber, chiller, and turbo pump (high vacuum). There is also a gas pipeline, vacuum pump (low vacuum), and control PC, but these components do not significantly contribute to the measured current consumption. When not in operation, the chiller and turbo pump periodically operate to maintain a constant temperature and pressure within the chamber.

Using (four) IoT current sensors connected through the IO-Link protocol, data was collected on the machine's three active wires and neutral wire over a month. This data was then cleaned and pattern-matched with time-series data to create an ML algorithm based on the periodic trend of the machine's idle state and the magnitude increase in current data observed when the machine operates a recipe. This model will then be implemented onto an edge computing device to track electrical usage and execute the three steps of the model: 1) accessing the machine state, 2) tracking the "recipe" (operation) executed, and 3) detecting anomalies in the machine's behavior.



<br>

## *METHODS*

<img width="800" alt="Screenshot 2024-07-03 at 4 02 21 PM" src="https://github.com/cjmason375/AI-in-Manuf-SURF-2024/assets/107148984/9b08e460-c3d7-4495-80a6-98e8302898ff">
<br> 



### *1) Data Collection:* IoT sensor connectivity and communication <br>

Before the SURF project began, BNC staff installed four ***ifm*** current transformer (CT) sensors in the circuit breaker box to monitor and collect current consumption data on the Plasma-Therm Apex machine's 3-phase, 4-wire 208 Volt Wye (Y) Configuration electric power plug, which includes three active wires and one neutral wire.

<img width="800" alt="Screenshot 2024-07-03 at 4 18 25 PM" src="https://github.com/cjmason375/AI-in-Manuf-SURF-2024/assets/107148984/b7e601fe-6f16-439f-ade8-159db856c784">

A laptop computer was installed near the breaker box, and the sensors were connected to the laptop through an ifm IO-Link Master and the IO-Link network communications protocol for measuring current using Analog-to-Digital Conversion (ADC). This laptop will not only serve as the edge computer for the project but can also be remotely accessed for data collection as the Cleanroom requires strict Personal Protective Equipment guidelines and is not easily accessible. The setup is depicted in the diagram below:

<img width="800" alt="Screenshot 2024-07-03 at 3 59 49 PM" src="https://github.com/cjmason375/AI-in-Manuf-SURF-2024/assets/107148984/1e7cef48-6291-40d4-ae2a-cfa9828f2664">

After the sensors were installed, the plasma etcher machine continued to be operated as usual by the staff within BNC's Cleanroom. The laptop continuously collected current data from May 16, 2024, to June 14, 2024, for the three-phase wires (named "Phase A," "Phase B," and "Phase C") and a neutral wire. The control PC connected to the plasma etching machine also kept track of the machine operation status log, which will be used to pattern-match with the current data from the time series and verify operation start times with the collected current data.

#### ***Real-world installation images:***

<img width="800" alt="Screenshot 2024-07-03 at 4 20 02 PM" src="https://github.com/cjmason375/AI-in-Manuf-SURF-2024/assets/107148984/5f8430f2-01e4-4c11-995b-329ce770bd25">
<img width="800" alt="Screenshot 2024-07-03 at 4 20 25 PM" src="https://github.com/cjmason375/AI-in-Manuf-SURF-2024/assets/107148984/d41c2726-95ec-4112-9d5a-31efb3925769">



<br> 

### *2) Database & Visualization:* cleaning, organizing, and visualizing data <br>

The "*moneo*" software served as an application software produced by ifm that directly integrated with the ifm sensors and visualized the collected current data. 

![moneo](https://github.com/cjmason375/AI-in-Manuf-SURF-2024/assets/107148984/76aedc9c-b18c-4fd1-b384-63099893c345)

Data for the three phases and neutral wire was collected every second (1-second intervals) over the month-long span. However, *moneo* displays data points averaged from 10-20 minutes of data collection, which the team determined would not be sufficient for research purposes or creating the most accurate Machine Learning model. Therefore, the raw data was extracted from the ***InfluxDB*** database without the post-processing that *moneo* performed. (*insert more info please*) Extracting the data for each phase resulted in a database with 2,699,013 data points for each of the four sensors - Phases A, B, C, and Neutral.



Cleaning and organizing data was essential to analyzing and visualizing the current data. Below is a screenshot of the original data collected in a comma-separated value (CSV) file.

<img width="800" alt="Screenshot 2024-07-04 at 1 23 38 AM" src="https://github.com/cjmason375/AI-in-Manuf-SURF-2024/assets/107148984/80b5a857-9a31-4ccc-bf58-11c8c1ce764c"> <br>

There were two significant issues with the raw current data that prevented immediate analysis of the current data:

  1. **Timestamp formatting errors**: The timezone needed to be converted from Coordinated Universal Time (UTC) to Eastern Standard Time (EST), needed the "T" and "Z" characters removed from the timestamps, and required the inclusion of microseconds into each timestamp to ensure standardized data points.
  2. **Conversion of ADC values**: The original current values, listed under the "value" column, were measured from the current transformers, but they were not actual current values. Therefore, conversion was needed to change the measured ADC values to actual values, measured in Amps. The necessary equation was determined to be:

### $$\scriptstyle Amps(A)\ = \frac{25}{8}\*(x-4)$$

***[Python Script to convert timestamps and ADC current values](https://github.com/cjmason375/AI-in-Manuf-SURF-2024/blob/main/raw_format.py)***



{adjusting time format of Excel file for status log}


### *3) Machine Learning:* training AI and ML model, implementing to edge computer, and real-time recognition  <br>


