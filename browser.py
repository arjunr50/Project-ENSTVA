import webbrowser
f=open("final.txt","r").readlines()
n=int(input("Enter the Limit: \n\tNB:should consider it less then 20 for efficiency :"))
for item in range(n):
    webbrowser.open(f[item])
f.close()

# list to store file lines
lines = []
# read file
with open(r"final.txt", 'r') as fp:
    # read an store all lines into list
    lines = fp.readlines()

# Write file
with open(r"final.txt", 'w') as fp:
    # iterate each line
    for number, line in enumerate(lines):
        # delete lines. or pass any Nth line you want to remove
        # note list index starts from 0
        if number not in range(n):
            fp.write(line)

print("----------------------------------------------------------")
print("---------------------Program Complete---------------------")
print("----------------------------------------------------------")

