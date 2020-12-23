# OpenCV Sailing utilities

Build a classifier that allows you to track sailing boat in realtime, and estimates:
- wind direction respect to the wind
- which sails are raised
- distance from the observer
- boat by night lights

It also detect buoys and other sea stuff.

This software will offer a simple API for using the classifier.


## Download data and create the classifier

```
# Download dataset from kaggle
sailingcv-download

# Create the classifier
sailingcv-create
```