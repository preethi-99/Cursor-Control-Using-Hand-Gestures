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
```
## **Execution**
```bash
🛠 Install dependencies
🎥 Run the script to start gesture-based cursor control
🖱 Use hand gestures to control the cursor
🏁 Exit the program with a key press
```
## **Results**
```bash
✅ CNN Accuracy: 84% (test dataset)
🎯 MediaPipe Integration: Improved real-time performance
🖱 Gesture-based cursor control successfully implemented
```

## **Authors**
```bash
👤 Preethi Ranganathan - prangana@gmu.edu
👤 Swapneel Suhas Vaidya - svaidya4@gmu.edu
👤 Gagandeep Patil - gpatil2@gmu.edu
```
