# Intorduction
This deep learning project is a first part of application, which can make the characters of balloons in Manga become big or small automatically when people read Manga by phone. In order to implement the application, we plan to use a deep learning model to recognize the parts in Manga like balloons, face and so on. We chosed Manga109 as the dataset and Yolov3 as the deep learning model.

### Yolov3
A Keras implementation of YOLOv3 (Tensorflow backend) inspired by [allanzelener/YAD2K.](https://github.com/allanzelener/YAD2K)

### Manga109
This data set (hereafter referred to as [Manga109](http://www.manga109.org/en/index.html)) has been compiled by the Aizawa Yamasaki Laboratory, Department of Information and Communication Engineering, the Graduate School of Information Science and Technology, the University of Tokyo. The compilation is intended for use in academic research on the media processing of Japanese manga. Manga109 is composed of 109 manga volumes drawn by professional manga artists in Japan.

# Quick Start
1. Change the path in Detect.py(for single image) or Test_in_batches.py(for batches)  
2. Run Detect.py or Test_in_batches.py
  
# Training
1. Generate your own annotation file and class names file.  
   One row for one image;  
   Row format: image_file_path box1 box2 ... boxN;  
   Box format: x_min,y_min,x_max,y_max,class_id (no space).  

2. Use convert.py to convert model
   The file model_data/yolo_weights.h5 is used to load pretrained weights.

3. Modify train.py and start training.  
   python train.py  
   Use your trained weights or checkpoint weights with command line option --model model_file when using yolo_video.py Remember to modify      class path or anchor path, with --classes class_file and --anchors anchor_file.
