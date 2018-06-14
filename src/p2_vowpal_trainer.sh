#!/bin/bash


 #vw -d ../data/p2_all_labeled_comments_vowpal.txt --passes 10 -f ../data/predictor.vw --ngram 1 --loss_function quantile -c

 vw -d ../data/p2_all_labeled_comments_vowpal.txt  --passes 10 -f ../data/predictor.vw  --ngram 3 -p ../data/p2_train_prediction_vowpal.txt --loss_function quantile -c


 vw  ../data/p2_test_comments_vowpal.txt -t -i ../data/predictor.vw -p ../data/p2_test_prediction_vowpal.txt

