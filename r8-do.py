from Reader import Reader
from naiveBayes_textclass import NaiveBayes
r = Reader()

train_x,train_y = r.read_dic('r8-train-stemmed.txt')
test_x,test_y = r.read_dic('r8-test-stemmed.txt')

nb = NaiveBayes()
nb.fit(train_x,train_y)
py = nb.predict_varfeature(test_x)

acc = 0

for i in range(len(py)):
    #print test_y[i],py[i]
    if test_y[i] == py[i]:
        acc += 1

print acc*1.0/len(py)