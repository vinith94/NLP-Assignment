import re

stopwords_list=[]
for line in open("stopwords.txt"):
    x= line.split()
    stopwords_list.append(x[0])


data_list = open("data.txt", "r")
output_list = open("stopwords_removed_data.txt", "w")

for line in data_list:

    line = re.sub("'m", "am", line)
    line = re.sub("'s", "is", line)
    line = re.sub("'d", "would", line)
    line = re.sub("'ll", "will", line)
    line = re.sub("'ve", "have", line)
    line = re.sub("'re", "are", line)
    line = re.sub("won't", "would not", line)
    line = re.sub("doesn't", "does not", line)        
    line = re.sub("n't", "not", line)
    line = re.sub("would't", "would not", line)
    line = re.sub("'t", "not", line)
    line = re.sub(' [^A-Za-z ]+', '', line)

    
    
    words = line.split()
    temp = 1;

    for word in words:
         if word == '+' and temp == 1:
            output_list.write(word)
            temp = 0
            continue
        
         elif word == '-' and temp == 1:
            output_list.write(word)
            temp = 0
            continue

         for i in range(0,len(stopwords_list)):
             if( word.lower() == stopwords_list[i]):
                 break
             if( i==len(stopwords_list)-1 and word.lower() != stopwords_list[i]):
                 output_list.write(" " + word.lower()) 
    output_list.write("\n")
data_list.close()
output_list.close()
