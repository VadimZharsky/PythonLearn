import os
import clr

# pathDLL = os.getcwd() + "\\MyTestCS.dll"
# clr.AddReference(pathDLL)

# from MyTestCS import ShopClass, DataGoods

# shop = ShopClass("Тест магазин")
# shop.createShopClass(20000)

# goods = DataGoods("чехол для телефона", 500, "RUB")

# for g in shop.listGoods:
#     print(f"{g.name}--{g.price} {g.unit}")

pathDLL = os.getcwd() + "\\CalcSharp.dll"
clr.AddReference(pathDLL)

from CalcSharp import CalcSharp

exp = CalcSharp("exp","454554445111/12121324323121")
result = exp.resolver()
print(result)