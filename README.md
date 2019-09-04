### K-Nearest_Neighbours
# K-Nearest Neighbours implemented onto the Wisconsin Breast Cancer UCI Data Set

## Introduction
This is but a personal project to exercise and implement what I have learned about KNN and some statistics principles.

The program is all written by me in Python and requires pandas and numpy to deal with the data manipulation involved and mathematical operations.

## How it all works

KNN is one of the most basic and introductory algorithms in the linear classification field. Utilizing an arbitrarily chosen metric and a data set of already labeled point the algorithm compares an unlabeled point to all other by calculating the similarity between them. Then, it labels the point by the most common class in the K-sized group of most similar points.

In this specific case, the metric I chose was the Euclidian Distance, that is, calculating the similarity between two points by computing it's distance as the square root of the sum of the squared differences between each feature (all of the 30 features are computed from the visual analysis of a digitized image of a fine needle aspirate (FNA) of breast tissue).

![Euclidian Distance formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/795b967db2917cdde7c2da2d1ee327eb673276c0)

*Euclidian Distance formula. _From [Wikipedia](https://en.wikipedia.org/wiki/Euclidean_distance)_ .*

It is important to note that each feature of the data set is represented in different measurement systems and units, so the standardization of the data is of great importance to refine the classification.

Besides any statistical optimization, it is fundamental to try and find the most efficient K-value so that the similarity metric has a wide enough, but not too broad scope. The method I used for finding it was running the program multiples times with different K-values and analysing the efficiency indicators (recall, precision and accuracy).

To conclude the explanation, in the end the program prints the accuracy and recall among some other statistical data. Along this line it is necessary to note that out of all features shown, the statistical recall is definitely one of, if not THE most important feature, as a false negative is the most risky and dangerous result a classificator of medical conditions can generate, leading a patient to believe they are healthy when they are not and need specific treatment.


## Results
An increase of about 8% in accuracy was found from just standardizing the measurements to z-score in order to minimize statistical exaggeration of some features in relation to others.

In this data set, from my analysis, the optimal K-value is around 9 as it maximizes the recall with high accuracy and no detriment in precision.

#### *The Good...*

K-values between (7-11) had the highest recall with little detriment in precision.

![Optimal K](https://i.imgur.com/e2P3TJk.png)

#### *The Bad...*

Way too low k-values ended up with results that are not terrible, but definitely not good enough. Besides a low k-value leading to overfitting beacuse of the Bias-Variance tradeoff, it lead to lower precision and accuracy that were the major negative point.

![Low K](https://i.imgur.com/ZlG0pGb.png)


#### *... And the ugly.*

Besides reaching high efficiency, a k-value higher than 20 resulted in a detriment in the recall which cannot be disregarded in this specific case, as I mentioned before.

![High K](https://i.imgur.com/Ykb995I.png)


## Conclusion
After the testing and analysis of the results many interesting concepts became clear about statistics and data sampling. Still, it is worth noting that the results obtained would be much more exaggerated and clear if the data set had more individuals analyzed.

In sum, the most significant changes in results came from the optimization of the k-value and the z-score standardization of the features.

Many more optimizations can be evaluated for this one problem such as using different similarity metrics, or implementing a system of weighted voting to make nearer neighbours have more influence over the classification than farther ones.
