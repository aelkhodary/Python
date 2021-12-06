class OutOfStock(Exception):
    pass


class InvalidItemType(Exception):
    pass


class Inventory:
    def lock(self, item_type):
        """Select the type of item that is going to
        be manipulated. This method will lock the
        item so nobody else can manipulate the
        inventory until it's returned. This prevents
        selling the same item to two different
        customers."""
        pass

    def unlock(self, item_type):
        """Release the given type so that other
        customers can access it."""
        pass

    def purchase(self, item_type):
        """If the item is not locked, raise an
        exception. If the item_type  does not exist,
        raise an exception. If the item is currently
        out of stock, raise an exception. If the item
        is available, subtract one item and return
        the number of items left."""
        raise OutOfStock("Sorry, that item is out of stock {}".format(item_type))
        pass


if __name__ == '__main__':
    item_type = "widget"
    inv = Inventory()
    inv.lock(item_type)
    try:
        try:
            num_left = inv.purchase(item_type)
        except OutOfStock as e:
            print(e.args)
            raise

        else:
            print(
                "Purchase complete. There are "
                "{} {}s left".format(num_left, item_type)
            )
        finally:
            inv.unlock(item_type)
    except BaseException:
        print("Please call Admin 302")