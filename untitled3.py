answer = input("What is the capital of France? ") #will show "what is the capital fo France?" and lets you input the users answer


if answer.strip().lower() == "paris": #converts any of the inputs all into lower case
    print("Correct! The capital of France is Paris.") #will show when the answer is right
else:
    print("Wrong answer. The correct answer is Paris.")#will show when the asnwer is wrong
    