class StatusChoices:
    CREATED: str = "created"
    PROCESSING: str = "processing"
    SHIPPED: str = "shipped"
    DELIVERED: str = "delivered"
    CANCELLED: str = "cancelled"

    @classmethod
    def choices(cls):
        return (
            (cls.CREATED, cls.CREATED.upper()),
            (cls.PROCESSING, cls.PROCESSING.upper()),
            (cls.SHIPPED, cls.SHIPPED.upper()),
            (cls.DELIVERED, cls.DELIVERED.upper()),
            (cls.CANCELLED, cls.CANCELLED.upper()),
        )

    @classmethod
    def default(cls):
        return cls.CREATED
