import math
from statistics import geometric_mean as gm
from statistics import mean as am

country = input("Enter file name (no extension): ") + ".txt"
textfile = open(country)
text = textfile.read()

lines = text.split("\n")
num_regs = len(lines)
datas = list()
# bigO = 3 * regions
for line in lines:
	data = line.split(" ")
	data = data[1:]
	new_data = list()
	for el in data:
		new_data.append(float(el))
	datas.append(new_data)

# calculate averages
# bigO = 3 * regions
avgs = list()
for i in range(3):
	temp_sum = 0
	for reg in datas:
		temp_sum += reg[i]
	avg = temp_sum / num_regs
	avgs.append(avg)

# replace absolute with relative values
# bigO = 3 * countries
for j in range(3):
	for reg in datas:
		reg[j] /= avgs[j]

# calculate each region's power index
# bigO = regions
reg_pis = list()
for reg in datas:
	reg_pi = 1 + math.sqrt(reg[0] * reg[1] * reg[2])
	reg_pis.append(reg_pi)

pi = gm(reg_pis)
sigma = am(reg_pis)
ripi = ((sigma / pi) ** 4) - 1
print("Regional disequilibrium of power index =", str(ripi))