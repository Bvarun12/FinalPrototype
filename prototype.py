class Supplier:
    def __init__(self, supplier_id, supplier_name, supplier_address, supplier_email, supplier_phone):
        self.Supplier_ID = supplier_id
        self.Supplier_Name = supplier_name
        self.Supplier_Address = supplier_address
        self.Supplier_Email = supplier_email
        self.Supplier_Phone = supplier_phone
        self.Products = []
        self.Filters = []

    def assign_product_to_supplier(self, inventory_product):
        if InventoryProduct not in self.Products:
            self.Products.append(inventory_product)
            inventory_product.supplier = self


class InventoryProduct:
    def __init__(self, product_id, product_name, product_description, product_price, supplier, product_quantity,
                 product_threshold, product_order_quantity, order_list):
        self.Product_ID = product_id
        self.Product_Name = product_name
        self.Product_Description = product_description
        self.Product_Price = product_price
        self.Product_Quantity = product_quantity
        self.Product_Threshold = product_threshold
        self.Product_Order_Quantity = product_order_quantity
        self.Order_List = order_list
        self.Products = []
        self.Supplier = []
        self.default_supplier = supplier

    def check_stock_level(self, order_list):
        if self.Product_Quantity < self.Product_Threshold:
            order_list.Products.append(InventoryProduct)
            return print("True")
        else:
            return print("False")

    def select_default_supplier(self, supplier):
        self.default_supplier = supplier

        self.select_default_supplier(Supplier)

    def add_new_meal_product(self):
        if InventoryProduct not in self.Products:
            self.Products.append(InventoryProduct)
            return print("Added")
        else:
            return print("Existent")

    def calculate_product_order(self):
        if self.Product_Quantity < self.Product_Threshold:
            self.Product_Order_Quantity = self.Product_Threshold - self.Product_Quantity

    def remove_product(self):
        self.Products.remove(InventoryProduct)


class OrderList:
    def __init__(self, ol_id, product_order_quantity):
        self.OL_ID = ol_id
        self.Products = []
        self.Product_Order_Quantity = product_order_quantity


class SupplierInventoryProduct:
    def __init__(self, product_id, product_name, product_description, product_quantity, supplier, order):
        self.Product_ID = product_id
        self.Product_Name = product_name
        self.Product_Description = product_description
        self.Product_Quantity = product_quantity
        self.Order = order

    def add_order(self, order, order_list):
        for i in order_list.products:
            if self.Product_Quantity > order_list.product_order_quantity:
                order.order_type = "purchaseorder"
                order.products.append(InventoryProduct)
                order.order_items.append(OrderItem)
            else:
                order.order_type = "backorder"
                order.products.append(InventoryProduct)
                order.order_items.append(OrderItem)


class Order:
    def __init__(self, o_id, order_type):
        self.Order_ID = o_id
        self.Order_Type = order_type
        self.Products = []
        self.Order_Item = []


class OrderItem:
    def __init__(self, order_item_id, order_type, product_id, product_name, product_description, product_quantity):
        self.Order_Item_ID = order_item_id
        self.Order_Type = order_type
        self.Product_ID = product_id
        self.Product_Name = product_name
        self.Product_Description = product_description
        self.Product_Quantity = product_quantity

    def calculate_product_quantity(self, supplier_inventory_product, order_list):
        OrderItem.product_quantity = order_list.product_order_quantity - supplier_inventory_product.product_quantity


class CustomerOrder:
    def __init__(self, order_id, order_detail, order_date, order_price, table_number, meal_quantity, order_status):
        self.Order_ID = order_id
        self.Order_Detail = order_detail
        self.Order_Date = order_date
        self.Order_Price = order_price
        self.Table_Number = table_number
        self.Meal_ID = []
        self.Meal_Name = []
        self.Meal_Quantity = meal_quantity
        self.Order_Status = order_status

    def calculate_total_amount(self):
        total = 0
        amount = 0
        for i in self.Meal_ID:
            amount = self.Meal_Quantity * self.Order_Price
            total = amount + total


