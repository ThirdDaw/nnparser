from .BaseNeuralNetwork import BaseNeuralNetwork


class BaseCVClassification(BaseNeuralNetwork):
    keywords = ["cv", "curriculum vitae", "resume", "summary"]


class EducationClassification(BaseNeuralNetwork):
    keywords = ["education", "university", "institute"]


class ExperienceClassification(BaseNeuralNetwork):
    keywords = ["years", "experience", "development"]


class SkillsClassification(BaseNeuralNetwork):
    keywords = ["skills", "communication", "communicating"]
