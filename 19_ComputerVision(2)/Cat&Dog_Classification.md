## Cat&Dog

### When training 10000 images of data, the prediction results of DT, KNN and SGD are as follows:

|### DT|### KNN|### SGD|
|:--:|:--:|:--:|
|![16884751850951688475181624.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/16884751850951688475181624.png)|![16884750707601688475052596.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/16884750707601688475052596.png)|![16884751307571688475081858.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/16884751307571688475081858.png)|

### The accuracy is as follows:

We can see that the accuracy of the three methods is between 0.5 and 0.6, and the accuracy of DT method is higher than that of the other two methods. But none of the three methods works very well.

|Models|Acc|
|--|--|
|DT|0.5762|
|KNN|0.5736|
|SGD|0.5416|

Based on the provided performance results of the classifiers, we can draw the following analysis:

- Decision Tree (DT) classifier has an accuracy of 0.5762, slightly higher than the KNN and SGD classifiers. However, from the classification report, it can be observed that the DT classifier has a higher recall for the positive class (1) (0.67), but a lower recall for the negative class (0) (0.48). This suggests that the DT classifier performs relatively well in identifying the positive class but has some issues in identifying the negative class.
- K-Nearest Neighbors (KNN) classifier has an accuracy of 0.5736, close to the accuracy of the DT classifier. The classification report of the KNN classifier shows that its recall for the positive class (0.47) is slightly lower than that of the DT classifier, but its recall for the negative class (0.67) is slightly higher. The confusion matrix of the KNN classifier also indicates a significant number of false positives and false negatives, which may affect its performance.
- Stochastic Gradient Descent (SGD) classifier has the lowest accuracy among the three classifiers, with an accuracy of 0.5416. The classification report and confusion matrix of the SGD classifier demonstrate its poor performance in terms of recall for the positive class (0.22) and a high number of false positives and false negatives. This suggests that the SGD classifier performs relatively poorly on this dataset.

the DT classifier has a certain advantage in the recall for the positive class, while the KNN classifier has a slight advantage in the recall for the negative class. Meanwhile, the SGD classifier exhibits low recall for the positive class and overall poor performance. However, to comprehensively and accurately assess the performance of the classifiers, it is recommended to consider other metrics such as precision, F1-score, and conduct experiments like cross-validation to evaluate the robustness and stability of the classifiers on different datasets.

### When training 20000 images of data, the prediction results of DT, KNN and SGD are as follows:

|DT|KNN|SGD|
|:--:|:--:|:--:|
|![16884760907581688476073532.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/16884760907581688476073532.png)|![16884761767571688476176159.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/16884761767571688476176159.png)|![16884762027591688476202713.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/16884762027591688476202713.png)|

Based on the provided classification reports and confusion matrices, we can analyze the performance of each classifier as follows:

|Model|Accuracy|Precision (Class 0)|Recall (Class 0)|F1-score (Class 0)|Precision (Class 1)|Recall (Class 1)|F1-score (Class 1)|
|--|--|--|--|--|--|--|--|
|DT|0.5768|0.59|0.52|0.55|0.57|0.63|0.60|
|KNN|0.5802|0.56|0.70|0.63|0.61|0.46|0.52|
|SGD|0.5132|0.65|0.06|0.11|0.51|0.97|0.67|

Based on these results, we can make the following observations:

- DT and KNN have similar accuracies, with DT slightly lower at 57.68% and KNN slightly higher at 58.02%. SGD has the lowest accuracy at 51.32%.
- KNN shows a higher precision and recall for class 0 compared to DT, indicating that it performs better at correctly classifying class 0 instances. However, KNN has lower precision and recall for class 1 compared to DT.
- SGD has the highest precision for class 0 among the three classifiers but has very low recall for class 0. It also has the highest recall for class 1 but the lowest precision for class 1.
  
  <br/>

|Models|2:1|4:1|
|--|--|--|
|DT|0.5762|0.5768|
|KNN|0.5736|0.5802|
|SGD|0.5416|0.5132|

Increasing the training data does not always lead to a significant improvement in performance. Here are some possible reasons and considerations:

- Data quality: The effectiveness of adding training data is closely related to the quality of the data. If the additional data is similar to the original dataset or contains similar patterns and features, the model may not learn new information from it. Additionally, if the added data has issues such as outliers or incorrect labeling, it can negatively impact the model.
- Imbalanced data distribution: If the data distribution is imbalanced, meaning some classes have very few samples, the model may prioritize optimizing for the majority classes, resulting in lower performance for the minority classes. But we have ensured that approximately equal numbers of images have been sampled from the "Dogs" class and the "Cats" class.
- Model complexity: There is a trade-off between model complexity and the amount of training data. When the training data is limited, using overly complex models may lead to overfitting. Increasing the training data can help alleviate overfitting to some extent, but if the model is already sufficiently simple, adding more data may have limited impact on improving performance.
- Feature selection and engineering: The predictive performance of a model depends not only on the amount of data but also on the selection and engineering of features. When adding training data, it is important to ensure that the new data contains informative features and to combine appropriate feature selection and engineering methods to extract and represent these features effectively.
- Hyperparameter tuning: After expanding the training data, the model's performance may be influenced by its hyperparameters. It may be necessary to further tune the hyperparameters to fully leverage the benefits of increased training data.

In conclusion, increasing the training data does not guarantee a significant performance improvement. In addition to increasing the data, other factors such as data quality, balanced data distribution, model complexity, feature selection and engineering, and hyperparameter tuning need to be considered to comprehensively optimize the model's performance.

We can see from the competition ranking that most people choose to use CNN for image classification prediction, and facts have proved that their method is indeed effective. Through the construction of convolution layer, pooling layer and full connection layer, CNN can effectively extract features from images and perform well in tasks such as image classification, target detection and image generation. Of course, through the processing of the original data and later parameter adjustment, the score of the traditional machine learning algorithm can also be improved to a certain extent, but the traditional machine learning algorithm may still be inferior to CNN in image processing.
