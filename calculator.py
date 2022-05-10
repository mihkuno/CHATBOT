from tkinter import *
app = Tk()
app.title('calculator')

calc_range = 9
calc_input_width = 40
calc_input = Entry(width=calc_input_width)
calc_input.grid(row=0, column=0, columnspan=4)

key_num_padx = 33
key_num_pady = 30

key_num = []
key_num_last = ['AC', 0, '.', '=']
operators = ['+', '-', '*', '/']

btn_rw = 1
btn_cl = 0

# refernce https://stackoverflow.com/questions/45728548/how-can-i-get-the-button-id-when-it-is-clicked
def inp_num(arg):
    current = calc_input.get()
    catch = ''
    if(isinstance(arg, int)):
        catch = str(key_num[arg].cget("text"))
    elif(isinstance(arg, str)):
        if(arg == 'AC'):
            calc_input.delete(0, END)
            return
        elif(arg == '0'):
            catch = 0
        elif(arg == '.'):
            catch = '.'
        elif(arg == '='):
            calc_input.delete(0,END)
            answer = eval(current)
            calc_input.insert(0, eval(str(answer)))
            print('equals to: '+str(answer))
            return
        else:
            try:
                if(current.split()[-1] in operators):
                    current = current[:-3]
                    catch = ' '+arg+' '
                    print('operator repeat!')
                else:
                    catch = ' '+arg+' '
            except:
                print('input is inadequate!')
    
    calc_input.delete(0,END)
    calc_output = str(current) + str(catch)
    calc_input.insert(0, calc_output)
    


for x in range(16):
    if(x in (3, 7, 11)):
        btn = operators[btn_rw-1]
        key_num.append(Button(text=btn, padx=key_num_padx, pady=key_num_pady, command=lambda c=btn: inp_num(str(c))))
        print('operator is appended')
        calc_range += 1
    elif(x > 11):
        for items in key_num_last:
            key_num.append(Button(text=str(items), padx=key_num_padx, pady=key_num_pady, command=lambda c=items: inp_num(str(c))))
    else:
        key_num.append(Button(text=str(calc_range), padx=key_num_padx, pady=key_num_pady, command=lambda c=x: inp_num(int(c))))
   
    try:
        if(x in (4,8)):
            btn_rw += 1
            btn_cl = 0
        elif(x == 12):
            btn_rw += 1
            btn_cl = 0
            print('i reached the 12 and added the 4th row')

        if(btn_rw <= 3):
            calc_range -=1
            
        key_num[x].grid(row=btn_rw, column=btn_cl)
        btn_cl += 1

    except:
        print('empty list must quit now')
        break

print(len(key_num))
app.mainloop()