

input_data=open("stopwords_removed_data.txt","r")

documents=""

for line in input_data:  
       documents  = documents + line

words = documents.split()
words.sort()



vocab=[]
freq=[]
vocabulary=[]
frequency=[]

count=0

for k in range(0,len(words)):
    if count==0:
        temp=words[k]
        vocab.append(str(temp))
        count +=1
    else:
        if temp==words[k]:
            count+=1
        else:
            freq.append(str(count))
            count=1;
            temp=words[k]
            vocab.append(str(temp))
freq.append(str(count))

input_data.close()

output = open("vocabulary_freq.txt", "w")

for k in range(len(freq)):
    output.write( vocab[k] +"  :  "+ freq[k])
    output.write("\n")
output.close()

output = open("vocabulary.txt", "w")


for k in range(len(freq)):
    if int(freq[k]) > 1:
        output.write(vocab[k])
        output.write("\n")

output.close()
