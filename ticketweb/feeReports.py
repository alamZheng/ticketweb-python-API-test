# -*- coding: utf-8 -*-

# secitonName = 'ss1'
# priceName = 'ss1'
faces = [10, 20]
facility = 13

perTicketUnits = [True, False]  # $ - True % - False
perTickets = [1.08, 10.18]

ccUnits = [False, False]  # $ - True % - False
ccPercents = [28, 48]

phoneUnits = [True, False]  # $ - True % - False
phones = [1.6, 16]

BOUnits = [True, False]  # $ - True % - False
BOs = [1.88, 18.8]

rebateUnits = [False, False]  # $ - True % - False
rebates = [20, 20]

tax1Units = [True, True]  # $ - True % - False
tax1s = [5.1, 5.1]
tax2Units = [True, True]  # $ - True % - False
tax2s = [5.3, 5.3]
tax3Units = [False, False]  # $ - True % - False
tax3s = [55, 55]
tax4Units = [True, True]  # $ - True % - False
tax4s = [5.7, 5.7]


def calculateFee(perTickets, Units, faces, rebateAmout=0):
    perTicketAmouts = []
    for i in range(len(faces)):
        if rebateAmout == 0:
            # print(i)
            perTicketAmout = perTickets[i] if Units[i] else perTickets[i] / \
                100 * faces[i]
            # print(perTicketAmout)
        else:
            print("perTickets="+str(perTickets[i]))
            # print(Units)
            print("face="+str(faces[i]))
            print("rebateAmouts="+str(rebateAmouts[i]))
            perTicketAmout = perTickets[i]/100 * (faces[i] + rebateAmouts[i]) if Units else perTickets[i]/100 * faces[i]
            # print(perTicketAmout)
        perTicketAmouts.append(perTicketAmout)

    return perTicketAmouts


def sumList(*arg):
    sum=arg
    # print(sum)
    sumNew=[0]*(len(sum)-1)
    sumLen=len(sum)
    # print(sumLen)
    for i in sum:
        # print(i)
        for index, item in enumerate(i):
            # print(index,item)
            sumNew[index]=sumNew[index]+item
    return(sumNew)


perTicketAmouts=calculateFee(perTickets, perTicketUnits, faces)
# perTicketAmouts = [0.9,0.92]
BOAmouts=calculateFee(BOs, BOUnits, faces)
# BOAmouts = []
rebateAmouts=calculateFee(rebates, rebateUnits, faces)
# rebateAmouts = [10,6]
tax1=calculateFee(tax1s, tax1Units, faces)
# tax1 = [10,6]
tax2=calculateFee(tax2s, tax2Units, faces)
# tax2 = [10,6]
tax3=calculateFee(tax3s, tax3Units, faces)
tax3=[111, 111]
tax4=calculateFee(tax4s, tax4Units, faces)
# tax4 = [10,6]
phoneAmouts=calculateFee(phones, phoneUnits, faces)
# phoneAmouts = [1.6,0.01]

taxs=sumList(tax1, tax2, tax3, tax4)

ccReabteToggle=True  # toggle if on = True else = False
CCAmouts=calculateFee(ccPercents, ccReabteToggle, faces, rebateAmouts)


print('   face   |    tax   |  rebate  |  CCAmout |   facility   | onlineFee|   phone  |    BO    | perTickets(hide in report)')
print()
for i in range(len(faces)):
    # print(i)
    service=perTicketAmouts[i] + CCAmouts[i] + rebateAmouts[i] + facility
    phoneAmouts[i]=service + phoneAmouts[i]
    print('{0:^10.4f},{1:^10.4f},{2:^10.4f},{3:^10.4f},{4:^14.4f},{5:^10.4f},{6:^10.4f},{7:^10.4f},{8:^10.4f}'
          .format(faces[i], taxs[i], rebateAmouts[i], CCAmouts[i], facility, service, phoneAmouts[i], BOAmouts[i], perTicketAmouts[i]))

print()
