<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Megha Murthy (mm2836)</td></tr>
<tr><td> <em>Generated: </em> 4/16/2023 3:20:40 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone1-deliverable/grade/mm2836" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231648910-4c56d26a-1d47-4128-ba86-f4772e424e13.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username not available<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231649322-63d775ac-eeac-45cf-8284-4b148ed66209.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email not available (already registered)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231649765-11d21290-c987-4fa6-9f93-4e0ba6bffd5a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid Email Validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231650388-4692a7c9-e67d-46bd-9ccd-ae401a797ac3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid Password<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231650550-0443ace8-9b93-449b-9c7c-9399fcd460b1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passwords Don&#39;t Match<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231650768-e443a46b-0765-405b-a2ed-64ffceb44c68.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Form Before Submitting<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232165775-439b64ee-dd6e-4632-b5de-3ffe84f14bb7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Valid User Data Present in Row 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/31">https://github.com/memu1227/IS601-006/pull/31</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>Majority of the validation checks comes from forms.py in the auth folder of<br>flask_samples. Essentially, when a user registers for an account, their inputed username is<br>checked against the existing database to see if the username is taken. If<br>it is taken, the user will get a message saying the username isn&#39;t<br>available. This is similar to how the email validation works. With the email,<br>it checks to see if its in the right format by checking if<br>theres an @ sign in the email (checked in forms.py). The password is<br>validated by checking if its a certain length (8 characters) (also checked in<br>forms.py). The password is confirmed by equating it to the password field (also<br>checked in forms.py). Essentially, the code checks against the database to see if<br>data already exists and based on the info in the database, it will<br>pass a message stating whether username/email already exists and validates information based on<br>user input.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232167631-dea2d8a6-4a73-4f09-a65e-2381c5f3a2da.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password mismatch validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232167695-eabd068a-5b09-41c2-b36d-90e9058ee5fd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username not in DB<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232167750-633c70e3-a45d-4085-9c76-44b14a45f2fd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/31">https://github.com/memu1227/IS601-006/pull/31</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>The login behavior is similar to the registration. Since the username/email and password<br>should already exist in the database if the user has already registered, the<br>code just checks to see if the information the user inputs matches up<br>with the information in the database. So, if the username isn&#39;t in the<br>database, a message stating that it&#39;s invalid will pop up. Similarly, if the<br>password doesn&#39;t match what is in the database, an invalid password message will<br>pop up. The login feature mostly just checks against the preexisting database.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232167912-a1cb5a09-db10-4a92-950f-f5ab5b28d8ae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful Logout Message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232168760-04e83aba-929a-459a-8128-44db65b2d37d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Can&#39;t access landing page if logged out<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/31">https://github.com/memu1227/IS601-006/pull/31</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>This process is also part of flask auth, more specifically auth.py. When the<br>user logs out, the session is removed from the server. This is why<br>the user can&#39;t access any pages they could previously access when logged in,<br>because the session no longer exists. Based on the code for the logout<br>route in auth.py, when the user logs out, the session keys set by<br>Flask-Principle are removed and user is set to anonymous. This basically means that<br>the user is no longer logged in or doesn&#39;t have permission to access<br>features they could access when logged in. After logging out, the user is<br>redirected back to the login page.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232168760-04e83aba-929a-459a-8128-44db65b2d37d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Can&#39;t access landing page if logged out<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232260231-d6b45e50-fca4-4bc6-8e77-6632f6e9bab3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Can&#39;t access role protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232265573-3bd77770-b710-445e-bdd7-d77417a50894.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Roles table with Valid Data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232265598-be8ef41a-68b9-4a07-82b2-dc668ccd11f9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>UserRoles Table with valid data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232265738-a26061fd-24f6-46d9-8984-eed5787eb3c8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Users table where 1st row is the admin user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/33">https://github.com/memu1227/IS601-006/pull/33</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>When logged out, the session no longer exists in the server. Therefore, any<br>pages that could previously be accessed when logged in, are no longer accessibly<br>since the user is made anonymous and doesn&#39;t exist in the server since<br>their session was removed.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>If the user isn&#39;t an admin, they won&#39;t be allowed to access the<br>admin features. The permission to access admin features is defined in the roles.py<br>code (<span style="font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px; white-space: pre; color:<br>rgb(220, 220, 170);">@</span><span style="font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px; white-space: pre;<br>color: rgb(156, 220, 254);">admin_permission</span><span style="font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px; white-space:<br>pre; color: rgb(220, 220, 170);">.</span><span style="font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px;<br>white-space: pre; color: rgb(220, 220, 170);">require</span><span style="background-color: rgb(30, 30, 30); color: rgb(212, 212,<br>212); font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px; white-space: pre;">(</span><span style="font-family: Menlo,<br>Monaco, &quot;Courier New&quot;, monospace; font-size: 12px; white-space: pre; color: rgb(156, 220, 254);">http_exception</span><span style="background-color:<br>rgb(30, 30, 30); color: rgb(212, 212, 212); font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace;<br>font-size: 12px; white-space: pre;">=</span><span style="font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px; white-space:<br>pre; color: rgb(181, 206, 168);">403</span><span style="background-color: rgb(30, 30, 30); color: rgb(212, 212, 212);<br>font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px; white-space: pre;">)) </span><div><span style="background-color: rgb(30,<br>30, 30); color: rgb(212, 212, 212); font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size:<br>12px; white-space: pre;">which is initialized in permissions.py. If the user doesn&#39;t have the<br>admin role assigned to them (assignments can be given by adding a specific<br>user to the userroles table), </span></div><div><span style="background-color: rgb(30, 30, 30); color: rgb(212, 212,<br>212); font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px; white-space: pre;">then the exception<br>403 message pops up. So any user that doesnt have the admin role<br>assigned wont have access to admin specific pages. </span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232326671-08ec7889-22fe-4f26-9d5f-08f836599120.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Registration Form<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232326751-b244b913-19be-464f-a0b4-130282ccefec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Navigation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232326845-318823d0-d128-4d62-872e-2ad7072dbb61.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data Output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/22">https://github.com/memu1227/IS601-006/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>Based on the layout.html and nav.html code, the styling utilizes the default bootstrap<br>framework for the general layout. The default layout makes everything easier to see<br>and read. For example, both the header and footer hieghts are fixed at<br>60px and the capitalization for each label is done by using the label<br>tag. For navigation, there are drop down menus for the admin roles so<br>it is more accessible for admins to easily list, assign, and apply roles.<br>This is done using html where the individual headers (profile, admin, etc) are<br>created using list tags.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232260231-d6b45e50-fca4-4bc6-8e77-6632f6e9bab3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error Message for not having access to roles<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232168760-04e83aba-929a-459a-8128-44db65b2d37d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message for not having access to landing page if not logged in<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232167695-eabd068a-5b09-41c2-b36d-90e9058ee5fd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message for invalid username<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/26">https://github.com/memu1227/IS601-006/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>The flash messages are fed into a separate template (flash.html) that returns the<br>category of the message (warning, error, danger, etc.) and the error message itself.<br>The messages were made user friendly by providing the severity of the error<br>(warning, danger) as seen in auth.py and giving concise messages ab the error<br>itself (invalid password, error logging in, etc). These messages are easy to understand<br>the severity is highlighted with colors. For example, a success is highlighted with<br>green, while invalid user is highlighted in yellow. We associate green with good<br>or success, yellow with warning, and red as danger. This color coding and<br>conciseness helps users understand the error (if there is one).&nbsp;&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232328061-c644f803-cf1a-4bdf-b62d-65fae3c42b53.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Profile<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/41">https://github.com/memu1227/IS601-006/pull/41</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>The data about the user is retrieved and displayed in the form using<br>a SELECT SQL query (<span style="background-color: rgb(30, 30, 30); color: rgb(212, 212, 212);<br>font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px; white-space: pre;"> </span><span style="font-family: Menlo,<br>Monaco, &quot;Courier New&quot;, monospace; font-size: 12px; white-space: pre; color: rgb(156, 220, 254);">result</span><span style="background-color:<br>rgb(30, 30, 30); color: rgb(212, 212, 212); font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace;<br>font-size: 12px; white-space: pre;"> = </span><span style="font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size:<br>12px; white-space: pre; color: rgb(78, 201, 176);">DB</span><span style="background-color: rgb(30, 30, 30); color: rgb(212,<br>212, 212); font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px; white-space: pre;">.</span><span style="font-family:<br>Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px; white-space: pre; color: rgb(220, 220, 170);">selectOne</span>&lt;span<br>style=&quot;background-color: rgb(30, 30, 30); color: rgb(212, 212, 212); font-family: Menlo, Monaco, &quot;Courier New&quot;,<br>monospace; font-size: 12px; white-space: pre;&quot;&gt;(</span><span style="font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px;<br>white-space: pre; color: rgb(206, 145, 120);">&quot;SELECT id, email, username FROM IS601_Users where id<br>= </span><span style="font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px; white-space: pre; color:<br>rgb(86, 156, 214);">%s</span><span style="font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px; white-space: pre;<br>color: rgb(206, 145, 120);">&quot;</span><span style="background-color: rgb(30, 30, 30); color: rgb(212, 212, 212); font-family:<br>Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px; white-space: pre;">, </span><span style="font-family: Menlo, Monaco,<br>&quot;Courier New&quot;, monospace; font-size: 12px; white-space: pre; color: rgb(156, 220, 254);">user_id</span><span style="background-color: rgb(30,<br>30, 30); color: rgb(212, 212, 212); font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size:<br>12px; white-space: pre;">)) <br>This SQL query selects the email and username of the<br>user based on the ID from the users table and sets it as<br>the username and email in the profile page so that it is already<br>prefilled.<br>Basically, a SQL query is executed to retrieve and set the username and<br>email on the profile page. </span><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232328789-313a4109-81cf-4107-8a6d-a7802da4cea4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password mismatch message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232328900-eca95d0b-7ca5-40ca-87a6-3c881094c27d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username already taken message/Password validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232329030-7a6db860-c220-41ad-af74-c0c38069037e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful profile saved message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232328542-8e566882-846b-42dd-ad32-706d9aa7a1f2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>1st row before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/232329098-537c566b-5493-4719-92b0-01a244e06fb9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>1st row after edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/41">https://github.com/memu1227/IS601-006/pull/41</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>The process is similar to the login/registration. If the user changes their username<br>and that username already exists in the database, a message about the taken<br>username will pop up. If the password doesnt match the confirm password field,<br>a message about password mismatch will pop up. Same with the email. If<br>the username already exists in the database, a message about the taken email<br>will pop up. This is all validated in auth.py.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>There were no real issues since it was easy to follow along with<br>the lecture slides. It&#39;s always easier to learn the logic while completing this<br>documentation or making mistakes. But, the lecture slides were easy to understand and<br>follow and the recordings also helped.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mm2836-prod.herokuapp.com/login">https://is601-mm2836-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone1-deliverable/grade/mm2836" target="_blank">Grading</a></td></tr></table>