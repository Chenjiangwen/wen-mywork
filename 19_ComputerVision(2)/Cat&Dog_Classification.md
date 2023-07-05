## Cat&Dog

### When training 10000 images of data, the prediction results of DT, KNN and SGD are as follows:

|DT|KNN|SGD|
|:--:|:--:|:--:|
|![16885438805121688543879688.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/16885438805121688543879688.png)|![16885439217571688543921078.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/16885439217571688543921078.png)|![16885440107521688544009813.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/16885440107521688544009813.png)|

### The accuracy is as follows:

We can see that the accuracy of the three methods is between 0.5 and 0.6, and the accuracy of DT method is higher than that of the other two methods. But none of the three methods works very well.

|Models|Acc|
|--|--|
|DT|0.579|
|KNN|0.5992|
|SGD|0.5426|

Based on the provided performance results of the classifiers, we can draw the following analysis:

- The KNN model achieved the highest accuracy score of 0.5992, indicating that it performed better than the other two models. KNN is a non-parametric algorithm that classifies new data points based on their similarity to existing data points. It calculates the distance between the new data point and its neighbors to determine its class. In this case, the KNN algorithm was able to accurately classify the data points more effectively than DT and SGD.
- The DT model achieved an accuracy score of 0.579, making it the second-best performing model. Decision trees are a type of supervised learning algorithm that creates a tree-like model for decision-making. Each internal node represents a feature or attribute, each branch represents a decision rule, and each leaf node represents the outcome or prediction. The DT model in this case might have been relatively accurate but not as effective as the KNN model in classifying the data.
- On the other hand, the SGD model achieved the lowest accuracy score of 0.5426. SGD is an optimization algorithm commonly used in training machine learning models, particularly in linear classifiers and regressors. It updates the model's parameters using a different subset of training data in each iteration, making it more efficient for large datasets. However, in this analysis, the SGD model did not perform as well as the other two models, suggesting that it was not able to effectively learn the underlying patterns in the data.

based on the accuracy scores, the KNN model outperformed the DT and SGD models in this analysis. The KNN algorithm's ability to classify new data based on similarity to existing data points helped achieve better accuracy. However, further evaluation and analysis, such as considering other performance metrics or conducting cross-validation, may be necessary to make a more comprehensive assessment of the models' performances.

### When training 20000 images of data, the prediction results of DT, KNN and SGD are as follows:

|DT|KNN|SGD|
|:--:|:--:|:--:|
|![16885443097481688544301857.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/16885443097481688544301857.png)|![16885443574961688544356509.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/16885443574961688544356509.png)|![16885443747561688544373938.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/16885443747561688544373938.png)|

Based on the provided classification reports and confusion matrices, we can analyze the performance of each classifier as follows:


|Model|Accuracy|Precision (Class 0)|Recall (Class 0)|F1-score (Class 0)|Precision (Class 1)|Recall (Class 1)|F1-score (Class 1)|
|--|--|--|--|--|--|--|--|
|DT|0.5758|0.58|0.57|0.58|0.58|0.58|0.58|
|KNN|0.6004|0.56|0.88|0.69|0.72|0.32|0.45|
|SGD|0.5466|0.53|0.86|0.66|0.63|0.23|0.34|

Based on the analysis of the models, we can draw the following conclusions:

1. Decision Tree (DT):
   - The accuracy of the DT model is 0.5758, indicating that it correctly predicts the class labels for approximately 57.58% of the instances.
   - The precision and recall for both Class 0 and Class 1 are consistent at 0.58, suggesting that the model performs equally well in identifying both classes.
   - The F1-score, which combines precision and recall, is also 0.58 for both classes. This indicates a balanced performance in terms of precision and recall for both classes.
2. K-Nearest Neighbors (KNN):
   - The KNN model achieves an accuracy of 0.6004, implying that it predicts the class labels accurately for around 60.04% of the instances.
   - The precision for Class 0 is 0.56, which means that when the model predicts Class 0, it is correct 56% of the time. However, the precision for Class 1 is lower at 0.32, indicating more false positive predictions.
   - The recall for Class 0 is high at 0.88, suggesting that the model effectively captures most of the instances belonging to Class 0. The recall for Class 1 is 0.45, indicating a moderate ability to identify instances of Class 1.
   - The F1-score for Class 0 is 0.69, indicating a good balance between precision and recall. For Class 1, the F1-score is higher at 0.72, suggesting a better harmonic mean between precision and recall compared to Class 0.
