# ***"Real-time manufacturing machine monitoring in edge analytics using electrical current consumption: Case study of plasma etcher operation and condition prediction"***

Technical Summary of work performed by Everett "CJ" Mason, Jr. at Purdue University's 2024 Summer Undergraduate Research Fellowship (SURF). <br> <br>
Feel free to contact me at *jemason@purdue.edu* or *everettmasonjr23@gmail.com*

View [abstract](https://github.com/cjmason375/AI-in-Manuf-SURF-2024/blob/main/Abstract.md) here.


<br>

## INTRODUCTION/BACKGROUND

#### *From Everett's [Annotated Literature Review](https://github.com/cjmason375/AI-in-Manuf-SURF-2024/blob/main/Annotated%20Literature%20Review):* <br>

*"The NSF AI in Manufacturing project seeks to innovate standard industrial processes by incorporating emerging Machine Learning (ML) and Artificial Intelligence (AI) practices for smart detection. Within this multi-university project, my team is focusing on the use of TinyML in the [Industrial Internet of Things](https://www.iberdrola.com/innovation/what-is-iiot#:~:text=The%20Industrial%20Internet%20of%20Things%20(IIoT)%20is%20the%20collection%20of,the%20internet%20to%20industrial%20applications.) (IIoT) and using multi-sensor analysis on machines for predictive maintenance and productivity monitoring."*

[Industry 4.0](https://www.ibm.com/topics/industry-4-0) is an ongoing shift for factories towards utilizing smart manufacturing means in modern manufacturing processes. This digitalization of the industrial world uses Artificial Intelligence (AI) and Machine Learning (ML) for automated real-time decision-making, optimizing productivity means, and reducing production costs. The [Internet of Things (IoT)](https://www.oracle.com/internet-of-things/what-is-iot/) has become increasingly important in this field, as IoT devices can connect and transfer data over the internet.

To effectively implement AI and ML into the industrial scene, collecting and analyzing data is essential for creating accurate and efficient models. For industrial purposes, IIoT encompasses a multitude of sensors and instruments that can be used to collect significant data about machine operation. Some primary data collection fields on machines are electrical consumption, motion/vibration, environment, sound, and vision. This collected data can then be used to train an ML model to track or make decisions based on a machine's operation state, the type of operation that a machine is running, abnormal behavior of the machine, or other parameters. 

With an ML model created, optimizing the speed at which the model can make decisions is crucial. Traditional ML methods rely on cloud computing, which incorporates multiple aspects that can slow decision-making, such as increased bandwidth, power consumption, and latency. [Edge computing](https://www.ibm.com/topics/edge-computing) is an effective solution as it prioritizes computing that performs within short proximity to the target device. In the case of IIoT, this means incorporating edge computing devices as close to the machine as possible.

The Purdue SURF Project revolves around the case study of implementing a ***multi-sensor analysis Machine Learning model*** on a plasma etcher machine at Purdue University's Birck Nanotechnology Center. Using (four) IoT current sensors connected through the IO-Link protocol, data was collected on the machine's three active wires and neutral wire over a month. This data was then cleaned and pattern-matched with time-series data to create an ML algorithm based on the periodic trend of the machine's idle state and the magnitude increase in current data observed when the machine actively performs a recipe. This model will then be implemented onto an edge computing device to track electrical usage and access the three steps of the model: 1) accessing the machine state, 2) tracking the "recipe" (operation) executed, and 3) detecting anomalies in the machine's behavior.


<br>

## METHODS
