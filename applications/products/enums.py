class CategoryChoices:
    ELECTRONICS: str = "electronics"
    CLOTHES: str = "clothes"
    FOOTWEAR: str = "footwear"
    FOOD: str = "food"
    GENERAL: str = "general"

    @classmethod
    def choices(cls):
        return (
            (cls.ELECTRONICS, cls.ELECTRONICS.upper()),
            (cls.CLOTHES, cls.CLOTHES.upper()),
            (cls.FOOTWEAR, cls.FOOTWEAR.upper()),
            (cls.FOOD, cls.FOOD.upper()),
            (cls.GENERAL, cls.GENERAL.upper()),
        )

    @classmethod
    def default(cls):
        return cls.GENERAL
