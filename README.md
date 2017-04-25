# ros-face-features

## Descritpion

This repository is simple way to train naural network and use predictor to detect age and gender for Robocup @Home robots

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
 
## License

#### Persian notes:

>تمام حقوق اعطا شده بنا بر این مجوز به عنوان حق‌تالیف نرم‌افزار اعطا شده‌اند و در صورتی که شرایط توضیح داده‌شده حفظ گردند غیر قابل ابطال می‌باشند. این پروانه به طور مشخص تاکید بر حق نامحدود شما برای اجرای برنامه‌ی تغییر نیافته دارد. خروجی یک کار تحت این پروانه فقط در صورتی تحت این پروانه خواهد بود که محتوای آن شامل کاری باشد که آن نیز تحت پروانه باشد. این پروانه حقوق شما برای استفاده عادی یا مشابه آن به گونه‌ای که در قانون حق‌تالیف  به آن اشاره شده است به رسمیت می‌شناسد.

> تا وقتی که پروانه‌ی شما به نحوی شما را باز دارد می‌توانید کارهای مشمول این پروانه را برای اجرا بسازید، اجرا نمایید و یا بدون رساندن تکثیر نمایید. به شرطی که قوانین این پروانه به طور کامل رعایت شود شما می‌توانید کار شامل این پروانه را  با اینکه شما صاحب پروانه‌ی آن نیستید تکثیر نموده و در اختیار دیگران قرار دهید تا تغییراتی را مختص شما روی برنامه انجام دهند و یا امکاناتی برای اجرای آن در اختیار شما قرار بدهند. اشخاصی که کار شامل پروانه را برای شما اجرا می‌کنند باید به طور خاص کار را به وکالت شما، تحت کنترل شما و با نظارت شما انجام دهند به نحوی که امکان نسخه‌برداری از کاری که در اختیار شما قرار دارد را جز برای رابطه‌ی کاری شما نداشته باشند.

> تکثیر تحت هر شرایط دیگری فقط بنا به ضوابط و قوانینی مجاز است که در زیر به آنها اشاره شده است. صدور پروانه‌هایی جزیی مجاز نیست و بند 10 این متن نیز آنها را غیرلازم می‌سازد.

[بیشتر بخوانید](https://lists.gnu.org/archive/html/www-fa-general/2013-02/msg00001.html)

Under GNU-GPL3

By [ahmdrz](https://github.com/ahmdrz)