class Meal:
    def __init__(self, meal_id, meal_name, meal_price):
        self.Meal_ID = meal_id
        self.Meal_Name = meal_name
        self.Meal_Price = meal_price
        self.Meal_Items = []

    def get_meal_item(self, meal_item):
        self.Meal_Items.append(meal_item)


class MealItem:
    def __init__(self, product_id, product_name, product_description, product_quantity):
        self.Product_ID = product_id
        self.Product_Name = product_name
        self.Product_Description = product_description
        self.Product_Quantity = product_quantity

    def get_quantity(self, inventory_product):
        inventory_product.product_quantity = inventory_product.product_quantity - self.Product_Quantity


class Invoice:
    def __init__(self, invoice_id, invoice_date, invoice_quantity, invoice_total_amount):
        self.Invoice_ID = invoice_id
        self.Invoice_Date = invoice_date
        self.Invoice_Quantity = invoice_quantity
        self.Invoice_Total_Amount = invoice_total_amount
        self.Invoice_Product = []


class DeliveryOrder:
    def __init__(self, delivery_id, delivery_date, delivery_product, delivery_quantity, invoice, supplier):
        self.Delivery_ID = delivery_id
        self.Delivery_Date = delivery_date
        self.Delivery_Product = delivery_product
        self.Delivery_Quantity = delivery_quantity
        self.Invoice = invoice
        self.Supplier = supplier


class RefundRequest:
    def __init__(self, refund_request_id, refund_reason, product_refunded, refund_amount, supplier):
        self.Refund_Request_ID = refund_request_id
        self.Refund_Reason = refund_reason
        self.Product_Refunded = product_refunded
        self.Refund_Amount = refund_amount
        self.Supplier = supplier


class ExchangeItem:
    def __init__(self, exchange_id, exchange_reason, new_product, supplier):
        self.Exchange_ID = exchange_id
        self.Exchange_Reason = exchange_reason
        self.New_Product = new_product
        self.Supplier = supplier


class User:
    def __init__(self, user_id, user_dob, user_name, user_address, user_email, user_phone):
        self.User_ID = user_id
        self.User_DoB = user_dob
        self.User_Name = user_name
        self.User_Address = user_address
        self.User_Email = user_email
        self.User_Phone = user_phone


class Owner(User):
    def __init__(self, owner_id, user_id, user_dob, user_name, user_address, user_email, user_phone):
        super().__init__(user_id, user_dob, user_name, user_address, user_email, user_phone)
        self.Owner_ID = owner_id

        def add_supplier_info(supplier):
            supplier.append(supplier)


class KitchenManager(User):
    def __init__(self, employee_id, user_id, user_dob, user_name, user_address, user_email, user_phone,
                 kitchen_manager_id):
        super().__init__(user_id, user_dob, user_name, user_address, user_email, user_phone)
        self.Kitchen_Manager_ID = kitchen_manager_id


class Employee(User):
    def __init__(self, employee_id, user_id, user_dob, user_name, user_address, user_email, user_phone, ):
        super().__init__(user_id, user_dob, user_name, user_address, user_email, user_phone)
        self.Employee_ID = employee_id


if __name__ == '__main__':
    carrot = InventoryProduct(product_id=1, product_name="carrot", product_description="carrot", product_price=1,
                              supplier="Tom", product_quantity=4, product_threshold=10, product_order_quantity=5,
                              order_list="carrot")

    carrot_order = OrderList(ol_id=1, product_order_quantity=5)
    carrot.check_stock_level(carrot_order)

    broccoli = InventoryProduct(product_id=1, product_name="broccoli", product_description="broccoli", product_price=1,
                              supplier="John", product_quantity=11, product_threshold=10, product_order_quantity=5,
                              order_list="broccoli")

    broccoli_order = OrderList(ol_id=1, product_order_quantity=5)
    broccoli.check_stock_level(broccoli_order)