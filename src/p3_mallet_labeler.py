


labaled_cm_out_file = open("../data/p3_all_labeled_comments_mallet.txt", "w")
friendly_str = open("../data/friendly_comments", "r").read()
friendly_cms = friendly_str.split("', '")


celebrity_str = open("../data/celebrity_comments", "r").read()
celebrity_cms = celebrity_str.split("', '")


for i in range(min(len(friendly_cms), len(celebrity_cms))):
    #friendly_cm_out_file.writelines(str(i) + "friendly " + cm)
    print("fr" + str(i) + " friendly " + friendly_cms[i], file = labaled_cm_out_file)


for i in range(min(len(friendly_cms), len(celebrity_cms))):
    #i += 1
    #friendly_cm_out_file.writelines(str(i) + "friendly " + cm)
    print("celeb" + str(i) + " celebrity " + celebrity_cms[i], file = labaled_cm_out_file)