emails = []
out = 'toList=['

while True:
    inp = input("leave blank to exit script\nenter email address: ")

    if inp == '':
            break
    print(f"is < {inp} > free of typo?")
    good = input("y/yes: ")

    if good in {'y', 'yes', 'Y', 'YES'}:
        print("ok, added...")

        inp = '\'' + inp + '\''
        if len(emails):
            out = out + ','

        emails.append(inp)
        out = out + inp
    else:
         print("ok, forgotten..")

if not len(emails):
    print("no emails given, doing nothing and exiting")
    exit(1)

out = out + ']'

print("writing toList.py:\n")
print(out)
print()

with open("toList.py", 'w') as outfile:
    outfile.write(out)

print()
#print("delete this file with\nrm setup_toList.py")



# this shell version never worked... python is much easier to use
# goal="toList=['"
# first="yaaasss"

# while true ; do
#     read inp
#     if [ -z $inp ]; then
#         echo "NO INPUT"
#         break
#     fi
#     if [ ! -z "${first}" ];
#         goal+="', '"
#         first=""
#     fi
#     goal+=inp
# done
# goal+="']\"""

# echo $goal > toList.py


# This will return true if a variable is unset or set to the empty string ("").
# if [ -z "${VAR}" ];
