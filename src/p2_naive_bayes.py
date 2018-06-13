import re #regular expression
import random
#file_friendly_comments = open("../data/friendly_comments", "r")

test_rate = 10
#preparing data
friendly_str = open("../data/friendly_comments", "r").read()
friendly_cms = friendly_str.split("', '")

celebrity_str = open("../data/celebrity_comments", "r").read()
celebrity_cms = celebrity_str.split("', '")
smothing = False
#prepare testcases
tc_celebrity_cms = []
tc_friendly_cms = []
test_case_count = 200
for _ in range(test_case_count):
    tc_celebrity_cms.append(celebrity_cms.pop(random.randint(0, len(celebrity_cms) - 1)))
    tc_friendly_cms.append(friendly_cms.pop(random.randint(0, len(friendly_cms) - 1)))

# for i in range(len(friendly_cms)):
#     if i % test_rate == 0:
#         friendly_cms_test.append(friendly_cms.pop(i))
friendly_wrd = []
for cm in friendly_cms:
    # if i % test_rate == 0:
    #     friendly_cms_test.append(cm)
    #     friendly_cms.remove(cm)
    friendly_wrd += re.findall(r"[\w']+", cm)
    

celebrity_wrd = []
for cm in celebrity_cms:
    celebrity_wrd += re.findall(r"[\w']+", cm)

print("friendly comments #: ", len(friendly_cms), ", words # : ", len(friendly_wrd))
print("celebrity comments #: ", len(celebrity_cms), ", words #: ", len(celebrity_wrd))


def p_word_in_class(w, c):
    #c is list of words 
    if(smothing):
        return (c.count(w) + 1)/ len(c)
    return (c.count(w))/ len(c)

def p_class(c, classes):
    total_wrd_count = 0
    for cc in classes:
        total_wrd_count += len(cc)
    return len(c) / total_wrd_count

def estimate_class(cm):
    words = cm.split(" ")
    p_celebrity = 1
    for w in words:
        #print("p_word is ", p_word_in_class(w, celebrity_wrd), "p total is ", p_celebrity)
        p_celebrity *= p_word_in_class(w, celebrity_wrd)
    p_celebrity *= p_class(celebrity_wrd, [friendly_wrd, celebrity_wrd])

    p_friendly = 1
    for w in words:
        p_friendly *= p_word_in_class(w, friendly_wrd)
    p_friendly *= p_class(friendly_wrd, [friendly_wrd, celebrity_wrd])
    #print("p's are :", p_celebrity, p_friendly)
    if p_celebrity > p_friendly :
        return "celebrity"
    else:
        return "friendly"
def recall(tc_cms, type):
    tp = 0
    for cm in tc_cms:
        if estimate_class(cm) == type:
            tp += 1
    return tp / len(tc_cms)


def precision(tc_target_cms, tc_other_cms, type):
    tp = 0
    pos = 0
    for cm in tc_target_cms:
        if estimate_class(cm) == type:
            tp += 1
            pos += 1
    for cm in tc_other_cms:
        if estimate_class(cm) == type:
            pos += 1
    return tp / pos


print ("without smothing")
print("celebrity:  precision is : ", precision(tc_celebrity_cms, tc_friendly_cms, "celebrity"), "recall is:", recall(tc_celebrity_cms, "celebrity"))
print("friendly:  precision is : ", precision(tc_friendly_cms, tc_celebrity_cms, "friendly"), "recall is:", recall(tc_friendly_cms, "friendly"))



print ("with smothing")

smothing = True
print("celebrity:  precision is : ", precision(tc_celebrity_cms, tc_friendly_cms, "celebrity"), "recall is:", recall(tc_celebrity_cms, "celebrity"))
print("friendly:  precision is : ", precision(tc_friendly_cms, tc_celebrity_cms, "friendly"), "recall is:", recall(tc_friendly_cms, "friendly"))

# pr_celebrity = 0
# # for cm in tc_celebrity_cms:
# #     print(estimate_class(cm))

