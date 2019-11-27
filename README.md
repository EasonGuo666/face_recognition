# face_recognition

A basic face recognition system based on tensorflow and CNN.

### 1 使用方法:

* <br> **1.获取人脸数据:**
    <br>获取自己人脸数据：直接运行get_my_faces.py打开摄像头拍摄，保存1000张图片之后，程序自动关闭
    <br>处理过后自己的人脸数据集会放在/my_faces/目录下
    <br>获取别人人脸数据：把别人的脸照片放在input_image/目录下，运行set_other_faces.py，
    <br>处理过后别人的脸部图片会被保存在other_faces/目录下

* <br> **2.训练模型**
    <br>运行train_faces.py，接下来就是等待。。。。。可以去刷会知乎，哔站，
    <br>/tmp/目录下保存了训练好的参数文件，文件名是`events.out.tfevents.1574744828.DESKTOP-VKL7EKQ`
    <br>train_faces.py的相对路径下也保存了一些参数文件，他们需要放在一起用（下一步讲怎么用）

* <br> **3.调用保存好的模型，识别人脸**
    <br>把/tmp/目录下任意一个文件移动到is_my_face.py相对路径下，运行is_my_face.py，程序会打开摄像头
    <br>把自己的脸怼到摄像头上，就能看到自己的脸被蓝色方框框选.
    <br>如果你和我用的一样都是Anaconda Spyder的话，会看到Ipython控制台输出Is this my face? True
