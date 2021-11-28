# GankenKun_pybullet

[<img src="http://img.youtube.com/vi/W16Qmjq5a-A/0.jpg" width="720">](http://www.youtube.com/watch?v=W16Qmjq5a-A)

### Video

Simulation on PyBullet
http://www.youtube.com/watch?v=W16Qmjq5a-A

### Preparation of the development environment

Ubuntu2004  
```
sudo apt install python3-pip
pip install pybullet
pip install numpy
pip install control
```

### main program

- GankenKun_velocity_control.py

Walking control with torso velocity input

### library for GankenKun

GankenKun/  

- kinematics.py  
Calculating the inverse kinematics based on the analytical solution  
(foot position -> joint angles)  

- foot_step_planner.py  
Calculating the footsteps from the goal position  

- foot_step_planner_v2.py  
Calculating the footsteps and zmpref from the given velocity command and initial states  

- preview_control_v2.py  
Generating the trajectory of the center of mass from the zmpref based on the preview controller. Refer to [yiqin/Preview-Control-Motion-Planning-in-Humanoid](https://github.com/yiqin/Preview-Control-Motion-Planning-in-Humanoid/blob/master/ZmpPreview.py)

- walking_v2.py  
Main walking engine and controller from given input and the initial state  

### What is GankenKun

GankenKun is an open platform humanoid robot developed by CIT Brains (Chiba Institute of Technology).  
The robot had won the prize in RoboCup.  

https://github.com/citbrains/OpenPlatform  
https://github.com/citbrains/OpenPlatform_ver3_0 (now developing ver.4)  

### other programs (developed for understanding pybullet)  

- display.py  
Displaying the humanoid robot GankenKun  

- stretch.py  
Controlling the positions of joints  

- camera.py  
Capturing the camera image  

- Walk.py  
Checking to be able to walk (Just up and down each foot)  

- inv_kine.py  
Solving the inverse kinematics  

- display_COG.py  
Calculating the centor of gravity  

- jacobian_test.py  
Calculating the Jacobian  

- COG_jacobian.py  
Calculating the centor of gravity Jacobian  

### ZMP Walking Using Preview Control

References
> - Maximo, M. R. (2015). Omnidirectional ZMP-Based Walking for a Humanoid Robot. Master's thesis, Aeronautics Institute of Technology.
> - Kajita, S., Hirukawa, H., Harada, K., & Yokoi, K. (2016). Introduction to Humanoid Robotics (1st ed). Springer Publishing Company, Incorporated.
> - Kajita, S., Kanehiro, F., Kaneko, K., Fujiwara, K., Harada, K., Yokoi, K., & Hirukawa, H. (2003). Biped walking pattern generation by using preview control of zero-moment point. 2003 IEEE International Conference on Robotics and Automation (Cat. No.03CH37422).
> - Park, J., & Youm, Y. (2007). General ZMP Preview Control for Bipedal Walking. Proceedings 2007 IEEE International Conference on Robotics and Automation.

### Walk Pattern 

```
python GankenKun/foot_step_planner_v2.py 
```

### Preview Control 

```
python GankenKun/preview_control_v2.py 
```

![](figures/zmp_walk_pattern.png)

### Walk simulation

```
python GankenKun_velocity_control.py
```

### For more detail  
http://www.cit-brains.net/  
