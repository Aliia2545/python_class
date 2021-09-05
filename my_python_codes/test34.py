import numpy as np
import random
# import matplotlib.pyplot as plt

MaxCell = 50
NumParticle = 2
NumDimen = 3
VMax = 5
NumIteration = 1000
GlobalBestVal = -1
c1 = c2 = 2
w = 0.75

fitness = np.random.uniform(0, 10, size=(50, 50, 50))
print(fitness)
PartPosition = [[[] for _ in range(NumDimen)] for _ in range(NumParticle)]
PartVelocity = [[[] for _ in range(NumDimen)] for _ in range(NumParticle)]
PartBestPosition = [[[] for _ in range(NumDimen)] for _ in range(NumParticle)]
PartValue = []
New_PartVelocity = [[[] for _ in range(NumDimen)] for _ in range(NumParticle)]
PartBestValue = []
GlobalBestPosition = []
GlobalBestRealPosition = []
Global_BestValue_list = []
Part_BestValue_list = []
b = []


def particle_position_and_velocity_initialization(num_particle, num_dimen, vmax):
    global GlobalBestVal
    # Global_BestValue_list.append(GlobalBestVal)
    for i in range(num_particle):
        for x in range(num_dimen):
            PartPosition[i][x] = random.randint(0, 49)
            PartVelocity[i][x] = random.randint(-vmax, vmax)
            PartBestPosition[i][x] = PartPosition[i][x]
        PartBestValue.append(fitness[PartBestPosition[i][0]][PartBestPosition[i][1]][PartBestPosition[i][2]])
        Part_BestValue_list.append(PartBestValue)
        if PartBestValue[i] > GlobalBestVal:
            GlobalBestVal = PartBestValue[i]

            for v in range(num_dimen):
                # print(GlobalBestPosition, "GlobalBestPosition")
                GlobalBestPosition.append(PartBestPosition[i][v])



def iteration(max_iter, num_particle, num_dimen, w, c1, c2, vmax):
    global GlobalBestVal

    for i in range(max_iter):
        for k in range(num_particle):
            for l in range(num_dimen):
                r1 = random.random()
                r2 = random.random()

                PartVelocity[k][l] = w * PartVelocity[k][l] + c1 * r1 * (
                        PartBestPosition[k][l] - PartPosition[k][l]) + c2 * r2 * (
                                                 GlobalBestPosition[l] - PartPosition[k][l])
                if PartVelocity[k][l] < -vmax:
                    PartVelocity[k][l] = -vmax
                if PartVelocity[k][l] > vmax:
                    PartVelocity[k][l] = vmax


                PartPosition[k][l] = PartPosition[k][l] + PartVelocity[k][l]

            ix = 49 if int(PartPosition[k][0]) >= 49 else 0 if int(PartPosition[k][0]) < 0 else int(PartPosition[k][0])
            iy = 49 if int(PartPosition[k][1]) >= 49 else 0 if int(PartPosition[k][1]) < 0 else int(PartPosition[k][1])
            iz = 49 if int(PartPosition[k][2]) >= 49 else 0 if int(PartPosition[k][2]) < 0 else int(PartPosition[k][2])
            # print(PartValue, "PartValue before append")
            # PartValue.append(fitness[ix][iy][iz])
            # print(PartValue, "PartValue after append")
            # print(PartValue[k], "PartValue[k] compare")
            # print(PartBestValue[k], "PartBestValue[k]")
            # if PartValue[k] > PartBestValue[k]:
            #     PartBestValue[k] = PartValue[k]
            if fitness[ix][iy][iz] > PartBestValue[k]:
                PartBestValue[k] = fitness[ix][iy][iz]
                for o in range(num_dimen):
                    PartBestPosition[k][o] = PartPosition[k][o]
            if fitness[ix][iy][iz] > GlobalBestVal:
                GlobalBestVal = fitness[ix][iy][iz]
                # Global_BestValue_list.append(GlobalBestVal)

                # print(GlobalBestVal, "после присваивания")

                for o in range(num_dimen):

                    GlobalBestPosition[o] = PartPosition[k][o]


        Global_BestValue_list.append(GlobalBestVal)


particle_position_and_velocity_initialization(num_particle=NumParticle, num_dimen=NumDimen, vmax=VMax)
iteration(max_iter=NumIteration, num_particle=NumParticle, num_dimen=NumDimen, w=w, c1=c1, c2=c2, vmax=VMax)

GlobalBest = GlobalBestVal
for c in range(NumDimen):
    GlobalBestRealPosition.append(round(GlobalBestPosition[c]))

# print(GlobalBestVal, "finally")
# print(GlobalBestRealPosition, "GlobalBestRealposition")
# print(Global_BestValue_list)
# print(len(Global_BestValue_list))

# plt.figure()
# plt.plot(list(range(NumIteration)), Global_BestValue_list)
# plt.scatter(list(range(NumIteration)), Global_BestValue_list)
# plt.show()



# plt.title("Global Best")
# plt.xlabel("Iteration")
# plt.ylabel("Evaluation of Global Best")
# plt.subplot(121)
# plt.title("Global Best")
# plt.xlabel("Iteration")
# plt.ylabel("Evaluation of Global Best")
# plt.plot(list(range(NumIteration)), Global_BestValue_list)
#
# plt.subplot(122)
# plt.title("Global Best")
# plt.xlabel("Iteration")
# plt.ylabel("Evaluation of Global Best")
# plt.plot(list(range(NumIteration)), Global_BestValue_list)
# plt.scatter(list(range(NumIteration)), Global_BestValue_list)
# plt.show()
#
#
