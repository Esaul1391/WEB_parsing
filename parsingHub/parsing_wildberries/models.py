from pydantic import BaseModel, root_validator


class Item(BaseModel):
    id: int
    name: str
    salePriceU: float
    brand: str
    sale: int
    rating: int
    volume: int

    # @root_validator(pre=True)
    # def convert_sale_price(self, values):
    #     sale_price = values.get("SalePriceU")
    #     if sale_price is not None:
    #         values["salePriceU"] = sale_price / 100
    #     return values

class Items(BaseModel):
    products: list[Item]