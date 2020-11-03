import collections
import csv, re
ans = collections.defaultdict(int)

# repl_str = re.compile('.*^\d+$.*')
filename = '/Users/dcheng/Google Drive File Stream/My Drive/facebook-review'
# filename = '/Users/dcheng/Google Drive File Stream/My Drive/test'
alist = [line.rstrip() for line in open(filename)]
# file1 = open(filename, 'r')
for line in alist:
    print line
    try:
        tmp = re.findall(r'\d+', line)
        for a in tmp:
            ans[a] += 1
        opt = input("Extra Search Needed?")
        if opt == 1:
            val = input("Enter your value: ")
            if val == '':
                raise Exception
            else:
                ans[val] += 1
    except:
        print('enter complete!!')

rows = []
for i, v in ans.iteritems():
    rows.append([i, v])

filename = "/Users/dcheng/Downloads/fb.codes2"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(rows)