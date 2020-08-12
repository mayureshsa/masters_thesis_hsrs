# Humanoid Robot Handling Hand -Signs Recognition
Masters Thesis, Mayuresh Amberkar, August 2020.

------------
## Abstract
*Recent advancements in human-robot interaction have led to tremendous improvement for humanoid robots but still lacks social acceptance among people. Though verbal communication is the primary means of human-robot interaction, non-verbal communication that is proven to be an integral part of the human interactions is not widely used in humanoid robots. This thesis aims to achieve human-robot interaction via non-verbal communication, especially hand-signs. It presents a prototype system that simulates hand-signs recognition in the NAO humanoid robot, and further an online questionnaire is used to examine peoples opinion on the use of non-verbal communication to interact with a humanoid robot. The positive results indicate a willingness to use non-verbal communication as a means to communicate with humanoid robots, thus encouraging robot designers to use non-verbal communications for enhancing human-robot interaction.*
## Problem
With the rapid developments in the field of humanoid robots, robot designers are always finding different ways to enhance Human-Robot Interaction (HRI) and improve its acceptance in the real world. 

## Purpose
The purpose of this thesis is to explore the use of non-verbal communication to achieve HRI via non-verbal communication in humanoid robots, especially using hand-signs. With some extensions to the developed prototype in this thesis, it can serve as an application to aid people with hearing disabilities.

## Goals

### Development Goal
Develop a system that recognizes hand-signs shown to a humanoid robot from an input image using state-of-the-art deep learning techniques. The system consists of three components:
#### 1. Humanoid Robot
Develop a humanoid robot serving as a tool to communicate and establish the HRI with an user. This thesis makes use of NAO humanoid robot.
#### 2. Hand-Signs Recognition Component (HSRC)
Develop a component that recognizes hand-signs via an input image. Essentially, HSRC produces different deep learning models using Convolution Neural Networks (CNN) trained from scratch and also using transfer learning.
#### 3. Integration Layer
Integrate the NAO humanoid robot and the HSRC handling all the requried preprocessing, postprocessing, and servicing operations.
### Research Goal
Assess peoples opinion on using non-verbal communication  to interact with a humanoid robot via online questionnaires.


## Major Contributions
1. A prototype that enables the humanoid robot to handle hand-signs recognition.
2. Using the Hand-Signs Recognition Component as a standalone application offering immediate solution to people with speech impairments.
3. Use of a reformed data collection technique of online questionnaires.
4. Evaluation results highlighting peoples willingness to accept humanoid robots and use of non-verbal communication for human-robot interactions.
