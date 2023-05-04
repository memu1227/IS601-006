import traceback
from flask import Blueprint, request, flash, render_template, redirect, url_for
from werkzeug.datastructures import MultiDict
from shop.forms import ItemForm
from sql.db import DB
from roles.permissions import admin_permission
from flask_login import login_required, current_user
shop = Blueprint('shop', __name__, url_prefix='/',template_folder='templates')

@shop.route("/admin/item", methods=["GET","POST"])
@admin_permission.require(http_exception=403)
def item():
    form = ItemForm()
    id = request.args.get("id", form.id.data or None)
    type = "Edit" if id else "Create"
    if form.validate_on_submit():
        if form.id.data: # it's an update
            try:
                result = DB.update("UPDATE IS601_S_Items set name = %s, description = %s, stock = %s, cost = %s, image=%s WHERE id = %s",
                form.name.data, form.description.data, form.stock.data, form.cost.data, form.image.data, form.id.data)
                if result.status:
                    flash(f"Updated {form.name.data}", "success")
            except Exception as e:
                print("Error updating item", e)
                flash(f"Error updating item {form.name.data}", "danger")
        else: # it's a create
            try:
                result = DB.update("""INSERT INTO IS601_S_Items (name, description, stock, cost, image) 
                VALUES (%s,%s,%s,%s,%s)""",
                form.name.data, form.description.data, form.stock.data, form.cost.data, form.image.data)
                if result.status:
                    flash(f"Created {form.name.data}", "success")
                    form = ItemForm() # clear form
            except Exception as e:
                print("Error creating item", e)
                flash(f"Error creating item {form.name.data}", "danger")
    if id:
        try:
            result = DB.selectOne("SELECT id, name, description, stock, cost, image FROM IS601_S_Items WHERE id = %s", id)
            if result.status and result.row:
                    form.process(MultiDict(result.row))
        except Exception as e:
            print("Error fetching item", e)
            flash("Item not found", "danger")
    return render_template("item.html", form=form, type=type)

@shop.route("/admin/items/delete", methods=["GET"])
@admin_permission.require(http_exception=403)
def delete():
    id = request.args.get("id")
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_S_Items WHERE id = %s", id)
            if result.status:
                flash("Deleted item", "success")
        except Exception as e:
            print("Error deleting item",e)
            flash("Error deleting item", "danger")
    return redirect(url_for("shop.items"))

@shop.route("/admin/items", methods=["GET","POST"])
@admin_permission.require(http_exception=403)
def items():
    rows = []
    try:
        result = DB.selectAll("SELECT id, name, description, stock, cost, image FROM IS601_S_Items LIMIT 25",)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error fetching items", e)
        flash("There was a problem loading items", "danger")
    return render_template("items.html", rows=rows)

@shop.route("/shop", methods=["GET","POST"])
@login_required
def shop_list():
    rows = []
    try:
        result = DB.selectAll("SELECT id, name, description, stock, cost, image FROM IS601_S_Items WHERE stock > 0 LIMIT 25",)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error fetching items", e)
        flash("There was a problem loading items", "danger")
    return render_template("shop.html", rows=rows)

@shop.route("/detailed_view", methods=["GET","POST"])
@login_required
def detailed_view():
    form = ItemForm()
    id = id = request.args.get("id", form.id.data or None)
    if id:
        try:
            result = DB.selectOne("SELECT id, name, description, category, stock, cost, image FROM IS601_S_Items WHERE id = %s", id)
            if result.status and result.row:
                    row = result.row
                    # pre-fill the form fields
                    form.id.data = row["id"]
                    form.name.data = row["name"]
                    form.description.data = row["description"]
                    form.category.data = row["category"]
                    form.stock.data = row["stock"]
                    form.cost.data = row["cost"]
                    form.image.data = row["image"]
        except Exception as e:
            print("Error fetching item", e)
            flash("Item not found", "danger")
    return render_template("detailed_view.html", row = row, form = form)

'''
UCID: mm2836, Date Implemented: 04/24/23
'''

