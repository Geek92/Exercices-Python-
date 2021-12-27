import random

#import shutil

def ponderate_delay(fichier):
    
    fi = open(fichier,'r')
    
    task_info = fi.readlines()
    
    fi.close()
    
    compl_time,weigth,limit_exe_time = 0,0,0
    
    total_delay = 0
    
    total_compl_time = 0
    
    delay_task = 0
    
    f0 = 0
    
    for i in range(1,int(task_info[0])+1):
        
        compl_time,weigth,limit_exe_time = map(int,task_info[i].split())
        
        total_compl_time += compl_time
        
        if total_compl_time > limit_exe_time:
            
            delay_task += 1
           
            f0 += weigth * (total_compl_time - limit_exe_time)
            
            total_delay += total_compl_time - limit_exe_time
    
    print("le temps totale de retards est: ",total_delay)
    
    print("le nombre de taches en retards, la valeur de f(0) ",delay_task, f0)
    
    return 0
    


def random_solut(fichier):
 
    fi = open(fichier,'r')
    
    task_info = fi.readlines()
    
    fi.close()
    
    f = open('file.txt','w')
    
    f.write(task_info[0])
    
    for i in range(100):
        
        number = random.randint(1,len(task_info) - 1)
        
        f.write(task_info[number])
        
        task_info.remove(task_info[number])
    
    f.close()

    #return f
    
    ponderate_delay("file.txt")
    
    return 0
    
    
    

#     number = 0
#     
#     
#     for i in range(100):
#         
#         number = random.randint(1,99)
#         
#         sost_row = ''
#         
#         sost_row = task_info[number]
#         
#         task_info[number] =  task_info[number + 1]
#         
#         task_info[number + 1] = sost_row

    #shutil.copy(fichier,"file.txt")
    
 
    
    
    
    
    
    

    


random_solut("n100_15_b.txt")
    
    

    
    
    