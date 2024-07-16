import pandas as pd
import re
import os
from typing import Dict

"""Get the absolute path of the excel file"""
def getPath(file):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(current_dir, 'data')
    file_path = os.path.join(folder_path, file)
    return file_path


"""Read the data from the excel file"""
def readExcelData(file_path):
    return pd.read_excel(file_path)


"""Get the data of the language specified: Dutch or English"""


def getLanguageData(data, language):
    return data.get([language])


"""Get the topics of the new words"""
def getTopics(data):
    return data[data["English"] == "-"]["Dutch"]


"""Get the dictionary of the topics and their corresponding words, paired into lists of two languages"""
def getDictionary(data):
    index_topics = getTopics(data).index
    words_per_topic = {}
    dutch_words = getLanguageData(data, "Dutch")
    english_words = getLanguageData(data, "English")
    topics = getTopics(data)
    i = 0
    for topic in topics[:-1]:
        """Filter the topic names to not include *** and (...)"""
        pattern = r"\*{3}\s*(.*?)\s*\("
        matches = re.findall(pattern, topic)
        filtered_topic = matches[0]

        """Separate words into topics"""
        topic_wordlist = []
        for w_index in range(index_topics[i] + 1, index_topics[i + 1]):
            topic_wordlist.append([dutch_words.iloc[w_index], english_words.iloc[w_index]])

        """Create a dictionary, where key is the topic and value is the list of lists of word pairs"""
        words_per_topic[filtered_topic] = topic_wordlist
        i += 1

    return words_per_topic


"""Get the data indexed from 0 to however many topics are there (dictionary used)"""
def getIndexedTopics(data: Dict[str, list]):
    indexed_topics = {}
    i = 0
    for topic in data.keys():
        indexed_topics[i] = topic
        i += 1
    return indexed_topics


"""Add the selected topics where the option is the range of indices, for instance, 1-5"""
"""The function does not iterate if the topic is already added to improve performance"""
def add_topics_range_of_indices(selected_topics, range_ind, added_topics, indexed_topics, dictionary):
    borders = range_ind.split("-")  # 1-6 to be split in "1" and "6"
    for index in range(int(borders[0]), int(borders[1]) + 1):
        add_single_topic(selected_topics, index, added_topics, indexed_topics, dictionary)
    return selected_topics


"""Add the selected topic where the option is a number, for instance, 15"""
def add_single_topic(selected_topics, index, added_topics, indexed_topics, dictionary):
    int_index = int(index)
    if int_index not in added_topics:
        topic = indexed_topics.get(int(index))
        selected_topics[topic] = dictionary.get(topic)
        added_topics.append(int_index)
    return selected_topics