@shop.route("/cart", methods=["GET","POST"])
@login_required
def cart():
    item_id = request.form.get("item_id")
    id = request.form.get("id", item_id)
    print("id", id)
    quantity = request.form.get("quantity", 1, type=int)
    user_id = current_user.get_id()
    if id and user_id:
        if quantity > 0:
            try:
                result = DB.selectOne("SELECT cost,name from IS601_S_Items WHERE id = %s", id)
                print("result", result)
                if result.status and result.row:
                    cost = result.row["cost"]
                    name = result.row["name"]
                    if item_id: # update from cart
                        result = DB.insertOne("""
                        UPDATE IS601_S_Cart SET
                        quantity = %(quantity)s,
                        cost = %(cost)s
                        WHERE item_id = %(id)s and user_id = %(user_id)s
                        """,{
                            "id":id,
                            "quantity": quantity,
                            "cost":cost,
                            "user_id":user_id
                        })
                        if result.status:
                            flash(f"Updated quantity for {name} to {quantity}", "success")
                    else: #add from shop
                        result = DB.insertOne("""
                        INSERT INTO IS601_S_Cart (item_id, quantity, cost, user_id)
                        VALUES(%(id)s, %(quantity)s, %(cost)s, %(user_id)s)
                        ON DUPLICATE KEY UPDATE
                        quantity = quantity + %(quantity)s,
                        cost = %(cost)s
                        """,{
                            "id":id,
                            "quantity": quantity,
                            "cost":cost,
                            "user_id":user_id
                        })
                        if result.status:
                            flash(f"Added {quantity} of {name} to cart", "success")
            except Exception as e:
                print("Error updating cart" ,e)
                flash("Error updating cart", "danger")
        else:
            # assuming delete
            try:
                result = DB.delete("DELETE FROM IS601_S_Cart where item_id = %s and user_id = %s", id, user_id)
                if result.status:
                    flash("Deleted item from cart", "success")
            except Exception as e:
                print("Error deleting item", e)
                flash("Error deleting item from cart", "danger")
    rows = []
    try:
        result = DB.selectAll("""SELECT c.id, item_id, name, c.quantity, (c.quantity * c.cost) as subtotal 
        FROM IS601_S_Cart c JOIN IS601_S_Items i on c.item_id = i.id
        WHERE c.user_id = %s
        """, current_user.get_id())
        if result and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error getting cart", e)
        flash("Error fetching cart", "danger")
    return render_template("cart.html", rows=rows)

