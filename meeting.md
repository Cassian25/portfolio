MEETING BRIEF — ORACLE PRIMAVERA CLOUD AND NETSUITE TASK SYNC

Purpose: Explain how task data moves from Oracle Primavera Cloud to NetSuite, who does what, and what we need to decide today.

Last meeting: 01 September 2026 — LIFL sits in the middle. Data is sent automatically when a task changes.


IN ONE SENTENCE

When a task is created or changed in Oracle Primavera Cloud, that system sends the details to LIFL. LIFL checks the data, converts it, and sends it to NetSuite so the same task is created or updated there.


THE BIG PICTURE

Oracle Primavera Cloud → task changed → LIFL → NetSuite → task created or updated

Already working: NetSuite → Oracle Primavera Cloud (project creation)
This project: Oracle Primavera Cloud → NetSuite (task sync)
Not doing: NetSuite asking Oracle Primavera Cloud for updates on a timer


WHO DOES WHAT

Oracle Primavera Cloud team — owns tasks, builds auto-send (about 3 to 4 months), shares sample data

LIFL team (us) — receives data, checks it, converts it, sends to NetSuite, keeps records, handles errors

NetSuite team — gives login access, confirms matching rules, helps with testing


WHAT LIFL DOES

LIFL is the middle layer between both systems.

Receive → Check → Convert → Log in to NetSuite → Send → Read reply → Save records


HOW DATA MOVES

User saves task in Oracle Primavera Cloud → Oracle Primavera Cloud sends to LIFL → LIFL checks and converts → LIFL sends to NetSuite → NetSuite creates or updates task → NetSuite sends back success or error

Every task must have: Project ID and Task ID from Oracle Primavera Cloud
New task = create in NetSuite | Changed task = update same task in NetSuite


HOW WE CONNECT

Oracle Primavera Cloud to LIFL: Oracle Primavera Cloud builds auto-send → LIFL gives web address (test + live) → Oracle Primavera Cloud sends task data when task changes → agree security → about 3 to 4 months on Oracle Primavera Cloud side

LIFL to NetSuite: NetSuite gives login access → LIFL uses task API script 2116 → NetSuite finds project and task using Oracle Primavera Cloud references


DECISIONS WE NEED TODAY

1. How will Oracle Primavera Cloud send updates to LIFL? — Owner: Oracle Primavera Cloud
2. When will auto-send be ready? What do we do until then? — Owner: Oracle Primavera Cloud + LIFL
3. When should sync run — on save, on approval, or after schedule update? — Owner: Oracle Primavera Cloud
4. LIFL web address for test and live — Owner: LIFL
5. How to secure the connection — Owner: Oracle Primavera Cloud + LIFL
6. NetSuite test login details — Owner: NetSuite
7. Field mapping agreed by all teams — Owner: All
8. Status values matched between both systems — Owner: Oracle Primavera Cloud + NetSuite
9. What if linked task or parent is not in NetSuite yet? — Owner: All
10. One-time upload for tasks that already exist? — Owner: All


QUESTIONS FOR ORACLE PRIMAVERA CLOUD TEAM

1. How will you tell LIFL when a task is created or changed?
Example: When user clicks Save, will your system call our web address automatically?

2. What is your plan and timeline for the automatic send?
Example: You said 3 to 4 months — which month can we start testing?

3. Can you share example data for different task types?
Example: One new task, one edited task, one milestone, one task with a linked predecessor.

4. What are the exact field names for Project ID and Task ID?
Example: Is it called projectCode or projectId in your system?

5. What date format and status values do you use?
Example: Dates like 2026-09-08? Status like In Progress, Complete — please share full list.

6. If LIFL is down, will you try sending again?
Example: Will you retry after 5 minutes? How many times?

7. Can you set up test projects for joint testing?
Example: One test project with parent, child, and linked tasks.

8. What happens in special cases?
Example: Task deleted — should NetSuite delete too? Many old tasks to sync — how? Child before parent — wait or skip?


QUESTIONS FOR NETSUITE TEAM

1. Please provide secure login details for test and live.
Example: Client ID, certificate, and test account access.

2. Please confirm task API works same in test and live.
Example: Script 2116 deploy 1 — same in both environments?

3. Please confirm how NetSuite finds the right project and task.
Example: Project matched using Oracle Primavera Cloud reference on project record — correct?

4. Please share valid task status values in NetSuite.
Example: Not Started, In Progress, Complete — full list for mapping.

5. When predecessor links change on update, what happens?
Example: Task had one link, now has two — replace old or add new?

6. Please share error messages and what LIFL should do.
Example: Project not found — stop and alert? Task not found — try create instead?

7. Please set up test projects with Oracle Primavera Cloud reference filled in.
Example: Test project with reference OPC-PROJ-1001 for end-to-end test.

8. If same update is sent twice by mistake, what happens?
Example: Same task sent two times — duplicate task or update once?


WHAT LIFL WILL DO

Before next meeting: Share test web address, ask for sample data, ask NetSuite for test access, confirm test projects ready, send question list to both teams

During build: Build middle system, test NetSuite connection, run full test when Oracle Primavera Cloud auto-send is ready

Go-live: Move to live, one-time sync if needed, joint testing and sign-off

We will not: Poll Oracle Primavera Cloud on a schedule, store passwords in code, retry forever when project not found


WHEN THINGS GO WRONG

Project ID or Task ID missing → stop and alert LIFL team
NetSuite cannot find project → log error, alert team, do not retry forever
Task not found on update → agree today — try as new or alert
Status does not match → stop and fix mapping
Predecessor not in NetSuite yet → wait and try again
NetSuite down or slow → try 3 times, then hold for manual review


SIGN-OFF CHECKLIST

Kickoff done — Oracle Primavera Cloud: ___ NetSuite: ___ LIFL: ___ Date: ___
Field mapping agreed — Oracle Primavera Cloud: ___ NetSuite: ___ LIFL: ___ Date: ___
Status mapping agreed — Oracle Primavera Cloud: ___ NetSuite: ___ LIFL: ___ Date: ___
Joint testing passed — Oracle Primavera Cloud: ___ NetSuite: ___ LIFL: ___ Date: ___
Live go-live — Oracle Primavera Cloud: ___ NetSuite: ___ LIFL: ___ Date: ___


ATTENDEES

LIFL — Mr. Surendra
Oracle Primavera Cloud — Mr. Raj, Mr. Maanikanta, Mr. Krishna
BONbLOC — Dharnish, Dhaksha, Logeshwaran


CLOSING STATEMENT

Oracle Primavera Cloud will automatically send task details to LIFL when a task is created or changed. LIFL will check and convert the data and send it to NetSuite. NetSuite will create or update the matching project task.

Today we need answers on how data will be sent, when auto-send will be ready, how fields and statuses map, and what to do when something goes wrong. Once agreed, all three teams can work in parallel.
