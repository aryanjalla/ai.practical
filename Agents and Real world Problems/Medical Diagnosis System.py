fever = input("Do yo have a fever (Y/N): ")
rashes = input("Do yo have a rash (Y/N): ")
cough = input("Do yo have a cough (Y/N): ")
headAche = input("Do yo have a headAche (Y/N): ")
bodyAche = input("Do yo have a bodyAche (Y/N): ")
sneezing = input("Do yo have a sneezing (Y/N): ")
chills = input("Do yo have a chills (Y/N): ")
runnyNose = input("Do yo have a runnyNose (Y/N): ")
soreThroat = input("Do yo have a sourThroat (Y/N): ")
swollenGlands = input("Do yo have a swollenGlands (Y/N): ")
conjuctives = input("Do yo have a conjuctives (Y/N): ")

if fever == 'Y' and headAche == 'Y' and runnyNose == 'Y' and rashes == 'Y':
    print("Result: You are diagnosed with German measles")
elif cough == 'Y' and sneezing == 'Y' and runnyNose == 'Y':
    print("Result: You are diagnosed with Measles")
elif fever == 'Y' and rashes == 'Y' and bodyAche == 'Y' and chills == 'Y':
    print("Result: You are diagnosed with Chicken pox")
elif fever == 'Y' and swollenGlands == 'Y':
    print("Result: You are diagnosed with Mumps")
elif fever == 'Y' and headAche == 'Y' and bodyAche == 'Y' and conjuctives == 'Y' and chills == 'Y' and  cough == 'Y' and runnyNose == 'Y' and soreThroat == 'Y':
    print("Result: You are diagnosed with Flu")