@shop.route("/purchase", methods=["GET","POST"])
@login_required
def purchase():
    cart = []
    total = 0
    quantity = 0
    order = {}
    first_name = str(request.form.get("first_name"))
    last_name = str(request.form.get("last_name"))
    address = str(request.form.get("address"))
    payment_method = request.form.get("payment_method")
    try:

        # get cart to verify
        
        result = DB.selectAll("""SELECT c.id, item_id, name, c.quantity, i.stock, c.cost as cart_cost, i.cost as item_cost, (c.quantity * c.cost) as subtotal 
        FROM IS601_S_Cart c JOIN IS601_S_Items i on c.item_id = i.id
        WHERE c.user_id = %s
        """, current_user.get_id())
        if result.status and result.rows:
            cart = result.rows
        # verify cart
        has_error = False
        for item in cart:
            if item["quantity"] > item["stock"]:
                flash(f"Item {item['name']} doesn't have enough stock left", "warning")
                has_error = True
                return redirect(url_for("shop.cart"))
            if item["cart_cost"] != item["item_cost"]:
                flash(f"Item {item['name']}'s price has changed, please refresh cart", "warning")
                has_error = True
                return redirect(url_for("shop.cart"))
            total += int(item["subtotal"] or 0)
            quantity += int(item["quantity"])
        # verify address
        if not address:
            flash(f"Please enter an address","Warning")
        # verify payment method
        valid_payment_methods = ['credit card', 'debit card', 'pay pal', 'google pay', 'apple pay']
        if payment_method.lower() not in valid_payment_methods:
            flash(f"Please enter a valid payment method (credit card, debit card, pay pal google pay, or apple pay)","danger")
            has_error = True
            return redirect(url_for("shop.cart"))
        # check can afford
        if not has_error:
            money_spent = int(request.form.get("money_received"))
            if total > money_spent:
                flash("You can't afford to make this purchase", "danger")
                has_error = True
                return redirect(url_for("shop.cart"))
            elif money_spent > total:
                flash(f"Thank you for your purchase, here is your extra change ({money_spent-total}) back")
            else:
                flash(f"Thank you for your successful purchase")
        '''
        UCID: mm2836, Date Implemented:05/03/23
        '''
        # create order data
        order_id = -1
        if not has_error:
            result = DB.insertOne("""INSERT INTO IS601_S_Orders (first_name,last_name,address,money_received,total_price, payment_method, number_of_items, user_id)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""", first_name, last_name, address, money_spent,total,payment_method, quantity, current_user.get_id())
            if not result.status:
                flash("Error generating order", "danger")
                DB.getDB().rollback()
                has_error = True
            else:
                order_id = int(DB.db.fetch_eof_status()["insert_id"])
                order["order_id"] = order_id
                order["total_spent"] = total
                order["quantity"] = quantity
                order["payment_method"] = payment_method
                order["address"] = address
        # record order history
        if order_id > -1 and not has_error:
            # Note: Not really an insert 1, it'll copy data from Table B into Table A
            result = DB.insertOne("""INSERT INTO IS601_S_OrderItems (quantity, cost, order_id, item_id, user_id)
            SELECT quantity, cost, %s, item_id, user_id FROM IS601_S_Cart c WHERE c.user_id = %s""",
            order_id, current_user.get_id())
            if not result.status:
                flash("Error recording order history", "danger")
                has_error = True
                DB.getDB().rollback()
        # update stock based on cart data
        if not has_error:
            result = DB.update("""
            UPDATE IS601_S_Items 
                set stock = stock - (select IFNULL(quantity, 0) FROM IS601_S_Cart WHERE item_id = IS601_S_Items.id and user_id = %(uid)s) 
                WHERE id in (SELECT item_id from IS601_S_Cart where user_id = %(uid)s)
            """, {"uid":current_user.get_id()} )
            if not result.status:
                flash("Error updating stock", "danger")
                has_error = True
                DB.getDB().rollback()

        # apply purchase (specific to my project)
        '''
        if not has_error:
            # here I'm using a known item_id to update my player's stats
            attrs = [("life", -1), ("speed", -2), ("fire_rate", -3), ("damage", -4), ("radius", -5)]
            for attr, target_id in attrs:
                try:
                    query = f"""
                    INSERT INTO IS601_S_Attributes (name, value, user_id)
                    VALUES (%(attr)s,
                    (SELECT IFNULL(SUM(quantity), 0) FROM IS601_S_OrderItems WHERE item_id = %(target_id)s and user_id = %(uid)s)
                    , %(uid)s)
                    ON DUPLICATE KEY UPDATE 
                    value = (SELECT IFNULL(SUM(quantity), 0) FROM IS601_S_OrderItems WHERE item_id = %(target_id)s and user_id = %(uid)s)
                    """
                    print(f"{attr} query", query)
                    result = DB.insertOne(query,
                    {"uid": current_user.get_id(),
                    "attr": attr,
                    "target_id": int(target_id)})
                except Exception as e:
                    print(f"Error updating attribute {attr}", e)
        '''
        # empty the cart
        if not has_error:
            result = DB.delete("DELETE FROM IS601_S_Cart WHERE user_id = %s", current_user.get_id())
        '''
        if not has_error:
            details = f"Spent {total} on {quantity} upgrades" # TBD
            current_user.account.remove_points(-total, reason="purchase", details=details)
            DB.getDB().commit()
            flash("Purchase successful!", "success")
        else:
            return redirect(url_for("shop.cart"))
        '''
    except Exception as e:
        print("Transaction exception", e)
        flash("Something went wrong", "danger")
        traceback.print_exc()
    # TODO route to thank you / summary page
    # TODO add link from cart page to this route
    return render_template("order_summary.html", rows=cart, order=order)

