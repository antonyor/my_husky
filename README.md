# my_husky  
Install on new laptop:   
Make sure you have ros installed correctly and have created a catkin workspace  
In src  
$ git clone https://github.com/antonyor/my_husky  
$ cd my_husky  
$ mv * ..  
$ rm -r my_husky  
$ sudo apt install ros-noetic-husky-navigation  
$ sudo apt install ros-noetic-husky-gazebo  
$ sudo apt install ros noetic-husky-viz  
   
The pi:  
Make sure you have ros installed correctly and have created a catkin workspace  
in src  
$ git clone https://github.com/husky/husky  
$ git clone https://github.com/husky/husky_robot   
Follow the tutorial to install the hokuyo node: http://wiki.ros.org/hokuyo_node/Tutorials/UsingTheHokuyoNode   
   
The network and environment variables are configured to my hotspot.  
If you’re using a different hotspot you’ll need to connect the raspberry pi wifi to it.  
On the raspberry pi use a text editor to edit the ~/.bashrc file and add these lines to the end  
$ vim ~/.bashrc  

export ROS_MASTER_URI=http://x.x.x.x:11311  
export ROS_IP=y.y.y.y    

where x.x.x.x is the ip address of the device running roscore  
And y.y.y.y is the ip address of the raspberry pi  
  
On the computer do the same  
$ vim ~/.bashrc  
  
export ROS_MASTER_URI=http://x.x.x.x:11311  
export ROS_IP=z.z.z.z  
where z.z.z.z is the ip address of the computer and x.x.x.x is the same ip address of line added in the pi’s bashrc script.  

It does not matter which device is running roscore. Just ensure that it matches the ip of the ROS_MASTER_URI variable and that the ROS_IP variables are set to each respective device’s ip. Also make sure you run roscore on the proper device before you start anything else  
  
  
Start:  
Connect computer to the hotspot  
Run   $ roscore   on  the computer  
Ssh into raspberry pi:   
$ ssh guest@172.20.10.11  
  Password: guest  
On the pi run:  
$ roslaunch husky_base startup.launch   
On the computer:  
For joystick control:   
$ roslaunch husky_control teleop.launch  
Hold the 5 button on the front of the controller and use the left joystick to move. Holding the 6 button instead will make the husky move faster  
For navigation and mapping:   
$ roslaunch husky_navigation setup.launch  
$ roslaunch husky_viz view_robot.launch  
To set a nav goal click the 2D nav goal button and click on a area in the map  
  
  
Common errors:   
Ensure that permissions are granted for the inputs    
   $ sudo chmod 777 ttyUSB0    
Install missing dependencies    
Ensure the serial cable is connected properly  
ssh: connect to host 172.20.10.11 port 22: No route to host  
  Turn off wifi on computer and turn back on  
  Try again  
Comm light is yellow  
  Turn the key  
  Make sure the e stop is off  
