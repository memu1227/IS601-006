from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
import pycountry
company = Blueprint('company', __name__, url_prefix='/company')

@company.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count as employees for the company
    # don't do SELECT *
    
    query = """SELECT companies.id,companies.name,companies.address,companies.city,companies.state,companies.zip,companies.website,
    COUNT(employee.id) as 'employees' FROM IS601_MP3_Companies companies LEFT JOIN IS601_MP3_Employees employee
    ON employee.company_id = companies.id WHERE 1=1"""
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    order_options = ['asc','desc']
    # TODO search-2 get name, country, state, column, order, limit request args
    name = request.args.get('company_name')
    country = request.args.get('country')
    state = request.args.get('state')
    column = request.args.get("column")
    order = request.args.get('order')
    limit = request.args.get('limit',default=10, type = int)
    # TODO search-3 append a LIKE filter for name if provided
    if name:
        query += " companies.name LIKE %(company_name)s"
        args["company_name"] = f"%{name}%"
    # TODO search-4 append an equality filter for country if provided
    if country:
        query += " AND companies.country = %(country)s"
        args["country"] = f"%{country}%"
    # TODO search-5 append an equality filter for state if provided
    if state:
        query += " AND companies.state = %(state)s"
        args["state"] = f"%{state}%"
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    if column in allowed_columns and order in order_options:
        query += f" ORDER BY {column} {order}"
    '''
    UCID: mm2836, Date Implemented: 04/08/23
    '''
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    query += " LIMIT %(limit)s"
    args["limit"] = limit
    try:
        limit = int(limit)
        if limit >= 100 or limit < 1:
            flash("Invalid Limit. Limit must be between 1 and 100","error")
            limit = 10
        query += " LIMIT %(limit)s" # TODO change this per the above requirements
        args["limit"] = limit
        print("query",query)
        print("args", args)
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    except ValueError:
        flash("Limit must be an integer","error")

    try:
        result = DB.selectAll(query, args)
        #print(f"result {result.rows}")
        if result.status:
            rows = result.rows
            print(f"rows {rows}")
    except Exception as e:
        # TODO search-9 make message user friendly
        flash(f"There was an error running the query: {str(e)}", "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    allowed_columns_list = [(value, value) for value in allowed_columns]
    return render_template("list_companies.html", rows=rows, allowed_columns=allowed_columns_list)
    '''
    UCID: mm2836, Date Implemented: 04/08/23
    '''
@company.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        name = request.form.get('name', type = str)
        address = request.form.get('address',type = str)
        city = request.form.get('city',type = str)
        state = request.form.get('state',type = str)
        country = request.form.get('country',type = str)
        zipcode = request.form.get('zipcode',type = str)
        website = request.form.get('website',type = str)

        # TODO add-2 name is required (flash proper error message)
        has_error = False # use this to control whether or not an insert occurs
        if not name:
            flash(f"Company Name is Required", "danger")
            has_error = True
        # TODO add-3 address is required (flash proper error message)
        if not address:
            flash(f"Address is Required", "danger")
            has_error = True
        # TODO add-4 city is required (flash proper error message)
        if not city:
            flash(f"City is Required", "danger")
            has_error = True
        # TODO add-5 state is required (flash proper error message)
        if not state:
            flash(f"State is Required", "danger")
            has_error = True
        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        # hint see geography.py and pycountry documentation
        elif country and state not in [s.name for s in pycountry.subdivisions.get(country_code=country)]:
            flash(f"Invalid state", "danger")
            has_error = True
        '''
        UCID: mm2836, Date Implemented: 04/08/23
        '''
        # TODO add-6 country is required (flash proper error message)
        if not country:
            flash(f"Country is required", "danger")
            has_error = True
        # TODO add-6a country should be a valid country mentioned in pycountry
        elif country not in [c.alpha_2 for c in pycountry.countries]:
            flash(f"Invalid country", "danger")
            has_error = True
        # hint see geography.py and pycountry documentation
        # TODO add-7 website is not required
        if not website:
            website = None
            has_error = False
        # TODO add-8 zipcode is required (flash proper error message)
        if not zipcode:
            flash(f"Zipcode is required.", "danger")
            has_error = True
        # note: call zip variable zipcode as zip is a built in function it could lead to issues

        
        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Companies
                (name, address, city, country, state, zipcode, website) 
                VALUES(%s, %s, %s, %s, %s, %s, %s)
                """, name, address, city, country, state, zipcode, website) # <-- TODO add-8 add query and add arguments
                if result.status:
                    flash("Added Company", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                flash(f"There was an error adding the company: {str(e)}", "danger")
        
    return render_template("add_company.html")
    '''
    UCID: mm2836, Date Implemented: 04/08/23
    '''
@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get("id") or False
    if not id: # TODO update this for TODO edit-1
        flash(f"ID is Required.","danger")
    else:
        if request.method == "POST":
            data = {"id": id} # use this as needed, can convert to tuple if necessary
            # TODO edit-1 retrieve form data for name, address, city, state, country, zip, website
            name = request.form.get('name', type = str)
            address = request.form.get('address',type = str)
            city = request.form.get('city',type = str)
            state = request.form.get('state',type = str)
            country = request.form.get('country',type = str)
            zipcode = request.form.get('zipcode',type = str)
            website = request.form.get('website',type = str)
            # TODO edit-2 name is required (flash proper error message)
            has_error = False # use this to control whether or not an insert occurs
            if not name:
                flash(f"Company Name is Required", "danger")
                has_error = True
            # TODO add-3 address is required (flash proper error message)
            if not address:
                flash(f"Address is Required", "danger")
                has_error = True
            # TODO add-4 city is required (flash proper error message)
            if not city:
                flash(f"City is Required", "danger")
                has_error = True
            # TODO add-5 state is required (flash proper error message)
            if not state:
                flash(f"State is Required", "danger")
                has_error = True
            # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
            # hint see geography.py and pycountry documentation
            elif country and state not in [s.name for s in pycountry.subdivisions.get(country_code=country)]:
                flash(f"Invalid state", "danger")
                has_error = True
            '''
            UCID: mm2836, Date Implemented: 04/08/23
            '''
            # TODO add-6 country is required (flash proper error message)
            if not country:
                flash(f"Country is required", "danger")
                has_error = True
            # TODO add-6a country should be a valid country mentioned in pycountry
            elif country not in [c.alpha_2 for c in pycountry.countries]:
                flash(f"Invalid country", "danger")
                has_error = True
            # hint see geography.py and pycountry documentation
            # TODO add-7 website is not required
            if not website:
                website = None
                has_error = False
            # TODO add-8 zipcode is required (flash proper error message)
            if not zipcode:
                flash(f"Zipcode is required.", "danger")
                has_error = True
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            # populate data dict with mappings
            data = {
                "id": id,
                "name": name,
                "address": address,
                "city": city,
                "state": state,
                "country": country,
                "zipcode": zipcode,
                "website": website
            }
            '''
            UCID: mm2836, Date Implemented: 04/08/23
            '''
            
            if not has_error:
                try:
                    # TODO edit-9 fill in proper update query
                    # name, address, city, state, country, zip, website
                    result = DB.update("""
                    UPDATE IS601_MP3_Companies
                    SET name = %s, address = %s, city = %s, country = %s, state = %s,
                    zipcode = %s, website = %s
                    WHERE id = %s
                    """, data)
                    if result.status:
                        print("updated record")
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-10 make this user-friendly
                    print("Records were not updated. {e}")
                    flash(f"Record were not updated: {str(e)}", "danger")
        row = {}
        try:
            # TODO edit-11 fetch the updated data
            result = DB.selectOne("SELECT name, address, city, country, state, zipcode, website FROM IS601_MP3_Companies WHERE id = %s", id)
            if result.status:
                row = result.row
                
        except Exception as e:
            # TODO edit-12 make this user-friendly
            flash(f"Data was not fetched properly: {str(e)}", "danger")
    # TODO edit-13 pass the company data to the render template
    return render_template("edit_company.html", company = row)
    '''
    UCID: mm2836, Date Implemented: 04/08/23
    '''
@company.route("/delete", methods=["GET"])
def delete():
    # TODO delete-6 if id is missing, flash necessary message and redirect to search
    if not request.args.get('id'):
        flash(f"Company ID is Required", "danger")
        return redirect(url_for("company.search"))
    else:
    # TODO delete-5 for all employees assigned to this company set their company_id to None/null
        DB.update("""UPDATE IS601_MP3_Employees SET company_id = %s where company_id = %s""", None, id)
        # TODO delete-1 delete company by id (unallocate any employees see delete-5)
        result = DB.delete("DELETE FROM IS601_MP3_Companies WHERE id = %s", id)
        if result.status:
            # TODO delete-4 ensure a flash message shows for successful delete
            flash("Company record has been deleted.", "success")
    # TODO delete-3 pass all argument except id to this route
    args = request.args.copy()
    args.pop("id")
    # TODO delete-2 redirect to employee search
    return redirect(url_for("company.search", **args))
    pass
    '''
    UCID: mm2836, Date Implemented: 04/08/23
    '''
    