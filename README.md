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

```bash
$ roscore &
$ rosparam set usb_cam/pixel_format yuyv #(optional) if requirement
$ rosrun usb_cam usb_cam_node &
$ make ros-gender
```
