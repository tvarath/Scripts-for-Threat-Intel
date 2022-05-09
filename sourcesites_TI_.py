import csv

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
query = input ("Enter Your HASH Value:")

for j in search (query, tld="co.in", num=100, stop=100, pause=2):
    print(j)

filename = "TIS.csv"
fields = "Results"

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(j)



