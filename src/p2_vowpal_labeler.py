labaled_cm_out_file = open("../data/p2_all_labeled_comments_vowpal.txt", "w")
test_cm_out_file = open("../data/p2_test_comments_vowpal.txt", "w")
friendly_str = open("../data/friendly_comments", "r").read()
friendly_cms = friendly_str.split("', '")


celebrity_str = open("../data/celebrity_comments", "r").read()
celebrity_cms = celebrity_str.split("', '")

sample_rate = 10 



# for i in range(min(len(friendly_cms), len(celebrity_cms))):
#     if i % sample_rate == 0: #this is test case
#        print("-1 | " + celebrity_cms[i] , file = test_cm_out_file)
#     else: 
#        print("-1 | " + celebrity_cms[i] , file = labaled_cm_out_file)
     
# for i in range(len(friendly_cms)):
#     if i % sample_rate == 0:
#        print("1 | " + friendly_cms[i] , file = test_cm_out_file)
#     else:  
#         print("1 | " + friendly_cms[i] , file = labaled_cm_out_file)


for i in range(min(len(friendly_cms), len(celebrity_cms))):
    if i % sample_rate == 0: #this is test case
       print("-1 | " + celebrity_cms[i] , file = test_cm_out_file)
       print("1 | " + friendly_cms[i] , file = test_cm_out_file)
    else: 
       print("-1 | " + celebrity_cms[i] , file = labaled_cm_out_file)
       print("1 | " + friendly_cms[i] , file = labaled_cm_out_file)