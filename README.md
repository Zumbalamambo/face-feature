# ros-face-features

### How to run gender feature:

`make train-gender`

`make predict-gender`

### How to run age feature:

`make train-age`

`make predict-age`

### Live face recognition:

`make face`

### ROS live image:

First of all , initilize roscore and ROS usb camera.

```bash
$ roscore &
$ rosparam set usb_cam/pixel_format yuyv #(optional) if requirement
$ rosrun usb_cam usb_cam_node &
```

#### For live face-recognition:

`make ros-recognizer`

#### For live face-age-predictor

`make ros-age`

#### For live face-gender-predictor

`make ros-gender`
 
#License

Under GNU-GPL3

By [ahmdrz](https://github.com/ahmdrz)