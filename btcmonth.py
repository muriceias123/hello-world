"""
Hey please, forgive my crazyness.
Here is the tool that I was saying
"""
"""
See how much bitcoins will take
in one month based in the diary
quantity earned.For each three 
inputs,an average will be calculated
and then do the prediction to one month
"""

from sys import argv

def write(filename, txt):
    write = open(filename, 'w')
    write.write(txt)
    write.close()    

def read(filename):
    read = open(filename, 'r')
    content = read.read()
    read.close()
    
    return content

def readline(filename):
    read = open(filename, 'r')
    content = read.readline()
    read.close()
    
    return content

#Input of the day
daylog = open("daylog.txt", 'r')

line1 = daylog.readline()
line2 = daylog.readline()
line3 = daylog.readline()
daylog.close()

print "Bro,Look to your earnings in the last three days:\n"
print "%s%s%s" % (line1, line2, line3)


btc_earned = raw_input("How much you made today bro?\n> ")

print "Nice!You made %s bitcoins today!" % btc_earned

daylog = open("daylog.txt", 'w')

if len(read("lines.txt")) == 0:
    write("lines.txt", "0")



if read("lines.txt") == "2":
    daylog.write("%s" % line1)
    daylog.write("%s\n" % line2)
    daylog.write("%s" % btc_earned)
    daylog.close()
    lines = open("lines.txt", 'w')
    lines.write("3")

elif read("lines.txt") == "1":
    daylog.write("%s\n" % line1)
    daylog.write(btc_earned)
    write("lines.txt", "2")
    daylog.close()
    

elif read("lines.txt") == "0":
    daylog.write(btc_earned)
    write("lines.txt", "1")
    daylog.close()


#Average calculation
average = read("average.txt")
if read("lines.txt") == "3":
    int_line1 = int(line1)
    int_line2 = int(line2)
    int_line3 = int(line3)
    average = str((int_line1 + int_line2 + int_line3) / 3)
    daylog = open("daylog.txt", 'w')
    daylog.truncate()
    daylog.close()
    lines = open("lines.txt", 'w')
    lines.truncate()
    lines.close()   

write("average.txt", average)
print "\t*Average/day: ", read("average.txt")

#Prediction
def predict():
    month = 30
    predict = int(average) * 30
    
    return predict

print "\n\n The average of bitcoins in one month is: ", predict()
