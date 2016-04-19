import math
import nltk
# function for creating separate docs for positive and negative
def create_doc(data):
    pos_write = open("positive_new.txt","w")
    neg_write= open("negative_new.txt","w")

    fo= open(data)
    global class_p
    class_p=0
    global class_n
    class_n=0
    for line in fo:
        
        words = line.split()
        
        
        if words[0]=='+':
            pos_write.write(line)
            class_p=class_p+1
            
            
        elif words[0]=='-':
            neg_write.write(line)
            class_n= class_n+1
    pos_write.close()
    neg_write.close()
    
    return

#function for creating vocabulary for the given training data
def create_vocab(data):
##    modify_data(data)
    global vocab
    vocab=[]
    fo= open(data)
    megadoc=""
    for line in fo:
        check=line.split()
        line = line.replace(check[0],"")
        megadoc= megadoc+line
    words= megadoc.split()
    for i in range(0,len(words)):
        if words[i] not in vocab:
        
           freq= words.count(words[i])
           if freq>1:
            vocab.append(words[i])
        
    return vocab




# for calculating the frequencies of words in + class
def pos_frequency(data):
##    modify_data(data)
    global pos_words
    pos_words=[]
    global pos_count
    pos_count=[]
    pos_write = open(data)
    megadoc=""
    for line in pos_write:
        check=line.split()
        line=line.replace(check[0],"")
        megadoc= megadoc+line
    temp= megadoc.split()
        
    global total_pos
    total_pos=0
    tem=[]
    for i in range(0,len(temp)):
        if temp[i] not in tem:
            tem.append(temp[i])
    total_pos = total_pos +len(tem)
    
    for i in range(0,len(temp)):
        if temp[i] in vocab:
            if temp[i] not in pos_words:
               pos_words.append(temp[i])
               x= temp.count(temp[i])
               pos_count.append(x)
    pos_write.close()
    return total_pos
# for calculating the frequencies of words in - class
def neg_frequency(data):
   
    global neg_words
    neg_words=[]
    global neg_count
    neg_count=[]
    neg_write = open(data)
    megadoc=""
    for line in neg_write:
        check=line.split()
        line=line.replace(check[0],"")
        megadoc= megadoc+line
    temp= megadoc.split()

    global total_neg
    total_neg=0

    tem=[]
    for i in range(0,len(temp)):
        if temp[i] not in tem:
            tem.append(temp[i])
    total_neg = total_neg+len(tem)
    for i in range(0,len(temp)):
        if temp[i] in vocab:
            if temp[i] not in neg_words:
       
               neg_words.append(temp[i])
               x= temp.count(temp[i])
               neg_count.append(x)
    neg_write.close()
    return total_neg
def calc_posprob(sentence):
    prob_p =math.log2(class_p/(class_p+class_n))
    for word in sentence:
        
            if word in pos_words:
                index= pos_words.index(word)
                count= pos_count[index]
                prob_1= math.log2((count+1)/(total_pos+len(vocab)))
                prob_p= prob_p+prob_1 
            else:
              prob_1 = math.log2(1/(total_pos+len(vocab)))
              prob_p= prob_p+prob_1
    return prob_p
def calc_negprob(sentence):
    prob_n =math.log2(class_n/(class_p+class_n))
    for word in sentence:
        
            if word in neg_words:
                index= neg_words.index(word)
                count= neg_count[index]
                prob_1= math.log2((count+1)/(total_neg+len(vocab)))
                prob_n= prob_n+prob_1 
            else:
                prob_1 = math.log2(1/(total_neg+len(vocab)))
                prob_n= prob_n+prob_1
    return prob_n
def multinomial_naive_bayes(data,test):
    
    create_doc(data)
    
    create_vocab(data)
    pos_frequency("positive_new.txt")
    neg_frequency("negative_new.txt")
    tp=0
    tn=0
    fp=0
    fn=0
    test_file = open(test)
    i=1
    for line in test_file:
        sentence = line.split()
        
        if sentence[0]=='+':
            original = 1
            sentence.remove('+')
        else:
            original =0
            sentence.remove('-')
        pos_prob = calc_posprob(sentence)
       
        neg_prob = calc_negprob(sentence)
        
        if pos_prob>neg_prob:
            detected =1
        else:
            detected =0
        
        i=i+1
        if original==1 and detected==1:
            tp=tp+1
        elif original ==0 and detected==1:
            fp=fp+1
        elif original ==1 and detected ==0:
            fn=fn+1
        else:
            tn=tn+1
    accuracy = (tn+tp)/(tn+tp+fp+fn)
    #print(accuracy)
    return accuracy
#multinomial_naive_bayes("train.txt","test.txt")
