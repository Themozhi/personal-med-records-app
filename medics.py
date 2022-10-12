import os
import pandas as ps
import webbrowser

os.chdir(str(os.path.expanduser('~')))
os.chdir('desktop')

class patient:
    def __init__(mem,name='',ID_number='',Type='',Room_no=''):
        mem.name=name
        mem.ID=ID_number
        mem.Type=Type
        mem.Room_no=Room_no

    def __repr__(mem):
        x={ 'Name        :':mem.name,'ID number   :':mem.ID,'Year        :':mem.Type,'Section     :':mem.Room_no}
        print('\n\n')
        return ps.Series(x).to_string()

    def chk_exists(ID):
        x=open('data','rt')
        d=x.readlines()
        x.close()
        if len(d)==0:
            return False,''
        else:
            for i in d:
                j=eval(i.strip('\n'))
                if j['ID number']==ID:
                    return True,d.index(i)
            return False,''

    def create_id():
        name=input('\nEnter the name             :')
        ID=input('\nEnter the ID number        :')

        if patient.chk_exists(ID)[0]:
            print('\n---ID number already exists---')
            return True
            #ID=input('\nEnter the ID number again:')
                    
        Type=input('\nEnter the Type of trauma   :')
        Room_no=input('\nEnter the Room_no          :')
        y=open('data','at')
        y.write('{"name":"%s","ID number":"%s","Type":"%s","Room_no":"%s"}\n'%(name,ID,Type,Room_no))
        y.close()
        print('\n')
        return patient(name,ID,Type,Room_no)

    def rem_ID(ID):
        if patient.chk_exists(ID)[0]:
            x=open('data','rt')
            d=x.readlines()
            x.close()
            d.pop(patient.chk_exists(ID)[1])
            x=open('data','wt')
            x.writelines(d)
            x.close
        else:
            print('---the ID number doesn\'t exists---')

    def rem_mem(mem):
        if patient.chk_exists(mem.ID)[0]:
            x=open('data','rt')
            d=x.readlines()
            x.close()
            d.pop(patient.chk_exists(mem.ID)[1])
            x=open('data','wt')
            x.writelines(d)
            x.close
        else:
            print('---the patient doesn\'t exists---')


    def find(ID):

        x=open('data','rt')
        d=x.readlines()
        x.close()
        for i in d:
                j=eval(i.strip('\n'))
                if j['ID number']==ID:
                    pos=d.index(i)
                    break
        else:
            return False,''
        j=eval(d[pos].strip('\n'))
        k,l,m,n=(i for i in tuple(j.values()))
        y=patient(k,l,m,n)
        return y,j

    def edit(mem):
        x=patient.find(mem.ID)[1]
        print('\n---just tap enter when not want to edit specific details---')
        k=input('\nEnter the name:')
        if k!='':
            x['name']=k
        k=input('\nEnter the ID number:')
        while True:
            if k!='':
                if patient.chk_exists(k)[0]:
                    print('\n---ID number already exists---\n--->please re-enter the ID number:')
                else:
                    x['ID number']=k
                    break

        k=input('\nEnter the Type of trauma:')
        if k!='':
            x['Type']=k
        k=input('\nEnter the Room_no:')
        if k!='':
            x['Room_no']=k
        k,l,m,n=(i for i in tuple(x.values()))
        z=('{"name":"%s","ID number":"%s","Type":"%s","Room_no":"%s"}\n'%(k,l,m,n))
        a=open('data','rt')
        d=a.readlines()
        a.close()
        d.pop(patient.chk_exists(mem.ID)[1])
        d.insert(patient.chk_exists(mem.ID)[1],z)
        patient.rem_ID(mem.ID)
        a=open('data','wt')
        a.writelines(d)
        a.close()

    def table():

        x=open('data','rt')
        d=x.readlines()
        x.close()

        s={
        'Name':['               '],
        'ID number':['                '],
        'Type':['               '],
        'Room_no':['                ']
        }

        for i in d:
            j=eval(i.strip('\n'))
            s['Name'].append(j['name'])
            s['ID number'].append(j['ID number'])
            s['Type'].append(j['Type'])
            s['Room_no'].append(j['Room_no'])
        print((ps.DataFrame(s,index=len(s['Name'])*['*']).sort_values('Name',ascending=True).to_string()))


def desk():
    print('\n--tap enter to enter the menu--')
    print('\n\n---> Menu:') if ''==input('') else print()
    print('\n1.Create ID')
    print('\n2.Remove ID')
    print('\n3.Find patient details')
    print('\n4.Edit details')
    print('\n5.Tabulate details')
    print('\n6.Book appointment(mail)')
    print('\n7.Exit the Program')
    while True:
        q=(input('\nEnter the prefix number to select='))
        if q.isdigit():
            if ( int(q)<1 or int(q)>7 ):
                print('\n---you\'ve entered invalid prefix, please enter the correct prefix---')
                q=(input('Re-enter the prefix number to select='))
            else:
                break
    return int(q)

print('\n\n-----medical data management-----')
x=desk()

while True:
    if x==7:
        print('\nexited\n\n.')
        exit()
    
    elif x==1:
        t=(patient.create_id())
        if t==True:
            print('\n--patient details not updated--')
        else:
            print('\n--patient details successfully updated--')
        x=desk()
    
    elif x==5:
        print('\n\n')
        patient.table()
        print('\n\n')
        x=desk()
    
    elif x==2:
        r=input('\nEnter the ID number of the patient:')
        m=patient.find(r)[0]
        if m==False:
            print('\n--patient details not exists--')
        else:
            patient.rem_mem(m)
            print('\n--patient details successfully removed--')
        x=desk()
    
    elif x==3:
        r=input('\nEnter the ID number:')
        w=(patient.find(r)[0])
        if w==False:
            print('\n--patient details not exists--')
        else:
            print(w)
        x=desk()

    elif x==4:
        n=input('\nEnter the name of the patient to be edited:')
        r=input('\nEnter the ID number of the patient to be edited:')
        m=patient.find(r)[0]
        if m==False:
            print('\n--patient details not exists--')
        elif m.name==n:
            if patient.edit(m):
                print('\n--patient details not updated--')
            else:
                print('\n--patient details successfully updated--')
        else:
            print('\n--patient name not matched--')
        x=desk()

    elif x==6:
        n=input('\nEnter the name of patient:')
        n=n.replace(' ','%20')
        t=input('\nEnter the time of appointment (9am - 5pm):')
        t=t.replace(' ','%20')
        d=input('\nType the reason of the consultation(briefly):')
        d=d.replace(' ','%20')
        print('\n\nSoon details of appointment schedule will reflect back to your mail..')
        webbrowser.open('mailto:?to=srikanth2110893@ssn.edu.in&subject=Appointment%20Booking&body=Name%20:%20'+n+'%0ATime%20:%20'+t+'%0ADetailes%20:%20'+d,new=1)
        x=desk()