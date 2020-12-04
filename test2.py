""" Structured English
This program will open the file Final.txt, which contains student grades on a final exam.
It will then create a list, where each item of the list is a line of the file.
It will display the number of items in the list, which is the number of grades.
It will then sum the grades in the list, and divide the sum by the number of grades to get an average.
It will display the average.
Then it will check each grade in the list and compare it to the average. 
It will keep track of how many grades were above the average,
and display that number as a percentage of the number of grades. 
"""

""" Pseudo-Code
def main:
  file = Final.txt
  displayWithList(file)
  calculate_percent_above_avg(file)

def displayWithList(file):
  infile = open(file)
  listGrades = lines of file
  close file
  print(number of grades: )
  print(len(listGrades))
  avg = sum(listGrades) / len(listGrades)
  print(Average of grades:)
  print(avg)
  
def calculate_percent_above_avg(file):
  counter = 0
  for line in file
    if grade > avg
      counter +=1
  percentHigher = counter / len(listGrades)
  print(The percent of grades above average is:)
  print(percentHigher %)

main()
"""

def main():
  file = "Final.txt"
  calculate_percent_above_average(file)

def calculate_percent_above_average(file):
  infile = open(file, 'r')
  listGrades = [int(line.rstrip()) for line in infile]
  infile.close()
  length = len(listGrades)
  sum1 = sum(listGrades)
  avg = sum1 / length
  print("Number of grades:", length)
  print("Average grade:", avg)
  counter = 0
  for item in listGrades:
    if item > avg:
      counter += 1
  percentHigher = counter / length
  print("Percent of grades above average:", end = " ")
  print("{0:.2%}".format(percentHigher))

main()
  

