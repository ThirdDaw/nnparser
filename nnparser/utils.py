import numpy as np

from nnparser.logic.nn.CVNetwork import *
from nnparser.logic.utils.TrainingFileReader import TrainingFileReader


def base_nn_work(section):
    nn = BaseCVClassification()

    nn_input = [0 for i in range(len(nn.keywords))]
    for i in range(len(nn.keywords)):
        if nn.keywords[i] in section.lower():
            nn_input[i] = 1

    reader = TrainingFileReader(
        r'C:\Users\ThreeDaws\Desktop\DissertationProject\nnparser\logic\nn\training_data\cv\base')

    training_input = np.array(reader.get_training_input(reader.read_file()))
    training_output = np.array([reader.get_training_output(reader.read_file()), ]).T

    nn.train(training_input, training_output, 10000)

    result = nn.think(np.array(nn_input))
    return result


def education_nn_work(section):
    nn = EducationClassification()

    nn_input = [0 for i in range(len(nn.keywords))]
    for i in range(len(nn.keywords)):
        if nn.keywords[i] in section.lower():
            nn_input[i] = 1

    reader = TrainingFileReader(
        r'C:\Users\ThreeDaws\Desktop\DissertationProject\nnparser\logic\nn\training_data\cv\education')

    training_input = np.array(reader.get_training_input(reader.read_file()))
    training_output = np.array([reader.get_training_output(reader.read_file()), ]).T

    nn.train(training_input, training_output, 10000)

    result = nn.think(np.array(nn_input))
    return result


def experience_nn_work(section):
    nn = ExperienceClassification()

    nn_input = [0 for i in range(len(nn.keywords))]
    for i in range(len(nn.keywords)):
        if nn.keywords[i] in section.lower():
            nn_input[i] = 1

    reader = TrainingFileReader(
        r'C:\Users\ThreeDaws\Desktop\DissertationProject\nnparser\logic\nn\training_data\cv\experience')

    training_input = np.array(reader.get_training_input(reader.read_file()))
    training_output = np.array([reader.get_training_output(reader.read_file()), ]).T

    nn.train(training_input, training_output, 10000)

    result = nn.think(np.array(nn_input))
    return result


def skills_nn_work(section):
    nn = SkillsClassification()

    nn_input = [0 for i in range(len(nn.keywords))]
    for i in range(len(nn.keywords)):
        if nn.keywords[i] in section.lower():
            nn_input[i] = 1

    reader = TrainingFileReader(
        r'C:\Users\ThreeDaws\Desktop\DissertationProject\nnparser\logic\nn\training_data\cv\skills')

    training_input = np.array(reader.get_training_input(reader.read_file()))
    training_output = np.array([reader.get_training_output(reader.read_file()), ]).T

    nn.train(training_input, training_output, 10000)

    result = nn.think(np.array(nn_input))
    return result
