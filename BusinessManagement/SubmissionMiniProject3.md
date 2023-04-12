<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Megha Murthy (mm2836)</td></tr>
<tr><td> <em>Generated: </em> 4/11/2023 11:45:13 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/mm2836" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231343638-39c6a5b7-431f-4213-b898-30b83cbbc91b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Index Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/230253629-b3437280-92a9-4925-8885-e59733040593.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Empty Table for Companies<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/230512518-587f54ae-6ce9-4495-95c2-ad2f5b8c103c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Empty Table for Employees<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/230739116-8e3001a5-2cdf-48fc-a43f-3f1187a29b1b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Checking CSV File<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/230739166-332035c1-1806-4eca-b805-cdd4ffd1c47c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Reading stream as dict and extracting company data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/230739209-ad4d2240-1df3-47dc-acc2-3caeddca032b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Extracting employee data and the flash messages<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/230697545-b5436b70-77f2-48a6-b5ac-576e9c1a1054.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message when file is not a csv file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/230697578-925216b8-ba5e-4c04-96bc-560fcc9200f1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message when no file is attached<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/230738861-d97acc22-b168-4cae-9b3f-d515475f320d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Uploading Companies (after checking for duplicates) and Employee List<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/230739262-e9b64ee8-216a-4ca7-8db5-ed53530f69d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company data uploaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231030040-fd803b75-1858-4841-9155-e22cbed5ea05.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee Data Uploaded<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231032421-45178cfb-57b1-429a-aed1-37f251afed59.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for requiring email, name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231029916-632d39d5-19b3-4f6d-b048-b5e8023a5253.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except block friendly message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231029231-eebd864b-6358-4b2e-a1ea-618eec73efd4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231027648-94f8a80a-b7fb-46ee-a694-d61a57076a63.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First Name Error (At the top)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231027730-5311b4f3-8487-4d12-98f2-b34d653f869e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Last Name Error (At the top)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231027794-89822f13-1c53-433c-a498-e66ece7ffadc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email Error (At the top)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231343517-2aef0f2c-5f8b-45f9-bf5b-e904c1f468bd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Valid Data prior to submission<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231030277-49281e46-5f6d-41ba-90ad-d9b77178d26e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Check Megha Murthy (company = Null)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231024121-d87545c4-ff8b-4d0f-96bb-cf9f73a90fe0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Appending like and equality filters + checking request args <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231024213-b43a1417-76bb-4ea8-801f-aa670774ed3d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>appending limit and sorting and user friendly message <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/230981773-78b4289d-469c-477a-9804-ffc35c0d9f12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First Name Filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/230981982-f353352f-be31-40b2-879d-5a11b700f8b6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Last Name Filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/230982151-d10bbf22-2b83-43f8-bb18-98202abfda97.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email Filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231024320-986a2a4a-bf18-464c-be47-f1da3ed40318.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company Filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231026162-63db0c10-c90e-4fb1-ac74-88060b7ffdd2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Ascending (up)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231026108-fc8354af-223b-43ba-9f7b-6866f669a67a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Descending (down)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231036874-23b98527-34bf-40d5-a023-99f3d32db9f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flash Messages and ID<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231037066-1231dc17-7a39-4e01-92fd-c2c08d3060de.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Queries and Updating Employee<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231307617-fef2f839-b049-46c4-b807-bd2eb9a53715.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data Before Edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231307679-978cb648-1a45-410e-ab3a-ea29a4c07517.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Edit was successful (Company Changed and Email)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231037828-6c0fe3a5-d1b1-4251-bf99-23f37625077a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Changes (Tar Mosely)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231038107-b4931693-40a4-4f68-9b51-45dd701d92c1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Changes (Tar Mosely - email changed and company id changed)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231307436-0333eb80-1946-43ae-a299-f63b2c6c966c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except block and query + website and zip flash messages<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231307338-b5734355-198c-42d6-8767-1e6e86eb9c5f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>requesting forms and flask messages up until city<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231326202-83f28f2e-89ad-4699-b19c-57d7c3d83439.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>State and Country flask messages and validations<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231307839-535206c8-1c4a-4c30-8a91-cc3b7341a840.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error Message for name, address, city, zip <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231326498-f727529f-4dfd-4814-91f2-d01412a1c7e2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error for State <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231307889-936cd9eb-a2d5-4980-8441-88fc9e7e2902.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Prior to Submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231307984-e7fa44c7-d475-4dee-8ee8-9286274b86fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231326740-f640600f-753e-4d84-ab9d-ba1faceab7c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error for Country<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231272872-9c846dbb-9b96-4d37-bbb3-734bfaeb1810.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Penguins Added to companies database<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231051601-f5d494e2-9605-4935-89d6-f090d998e85a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Filtering and Fetching<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231051719-f8b3e38b-c7ff-45c6-82f2-f1151ec03a94.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Limits and Except Block<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231310433-623bf00c-d9ad-418a-a619-09d5e714724c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name Filter Applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231310502-58cc5729-fd6a-46b2-a94b-34e4a24c8461.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Country Filter Applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231310550-5558fcf5-42af-41ad-a936-6c7826b1172b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>State Filter Applied (Rhode Island)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231310626-0f628ec6-f476-440f-8d65-2a4d4a581a61.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Ascending (Up)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231310699-e5b50eab-1dd3-40c6-937f-4a0514f6cf22.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Descending (Down)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231304975-4c683f0a-8a0a-4a81-a16e-0df5cf40148b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except Blocks and Queries<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231311092-0b17018a-cc48-4f54-b363-3fff03985663.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Request Args + Name, City, Address Flask<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231327095-c0420099-824a-4b87-bfdf-fe184fff7d7b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>State and Country Flask Messages and Validation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231311266-1aa7ec7f-2c28-474e-a04a-d6175ba20f91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231311340-8428ca54-8292-4315-b5c1-5531866a0b91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Edit (Penguins took their business to the bahamas and changed their address<br>and created a website for their business needs - so everything changed but<br>the company name)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231280011-9b2bc09e-7812-478f-a60d-0ccf88f34ee4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Company Change (Everything changed but the company name)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231280749-0a8e0b54-40e2-456a-a501-4373d3f87d25.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Company Change<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231058115-0cc96ea8-cc0c-4a95-90fc-ef267876057f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for Delete Route for Employee<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231311955-106f4f29-0461-4b64-afbf-324293551d25.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Deletion for Employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231311991-92fbb8e3-23bd-498e-964d-ed0cbac892a4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Deletion for Employee<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231059166-17f4438a-f17e-4025-86fc-244f6266b174.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for Company Delete Route<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231311753-6412adc8-fcd2-48d7-a87c-39ef2dbd41ee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Deletion for Company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231311844-e6e023b2-648c-419e-be61-c46ad213055d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Deletion for Company<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231327443-02463ccf-455b-4367-af79-3e7b54f95889.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Cases for Adding Company and Employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231333726-fcdc5d8c-c946-42c8-ae55-7a74e163875a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Cases for Searching Companies<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231333652-72af24d8-bcf3-4ba6-ace3-b26e75bb5914.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Cases for Editing Companies<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67402270/231336951-0f14fc2a-d2ce-4458-98c2-f797b0a2b4db.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases for searching employees<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>I learned that debugging can take a really long time. I also had<br>issues with just formatting the queries or validating the states and countries for<br>companies. Overall, I was overcomplicating a lot of things that weren&#39;t too bad<br>to implement. Print statements did help with state and country validation. Overall, I&#39;m<br>glad the professor was very helpful in answering all of my numerous questions<br>and I really appreciated that.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/mm2836" target="_blank">Grading</a></td></tr></table>