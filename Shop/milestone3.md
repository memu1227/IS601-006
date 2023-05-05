<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 Shop Project</td></tr>
<tr><td> <em>Student: </em> Megha Murthy (mm2836)</td></tr>
<tr><td> <em>Generated: </em> 5/5/2023 2:07:39 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-3-shop-project/grade/mm2836" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Orders will be able to be recorded </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Orders table with valid data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/235513864-091f4693-2450-470d-8c7e-be868887353c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Orders table from VSCode db<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of OrderItems table with validate data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/235528606-89156c98-ae98-499b-bcdc-aa9c4ced660f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Valid Data in OrdersItems table based on orders table <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the purchase form UI from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/236381204-a23abe12-4e87-4ecb-b014-b9997960199e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Purchase form UI from Heroku (pending purchase page bc it was easier to<br>put it there since if you checkout without the cart being updated, it<br>would send a message, and you can also go back to the cart<br>to update the cart easily... it just made sense to me)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot showing the items pending purchase from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/236381356-1d2359ad-168b-4769-b745-5e617774982a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Pending Purchase Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a screenshot showing the Order Process validations from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/236323023-a235baba-fd3e-4313-b84c-45aecdfb169a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Order Process Validations from the Code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a screenshot showing the Order Process validations from the UI (Heroku)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/236381437-f9d3d39f-3a1d-4089-8a08-b1af49ff8da3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Price Difference Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/236381641-a2f8dc22-9c54-4fa2-904b-bcbb0d20f542.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Unavailable Stock Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/236381774-8c4d8dc8-8007-444f-b5fc-32f28f85c77a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid Money Received<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly describe the code flow/process of the purchase process</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>User adds items from shop to cart<div>2) User goes to cart and<br>clicks order<br>3) Takes user to order form/pending purchase page</div><div>4) User can see if<br>there are any price differences from when they last put an item in<br>the cart to what the price of the item is now</div><div>5) User fills<br>out form, if any of the fields are left blank, they wont be<br>able to submit the form or checkout. If everything is filled out correctly<br>but the cart hasnt been updated with respect to the price changes of<br>the items in the cart, a message will tell the user to go<br>back and refresh the cart. If the amount the user pays is less<br>than what the total is, a message will tell the user they can&#39;t<br>afford to make that purchase. If the user spends more than the total,<br>a message will tell the user that they will be receiving some change<br>back. (Honestly I did this just to check to see what happens I<br>probably couldve just done an equality check but this was more fun).&nbsp;</div><div>6) If<br>the user adds more items than is available (quantity of item in cart<br>&gt; stock), message will show that there arent that many available items in<br>stock<br>7) For payment method, I created a list of viable options and if<br>the user doesn&#39;t choose one from the list, theyll get a method showing<br>that the payment method is viable and to choose one from the list<br>(which will be printed with the message).</div><div>8) User checkouts out and gets to<br>confirmation page.&nbsp;</div><br></li><br></ol><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/59">https://github.com/memu1227/IS601-006/pull/59</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mm2836-prod.herokuapp.com/cart">https://is601-mm2836-prod.herokuapp.com/cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Order Confirmation Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot showing the order details from the purchase form and the related items that were purchased with a thank you message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/236334778-9e9bc5ef-16a3-4f0e-92c5-0b82487f7dbb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Orders Table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/236334938-4c08edc6-494b-4105-9122-ceba4b65ca00.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Order Items Table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/236335408-71729bfb-e6ee-4942-a8f6-9bf33b052df5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Order Confirmation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how this information is retrieved and displayed from a code logic perspective</td></tr>
<tr><td> <em>Response:</em> <p>In the python script, sql queries using the select keyword are used to<br>select the order based on the order id and user id for the<br>order confirmation page and the detailed orders view. This basically fetches the items<br>and then the variables are set by adding it to a list and<br>sending that list to the html template through the render_template(). Within that specified<br>template, the actual details can be shown because the html template is essentially<br>what is shown to the user. The data is inserted into the table<br>using the insert keyword and this creates an entry. The update keyword is<br>used to update the items table to reflect changes to quantity and stock.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/56">https://github.com/memu1227/IS601-006/pull/56</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mm2836-prod.herokuapp.com/purchase">https://is601-mm2836-prod.herokuapp.com/purchase</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> User will be able to see their Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history for a user</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/236335935-0f2e07cf-52c2-476a-9570-7d5b2c3694c9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Purchase History for User<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/236350609-055486f4-b551-4b38-b9bd-0aedd0b5db5e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Order Details Page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/236352795-a3dda75f-74f9-40dd-88e5-7938fe1c9c9c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for Detailed View<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details</td></tr>
<tr><td> <em>Response:</em> <p>The order view just shows the order details of a specific order from<br>a list. This is unique to each user and users can view their<br>order history. This is done by just fetching the data from the orders<br>table where the user_id is the user id of the current user. This<br>way, only the logged in user can see their purchase history and the<br>order details is fetched using the order id for which that order refers<br>to from the database. So essentially, the full list of user orders uses<br>the user id to fetch all the orders that the current user has<br>ordered. The order details page uses the order_id of each individual order to<br>get the details.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/57">https://github.com/memu1227/IS601-006/pull/57</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mm2836-prod.herokuapp.com/detailed_order?id=13">https://is601-mm2836-prod.herokuapp.com/detailed_order?id=13</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Store Owner Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history from multiple users</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/236363454-48a55b53-ee62-48d5-916d-dcd455ee1fe0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Purchase history of multiple users (mm321 and percyjackson and harrypotter)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/236363587-6309459c-adc3-4f51-b8c8-5b6c573556be.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Full details of the purchase<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details (mostly how it differs from the user's purchase history feature)</td></tr>
<tr><td> <em>Response:</em> <p>This purchase history doesn&#39;t use the current user_id to fetch all the order<br>history. It basically just grabs all the orders from the orders table without<br>filtering for the user_id. To show the username, the users table is joined<br>onto the orders table so the username can also be displayed. The order<br>details works the same way as the user&#39;s order details table since the<br>detail of an order doesn&#39;t necessarily change. Basically its the same code as<br>the user order history, but the store owner&#39;s purchase history page doesn&#39;t have<br>a where clause to filter for user_id.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/58">https://github.com/memu1227/IS601-006/pull/58</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mm2836-prod.herokuapp.com/purchase_history">https://is601-mm2836-prod.herokuapp.com/purchase_history</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart page showing the button to place an order</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/236380844-f7f34b24-302a-44e6-a2d5-44ade02cfd96.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart with Order Button<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Honestly, this assignment wasn&#39;t too bad. I did struggle a bit with the<br>pending purchase page and the percent differences and also trying to get the<br>order details for the store owners to show up. Once i realized that<br>i didn&#39;t have to make separate functions of the order details and that<br>it didn&#39;t require filtering with user_id as well, I could jsut use the<br>same order function as the users to view the store owner&#39;s detailed order<br>page. The percent differences, I was mostly confused as to why the subtotals<br>weren&#39;t really changing in the cart after changing the prices but this was<br>not really an issue and more of a misunderstanding of what the assignment<br>expected, which was cleared by the professor. I think this whole shop assignment<br>in general was easier to complete than burger machine.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-3-shop-project/grade/mm2836" target="_blank">Grading</a></td></tr></table>