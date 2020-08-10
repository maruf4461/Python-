#7.1 Write a program that prompts for a file name, then opens that file and reads through the file,
#and print the contents of the file in upper case. Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt
name = input('Enter File Name:  ')
handle = open(name)
for file in handle:
    x = file.strip()
    print(x.upper())

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
t = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    num = float(line[line.find(':')+1:])
    t = num + t
avg = t/count
print('Average spam confidence:',avg)
