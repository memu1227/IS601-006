<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Megha Murthy (mm2836)</td></tr>
<tr><td> <em>Generated: </em> 2/19/2023 10:55:32 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-1-tracker-app/grade/mm2836" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/219969902-e5048fef-4aa4-4ae0-a860-e6ebe51ee7db.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of updated add task code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/219970163-933f03bf-1ecd-406e-9cb7-916eaf5ffb43.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message after adding task successfully and not successfully<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <p>The lastActivity was updated with datetime.now(), where the .now() function returns the current<br>date and time of the system (in this case, the time shown on<br>my PC).<br>Since the task template is a dictionary with key-value pairs (&quot;name&quot;: &quot;&quot;,<br>etc.), the name, description, and due date were set in this function by<br>initializing the items in the dictionary by attaching values to the keys (name,<br>description, due, etc.), similar to what was done when updating the lastActivity. The<br>due date was set by calling the predefined str_to_datetime function. If the user<br>inputs a value for name, description, and due date, the task will be<br>appended to a list (pre-initialized above). If one or more of the information<br>is missing, the system will print an error message. This was done by<br>using an if/else loop.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/219971048-4e1f1d06-b1f0-4492-b7ba-df280169d85c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for process update<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <p>Since the index is already adjusted when the user inputs the index value,<br>we have to ensure that the user doesn&#39;t input a value of 0<br>or less for the input or a value thats greater than or equal<br>to the length of the number of tasks in the list view. This<br>is done using an if statement. The task was found by it&#39;s index<br>by setting the variable task equal to the index value in the predefined<br>tasks list that was recently appended to when adding new tasks. The todo&#39;s<br>in each print statement were replaced using the correct curly brace ({ })<br>format.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/220000721-c7fbd865-cdb5-4f2b-9d80-7217de1829d8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for updating task<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/219979538-f429b13a-e4cb-4c7d-acec-2577bcc6d5e4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Terminal Ouput<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <p>Since the index is already adjusted when the user inputs the index value,<br>we have to ensure that the user doesn&#39;t input a value of 0<br>or less for the input or a value thats greater than or equal<br>to the length of the number of tasks in the list view. This<br>is done using an if statement. The task was found by it&#39;s index<br>by setting the variable task equal to the index value in the predefined<br>tasks list that was recently appended to when adding new tasks. The lastActivity<br>was updated with datetime.now(), where the .now() function returns the current date and<br>time of the system (in this case, the time shown on my PC).<br>Since<br>the task template is a dictionary with key-value pairs (&quot;name&quot;: &quot;&quot;, etc.), the<br>name, description, and due date were updated in this function by initializing the<br>items in the dictionary by attaching values to the keys (name, description, due,<br>etc.), similar to what was done when updating the lastActivity. The due date<br>was set by calling the predefined str_to_datetime function.&nbsp;If any of the values for<br>name, description, due date were changed or just rewritten, the task would be<br>updated. If all the values were left blank, the task would not be<br>updated. This was done using an if loop to check if the user<br>inputed a value for either the name or the description or the due<br>date.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/219981731-2d91d635-47f8-4562-a713-31c7c916b1a2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code ss<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/219981828-a081b8b8-4f54-4e6f-a597-820cbe392b70.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows the code running<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <p>Since the index is already adjusted when the user inputs the index value,<br>we have to ensure that the user doesn&#39;t input a value of 0<br>or less for the input or a value thats greater than or equal<br>to the length of the number of tasks in the list view. This<br>is done using an if statement. The task was found by it&#39;s index<br>by setting the variable task equal to the index value in the predefined<br>tasks list that was recently appended to when adding new tasks. Since there<br>is a &quot;done&quot; value in the task dictionary (from the template at the<br>beginning of the code that is set to false), I used an if<br>loop to check that the task at the specified index wasn&#39;t marked as<br>done, and if it wasn&#39;t, set the date time to the current time<br>on the system using datetime.now(). This marks it as done. If it&#39;s already<br>marked as done (done is set to True), it should output a message<br>saying that the task has already been completed.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/219984024-31f2212f-af5d-460d-970e-d744e0392935.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code SS<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/219984973-97f1008f-b4ef-4753-8066-314a4afb572a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/219985074-a953a320-bf8b-4ec8-b29e-604a7e276e12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>List of tasks<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/219985763-8244cfd2-54d3-450b-b2bb-7a69377cee48.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/219985943-0452831a-6d92-427e-a172-6fc223a8fd08.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows task was deleted successfully (message + list view)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <p>Since the index is already adjusted when the user inputs the index value,<br>we have to ensure that the user doesn&#39;t input a value of 0<br>or less for the input or a value thats greater than or equal<br>to the length of the number of tasks in the list view. This<br>is done using an if statement. The task was found by it&#39;s index<br>by setting the variable task equal to the index value in the predefined<br>tasks list that was recently appended to when adding new tasks. The task<br>was deleted using the pop function to delete the task at the index<br>prompted by the user input. To check for a successful removal, the task<br>was checked to make sure it is no longer in the overall tasks<br>list. If it was successfully removed, the function would print out that the<br>task was removed successfully. This was done using an if else statement.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/219989872-3d96ff87-8054-494f-ba9c-93d0035e87f7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/219990076-07e1143c-0b16-4a89-93df-1a7852d21352.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code shows incomplete tasks and then the message about no tasks after i<br>marked all tasks as done <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <p>Used a for loop to loop through each task in the tasks list<br>and if they were not marked as done, it would append it to<br>a separate list that would be passed on to the list_tasks function to<br>display after the incomplete function is called. If all tasks were marked as<br>done, the output would just print out that there were no tasks to<br>show.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/220001167-a00f2360-79c7-4c6f-8783-ad16d5803164.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/220001061-a3e69d34-485e-4a6e-8922-1dd5901f4e0a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <p>Used a for loop to loop through each task in the tasks list.<br>if the task was not marked as done and the due date has<br>already passed, the function will append the task to a separate list that<br>would be passed on to the list_tasks function to display after the overdue<br>function is called. The output will print out any overdue tasks and if<br>there are no over due tasks, it will show that are no tasks<br>to show.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/220002837-ff678785-a406-4137-a091-c02557759e43.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/220002718-65393889-9902-489b-8632-a9d8622b3add.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <p>Since the index is already adjusted when the user inputs the index value,<br>we have to ensure that the user doesn&#39;t input a value of 0<br>or less for the input or a value thats greater than or equal<br>to the length of the number of tasks in the list view. This<br>is done using an if statement. The task was found by it&#39;s index<br>by setting the variable task equal to the index value in the predefined<br>tasks list that was recently appended to when adding new tasks. The difference<br>in time between the due date and the current date was calculated by<br>simple subtraction of the due date and the current date. The difference was<br>then converted to seconds and checked to see (via if/else statement) if the<br>total seconds in the difference is less than 0, which means that the<br>task is overdue. If it is overdue, then the absolute value was taken<br>in order to be used for calculations in figuring out how much time<br>has passed or how much time is remaining for the task. If the<br>task is overdue, the printed statement would print out by how much time<br>the task is overdue in days, hours, minutes, and seconds. This calculation was<br>done using the 60 seconds in a minute, 60 minutes in an hour<br>calculations and the modulus function to find the seconds or minutes remaining after<br>converting the time diff to seconds or minutes.&nbsp; If the task isn&#39;t overdue<br>the print statement will print out the time remaining using the same calculation<br>as above.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/220005014-6e5e7ffe-9339-4062-b7fe-235e114ff1de.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>From the terminal<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/220005135-3a9c70a4-2cf3-450b-a7f5-c6f7f62ddb87.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>JSON file with data from the result of the output of the ss<br>above<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <p>One of the main issues I had was just handling the data types<br>and comparing data types (string vs datetime) as well as the indexing. I<br>figured out how to fix this issue by just converting any datetime values<br>to a string first and then passing it thru the str_to_datetime function. This<br>seemed to solve most of the issues. Honestly, the debugging probably helped teach<br>me more of the logic behind the code than anything.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/9#issue-1587006645">https://github.com/memu1227/IS601-006/pull/9#issue-1587006645</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-1-tracker-app/grade/mm2836" target="_blank">Grading</a></td></tr></table>