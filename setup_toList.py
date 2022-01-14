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