3. Stochastic Gradient Descent (SGD):
   - The SGD model has an accuracy of 0.5466, indicating that it correctly predicts the class labels for approximately 54.66% of the instances.
   - The precision for Class 0 is 0.53, suggesting that the model correctly predicts Class 0 around 53% of the time. The precision for Class 1 is lower at 0.23, indicating a higher number of false positive predictions.
   - The recall for Class 0 is high at 0.86, indicating a good ability to capture instances of Class 0. The recall for Class 1 is 0.34, suggesting a moderate ability to identify instances of Class 1.
   - The F1-score for Class 0 is 0.66, indicating a reasonably balanced performance in terms of precision and recall. For Class 1, the F1-score is 0.63, suggesting a fairly balanced harmonic mean between precision and recall.

|Models|2:1|4:1|
|--|--|--|
|DT|0.579|0.5758|
|KNN|0.5992|0.6004|
|SGD|0.5426|0.5466|

we can observe the accuracy of the models on the 2:1 training set and the 4:1 test set as follows:

1. Decision Tree (DT) model:

- The accuracy on the 2:1 training set is 0.579, while on the 4:1 test set, it is 0.5758. This suggests that the model performs consistently on both the training and test sets, demonstrating a certain level of generalization ability.

2. K-Nearest Neighbors (KNN) model:

- The accuracy on the 2:1 training set is 0.5992, and on the 4:1 test set, it is 0.6004. This indicates that the model's performance is relatively stable on both the training and test sets, with slightly higher accuracy on the test set.

3. Stochastic Gradient Descent (SGD) model:

- The accuracy on the 2:1 training set is 0.5426, while on the 4:1 test set, it is 0.5466. This suggests that the model's performance is consistent on both the training and test sets, without any significant signs of overfitting or underfitting.

Increasing the training data does not always lead to a significant improvement in performance. Here are some possible reasons and considerations:

- Data quality: The effectiveness of adding training data is closely related to the quality of the data. If the additional data is similar to the original dataset or contains similar patterns and features, the model may not learn new information from it. Additionally, if the added data has issues such as outliers or incorrect labeling, it can negatively impact the model.
- Imbalanced data distribution: If the data distribution is imbalanced, meaning some classes have very few samples, the model may prioritize optimizing for the majority classes, resulting in lower performance for the minority classes. But we have ensured that approximately equal numbers of images have been sampled from the "Dogs" class and the "Cats" class.
- Model complexity: There is a trade-off between model complexity and the amount of training data. When the training data is limited, using overly complex models may lead to overfitting. Increasing the training data can help alleviate overfitting to some extent, but if the model is already sufficiently simple, adding more data may have limited impact on improving performance.
- Feature selection and engineering: The predictive performance of a model depends not only on the amount of data but also on the selection and engineering of features. When adding training data, it is important to ensure that the new data contains informative features and to combine appropriate feature selection and engineering methods to extract and represent these features effectively.
- Hyperparameter tuning: After expanding the training data, the model's performance may be influenced by its hyperparameters. It may be necessary to further tune the hyperparameters to fully leverage the benefits of increased training data.

In conclusion, increasing the training data does not guarantee a significant performance improvement. In addition to increasing the data, other factors such as data quality, balanced data distribution, model complexity, feature selection and engineering, and hyperparameter tuning need to be considered to comprehensively optimize the model's performance.

We can see from the competition ranking that most people choose to use CNN for image classification prediction, and facts have proved that their method is indeed effective. Through the construction of convolution layer, pooling layer and full connection layer, CNN can effectively extract features from images and perform well in tasks such as image classification, target detection and image generation. Of course, through the processing of the original data and later parameter adjustment, the score of the traditional machine learning algorithm can also be improved to a certain extent, but the traditional machine learning algorithm may still be inferior to CNN in image processing.
