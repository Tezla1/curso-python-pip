import csv

def read_csv(path):
  with open(path, "r") as csvfile:
    reader = csv.reader(csvfile,delimiter=",")
    header = next(reader)
    data = []
    print(header)
    for row in reader:
      iterble = zip(header, row)
      country_dict = {key: value for key, value in iterble}
      data.append(country_dict)
    return data  
    

if __name__ == "__main__":
  data = read_csv("./App/data.csv")
  print(data[0])
  