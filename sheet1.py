###2
##print(5**9)
##print(3//2)
##print(7//3)
##print(7/3)
##print(6 == 6)
##a= 20; a+= 30; a%=3; print(a)
##print(True * False
##)
##print(True & False)
##print(True and False)
##print(((6>3) and (7<4) or (18==3)) and (9>3))
##print(True is False)
###print(False in ‘False’
##
###this throws an Error
##print(((True == False) or (False > True)) and (False <= True))
##
##
##
###3
##s1 = 'Nice to have it'
##s2 = 'here'
##print(s1+' '+s2)
###4
##a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
##print(a[3][1][2][0])
###5
##a.insert(0,s1)
##a.append(s2)
##print(a)
###6
##numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
##953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
##687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
##742, 717, 958,743, 527]
##
##
##for i in numbers :
##    if (i==237):
##        break
##    elif(i%2==0):
##        print(i)
##    else :
##        pass
###7
##color_list_1 = set(["White", "Black", "Red"])
##color_list_2 = set(["Red", "Green"])
##color_list_1.difference_update(color_list_2)
##print(color_list_1)
##
#####8
####x=input()
####for i in x:
####    
###9
##n=int(input())
##x=n+(11)*n+(111)*n
##print(x)
##
###10
##
###12
##d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 'Marks': [57,87,67,79]}
##a=d['Marks']
##max=a[0]
##for i in range(len(a)):
##    if(max < a[i]):
##        max=a[i]
##        pos=i
##print(d['Student'][pos])
##
##13
##d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
##'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
##'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
##
##c=d['Subject']
##a=[]
##for i in range(len(c)):
##	if(c[i]=='Python'):
##		a+=[i]
##new_Data={'Name':[],'Subject':[],'Ratings':[]}
##
##for i in a:
##    new_Data['Name'].append(d['Name'][i])
##    new_Data['Subject'].append(d['Subject'][i])
##    new_Data['Ratings'].append(d['Ratings'][i])
##print(new_Data)