@shop.route("/detailed_order", methods=["GET","POST"])
@login_required
def detailed_order():
    order = {}
    id = id = request.args.get("id")
    if id:
        try:
            result = DB.selectOne("SELECT id, address, total_price, payment_method, money_received, number_of_items FROM IS601_S_Orders WHERE id = %s", id)
            if result.status and result.row:
                    row = result.row
                    order["order_id"] = row["id"]
                    order["total_spent"] = row["money_received"]
                    order["quantity"] = row["number_of_items"]
                    order["payment_method"] = row["payment_method"]
                    order["address"] = row["address"]
        except Exception as e:
            print("Error fetching item", e)
            flash("Item not found", "danger")
        # locking query to order_id and user_id so the user can see only their orders
        total = 0
        result2 = DB.selectAll("""
        SELECT name, oi.cost, oi.quantity, (oi.cost*oi.quantity) as subtotal FROM IS601_S_OrderItems oi JOIN IS601_S_Items i on oi.item_id = i.id WHERE order_id = %s ANd user_id = %s
        """, id, current_user.get_id())
        
        if result2.status and result2.rows:
            rows = result2.rows
            total = sum(int(r["subtotal"]) for r in rows)
    return render_template("order_detailed_view.html", order = order,total = total,rows = rows)

"""
UCID: mm2836, Date Implemented: 05/04/23
"""
    

@shop.route("/orders", methods=["GET"])
@login_required
def orders():
    rows = []
    try:
        result = DB.selectAll("""
        SELECT id, money_received, number_of_items, payment_method created FROM IS601_S_Orders WHERE user_id = %s
        """, current_user.get_id())
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error getting orders", e)
        flash("Error fetching orders", "danger")
    return render_template("orders.html", rows=rows)

@shop.route("/order", methods=["GET"])
@login_required
def order():
    rows = []
    total = 0
    id = request.args.get("id")
    if not id:
        flash("Invalid order", "danger")
        return redirect(url_for("shop.orders"))
    try:
        # locking query to order_id and user_id so the user can see only their orders
        result = DB.selectAll("""
        SELECT name, oi.cost, oi.quantity, (oi.cost*oi.quantity) as subtotal FROM IS601_S_OrderItems oi JOIN IS601_S_Items i on oi.item_id = i.id WHERE order_id = %s ANd user_id = %s
        """, id, current_user.get_id())
        if result.status and result.rows:
            rows = result.rows
            total = sum(int(row["subtotal"]) for row in rows)
    except Exception as e:
        print("Error getting order", e)
        flash("Error fetching order", "danger")
    return render_template("order.html", rows=rows, total=total)


@shop.route('/shop/pending', methods=['GET'])
@login_required
def pending():
    #fetch cart
    rows = []
    try:
        result = DB.selectAll("""SELECT c.id, item_id, name, c.quantity, (c.quantity * c.cost) as subtotal 
        FROM IS601_S_Cart c JOIN IS601_S_Items i on c.item_id = i.id
        WHERE c.user_id = %s
        """, current_user.get_id())
        if result and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error getting cart", e)
        flash("Error fetching cart", "danger")
    # Calculate the percentage change in unit cost and the total purchase price
    items = []
    total_price = 0
    for row in rows:
        item_id = row["item_id"]
        name = row["name"]
        quantity = row["quantity"]
        item_cost = row["subtotal"] / quantity
        percentage_change = 0.0

        # Get the current stock and cost of the item from the database
        try:
            result = DB.selectOne("""SELECT stock, cost from IS601_S_Items WHERE id = %s""", item_id)
            if result.status and result.row:
                stock = result.row["stock"]
                product_cost = result.row["cost"]

                # Calculate the percentage change in unit cost
                if product_cost != item_cost:
                    percentage_change = round(((item_cost - product_cost) / product_cost) * 100, 2)
            else:
                flash(f"Error getting info for item {name}", "warning")
        except Exception as e:
            print("Error getting item info", e)
            flash(f"Error getting info for item {name}", "warning")

        # Add the item to the list with the calculated values
        items.append({'name': name, 'quantity': quantity, 'unit_cost': item_cost, 
                    'subtotal': row["subtotal"], 'percentage_change': percentage_change})

        # Calculate the total purchase price
        total_price += row["subtotal"]
    # Render the HTML template with the items and total price
    return render_template('pending_purchase.html', items=items, total_price=total_price)



