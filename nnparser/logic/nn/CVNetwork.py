from .BaseNeuralNetwork import BaseNeuralNetwork


class BaseCVClassification(BaseNeuralNetwork):
    criteria_number = 4
    keywords = ["cv", "curriculum vitae", "resume", "summary"]


class EducationClassification(BaseNeuralNetwork):
    criteria_number = 3
    keywords = ["education", "university", "institute"]


class ExperienceClassification(BaseNeuralNetwork):
    criteria_number = 3
    keywords = ["years", "experience", "development"]


class SkillsClassification(BaseNeuralNetwork):
    criteria_number = 3
    keywords = ["skills", "communication", "communicating"]
