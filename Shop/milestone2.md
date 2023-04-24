<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Megha Murthy (mm2836)</td></tr>
<tr><td> <em>Generated: </em> 4/24/2023 1:07:07 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-2-shop-project/grade/mm2836" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233854996-ff27dd31-a617-4cad-ad23-fd8a96db6a1a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin page for creating items<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233860749-b7be8757-41dc-4f37-a0c7-95559b038235.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Products Table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <p>&nbsp;The user, who has the role of an admin, can add a product<br>by filling in a form which includes the name, category, stock, cost, image<br>(optional), and description of the project. Once the user clicks on &quot;Add&quot; ,<br>the information is sent to the backend where validation of the data occurs.<br>This entails checking to see if the fields are filled in or if<br>the values are valid.&nbsp; Once the data is validated, it gets sent to<br>the database via the SQL queries for inserting or updating data. If the<br>data is stored in the database, then it sends a message stating that<br>it was successful. This message will eventually get back to the admin so<br>that they know their entry of a new product has been successful (or<br>a failure, depending).&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/49">https://github.com/memu1227/IS601-006/pull/49</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mm2836-prod.herokuapp.com/admin/item">https://is601-mm2836-prod.herokuapp.com/admin/item</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233863192-78e8526b-9950-4525-8ce2-9734eea4491f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First Four Items from nonadmin shop page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233863278-14e12bf3-504d-4fca-a412-b99b60712124.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Items 5-8 from nonadmin shop page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233863322-75390606-76a8-47ab-954e-37fa82f53cf6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Last two items from nonadmin shop page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233875114-1bd37c71-ff57-4c00-b824-49e4ac970516.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Filtering and Sorting on the Shop Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233875222-cba00643-3d94-44bb-8cf6-d9a1b2180b91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code from shop.html<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233875275-e79ca963-2fbd-421b-9ff2-dd6e5be2be7e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code from Shop.py<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <p>So the user can see the fields that they can sort and filter<br>on. Once the user chooses how they want to sort/filter the products, the<br>Flask application (shop.py) puts together a query based on the user&#39;s inputs. It<br>then executes the query and sends out a list of the sorted and<br>filtered items.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/50">https://github.com/memu1227/IS601-006/pull/50</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mm2836-prod.herokuapp.com/shop">https://is601-mm2836-prod.herokuapp.com/shop</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233880213-1f472920-e166-4519-b5c6-f7d6e7ff040a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Products List<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <p>All the items are stored in and retrieved from the database. The selectAll<br>method in db.py executes the query, retrieves all the items, returns it as<br>an object and displays them to the admin. If they are successfully retrieved,<br>they are stored in rows, which is then passed onto the items.html, which<br>displays the items in each row.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/48">https://github.com/memu1227/IS601-006/pull/48</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mm2836-prod.herokuapp.com/admin/items">https://is601-mm2836-prod.herokuapp.com/admin/items</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/234055395-93a4a44b-227f-44c4-9b18-86da08d10f9a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shop Page Edit button for Admins<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/234057604-e8ea2815-3668-49d2-930c-6948a99872e6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product View Page with Edit Button<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233886663-942c5370-e713-49c2-a657-cb16912e8ea8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit button on product list page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233887139-d2139c79-4d40-42b9-9ccb-42c5e923ba3d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233887525-12e6c4d4-2c24-4129-9881-ee2f8d4cdffa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Edit (description changed)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>When the edit form is submitted, if the item exists, the function uses<br>the db.update method to update the items in the database using the update<br>keyword. If the item isn&#39;t in the database (checks to see if item<br>id is in the database), then the function uses the insert keyword with<br>the db.update method to add the item to the database. In this case,<br>we are editing an already existing item, so it just uses the update<br>keyword to change any of the fields the admin changed.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/51">https://github.com/memu1227/IS601-006/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mm2836-prod.herokuapp.com/admin/item?id=1">https://is601-mm2836-prod.herokuapp.com/admin/item?id=1</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/234058381-99d186c7-44f6-4817-ad34-43c591554c79.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Clickable product name to go to product details page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/234058552-c7414f1f-4cca-4c1a-96ba-7ed32a9b3e13.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results of Product Detailed Page (without edit button as was shown for admins)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/234059189-0ccc0046-ff72-408b-854f-bfacbb89e9c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for detailed view page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>The code was essentially the same as updating an item. Except this time,<br>I removed the save button since the user nor admin need that button<br>and I added an edit button to the detailed view page if the<br>user was an admin. The fields were prefilled by getting the form data<br>in the code (attached in the screenshot). Essentially, it works the same as<br>the edit page minus the save button.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/51">https://github.com/memu1227/IS601-006/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mm2836-prod.herokuapp.com/detailed_view?id=3">https://is601-mm2836-prod.herokuapp.com/detailed_view?id=3</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233887942-e56f73d2-93e2-4c09-98a2-de012c35a3f2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233888199-f4c50188-9c8b-4163-9728-b6ade73cc3ac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Can&#39;t shop and add to cart if not logged in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233888428-46bf2fc6-791d-41b9-ac12-dd0a5cbdd213.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Carts Table with some records<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>There is only one cart per user. The cart saves even if you<br>log out and log back in.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <p>The item id, quantity, and cost are stored in the carts table.&nbsp; if<br>the item id and user id already exists in this table, then any<br>updates to the quantity of an item gets updated accordingly. If the user<br>id and item id doesnt exist in the carts table, then a new<br>row/entry is created. The db.selectOne method is used to retrieve the item name<br>and cost and the insert and update keywords are used to either update<br>the quantity/cost if the item already exists in the database, or create a<br>new entry. A message will be flashed for successful updates or insertion and<br>the list of items in the cart is retrieved using the selectAll db<br>method.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/48">https://github.com/memu1227/IS601-006/pull/48</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/234062651-fd0a2831-9e0f-4c35-ac74-1704ec95dfde.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added a view cart button on <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/234063380-58338703-159e-45e7-ad97-a83dd141b5c8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>View Cart View with links to product detailed view on each item<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <p>The cart code checks to see if the user_id and&nbsp; item id are<br>present and it they are, it retrieves the name of the item using<br>a select query based on the id.&nbsp; Using the item_id the code updates<br>the quantity and cost using an UPDATE query. if the item id doesn&#39;t<br>exist, it adds the item to the cart using a CREATE query. It<br>then sends a message saying the item was added successfully to the cart.<br>Regarding the quantity, if the quantity isn&#39;t a positive number, it just gets<br>deleted from the cart. The cost is calculated by doing quantity * cost<br>per item. The subtotal and total is then displayed to the user after<br>it is passed through cart.html, which creates rows to display the information.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/51">https://github.com/memu1227/IS601-006/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mm2836-prod.herokuapp.com/cart">https://is601-mm2836-prod.herokuapp.com/cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233888765-31dd029d-def9-4f94-b06a-51e21daf7543.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before updating cart quantity <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233888898-7443e82a-6f77-490b-8d22-ae604072dcdb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After updating cart quantity (changed all to 2 and Price also changed)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233888898-7443e82a-6f77-490b-8d22-ae604072dcdb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233889067-b9d784aa-1ef4-4603-a034-52d3c945c381.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After (no items in the cart)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233889286-9005c312-6242-4d1f-bc80-3596c5b3f39b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before I click update<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233889363-ab534601-dbbf-45ce-ab0c-87eb044dfb69.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After I click update<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <p>During the updating process, a value of 0 or negatives simply causes the<br>item to be deleted. This logically makes sense because if you change the<br>value from 2 to 0, its essentially the same thing as deleting the<br>item. Same with the negative. A negative number is not a valid number<br>of items for purchase. Entering in 0 or a negative number just triggers<br>the sql query to delete the item from the database.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/48">https://github.com/memu1227/IS601-006/pull/48</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233889519-42761ea3-fe2e-4e0a-8cd9-84bea3918e39.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting an item<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233889583-a607959f-df2b-4880-9f96-55aa7cd3bae7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deleting an item<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233891109-ae2054f1-6623-4470-9bdc-7a4dbb858157.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before clearing the cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/233891196-9d757886-f252-4347-b0b6-66a0742157ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After clearing the cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <p>The delete process is the same for all of the screenshots above. If<br>you press the x under actions, it deletes the item. If you change<br>the quantity to 0, it deletes the item. If you update the quantity<br>to a negative number, it deletes the item. This is basically done using<br>the db.delete method along with the DELETE sql query.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/48">https://github.com/memu1227/IS601-006/pull/48</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>There were mostly just syntax errors or wrong code placements. Had a bit<br>of difficulty with the edit/product view page but I figured it out in<br>the end by looking at the previous code from prior lessons or just<br>the code that was given to us.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mm2836-prod.herokuapp.com/login">https://is601-mm2836-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-2-shop-project/grade/mm2836" target="_blank">Grading</a></td></tr></table>