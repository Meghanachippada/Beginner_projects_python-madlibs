def madlib():

    name = input("the name is:")
    adjective1 = input("The adjective is:")
    verb1 = input("the verb is:")
    verb2 = input("the verb is:")
    pronoun1=input("the pronoun is:")
    noun1 = input("the noun is:")
    noun2 = input("the noun is:")
    noun3 = input("the noun is:")
    verb3 = input("the verb is:")
    pronoun2 = input("the pronoun is:")
    moral = input("the moral of the story is:")
    
    madlib=f"{name}had learned from his friends that lying is the {adjective1} way out of any situation. So he became fond \
of {verb1} and enjoyed telling small lies. When his parents {verb2} him and warned him against telling lies,he shrugged  \
them off ,saying'Lies never harm {pronoun1}!' Adam's {noun1} decided to explain to him why lying is bad. One evening , \
{noun2} and his {noun1} were walking down the street with some groceries. Just then,they saw a {noun3} rammed into a bookstore. \
Adam's father asked a man what happened and he replied, \
'The car driver lied to his {noun1} that he could see without spectacles,they both {verb3} in the car when the accident happened, \
the father is seriously hurt,im sure the boy regrets ever lying!' Adams father looked at Adam and said,'See Adam ,a lie is so dangerous!\
{pronoun2} can hurt people!' Adam realized the huge cost of a lie and stopped lying. \
He never again thought of lying to his father at any cost.So the moral of the story is {moral}! "
    
    print (madlib)

if __name__ == '__main__':
    madlib()