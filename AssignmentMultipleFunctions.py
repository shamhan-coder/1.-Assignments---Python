class multipleFunctions():
    def SubfieldsInAI():

        lists=["Sub-fields in AI are:","Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for temp in lists:
            print(temp)

    def OddEven():
        num=int(input("Enter The Number :"))
        if((num%2)==1):
            message="Odd number"
            print(num,"is Odd Number")
        else:
            print(num,"is Even Number")
            message="Even Number"
        return message
    
    def marriageeligibilty():
        gender=input("Enter the Gender :")
        age=int(input("Enter the age :"))
        if (gender=="female"):
            if(age>=18):
                print("Eligibile for Marriage")
            else:
                print("Not Eligible for Marriage")
        if (gender=="male"):
            if(age>=21):
                print("Eligibile for Marriage")
            else:
                print("Not Eligible for Marriage")
      
    def marks():
        sub1=int(input("Subject 1 = "))
        sub2=int(input("Subject 2 = "))
        sub3=int(input("Subject 3 = "))
        sub4=int(input("Subject 4 = "))
        sub5=int(input("Subject 5 = "))


        Total=sub1+sub2+sub3+sub4+sub5
        print("Total",Total)
        percentage=Total/5
        print("Percentage",percentage)
        
    def triangle():
        h1=int(input("Enter the Height 1 :"))
        b1=int(input("Enter the Breadth :"))
        print("Area formula: (Height*Breadth)/2")


        Area=(h1*b1)/2
        print("Area of Triangle", Area)

        h3=int(input("Enter the Height 1 :"))
        b2=int(input("Enter the Breadth :"))
        h4=int(input("Enter the Height 2 :"))
        peri=h3+h4+b2
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Permeter",peri)
        