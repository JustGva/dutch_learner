from topics import *

# import re

path = getPath("dutch_words.xlsx")
df = readExcelData(path)
dictionary = getDictionary(df)  # Topic - Words
indexed_topics = getIndexedTopics(dictionary)  # Number - Topic
run = True

selected_topics = {}
added_topics = []  # keep track of which topics were not chosen

"""Possible regular expression recognizing correct input (make a test?)"""
# pattern = r"\b\d+(?:-\d+)?(?:,\s*\d+(?:-\d+)?)*\b"
# matches = re.findall(pattern, "1, 2a, 3-5, 5, 5-8")
# for match in matches:
#     print(match)
# print(getIndexedTopics(dictionary))

"""Selection of the mode"""
while True:
    try:
        mode = int(input("Please choose the mode for learning the language:\n"
                         "type '1' for English => Dutch, \ntype '2' for Dutch => English "))
        if mode == 1 or mode == 2:
            user_topics = input("Please enter the range of indices between 1 and xx, "
                                "or enter topics separated by commas, "
                                "or 'all' for all topics: ")
            # List of options separated by comma, no whitespaces
            options = user_topics.replace(" ", "").split(",")
            print(options)
            for o in options:
                match "all" == o:
                    case True:
                        # All the topics
                        selected_topics = dictionary
                    case False:
                        match "-" in o:
                            case True:
                                # Bring these elements into the selected_topics
                                add_topics_range_of_indices(selected_topics, o, added_topics, indexed_topics,
                                                            dictionary)

                            case False:
                                # There is an integer given, so add only the given integer
                                add_single_topic(selected_topics, o, added_topics, indexed_topics, dictionary)
            print(selected_topics.keys())
            print(selected_topics)
            break
        else:
            print("Please enter a valid mode: '1' or '2': ")
    except ValueError:
        print("Invalid input, please enter the correct input: ")
