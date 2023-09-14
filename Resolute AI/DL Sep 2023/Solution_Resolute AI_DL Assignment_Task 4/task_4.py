import cv2
import numpy as np
from sklearn.ensemble import IsolationForest

def detect_and_localize_defects(image_path):

    fabric = cv2.imread(image_path)

    grayscale_image = cv2.cvtColor(fabric, cv2.COLOR_BGR2GRAY)

    blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)

    flattened_image = blurred_image.reshape((-1, 1))

    isolation_forest = IsolationForest(contamination=0.03, random_state=42)
    isolation_forest.fit(flattened_image)

    anomaly = isolation_forest.predict(flattened_image)
    anomaly = anomaly.reshape(blurred_image.shape)

    threshold = -0.5
    defect = anomaly < threshold

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    defect = cv2.morphologyEx(
        defect.astype(np.uint8), cv2.MORPH_CLOSE, kernel)

    masked_fabric_defect = fabric.copy()
    masked_fabric_defect[defect == 0] = [0, 0, 255]

    return masked_fabric_defect


image_path = input("Enter Fabric image path: ")
result_image = detect_and_localize_defects(image_path)

image_name = image_path.split('/')[-1]
cv2.imwrite('./Masked Fabric Defects/'+image_name, result_image)