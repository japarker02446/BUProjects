# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: April 24, 2022
Homework Problem 6.3

Use the full dataset (all three class labels) to implement K-means classification.
"""
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import random
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix

# Set the input directory path.
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    os.chdir(r'C:\Users\jparker\Code\Python\CS677\HW6')

# Import helper functions to seed data from file.
from JparkerHw6Helper import *

### Question 3.1, load the full data set.
seed_df = JparkerHw6Helper.load_data()

# Initialize a list to hold inertia values.
inertia_list = []

# Calculate distortion (aka inertia) vs. k for k = 1 - 8.
for k in range(1, 8):
    kmeans_classifier = KMeans(n_clusters = k)
    y_kmeans = kmeans_classifier.fit_predict(seed_df)
    inertia = kmeans_classifier.inertia_
    inertia_list.append(inertia)

fig, ax = plt.subplots(1, figsize = (7, 5))
plt.plot(range(1,8), inertia_list, marker = 'o', color = 'black')
plt.xlabel('Number of clusters: k')
plt.ylabel('Inertia')
plt.tight_layout()
plt.show()

# Best k is 4

# For the remaining questions:
# Pick two features at random from the data and plot the data points with
# different colors for each of the three classes.
random.seed(16)
f1 = random.randrange(0, 7)
f2 = random.randrange(0, 7)

# Question 3.2
# Run K-means clustering with best k (k* = 4).
kmeans_classifier = KMeans(n_clusters = 4)
y_kmeans = kmeans_classifier.fit_predict(seed_df)
centers = kmeans_classifier.cluster_centers_

plt.figure(figsize=(11,9))
plt.scatter(seed_df.iloc[:, f1], seed_df.iloc[:, f2], c = y_kmeans)
plt.scatter(centers[:, f1], centers[:, f2], c = 'red', marker = 'x', s = 200, alpha = 0.8)
plt.xlabel('f1: ' + str(seed_df.columns[f1]))
plt.ylabel('f2: ' + str(seed_df.columns[f2]))
plt.title('KMeans with k = 4')
plt.show()

# The points are not related (f1 = compactness, f2 = kernel_length)

# Question 3.3
# Assign cluster labels based on the majority class label in the cluster.
# Print the centroid value and assign label.
seed_df = seed_df.merge(pd.DataFrame({'k4_means': y_kmeans}), \
                        left_index = True, right_index = True)

# This is probably more complicated than it needs to be.
# For each cluster i = 0 - 4,
# For each class j in cluster i,
# Which class label j appears the most?
cluster_max = [0] * 4
cluster_label = [0] * 4
for i in range(4):
    for j in set(seed_df.loc[seed_df['k4_means'] == i, 'class']):
        class_count = seed_df.loc[seed_df['k4_means'] == i, 'class'].value_counts()[j]
#       print(i, j, class_count)
        if cluster_max[i] < class_count:
            cluster_max[i] = class_count
            cluster_label[i] = j

# Fill in the predicted cluster labels in seed_df
for i in seed_df.index:
    seed_df.loc[i, 'k4_label'] = cluster_label[seed_df.loc[i, 'k4_means']]

# Print the centroid and assigned label.
centroid_df = pd.DataFrame(
                {str(seed_df.columns[f1]):centers[:, f1].tolist(), \
                 str(seed_df.columns[f2]):centers[:, f2].tolist(), \
                 'label':cluster_label
                }
            )

print("The four centroids and class labels are:")
print(centroid_df)

# Question 3.4
# For the three largest clusters (let's call them A, B and C) assign
#   EACH data point to one of these clusters based on the distance to each
#   centroid by Euclidean distance.
# REFERENCE: https://stackoverflow.com/questions/1401712/how-can-the-euclidean-distance-be-calculated-with-numpy
# Remember to use our features f1 and f2.
#
# Going to manually review the cluster sizes to see that the largest three
# are clusters 1, 2 and 3 (not 0).
euclid_df = centroid_df.iloc[1:, :]

for i in seed_df.index:
    best_distance = 0
    seed_point = np.array((seed_df.loc[i,seed_df.columns[f1]], \
                           seed_df.loc[i,seed_df.columns[f2]]))

    for j in euclid_df.index:
        centroid_point = np.array((euclid_df.loc[j,seed_df.columns[f1]], \
                                   euclid_df.loc[j,seed_df.columns[f2]]))
        this_distance = np.linalg.norm(seed_point - centroid_point)

        if best_distance < this_distance:
            best_distance = this_distance
            seed_df.loc[i, 'euclid_label'] = euclid_df.loc[j, 'label']
#       print(i, j, best_distance, euclid_df.loc[j, 'label'])

# What is the overall accruacy for this new classifier?
ax = plt.subplot()
conmat = confusion_matrix(seed_df['class'], seed_df['euclid_label'])
sns.heatmap(conmat, square = True, annot = True, fmt = 'd', ax = ax, \
            xticklabels = ['1', '2', '3'], \
            yticklabels = ['1', '2', '3'], \
            cmap = 'Blues', cbar = False)
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_title('KMeans Euclidean Confusion Matrix')
plt.show()

# The accuracy is only 12 / 210 = 0.057.

# Question 3.5.
# Use the same classifier as question 3.4 (yikes)
# Using only the class labels for the SVM model (question 6.2) what is the
#   accuracy and confusion matrix?
sub_df = seed_df.loc[(seed_df['class'].isin([1,3])) & \
                     (seed_df['euclid_label'].isin([1,3]))]

ax = plt.subplot()
conmat = confusion_matrix(sub_df['class'], sub_df['euclid_label'])
sns.heatmap(conmat, square = True, annot = True, fmt = 'd', ax = ax, \
            xticklabels = ['1', '3'], \
            yticklabels = ['1', '3'], \
            cmap = 'Blues', cbar = False)
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_title('KMeans Euclidean Two-Class Confusion Matrix')
plt.show()

# The accuracy is 0.
# This classifier ... was really BAD!