# **Gesture-Based Cursor Control**

## **Overview**
This project enables **touchless cursor control** using **hand gestures**, leveraging **CNN for gesture recognition** and **MediaPipe for real-time tracking**.

---

## **Approach**
### **1. CNN-Based Gesture Recognition**
- 📷 **Dataset**: 21,600 hand gesture images.
- 🏷️ **Model**: 4 Conv2D layers, Batch Normalization, Max Pooling, Dropout.
- 📊 **Accuracy**: **84% (test dataset)**.
- ❗ **Issue**: Poor real-time detection.

### **2. MediaPipe-Based Hand Tracking**
- 🖐 **Real-time hand tracking & landmark detection**.
- 🖱 **Maps hand movements to cursor actions**.
- 🔄 **Smooth motion for better user experience**.

---

## **Hand Gesture to Mouse Action Mapping**
| Gesture | Action |
|---------|--------|
| Index Finger Up | Move Cursor |
| Thumb & Index Touch | Left Click |
| Index & Middle Touch | Right Click |

---

## **Installation**
Install required dependencies:
```bash
pip install opencv-python mediapipe autopy
