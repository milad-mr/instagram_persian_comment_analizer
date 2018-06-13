#!/bin/bash


 #vw -d ../data/p2_all_labeled_comments_vowpal.txt --passes 10 -f ../data/predictor.vw --ngram 1 --loss_function quantile -c

 vw -d ../data/p2_all_labeled_comments_vowpal.txt --readable_model ../data/predictor_readable.txt --passes 10 --ngram 1 --loss_function Quantile -c


 vw -d ../data/p2_test_comments_vowpal.txt -t -i ../data/predictor.vw -p ../data/prediction.txt

