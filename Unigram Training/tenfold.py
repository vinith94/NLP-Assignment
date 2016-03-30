import math


from unigram_training import multinomial_naive_bayes

i=0
j=25

avg_accuracy=[]
while i<=250 and j<=250:     



    input_data=open("stopwords_removed_data.txt","r")
    count_positive=0
    count_negative=0
    train=""
    test=""


    for line in input_data:
        #print(line)
        words=line.split()
        if words[0]=='+':
            count_positive +=1
        elif words[0]=='-':
            count_negative +=1
        if words[0]=='+' and count_positive > i and count_positive <= j:
            test += line
        elif words[0]=='-' and count_negative > i and count_negative <= j:
            test += line
        else:
            train += line

    input_data.close()

    train_list= open("train.txt","w")
    test_list=open("test.txt","w")

    for k in range(len(train)):
        train_list.write(train[k])
    for k in range(len(test)):
        test_list.write(test[k])
    train_list.close()
    test_list.close()

    accuracy=multinomial_naive_bayes("train.txt","test.txt")
    print(accuracy)
    avg_accuracy.append(accuracy)
    i=i+25
    j=j+25
print("Average Accuracy")
print( sum(avg_accuracy)/len(avg_accuracy))
