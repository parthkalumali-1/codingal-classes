medical = input("Do you have a medical cause? (Y/N): ")
attendance = int(input("Enter attendance percentage: "))

if medical == "Y":
    print("Allowed to take exam")

else:
    if attendance > 75:
        print("Allowed to take exam")
    else:
        print("Not allowed to take exam")