### This code will be able to read papers, identify the users typing style, then identify the user 
### Note to self: for i in word_list = for "whatver / whatvers" in word list
### Sentence lngh function
### Make function that will give a % value as a decimal for each character 
### Make a function that gives the % value each word takes up
### Subtract shared values in dictonary, add up total difference and absoulte value. Give a score, small score = similar, large score = differnt
### Scores: Average word length, character freq, word freq, avg sentence lngh, matches of sentences that contain the same two words from both texts
### Gives scores to common vs uncommon, word types, ect

from multiprocessing.sharedctypes import Value
from re import X
from typing import Counter, Dict

file_choice = input("What file would you like to use? Type copy for copypasta: ")

if(file_choice == "copy"):
    name_of_file = "C:\Python Projects\Text_Reading\copypasta.txt"

else: 
    name_of_file = "C:\Python Projects\Text_Reading\TestText.txt"

with open(name_of_file) as file:
    lines = [line.rstrip('\n') for line in file]

file_choice2 = input("What file would you like to use? Type copy for copypasta: ")

if(file_choice2 == "copy"):
    name_of_file2 = "C:\Python Projects\Text_Reading\copypasta.txt"
else: 
    name_of_file2 = "C:\Python Projects\Text_Reading\TestText.txt"

with open(name_of_file2) as file2:
    lines2 = [line.rstrip('\n') for line in file2]
    
def breakup(lines_list):
    word_list = []
    text_lines = len(lines_list)
    times = 0
    for i in range(text_lines):
        words = lines_list[times].split()
        times += 1
        word_list = word_list + words
    return word_list
def avglen(inlist):
    x = 0 
    all_len = []
    words_in_list = len(inlist)
    for i in range(words_in_list):
        cur_len = len(inlist[x])
        all_len.append(cur_len)
        x += 1 
    len_sum = sum(all_len)
    avg_len = len_sum / len(inlist)
    print(avg_len)
    return avg_len
def char_pre(testlist):
    all_freq = {}
    t = 0
    l = len(testlist)
    for i in range(l):
        for i in testlist[t]:
            if i in all_freq:
                all_freq[i] += 1
            else:
                all_freq[i] = 1
        t += 1 
    values = all_freq.values()
    total = sum(values)
    per = {}
    for i in all_freq:
        per[i] = float(all_freq[i]/total)
    return per
def combine_zero_dic(word_list, word_list2):
    wrd_dic_1 = {}
    wrd_dic_1 = char_pre(word_list)
    wrd_dic_2 = {}
    wrd_dic_2 = char_pre(word_list2)
    wrd_dic_1.update({}.fromkeys(wrd_dic_1,0))
    wrd_dic_2.update({}.fromkeys(wrd_dic_2,0))
    full_word_dic = wrd_dic_1 | wrd_dic_2
    return(full_word_dic)
def create_baseline(chrs, full):
    chrs = char_pre(chrs)
    a = Counter(chrs)
    b = Counter(full)
    add_dict = a + b
    dict_3 = dict(add_dict)
    baseline_chrpre = combo | dict_3
    return baseline_chrpre
    
avglen(breakup(lines))
avglen(breakup(lines2))


word_list = breakup(lines)
word_list2 = breakup(lines2)

combo = combine_zero_dic(word_list, word_list2)
base = create_baseline(word_list, combo)
base2 = create_baseline(word_list2, combo)
for key in base:
    if key in base2:
        base[key] = base[key] - base2[key]
    else:
        pass
for i in base:
    base[i] = abs(base[i])
sum_score  = base.values()
score = sum(sum_score)*100
print(score)
