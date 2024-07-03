# ***"Real-time manufacturing machine monitoring in edge analytics using electrical current consumption: Case study of plasma etcher operation and condition prediction"***

Technical Summary of work performed by Everett "CJ" Mason, Jr. at Purdue University's 2024 Summer Undergraduate Research Fellowship (SURF). <br> <br>
Feel free to contact me at *jemason@purdue.edu* or *everettmasonjr23@gmail.com*

View [abstract](https://github.com/cjmason375/AI-in-Manuf-SURF-2024/blob/main/Abstract.md) here.



<br>

## *INTRODUCTION/BACKGROUND*

#### *From Everett's [Annotated Literature Review](https://github.com/cjmason375/AI-in-Manuf-SURF-2024/blob/main/Annotated%20Literature%20Review):* <br>

*"The NSF AI in Manufacturing project seeks to innovate standard industrial processes by incorporating emerging Machine Learning (ML) and Artificial Intelligence (AI) practices for smart detection. Within this multi-university project, my team is focusing on the use of TinyML in the [Industrial Internet of Things](https://www.iberdrola.com/innovation/what-is-iiot#:~:text=The%20Industrial%20Internet%20of%20Things%20(IIoT)%20is%20the%20collection%20of,the%20internet%20to%20industrial%20applications.) (IIoT) and using multi-sensor analysis on machines for predictive maintenance and productivity monitoring."*

[Industry 4.0](https://www.ibm.com/topics/industry-4-0) is an ongoing shift for factories towards utilizing smart manufacturing means in modern manufacturing processes. Traditionally, factories operated on the standard of *[preventative maintenance](https://www.ibm.com/topics/what-is-preventive-maintenance#:~:text=Preventive%20maintenance%20is%20the%20act,fixing%20things%20before%20they%20break)*, in which regular checks would occur for maintenance tasks to prevent unexpected future failures. However, the precautionary nature of this method would result in higher costs, increased waste as tools were  replaced before reaching their full lifespan, and increased labor. Industry 4.0 sees the ***shift from preventative maintence to [predictive maintenance](https://www.ibm.com/topics/predictive-maintenance)***. This digitalization of the industrial world uses Artificial Intelligence (AI) and Machine Learning (ML) for automated real-time decision-making, optimizing productivity means, and reducing production costs. By intelligently predicting the failures of machines or tool parts, many drawbacks of preventative maintenance can be greatly reduced.

To effectively implement AI and ML into the industrial scene, collecting and analyzing data is essential for creating accurate and efficient models. The [Internet of Things (IoT)](https://www.oracle.com/internet-of-things/what-is-iot/) has become increasingly important in this field, as IoT devices can connect and transfer data over the internet. For industrial purposes, IIoT encompasses a multitude of sensors and instruments that can be used to collect significant data about machine operation. Some primary data collection fields on machines are electrical consumption, motion/vibration, environment, sound, and vision. This collected data can then be used to train an ML model to track or make decisions based on a machine's operation state, the type of operation that a machine is running, abnormal behavior of the machine, or other parameters. 

With an ML model created, optimizing the speed at which the model can make decisions is crucial. Traditional ML methods rely on cloud computing, which incorporates multiple aspects that can slow decision-making, such as increased bandwidth, power consumption, and latency. [Edge computing](https://www.ibm.com/topics/edge-computing) is an effective solution as it prioritizes computing that performs within short proximity to the target device. In the case of IIoT, this means incorporating edge computing devices as close to the machine as possible.

The Purdue SURF Project revolves around the case study of implementing a ***multi-sensor analysis Machine Learning model*** on a plasma etcher machine within the Semiconductor Cleanroom at Purdue University's Birck Nanotechnology Center (BNC). The machine has multiple components that contribute to the overall current consumption: the main chamber, loading chamber, chiller, and turbo pump (high vacuum). There is also a gas pipline, vacuum pump (low vacuum), and control PC, but these components do not significantly contribute to the measured current consumption. When not in operation, the chiller and turbo pump periodically operate to maintain a constant temperature and pressure within the chamber.

Using (four) IoT current sensors connected through the IO-Link protocol, data was collected on the machine's three active wires and neutral wire over a month. This data was then cleaned and pattern-matched with time-series data to create an ML algorithm based on the periodic trend of the machine's idle state and the magnitude increase in current data observed when the machine oeprates a recipe. This model will then be implemented onto an edge computing device to track electrical usage and execute the three steps of the model: 1) accessing the machine state, 2) tracking the "recipe" (operation) executed, and 3) detecting anomalies in the machine's behavior.



<br>

## *METHODS*

<img width="1164" alt="Screenshot 2024-07-03 at 4 02 21 PM" src="https://github.com/cjmason375/AI-in-Manuf-SURF-2024/assets/107148984/9b08e460-c3d7-4495-80a6-98e8302898ff">


### *1) Data Collection:* IoT sensor connectivity and communication <br>

Before the SURF project began, BNC staff installed four ***ifm*** current transformer (CT) sensors in the circuit breaker box to monitor and collect current consumption data on the plasma etcher machine's 3-phase electric power plug, which includes three active wires and one neutral wire. A laptop computer was installed near the breaker box, and the sensors were connected to the laptop through an ifm IO-Link Master and the IO-Link network communications protocol for measuring current using Analog-to-Digital Conversion (ADC). This laptop will not only serve as the edge computer for the project, but is also able to be remotely accessed for data collection as the Cleanroom requires strict Personal Protective Equipment guidelines and is not easily accessible. The setup is depicted in the diagram below:

<img width="734" alt="Screenshot 2024-07-03 at 3 59 49 PM" src="https://github.com/cjmason375/AI-in-Manuf-SURF-2024/assets/107148984/1e7cef48-6291-40d4-ae2a-cfa9828f2664">

After installation of sensors, the plasma etcher machine continued to be operated as normal by the staff within BNC's Cleanroom. The laptop continously collected current data from the span of May 16, 2024 to June 14, 2024 for the three phase wires (named "Phase A", "Phase B", and "Phase C") and neutral wire.


Moneo software installed on the computer continued to collect 



### *2) Database & Visualization:* cleaning, organizing, and visualizing data <br>

### *3) Machine Learning:* training AI and ML model, implementing to edge computer, and real-time recognition  <br>


