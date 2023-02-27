<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Megha Murthy (mm2836)</td></tr>
<tr><td> <em>Generated: </em> 2/27/2023 12:37:02 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/m4-simple-calc/grade/mm2836" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sum-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/221473034-e7de4600-48ca-41eb-95d0-c6ac193b0175.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Addition<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/221473165-c4f0f2a0-8d73-4291-8cce-4c6d114c5d43.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Subtraction<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/221473269-57331744-d4f0-45bb-806f-5aaf488dc677.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Multiplication<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/221473398-ae235a0c-a766-4be6-86c6-28da525c237e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Division<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/221474143-3a099ad2-02f7-4d14-bf13-795430f476e5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Addition test case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/221473697-35484e53-2850-4ca8-aacd-c2b375ae8a51.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/221477049-55f7870a-0a80-4658-832d-777a8133d2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Add Ans<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/221473697-35484e53-2850-4ca8-aacd-c2b375ae8a51.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/221475987-13f9691e-eb06-4c25-aa59-9a0f2c669f22.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Subtraction<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/221473697-35484e53-2850-4ca8-aacd-c2b375ae8a51.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/221476973-93c4c397-9803-44fd-a842-50d4fce7fc05.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Sub Ans<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/221473697-35484e53-2850-4ca8-aacd-c2b375ae8a51.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/221476210-6cbf63d3-da17-4f14-b869-a8a1bf76bee6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Multiplication<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/221473697-35484e53-2850-4ca8-aacd-c2b375ae8a51.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/221476889-e3a57f4b-92b5-40da-9f1a-c7dae33690b9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Mult Ans<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/221473697-35484e53-2850-4ca8-aacd-c2b375ae8a51.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/221476341-87fb0286-e95c-49c7-aedc-4cde11a9dafe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Division<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/221473697-35484e53-2850-4ca8-aacd-c2b375ae8a51.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/221476760-b190774d-402d-42dd-aafb-19e35c4510aa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Div Ans<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/221473697-35484e53-2850-4ca8-aacd-c2b375ae8a51.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing in pytest<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>I learned classes are useful for creating objects and properties. Different functions can<br>also be created for each object and overall classes just help to organize<br>code.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>Test cases make the testing process more automated. It&#39;s essentially just a more<br>convenient and quicker way of testing your code to see if it meets<br>the requirements and does what it is expected to do. In. the case<br>of this calculator assignment, the test cases just checked to see if your<br>code could perform the basic mathematic operations and give the correct outputs to<br>those mathematic operations regardless of whether the numbers were positive or negative.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/memu1227/IS601-006/pull/11#issue-1600513867">https://github.com/memu1227/IS601-006/pull/11#issue-1600513867</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/m4-simple-calc/grade/mm2836" target="_blank">Grading</a></td></tr></table>