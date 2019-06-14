import re
import sys
import time

def main():
    filename1 = input("Enter Comparing file : ")
    print("Entered filename 1 : ", filename1)
    filename2 = input("Enter SQL File in text : ")
    print("Entered filename 2 : ", filename2)
    f1 = open(filename1, 'r')
    f2 = open(filename2, 'r')

    word2 = set(re.findall(r"([a-zA-Z_\-]+)", f2.read()))

    f1_list = []
    for line in f1:
        l1 = line.strip()
        f1_list.append(l1)

    word1 = set(f1_list)

    common = word1.intersection(word2)
    print(common)

    f1.close()
    f2.close()


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(" ")
    print("Total Execution Time : {:.2f} sec".format(end - start))
    sys.exit(0)