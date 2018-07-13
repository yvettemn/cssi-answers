#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def read_process_data():
    with open('third_party/jane-eyre.txt') as f:
        # the following line
        # - joins each line in the file into one big string
        # - removes all newlines and carriage returns
        # - converts everything to lowercase
        content = ' '.join(f.readlines()).replace('\n','').replace('\r','').lower()
        return content


# You do not need to call this function unless you are doing level 3
def get_stop_words():
    with open('stop-words.txt') as f:
        str = ' '.join(f.readlines()).replace('\n', '').replace('\r', '').lower()
        return str.split(' ')

def get_highest_words(counts_dictionary, count):
    highest = sorted(counts_dictionary.items(), key=lambda x:x[1])[::-1][:count]
    for word in highest:
        print("%s: %s" % (word[0], word[1]))


content = read_process_data()
# Write your solution below!

word_count = {}
stop_words = get_stop_words()

words = content.split(" ")
for word in words:
    # Level 3: Only process word if it isn't in the stop words list
    # Level 2: Only process word if it isn't the empty string
    if word != "" and word not in stop_words:
        if word in word_count:
            # Read the number of occurances of the word
            count = word_count[word]
        else:
            # But if there wasn't something in the dictionary already, set it to zero...
            count = 0
        # ...then increase the count for the word by 1
        count += 1
        # Finally, store the new count in the dictionary.
        word_count[word] = count

# Decrease the indent: we are no longer inside the loop
# Print the words with the highest counts.
get_highest_words(word_count, 15)
