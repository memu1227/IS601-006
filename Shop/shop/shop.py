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
                result = DB.update("UPDATE IS601_S_Items set name = %s, description = %s, category = %s, stock = %s, cost = %s, image=%s WHERE id = %s",
                form.name.data, form.description.data, form.category.data, form.stock.data, form.cost.data, form.image.data, form.id.data)
                if result.status:
                    flash(f"Updated {form.name.data}", "success")
            except Exception as e:
                print("Error updating item", e)
                flash(f"Error updating item {form.name.data}", "danger")
        else: # it's a create
            try:
                result = DB.update("""INSERT INTO IS601_S_Items (name, description, category, stock, cost, image) 
                VALUES (%s,%s,%s,%s,%s,%s)""",
                form.name.data, form.description.data, form.category.data, form.stock.data, form.cost.data, form.image.data)
                if result.status:
                    flash(f"Created {form.name.data}", "success")
                    form = ItemForm() # clear form
            except Exception as e:
                print("Error creating item", e)
                flash(f"Error creating item {form.name.data}", "danger")
    if id:
        try:
            result = DB.selectOne("SELECT id, name, description, category, stock, cost, image, visibility FROM IS601_S_Items WHERE id = %s", id)
            if result.status and result.row:
                    form.process(MultiDict(result.row))
        except Exception as e:
            print("Error fetching item", e)
            flash("Item not found", "danger")
    return render_template("item.html", form=form, type=type)

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
    return render_template("item.html", row = row, form = form)

'''
UCID: mm2836, Date Implemented: 04/24/23
'''

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
        result = DB.selectAll("SELECT id, name, description, category, stock, cost, image, visibility FROM IS601_S_Items LIMIT 25",)
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
    name = request.args.get('name')
    category = request.args.get('category')
    stock = request.args.get('stock')
    cost = request.args.get('cost')
    column = request.args.get('column')
    order = request.args.get('order')
    query = "SELECT i.id, i.name, i.description, i.category, i.stock, i.cost, i.image, i.visibility FROM IS601_S_Items i WHERE i.stock > 0"
    args = {}
    allowed_columns = ["name","category","stock","cost"]
    if name:
        query += " AND i.name like %(name)s"
        args["name"] = f"%{name}%"
    if category:
        query += " AND i.category like %(category)s"
        args["category"] = category
    if stock:
        query += " AND i.stock = %(stock)s"
        args["stock"] = stock
    if cost: 
        query += "AND i.cost = %(cost)s"
        args["cost"] = cost
    if column and order:
        if column in allowed_columns and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order} "
    try:
        query += " LIMIT 25"
        result = DB.selectAll(query,args)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error fetching items", e)
        flash("There was a problem loading items", "danger")
    allowed_columns_list = [(value, value) for value in allowed_columns]
    return render_template("shop.html", rows=rows, allowed_columns=allowed_columns_list)
'''
UCID: mm2836, Date: 04/23/23
'''
    

@shop.route("/cart", methods=["GET","POST"])
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