#!/bin/bash


 ../tools/mallet-2.0.8/bin/mallet train-classifier  --input ../data/all_comments.mallet --trainer MaxEnt --trainer NaiveBayes   --training-portion 0.9 
