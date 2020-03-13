def getDiet(calories,diseases):
    from pandas import DataFrame, read_csv

    df = DataFrame(read_csv("foodData.csv"))
    permeal = calories/3

    # snacks=["Kuzhalappam","pastry","biscuit","fries","chocolate","pasta","vada pav","sandwich","noodles","Chicken Shawarma","Cheese Pizza","Pizza","Coconut Pudding","Tapioca Pudding","Vanilla Pudding","Chocolate Pudding","Cornbread Pudding"]
    # Drinks=["coffee","tea","milk","shake","Apple Juice","Pineapple Juice","Orange Juice"]
    # others=["curd","yogurt","burger","peanuts"]
    # fruits=["banana","apple","grapes","carrots","Watermelon"]
    # curry=["ayala curry","Matthi curry","Vegetable Khurma","Boiled Eggs","Vegetable Khurma","Gobi Manchurian","Gobi Fry","Butter Chicken","Pepper Chicken","Gobi Chicken","Crab Curry","Payar Curry","Cheese Paneer","Mango Pickle","Coconut Chutney","Kadala Curry","Egg Curry","Baby Spinach","Tomato","fish","sambar","avial","stew","pork","Aloo Gobi","Gobi Curry","Beef Curry","Paneer Curry","Fish Curry","Prawn Curry","Sweet Peas"]

    
    
    # l2 = []
    # f1 = []
    # f2 = []
    # f3 = []
    # f4 = []

    # cholesterol=["cheese","burger","egg yolk","butter","chicken","cheese","ice cream"]
    # thyroid=["raw cabbage","raw cauliflower","gluten containing foods","junk foods","high- sugar","green-tea"]
    # diabetes=["sugar","oil,coconut(in moderation)","fried foods","mutton","parottas","snacks","soft drinks","egg yolk","salt(inlimit)","honey","dried fruits","mangoes","jackfruits"]
    # pcos=["biscuits","cakes","bread","dried fruits","ice cream","yogurt","soda","milk","cheese","butter","soy products","caffeine"]
    # hypertension=["maida","bread","noodles","pizza","burgers","chocolate","cakes","chips","coconut","milk","butter","achar"]

    # if(diseases=="Cholesterol"):
    #     f4.append(cholesterol)
    # elif(diseases=="Thyroid"):
    #     f4.append(thyroid)
    # elif(diseases=="Diabetes"):
    #     f4.append(diabetes)
    # elif (diseases == "PCOS"):
    #     f4.append(pcos)
    # elif (diseases == "Hypertension" ):
    #     f4.append(hypertension)
    # else:
    #     f4.append('')
    # def morn(permeal):
    #     morning=["Brown Bread","Kai pathiri","Malabar nice pathiri","Ada Dosa","Wheat Ada","Rice Rotti","Potato Rotti","idli","dosa","puttu","oats","salad","bread","idiyappam","appam","ada","vada","Poori","Methi Poori","Gobi Paratha"]
    #     df = DataFrame(read_csv("foodData.csv"))
    #     datas = []
    #     datas.append(df.loc[df['name'].isin(morning)])
    #     x = randint(0,len(datas[0])-1)
    #     calories = datas[0].iloc[x]["calories"]
    #     name = (datas[0].iloc[x]["name"])
    #     c1 = calories
    #     count = -1
    #     while( c1 <= permeal):
    #         c1 += calories
    #         count+=1
    #     ccurry = curry[randint(0,len(curry)-1)]
    #     f1 = {"name":name, "count":count+1 ,"curry":ccurry}
    #     return f1
    # def aftern(permeal):
    #     afternoon=["Cucumber Salad","Tomato Salad","Spinach Salad","Fresh fruit salad","Porotta","salad","rice","chappati","Chicken Biriyani","Beef Biriyani","Mutton Biriyani","Vegetable Biriyani"]
    #     df = DataFrame(read_csv("foodData.csv"))
    #     datas = []
    #     datas.append(df.loc[df['name'].isin(afternoon)])
    #     x = randint(0,len(datas[0])-1)
    #     calories = datas[0].iloc[x]["calories"]
    #     name = (datas[0].iloc[x]["name"])
    #     c1 = calories
    #     count = -1
    #     while( c1 <= permeal):
    #         c1 += calories
    #         count+=1
    #     ccurry = curry[randint(0,len(curry)-1)]
    #     f1 = {"name":name, "count":count+1 ,"curry":ccurry}
    #     return f1
    # def night(permeal):
    #     night=["Brown Bread","Cucumber Salad","Tomato Salad","Spinach Salad","Fresh fruit salad","Kai pathiri","Malabar nice pathiri","Rice Rotti","Potato Rotti","rice","pathiri","dosa","porotta","salad","rice","chappati","Chicken Biriyani","Beef Biriyani","Mutton Biriyani","Vegetable Biriyani","Poori","Methi Poori","Gobi Paratha"]
    #     df = DataFrame(read_csv("foodData.csv"))
    #     datas = []
    #     datas.append(df.loc[df['name'].isin(night)])
    #     x = randint(0,len(datas[0])-1)
    #     calories = datas[0].iloc[x]["calories"]
    #     name = (datas[0].iloc[x]["name"])
    #     c1 = calories
    #     count = -1
    #     while( c1 <= permeal):
    #         c1 += calories
    #         count+=1
    #     ccurry = curry[randint(0,len(curry)-1)]
    #     f1 = {"name":name, "count":count+1 ,"curry":ccurry}
    #     return f1

    # f1 = morn(permeal)
    # f2 = aftern(permeal)
    # f3 = night(permeal)

    # l2.append(f1)
    # l2.append(f2)
    # l2.append(f3)
    # l2.append(f4)

    # return l2
    return -1
