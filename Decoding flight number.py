# %% [markdown]
# Decode a flight number

# %%
f_code = input("Enter a flight code:")
f_code_lwr = f_code.lower()
airline = f_code_lwr[0:2]
f_number = f_code[2:6].lstrip("0")
origin = f_code[7:10]
dest = f_code[10:13]
hr = f_code[15:17].lstrip("0")+"H "
hr_int = int(f_code[15:17])
mn = f_code[17:].lstrip("0")+"M "
mn_int = int(f_code[17:19])
chk_1 = f_code_lwr.count(".")

if chk_1 !=2:
    print("code {} is invalid".format(f_code))
else:
    print("Enter a flight code:\n" + f_code)
    print("=========================")

    if airline == "aa":
        print("American Airlines " + f_number + "\n" + origin + " -> " + dest )
    elif airline == "jb":
        print("Jet Blue " + f_number + "\n" + origin + " -> " + dest)
    elif airline == "si":
        print("Singapore Airlines " + f_number + "\n" + origin + " -> " + dest)
    else:
        print("invalid flight code")
    if f_code_lwr[14] == "i":
        if hr =="0":
            print("ENROUTE - ETA " + mn)
        else:    
            print("ENROUTE - ETA " + hr + mn)
        print("=========================")
    elif f_code_lwr[14] == "g":
        if hr_int !=0:
            print("DEPARTING IN "+ hr + mn)
        elif hr_int == 0:
            print("DEPARTING IN "+ mn)
            if mn_int < 30:
                print("NOW BOARDING")
        print("=========================")
    else:
        print("invalid flight code")



