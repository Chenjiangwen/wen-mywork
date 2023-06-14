import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import numpy as np
import pandas as pd

# a. 首先导入数据集，使用pandas库读取csv文件：
data = pd.read_csv('votes.csv')

# b. 接下是自定义DecisionTreeClassifier类构建决策树分类器：

# 将数据集按照指定的比例或数量分割成训练集和测试集。
def my_train_test_split(X, y, test_size=0.3, shuffle=True, random_state=None):
    if shuffle:
        if random_state is not None:
            np.random.seed(random_state)
        indices = np.random.permutation(len(X))
        X, y = X[indices], y[indices]
    if isinstance(test_size, float):
        split_idx = int(len(X) * (1 - test_size))
    elif isinstance(test_size, int):
        split_idx = len(X) - test_size
    else:
        raise ValueError("Invalid type of 'test_size' parameter")
    X_train, y_train = X[:split_idx], y[:split_idx]
    X_test, y_test = X[split_idx:], y[split_idx:]
    return X_train, X_test, y_train, y_test

def my_accuracy_score(y_true, y_pred):
    correct = np.sum(y_true == y_pred)
    return correct / len(y_true)

def my_confusion_matrix(y_true, y_pred):
    classes = np.unique(y_true)
    matrix = np.zeros((len(classes), len(classes)), dtype=np.int)
    for i in range(len(classes)):
        for j in range(len(classes)):
            matrix[i, j] = np.sum((y_true == classes[i]) & (y_pred == classes[j]))
    return matrix

def my_classification_report(y_true, y_pred):
    classes = np.unique(y_true)
    report = "              precision    recall  f1-score   support\n\n"
    for cl in classes:
        tp = np.sum((y_true == cl) & (y_pred == cl))
        fp = np.sum((y_true != cl) & (y_pred == cl))
        tn = np.sum((y_true != cl) & (y_pred != cl))
        fn = np.sum((y_true == cl) & (y_pred != cl))
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        f1_score = 2 * precision * recall / (precision + recall)
        support = np.sum(y_true == cl)
        report += f"  {cl:10}{precision:10.3f}{recall:10.3f}{f1_score:10.3f}{support:10d}\n"
    report += '\n'
    # Compute micro-averaged metrics
    tp_micro = np.sum(y_true == y_pred)
    fp_micro = np.sum(y_true != y_pred)
    tn_micro = 0
    fn_micro = 0
    for cl in classes:
        tn_micro += np.sum((y_true != cl) & (y_pred != cl))
        fn_micro += np.sum((y_true == cl) & (y_pred != cl))
    precision_micro = tp_micro / (tp_micro + fp_micro)
    recall_micro = tp_micro / (tp_micro + fn_micro)
    f1_score_micro = 2 * precision_micro * recall_micro / (precision_micro + recall_micro)
    support_micro = len(y_true)
    report += f"{'micro-avg:':10}{precision_micro:10.3f}{recall_micro:10.3f}{f1_score_micro:10.3f}{support_micro:10d}\n"
    # Compute macro-averaged metrics
    precision_macro = np.mean([np.sum((y_true == cl) & (y_pred == cl)) / np.sum(y_pred == cl) for cl in classes])
    recall_macro = np.mean([np.sum((y_true == cl) & (y_pred == cl)) / np.sum(y_true == cl) for cl in classes])
    f1_score_macro = 2 * precision_macro * recall_macro / (precision_macro + recall_macro)
    support_macro = len(y_true)
    report += f"{'macro-avg:':10}{precision_macro:10.3f}{recall_macro:10.3f}{f1_score_macro:10.3f}{support_macro:10d}\n"
    return report

X = data.drop('party', axis=1).values
y = data['party'].values
X_train, X_test, y_train, y_test = my_train_test_split(X, y, test_size=0.3)


clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
# ```
#
# c. 构建好分类器并将数据分为训练集和测试集后，我们可以使用predict方法进行分类预测并计算模型的准确率、混淆矩阵以及其他评价指标。代码如下：
#
# ```
# 对测试集进行预测并输出评价指标
y_pred = clf.predict(X_test)
print("Size of training set:", len(X_train))
print("Size of testing set:", len(X_test))
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))
print(my_classification_report(y_test, y_pred))
# ```
#
# d. 最后为了得到学习曲线，我们需要不断增加训练样本的数量并记录模型在测试集上的准确率，从而得到随着训练样本数量增加时准确率的变化情况。代码如下：
#
# ```
# 绘制学习曲线
train_sizes = [50, 100, 150, 200, 250, 300]
train_acc, test_acc = [], []
for size in train_sizes:
    clf.fit(X_train[:size], y_train[:size])
    y_pred = clf.predict(X_test)
    train_acc.append(clf.score(X_train[:size], y_train[:size]))
    test_acc.append(accuracy_score(y_test, y_pred))

plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_acc, label='Training accuracy')
plt.plot(train_sizes, test_acc, label='Testing accuracy')
plt.legend(loc='lower right')
plt.title('Learning curve')
plt.xlabel('Training examples')
plt.ylabel('Accuracy')
plt.ylim(0.6, 1.1)
plt.show()

