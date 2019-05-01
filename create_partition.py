import glob, os
import numpy as np

def create_partition_and_labels(samples_dir, training_percentage, randomise=True):

    label_translation = ["B", "C1", "C2", "C3", "C4", "C5", "C6", "C7",
                         "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9",
                         "T10", "T11", "T12", "L1", "L2", "L3", "L4", "L5",
                         "S1", "S2"]

    partition = {}
    training_labels = []
    validation_labels = []
    labels = {}

    ext_len = len(".npy")
    paths = glob.glob(samples_dir + "/**/*.txt", recursive=True)
    no_of_training = round(len(paths) * training_percentage)

    if randomise:
        np.random.shuffle(paths)

    for i, sample_path in enumerate(paths):

        sample_path_without_ext = sample_path[:-ext_len]
        label = sample_path_without_ext.rsplit('/', 1)[1]

        # assign to lists for partition
        if i < no_of_training:
            training_labels.append(label)
        else:
            validation_labels.append(label)

        # read file and assign to labels
        metadata_string = open(sample_path, "r").read()
        metadata_split = metadata_string.split(" ")
        centroid_coords = list(map(int, metadata_split[1:]))
        label_name = metadata_split[0]
        label_index = label_translation.index(label_name)
        labels[label] = [centroid_coords, label_index]

    partition["train"] = training_labels
    partition["validation"] = validation_labels
    return partition, labels