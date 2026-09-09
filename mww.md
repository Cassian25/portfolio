# OPC → NetSuite Project Task / Milestone API

## Middleware Integration Guide (Python)

This document covers the NetSuite RESTlet API for Oracle Primavera Cloud (OPC) integration, the agreed integration approach from the stakeholder meeting, and how to build LIFL middleware to authenticate, validate JSON, and push project task data to NetSuite.

---

## Minutes of Meeting — Integration Approach

| Field | Details |
|-------|---------|
| Date | 01-09-2026 |
| Time | 13:30 to 14:00 (30 mins) |
| Venue | Online |
| Purpose | Project Creation OPC → NetSuite |

### Attendees

| Organization | Participants |
|--------------|--------------|
| LIFL | Mr. Surendra |
| OPC | Mr. Raj, Mr. Maanikanta, Mr. Krishna |
| BONbLOC | Dharnish, Dhaksha, Logeshwaran |

---

### 1. Objective

The meeting was conducted to discuss Project Creation and Task/Activity integration between Oracle Primavera Cloud (OPC) and NetSuite. The primary focus was to finalize the integration approach for pushing Project Task/Activity details from OPC to NetSuite whenever a task is created or updated in OPC.

---

### 2. Key Discussion Points

#### 2.1 Project Creation — NetSuite → OPC (Already Done)

- The Project Creation integration from NetSuite to OPC has been successfully implemented.
- Projects created in NetSuite are successfully created in OPC using the OPC API endpoint.
- Project information is mapped between both systems successfully.

#### 2.2 Task/Activity Creation — OPC → NetSuite (This Project)

- After the project is created in OPC, the LIFL team will manually create Task/Activity details under the respective project in OPC.
- Task/Activity created in OPC must be automatically created in the corresponding NetSuite project.
- If the Task/Activity is subsequently updated in OPC, the corresponding NetSuite task must also be updated automatically.
- The NetSuite team has already shared the RESTlet endpoint and required payload structure for Task/Activity creation.

#### 2.3 Integration Method — Push vs. Get

| Approach | Proposed By | Summary |
|----------|-------------|---------|
| **Push** | NetSuite Team | OPC triggers the NetSuite RESTlet whenever a Task/Activity is created or updated. NetSuite creates or updates the corresponding Project Task. |
| **Get** | OPC Team | OPC does not provide an after-submit trigger similar to NetSuite. OPC proposed NetSuite periodically retrieve Task/Activity details via a Get API. |

#### 2.4 Challenges with the Get Method (Not Recommended)

The NetSuite team explained that the Get method would introduce several technical and performance challenges:

- A Scheduled Script would be required in NetSuite to periodically retrieve task/activity details.
- The script would need to retrieve project and activity data repeatedly.
- Processing a large number of projects and activities could result in high governance/load consumption.
- Additional logic would be required to identify newly created and updated activities.
- The approach may not provide efficient real-time integration.
- **The NetSuite team did not recommend the Get method as the preferred solution.**

#### 2.5 Challenges with the Push Method

- The OPC team confirmed that OPC currently does not have a direct after-save/after-submit trigger for this requirement.
- OPC does not support custom scripting in the same manner as NetSuite.
- Implementing push functionality within OPC would require additional development/customization.
- The OPC team indicated this customization could take approximately **3–4 months** and will require middleware support.

#### 2.6 LIFL Proposal (Accepted)

- LIFL confirmed they already have middleware/infrastructure available for integration activities.
- LIFL is currently using this infrastructure for other integrations, including bank integrations.
- LIFL proposed developing the required middleware/push mechanism internally with OPC team support.
- The middleware will receive Task/Activity information and push it to the NetSuite RESTlet endpoint for creating or updating the corresponding Project Task.

---

### 3. Final Decision / Conclusion

**Agreed architecture:**

```
OPC → LIFL Middleware/Server → NetSuite RESTlet → Project Task
```

| Decision | Detail |
|----------|--------|
| OPC role | Continue to manage Project Task/Activity information |
| LIFL role | Develop the middleware/push mechanism using existing infrastructure |
| NetSuite role | Receive pushed data via RESTlet and create/update Project Tasks |
| Updates | Task updates from OPC are pushed to NetSuite; corresponding NetSuite task is updated |
| Rejected approach | Periodic Get/poll from NetSuite |

**Key outcome:** The team agreed to proceed with **Push-based integration through LIFL's middleware/server** rather than using a periodic Get method from NetSuite, subject to required development and technical coordination between the LIFL, OPC, and NetSuite teams.

---

## 1. API Overview

This RESTlet receives Project Task and Milestone data from Oracle Primavera Cloud (OPC), creates or updates the corresponding NetSuite Project Task, and maps predecessor relationships.

| Property | Value |
|----------|-------|
| HTTP Method | POST |
| Endpoint | `https://12029751-sb1.restlets.api.netsuite.com/app/site/hosting/restlet.nl?script=2116&deploy=1` |

---

## 2. Request Headers

| Header | Value |
|--------|-------|
| Content-Type | `application/json` |
| Authorization | `Bearer <OAuth 2.0 Access Token>` |

---

## 3. Mode

The payload supports two modes:

- **create** – Creates a Project Task when the OPC Task ID does not already exist.
- **update** – Updates an existing Project Task. The OPC Task ID must already exist.

If `mode` is omitted, the RESTlet defaults to `create`. If `create` is requested but the task already exists, the script automatically switches to `update`.

---

## 4. Sample JSON Payload – Create

```json
{
  "mode": "create",
  "opcProjectId": "OPC-PROJ-1001",
  "opcTaskId": "OPC-TASK-2001",
  "taskName": "Foundation Work",
  "startDate": "2026-08-28",
  "endDate": "2026-09-05",
  "isMilestone": false,
  "status": "In Progress",
  "parent": "Civil Works",
  "plannedwork": 40,
  "lineFields": {
    "predecessor": [
      {
        "task": "OPC-TASK-1999",
        "type": "FS",
        "lagdays": 2
      }
    ]
  }
}
```

---

## 5. Sample JSON Payload – Update

```json
{
  "mode": "update",
  "opcProjectId": "OPC-PROJ-1001",
  "opcTaskId": "OPC-TASK-2001",
  "taskName": "Foundation Work - Updated",
  "startDate": "2026-08-29",
  "endDate": "2026-09-08",
  "isMilestone": false,
  "status": "Completed",
  "parent": "Civil Works",
  "plannedwork": 45,
  "lineFields": {
    "predecessor": [
      {
        "task": "OPC-TASK-1999",
        "type": "FS",
        "lagdays": 0
      }
    ]
  }
}
```

---

## 6. Payload Field Description

| Field | Type | Required | Example | Description |
|-------|------|----------|---------|-------------|
| mode | String | No | create / update | Controls create or update behavior. Defaults to create. |
| opcProjectId | String | Yes | OPC-PROJ-1001 | Used to find the NetSuite Project through `custentity_lifl_opc_ref`. |
| opcTaskId | String | Yes | OPC-TASK-2001 | Used to identify the NetSuite Project Task. |
| taskName | String | No | Foundation Work | Mapped to the Project Task title. |
| startDate | Date string | No | 2026-08-28 | Mapped to `startdate`. |
| endDate | Date string | No | 2026-09-05 | Mapped to `enddate`. |
| isMilestone | Boolean | No | true / false | Indicates whether the OPC item is a milestone. Planned work is set only when false. |
| status | String | No | In Progress | Mapped to NetSuite status. |
| parent | String | No | Civil Works | Exact parent task name searched within the same Project. |
| plannedwork | Number | No | 40 | Mapped to `plannedwork` when `isMilestone` is false. |
| lineFields.predecessor | Array | No | [{ ... }] | Contains predecessor task relationships. |

---

## 7. Predecessor Fields

| Field | Type | Required | Example | Description |
|-------|------|----------|---------|-------------|
| task | String | Yes | OPC-TASK-1999 | Predecessor identifier. The RESTlet first searches by OPC Task ID, then by exact task name. |
| type | String | No | FS | Predecessor relationship type. |
| lagdays | Number | No | 2 | Lag days for the predecessor relationship. |

---

## 8. Predecessor Relationship Types

| Predecessor Type | Description |
|------------------|-------------|
| Finish-to-Start (FS) | The predecessor task must finish before the current task can start. |
| Finish-to-Finish (FF) | The predecessor task must finish before the current task can finish. |
| Start-to-Start (SS) | The predecessor task must start before the current task can start. |
| Start-to-Finish (SF) | The predecessor task must start before the current task can finish. |

Example:

```json
{
  "task": "OPC-TASK-1999",
  "type": "FS",
  "lagdays": 2
}
```

---

## 9. Processing Flow

1. Validate `opcProjectId` and `opcTaskId`.
2. Find the NetSuite Project using the OPC Project reference.
3. Find an existing NetSuite Project Task using OPC Task ID and Project.
4. Create or load the Project Task based on mode.
5. Set task name, dates, status, planned work, parent, and raw payload.
6. Process predecessor relationships when supplied.
7. Save the record and return the NetSuite Task Internal ID.

---

## 10. Successful Response

```json
{
  "status": "Success",
  "message": "Project Task Created successfully",
  "netSuiteTaskId": "12345"
}
```

---

## 11. Error Response Examples

```json
{
  "status": "Error",
  "message": "Missing required parameters: opcProjectId or opcTaskId"
}
```

```json
{
  "status": "Error",
  "message": "NetSuite Project not found for OPC Project ID: OPC-PROJ-1001"
}
```

---

## 12. NetSuite Field Mapping

| OPC Payload Field | NetSuite Field | Purpose |
|-------------------|----------------|---------|
| opcProjectId | custentity_lifl_opc_ref | Project reference used for lookup. |
| opcTaskId | custevent_lifl_opc_task_ref | OPC task reference stored on the Project Task. |
| taskName | title | Project Task title. |
| parent | parent | Parent Project Task. |
| status | status | Task status. |
| plannedwork | plannedwork | Planned work. |
| startDate | startdate | Task start date. |
| endDate | enddate | Task end date. |
| lineFields.predecessor[].task | predecessor.task | Predecessor task. |
| lineFields.predecessor[].type | predecessor.type | Predecessor relationship type. |
| lineFields.predecessor[].lagdays | predecessor.lagdays | Predecessor lag days. |

> **Note:** The table above maps **Project Task** fields. For **Project (Job) header** fields, see Section 13.

---

## 13. NetSuite Project Header Fields (Job Record)

Reference from NetSuite Project header field export. These are **project-level** fields on the Job record — distinct from Project Task fields handled by the RESTlet in Sections 1–12.

**Context:** NetSuite → OPC project creation is already implemented. These fields define the NetSuite Project record structure that OPC tasks/activities link to via `opcProjectId` / `custentity_lifl_opc_ref`.

### 13.1 Primary Information

| Field Name | Field ID | Field Type | Mandatory | Custom | Description |
|------------|----------|------------|-----------|--------|-------------|
| Actual End Date | endDate | Date | No | No | Enter the date the project is finished. |
| Auto | autoName | Check Box | No | No | Clear the box to manually enter an ID for this project. |
| category | category | List/Record (reference) | No | No | |
| Comments | comments | Free-Form Text | No | No | Enter other information about this project. |
| contact | contact | List/Record (reference) | No | No | |
| currency | currency | List/Record (reference) | No | No | |
| customForm | customForm | List/Record (reference) | No | No | |
| entityStatus | entityStatus | List/Record (reference) | No | No | |
| Estimated End Date | projectedEndDate | Date | No | No | Enter the date you plan to complete all project tasks by. |
| Inactive | isInactive | Check Box | No | No | If checked, the project no longer appears on the list of projects. |
| jobType | jobType | List/Record (reference) | No | No | |
| language | language | List/Record (reference) | No | No | |
| parent | parent | List/Record (reference) | No | No | |
| JobID | entityId | Free-Form Text | No | No | NetSuite copies the Project Name as the Project ID. |
| Project | altName | Free-Form Text | No | No | When using Auto-Generated Numbers, the assigned project number is displayed here. |
| Project Name | companyName | Free-Form Text | No | No | Enter a unique project name. |
| projectManager | projectManager | List/Record (reference) | No | No | |
| Start Date | startDate | Date | No | No | Estimated date work will start. NetSuite schedules all project tasks without predecessors to start on this date. |
| subsidiary | subsidiary | List/Record (reference) | No | No | |

### 13.2 Classification

| Field Name | Field ID | Field Type | Mandatory | Custom | Description |
|------------|----------|------------|-----------|--------|-------------|
| Account | accountNumber | Free-Form Text | No | No | If you assign account numbers for projects, enter the account number here. |
| category | category | List/Record (reference) | No | No | |
| cseg_job_id | cseg_job_id | List/Record (reference) | No | No | |
| jobType | jobType | List/Record (reference) | No | No | |

### 13.3 Financial

| Field Name | Field ID | Field Type | Mandatory | Custom | Description |
|------------|----------|------------|-----------|--------|-------------|
| baselineBudget | baselineBudget | List/Record (reference) | No | No | |
| billingSchedule | billingSchedule | List/Record (reference) | No | No | |
| estimateAtCompletionBudget | estimateAtCompletionBudget | List/Record (reference) | No | No | |
| Estimated Cost | estimatedCostJc | Currency/Number | No | No | The estimated cost for completing the project. |
| Estimated Gross Profit | estimatedGrossProfit | Currency/Number | No | No | Estimated Gross Profit based on project settings. |
| Estimated Gross Profit Percent | estimatedGrossProfitPercent | Currency/Number | No | No | Shows the expected profit percentage. |
| Estimated Revenue | estimatedRevenueJc | Currency/Number | No | No | The estimated revenue for this project. |
| Exchange Rate | fxRate | Currency/Number | No | No | Currency exchange rate when the project was created. |
| jobBillingType | jobBillingType | List/Record (reference) | No | No | |
| jobItem | jobItem | List/Record (reference) | No | No | |
| Opening Balance | openingBalance | Currency/Number | No | No | |
| Opening Balance Date | openingBalanceDate | Date | No | No | |
| openingBalanceAccount | openingBalanceAccount | List/Record (reference) | No | No | |
| Project Price | jobPrice | Currency/Number | No | No | Price billed to the customer; used to calculate gross profit margin. |
| projectExpenseType | projectExpenseType | List/Record (reference) | No | No | |

### 13.4 Charges & Billing Summary

| Field Name | Field ID | Field Type | Mandatory | Custom | Description |
|------------|----------|------------|-----------|--------|-------------|
| Expense | chargeExpenseAmount | Currency/Number | No | No | Total billed expense charges. |
| Hold | chargeAmountHoldForBilling | Currency/Number | No | No | Total of charges with Hold status. |
| Labor | chargeLaborAmount | Currency/Number | No | No | Total billed labor charges. |
| Processed | chargeAmountBilled | Currency/Number | No | No | Total amount billed to the customer. |
| Ready | chargeAmountReadyForBilling | Currency/Number | No | No | Total of charges with Ready for Billing status. |
| Remaining | chargeAmountRemaining | Currency/Number | No | No | Total charge amount not yet billed or in Ready stage. |
| Total Pending Charges | chargeAmountPending | Currency/Number | No | No | Total charges generated but not yet billed. Click to open Manage Pending Charges. |

### 13.5 Scheduling

| Field Name | Field ID | Field Type | Mandatory | Custom | Description |
|------------|----------|------------|-----------|--------|-------------|
| Calculated End Date | calculatedEndDate | Date | No | No | NetSuite-calculated project end date. |
| Calculated End Date Baseline | calculatedEndDateBaseline | Date | No | No | Calculated End Date when the baseline was set. |
| Calculated Start Date | calculatedStartDate | Date | No | No | If Backward scheduling, displays the calculated start date. |
| Calculated Start Date Baseline | calculatedStartDateBaseline | Date | No | No | |
| Estimated End Date Baseline | projectedEndDateBaseline | Date | No | No | Estimated End Date when the baseline was set. |
| Last Baseline Date | lastBaseLineDate | Date | No | No | Date when the last project baseline was set. |
| Scheduled End Date | scheduledEndDate | Date | No | No | If Backward scheduling, enter the project end date. |
| Scheduled End Date Baseline | scheduledEndDateBaseline | Date | No | No | |
| schedulingMethod | schedulingMethod | List/Record (reference) | No | No | |
| Start Date Baseline | startDateBaseline | Date | No | No | Start Date when the baseline was set. |
| wbs | wbs | List/Record (reference) | No | No | |

### 13.6 Time & Work Tracking

| Field Name | Field ID | Field Type | Mandatory | Custom | Description |
|------------|----------|------------|-----------|--------|-------------|
| Actual Work | actualTime | Free-Form Text | No | No | Actual time entered for the project. |
| Allocated Work | allocatedTime | Free-Form Text | No | No | Total hours allocated to this project (includes task allocations). |
| Calculated Work | calculatedWork | Free-Form Text | No | No | Total time calculated from planned and actual time on project tasks. |
| Calculated Work Baseline | calculatedWorkBaseline | Free-Form Text | No | No | |
| Initial Time Budget | estimatedTime | Free-Form Text | No | No | Sum of initial time budgeted for CRM Tasks in this project. |
| Percent Complete by Allocated Work | percentCompleteByRsrcAlloc | Currency/Number | No | No | Progress based on allocated resources. |
| Percent Work Complete | percentTimeComplete | Currency/Number | No | No | Percent of total planned project time completed. |
| Planned Work | plannedWork | Free-Form Text | No | No | Total planned time entered for project tasks. |
| Planned Work Baseline | plannedWorkBaseline | Free-Form Text | No | No | |
| Remaining Work | timeRemaining | Free-Form Text | No | No | Time for work yet to be done on all project tasks. |
| Rev Rec Override Percent Complete | percentComplete | Currency/Number | No | No | Estimate of how much total project work is complete. |
| timeApproval | timeApproval | List/Record (reference) | No | No | |

### 13.7 Preferences

| Field Name | Field ID | Field Type | Mandatory | Custom | Description |
|------------|----------|------------|-----------|--------|-------------|
| Allow Allocated Resources to Enter Time to All Tasks | allowTaskTimeForRsrcAlloc | Check Box | No | No | Allow allocated resources to enter time against any project task. |
| Allow Expenses | allowExpenses | Check Box | No | No | Allow expenses to be entered for this project. |
| Allow Time Entry | allowTime | Check Box | No | No | Enable time entry for this project. |
| Apply to all time entries | applyProjectExpenseTypeToAll | Check Box | No | No | Apply selected project expense type to all time entries. |
| Classify Time as Exempt | isExemptTime | Check Box | No | No | Exempt time is excluded from utilization calculations. |
| Classify Time as Productive | isProductiveTime | Check Box | No | No | Productive time is worked on project but excluded from revenue calculation. |
| Classify Time as Utilized | isUtilizedTime | Check Box | No | No | Utilized time directly contributes to project revenue. |
| Create Planned Time Entries | materializeTime | Check Box | No | No | Generate time entries for planned work on project tasks. |
| Default Shipping Address | defaultShippingAddress | Free-Form Text | No | No | Default shipping address from the customer record. |
| Display All Resources for Project Task Assignment | allowAllResourcesForTasks | Check Box | No | No | Allow any employee or vendor to be assigned to a project task. |
| Forecast Charge Run on Demand | forecastChargeRunOnDemand | Check Box | No | No | Update charge runs only when manually triggered and during nightly update. |
| Include CRM Task In Project Totals | includeCrmTasksInTotals | Check Box | No | No | Include CRM tasks in costs, planned time, and actual time totals. |
| Limit Time and Expenses To Resources | limitTimeToAssignees | Check Box | No | No | Only Resources subtab resources can enter time and expenses. |
| Use Allocated Time for Forecast | useAllocatedTimeForForecast | Check Box | No | No | Use allocated time for project forecast reports. |

### 13.8 Custom Fields (LIFL)

| Field Name | Field ID | Field Type | Mandatory | Custom | Description |
|------------|----------|------------|-----------|--------|-------------|
| Allow Purchase Orders | custentity_p2p_allow_purchase | Check Box | No | Yes | |
| Allow Vendor Bills | custentity_p2p_allow_vendor_bill | Check Box | No | Yes | |
| custentity_lifl_prj_clu_man | custentity_lifl_prj_clu_man | List/Record (reference) | No | Yes | |
| custentity_lifl_prj_cus | custentity_lifl_prj_cus | List/Record (reference) | No | Yes | |
| custentity_lifl_prj_location | custentity_lifl_prj_location | List/Record (reference) | No | Yes | |
| custentity_lifl_prj_sub | custentity_lifl_prj_sub | List/Record (reference) | No | Yes | |
| custentity_lifl_project_so_ref | custentity_lifl_project_so_ref | List/Record (reference) | No | Yes | |
| Project Capacity (MT) | custentity_lifl_prj_cap | Currency/Number | No | Yes | |

> **Integration note:** The Task/Activity RESTlet resolves the NetSuite Project using `custentity_lifl_opc_ref` (OPC Project ID). Confirm this custom field exists on the Job record even if not listed in this export.

### 13.9 System Information

| Field Name | Field ID | Field Type | Mandatory | Custom | Description |
|------------|----------|------------|-----------|--------|-------------|
| Average Recalculation Duration | averageProjectPlanRecalculationDuration | Free-Form Text | No | No | |
| Date Created | dateCreated | Date/Time | No | No | Date the project was created. |
| External ID | externalId | Free-Form Text | No | No | Job external ID, if assigned. |
| Internal ID | id | Free-Form Text | No | No | Job internal ID. |
| Last Modified Date | lastModifiedDate | Date/Time | No | No | Date the job record was last modified. |
| Last Recalculation | lastProjectPlanRecalculationDateTime | Date/Time | No | No | |
| Last Recalculation Duration | lastProjectPlanRecalculationDuration | Free-Form Text | No | No | |
| Last Recalculation Status | lastProjectPlanRecalculationStatus | Free-Form Text | No | No | |
| Last Recalculation Trigger | lastProjectPlanRecalculationTrigger | Free-Form Text | No | No | |
| Reference Name | refName | Free-Form Text | No | No | |

---

## 14. Important Notes

- `opcProjectId` and `opcTaskId` are mandatory.
- The complete incoming JSON payload is stored in `custevent_lifl_opc_payload` for audit/reference.
- Dates are converted from the supplied date strings to JavaScript Date values by the RESTlet.
- Predecessors are searched first by OPC Task ID and then by exact task name.
- For update mode, the RESTlet returns an error if the OPC Task cannot be found.
- The current code logs that existing predecessor lines are cleared during update, but the actual removeLine logic is commented out. Test predecessor updates carefully if existing relationships need to be replaced.

---

## 15. Python Middleware Feasibility

**Yes — this integration is fully doable in Python on LIFL's existing middleware infrastructure.**

| Requirement | Possible in Python? |
|-------------|---------------------|
| Authenticate with OAuth 2.0 / private key (JWT) | Yes |
| Build and validate JSON payloads | Yes |
| Push (POST) create/update to the NetSuite RESTlet | Yes |
| Receive Task/Activity events from OPC and forward to NetSuite | Yes |
| Retry, logging, audit of raw payload | Yes |
| NetSuite scheduled Get/poll from OPC | Possible but **not recommended** (rejected in meeting) |

---

## 16. What the LIFL Middleware Will Do (Agreed Flow)

Based on the meeting decision, the middleware sits between OPC and NetSuite:

```
OPC (Task/Activity create or update)
        ↓
LIFL Middleware/Server (receive, transform, validate)
        ↓
NetSuite RESTlet (create or update Project Task)
```

1. **Receive Task/Activity data from OPC** — via OPC customization/API support (OPC team coordination required; native after-submit trigger not available today).
2. **Authenticate to NetSuite** — obtain a Bearer token (OAuth 2.0 / private key).
3. **Normalize to JSON** — map OPC fields to the RESTlet payload shape (`opcProjectId`, `opcTaskId`, dates, predecessors, etc.).
4. **Validate** — required fields, date format, predecessor types (`FS` / `FF` / `SS` / `SF`).
5. **Push (POST)** to the NetSuite RESTlet endpoint on create and update events.
6. **Handle response** — parse `status: Success` + `netSuiteTaskId`, or log and surface error messages.

> **Note:** The Get/poll approach (NetSuite scheduled script pulling from OPC) was explicitly rejected due to governance, performance, and real-time concerns. Middleware push is the agreed direction.

---

## 17. Authentication with Private Keys (NetSuite)

The RESTlet expects `Authorization: Bearer <OAuth 2.0 Access Token>`. A common NetSuite pattern using a **private key**:

1. Create a JWT (claims: `iss`, `aud`, `iat`, `exp`, etc.).
2. Sign it with your **certificate private key** (RSA / ES256, depending on setup).
3. Exchange the JWT for an access token at NetSuite's token endpoint.
4. Call the RESTlet with `Authorization: Bearer <access_token>`.

Recommended Python libraries:

- `cryptography` or `PyJWT` — sign JWT with the private key
- `requests` or `httpx` — token exchange + RESTlet POST

> **Note:** If your setup uses Token-Based Auth (TBA) instead of OAuth 2.0, that uses HMAC with consumer/token secrets — also supported in Python, but a different flow from private-key JWT.

---

## 18. JSON Validation (Python)

```python
import json

def ensure_json(raw: str | bytes | dict) -> dict:
    if isinstance(raw, dict):
        return raw
    try:
        data = json.loads(raw)
    except (TypeError, json.JSONDecodeError) as exc:
        raise ValueError("Payload is not valid JSON") from exc
    if not isinstance(data, dict):
        raise ValueError("JSON root must be an object")
    return data


def validate_task_payload(data: dict) -> None:
    required = ("opcProjectId", "opcTaskId")
    missing = [field for field in required if not data.get(field)]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")
```

---

## 19. Minimal POST Example (Python)

```python
import requests

RESTLET_URL = (
    "https://12029751-sb1.restlets.api.netsuite.com"
    "/app/site/hosting/restlet.nl?script=2116&deploy=1"
)

payload = {
    "mode": "create",
    "opcProjectId": "OPC-PROJ-1001",
    "opcTaskId": "OPC-TASK-2001",
    "taskName": "Foundation Work",
    "startDate": "2026-08-28",
    "endDate": "2026-09-05",
    "isMilestone": False,
    "status": "In Progress",
    "parent": "Civil Works",
    "plannedwork": 40,
    "lineFields": {
        "predecessor": [
            {"task": "OPC-TASK-1999", "type": "FS", "lagdays": 2}
        ]
    },
}

response = requests.post(
    RESTLET_URL,
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    },
    json=payload,
    timeout=60,
)

response.raise_for_status()
result = response.json()
```

---

## 20. Suggested Python Stack

| Layer | Library / Tool |
|-------|----------------|
| HTTP client | `httpx` or `requests` |
| JWT / private key signing | `PyJWT` + `cryptography` |
| Config / secrets | Environment variables or a secrets vault |
| Middleware hosting | LIFL existing integration infrastructure (same platform used for bank integrations) |
| Event/receive layer | REST endpoint or queue consumer (depends on OPC delivery mechanism agreed with OPC team) |
| Retry / resilience | Exponential backoff, dead-letter logging for failed NetSuite pushes |

---

## 21. Suggested Project Structure

### Integration Flow

```
OPC (Task create/update)
        ↓
LIFL Middleware Server
        ↓
NetSuite RESTlet (script 2116)
        ↓
NetSuite Project Task
```

### Proposed Project Folder Structure

```
lifl-opc-netsuite-middleware/
├── config/
│   └── settings.py
├── auth/
│   └── netsuite_oauth.py
├── receivers/
│   └── opc_webhook.py
├── transformers/
│   └── task_mapper.py
├── validators/
│   └── payload_validator.py
├── clients/
│   └── netsuite_client.py
├── services/
│   └── task_sync_service.py
├── logging/
│   └── audit_logger.py
├── main.py
├── requirements.txt
└── .env.example
```

### Folder Responsibilities

| Folder / File | Purpose |
|---------------|---------|
| `receivers/` | Receive task/activity events from OPC when a task is created or updated |
| `validators/` | Validate JSON; enforce required fields such as `opcProjectId` and `opcTaskId` |
| `transformers/` | Map OPC fields to the NetSuite RESTlet payload format |
| `auth/` | Obtain NetSuite Bearer token using OAuth 2.0 / private key |
| `clients/` | POST create/update requests to the NetSuite RESTlet |
| `services/` | Orchestrate receive → validate → map → push → handle response |
| `logging/` | Audit trail of raw OPC payload and NetSuite response |
| `config/` | Sandbox and production URLs, credentials references, and runtime settings |
| `main.py` | Application entry point for API server or worker |
| `requirements.txt` | Python dependencies |
| `.env.example` | Environment variable template for secrets |

### Optional Production Folders

```
lifl-opc-netsuite-middleware/
├── tests/
├── docs/
│   └── mww.md
├── scripts/
│   └── bulk_sync.py
└── docker/
    └── Dockerfile
```

### Document Structure in `mww.md`

| Section | Content |
|---------|---------|
| Meeting minutes | Push vs Get decision; LIFL middleware agreed |
| Sections 1–12 | NetSuite RESTlet API, payload, field mapping |
| Section 13 | NetSuite Project header fields |
| Sections 15–21 | Python feasibility, middleware flow, auth, validation, project structure |
| Section 24 | Questionnaires for OPC and NetSuite teams, UAT scenarios |

### Summary

LIFL will build a Python middleware with clear layers: receive from OPC, validate, map, authenticate, push to NetSuite RESTlet, and log. The folder structure above supports that flow and aligns with the agreed push-based integration architecture.

---

## 22. Middleware Design Notes

### From the RESTlet API

- Default `mode` is `create`; if the task already exists, the RESTlet auto-switches to update — middleware can still send explicit `mode` for clarity.
- On **update**, a missing OPC task returns an error from the RESTlet.
- **Predecessors:** the RESTlet may not fully clear old predecessor lines (remove logic is commented out) — plan tests for replace vs append behavior.
- Store/log the same JSON you send; NetSuite persists it in `custevent_lifl_opc_payload` for audit.

### From the Meeting Decision

- **NetSuite → OPC project creation is already live** — this middleware covers **OPC → NetSuite Task/Activity only**.
- **Push via LIFL middleware is the agreed pattern** — do not implement NetSuite scheduled Get/poll scripts.
- **OPC has no native after-submit trigger** — LIFL middleware development depends on OPC team support for how task events are delivered (estimated 3–4 months for OPC-side customization).
- **LIFL already runs integration middleware** (e.g. bank integrations) — reuse that infrastructure and patterns.
- **Coordination required** across LIFL, OPC, and NetSuite teams for event delivery, payload mapping, and error handling.

---

## 23. Bottom Line

Python is a solid choice for the **LIFL middleware layer** in this OPC → NetSuite integration. The agreed architecture is push-based: OPC sends Task/Activity data to LIFL middleware, which authenticates, validates JSON, and POSTs to the NetSuite RESTlet. The periodic Get approach from NetSuite was rejected. Private-key OAuth, JSON validation, and push workflows are all standard in Python. Development should align with OPC team delivery mechanism and LIFL's existing integration infrastructure.

---

## 24. Integration Questionnaire — OPC & NetSuite Teams

Use this section during kickoff, design, and UAT. Capture answers in the **Response** column during meetings.

**Legend:** Owner = OPC | NS (NetSuite) | LIFL | All

---

### 24.1 Questions for OPC Team

#### A. Authentication & API Access

| # | Question | Why It Matters | Response | Owner |
|---|----------|----------------|----------|-------|
| OPC-01 | What is the OPC **base URL** for sandbox and production? | Required to configure middleware HTTP client | | OPC |
| OPC-02 | Which authentication method is used — **OAuth 2.0 client credentials**, API key, or other? | Determines Python auth module design | | OPC |
| OPC-03 | Please provide **client ID**, **client secret** (or cert), and required **scopes**. | Middleware cannot call OPC without credentials | | OPC |
| OPC-04 | What is the OPC **token URL** and how long does the access token last? | Token caching and refresh logic | | OPC |
| OPC-05 | Is there a **refresh token** flow, or must we request a new token each time? | Affects session management | | OPC |
| OPC-06 | Is there an **IP allowlist** or firewall rule for API access from LIFL middleware server? | Infra team must whitelist before go-live | | OPC |
| OPC-07 | What are the **API rate limits** (requests per minute/hour)? What happens when exceeded? | Retry/backoff design | | OPC |
| OPC-08 | Is there official **API documentation** (Swagger/OpenAPI) for project and activity endpoints? | Speeds development and reduces guesswork | | OPC |

#### B. Event Delivery & Auto-Trigger (Critical)

| # | Question | Why It Matters | Response | Owner |
|---|----------|----------------|----------|-------|
| OPC-09 | **How will OPC notify LIFL middleware when a task/activity is created or updated?** Webhook, queue, file, or must middleware poll? | Core architecture decision from meeting | | OPC |
| OPC-10 | OPC has no native after-save trigger today — what is the **planned solution and timeline** (estimated 3–4 months)? | Sets project schedule and interim approach | | OPC |
| OPC-11 | If **webhook**: what is the HTTP method (POST/PUT), required headers, and exact payload format? | Build `receivers/opc_webhook.py` | | OPC |
| OPC-12 | If **webhook**: will create and update be separate event types or one generic "task changed" event? | Determines `mode` handling in middleware | | OPC |
| OPC-13 | If **webhook**: will OPC **retry** if middleware returns 500 or timeout? How many times and at what interval? | Idempotency and duplicate handling | | OPC |
| OPC-14 | What **security** protects OPC → middleware calls — shared secret, API key, mTLS, IP restriction? | Prevents unauthorized pushes | | OPC |
| OPC-15 | What is the **middleware callback URL** format OPC will call (sandbox + production)? | LIFL infra must expose endpoint | | OPC + LIFL |
| OPC-16 | If **polling interim** is needed: is there a `lastModifiedDate` or change-log API for delta sync? | Avoid full project scan every run | | OPC |
| OPC-17 | At what point should sync fire — on **save**, on **publish/approve**, or on **schedule recalculation**? | Defines when NetSuite receives data | | OPC |

#### C. Task / Activity Field Mapping

| # | Question | Why It Matters | Response | Owner |
|---|----------|----------------|----------|-------|
| OPC-18 | Please share **sample JSON** for: task create, task update, milestone create/update, task with predecessors. | Primary input for mapper development | | OPC |
| OPC-19 | What field is the unique **OPC Task ID**? (maps to RESTlet `opcTaskId` / NetSuite `custevent_lifl_opc_task_ref`) | Required for create/update matching | | OPC |
| OPC-20 | What field is the unique **OPC Project ID**? (maps to RESTlet `opcProjectId` / NetSuite `custentity_lifl_opc_ref`) | Required to find correct NetSuite project | | OPC |
| OPC-21 | Which OPC fields map to: **task name**, **start date**, **end date**, **status**, **parent**, **planned work**, **is milestone**? | Complete field mapping document | | OPC |
| OPC-22 | What **date format** does OPC use — `YYYY-MM-DD` only, or datetime with timezone? | Validation rules in middleware | | OPC |
| OPC-23 | List all possible **status values** in OPC with business meaning. | Map to NetSuite Project Task status | | OPC |
| OPC-24 | For **parent task**, do you send OPC task ID, task name, WBS code, or a combination? | RESTlet searches parent by exact name in same project | | OPC |
| OPC-25 | For **predecessors**, confirm field names for: predecessor task reference, relationship type (`FS`/`FF`/`SS`/`SF`), lag days. | Maps to `lineFields.predecessor[]` | | OPC |
| OPC-26 | Can a task have **multiple predecessors**? Is there a maximum count? | Payload size and validation | | OPC |
| OPC-27 | Can **opcTaskId** or **opcProjectId** change after the record is created? | Breaks update matching if IDs are mutable | | OPC |
| OPC-28 | What unit is **planned work** in OPC — hours, days, percent? | Maps to NetSuite `plannedwork` | | OPC |
| OPC-29 | How are **milestones** represented in OPC API vs regular tasks? | Sets `isMilestone` correctly | | OPC |

#### D. OPC Business Scenarios & Edge Cases

| # | Question | Why It Matters | Response | Owner |
|---|----------|----------------|----------|-------|
| OPC-30 | After LIFL manually creates tasks in OPC, when should the first sync to NetSuite occur? | UAT workflow alignment | | OPC |
| OPC-31 | If a user edits the same task multiple times quickly, will middleware receive **multiple events** or one batched event? | Duplicate/race condition handling | | OPC |
| OPC-32 | Can tasks be **deleted** in OPC? If yes, should NetSuite task be deleted, inactivated, or ignored? | No delete handling in current RESTlet — gap to resolve | | OPC + NS |
| OPC-33 | Can a task be **moved to a different project** in OPC after creation? | Project lookup may break | | OPC |
| OPC-34 | If **predecessor task is not yet synced** to NetSuite, should middleware retry later, skip predecessor, or fail the whole task? | Ordering and retry strategy | | All |
| OPC-35 | If **parent task is not yet synced**, should child task sync wait, retry, or proceed without parent? | Parent/child ordering | | All |
| OPC-36 | Is **bulk initial sync** required for existing tasks on a project already live in both systems? | One-time migration script | | All |
| OPC-37 | How many tasks per project (typical and maximum)? | Performance and batch design | | OPC |
| OPC-38 | Are there **read-only/computed fields** in OPC that should not be sent to NetSuite? | Avoid overwriting NS-calculated values | | OPC |

#### E. OPC Testing & Go-Live

| # | Question | Why It Matters | Response | Owner |
|---|----------|----------------|----------|-------|
| OPC-39 | Is there a **sandbox/test OPC** environment aligned with NetSuite sandbox? | End-to-end testing | | OPC |
| OPC-40 | Can you provide **1–2 test projects** with sample tasks, parent/child hierarchy, and predecessors? | UAT test cases | | OPC |
| OPC-41 | Who is the **OPC integration contact** for defects and API questions during development? | Escalation path | | OPC |
| OPC-42 | What is the **go-live cutover plan** for in-flight projects and tasks already in OPC? | Avoid missed or duplicate sync | | All |
| OPC-43 | Will OPC team participate in **joint UAT** sign-off with LIFL and NetSuite? | Acceptance criteria | | All |

---

### 24.2 Questions for NetSuite Team

#### A. Authentication & RESTlet Access

| # | Question | Why It Matters | Response | Owner |
|---|----------|----------------|----------|-------|
| NS-01 | Confirm **OAuth 2.0 JWT** setup: Client ID, Certificate ID, private key (`.pem`), token URL, algorithm (`PS256`/`RS256`), required scopes. | NetSuite auth module | | NS |
| NS-02 | Is the RESTlet URL the same for sandbox and production? Confirm `script=2116&deploy=1` for both environments. | Environment config | | NS |
| NS-03 | Is there an **IP restriction** on the integration role or RESTlet access? | LIFL server must be whitelisted | | NS |
| NS-04 | What is the **token expiry** duration? Any guidance on caching tokens in middleware? | Avoid auth on every request vs stale token | | NS |
| NS-05 | Does the integration use **OAuth 2.0 JWT** or **Token-Based Auth (TBA)**? | Different Python implementation | | NS |
| NS-06 | Are there concurrent connection limits or throttling on RESTlet calls? | Rate limiting in middleware | | NS |

#### B. Project & Task Lookup

| # | Question | Why It Matters | Response | Owner |
|---|----------|----------------|----------|-------|
| NS-07 | Confirm project lookup: **`custentity_lifl_opc_ref`** = RESTlet `opcProjectId`? | Task cannot be created without valid project | | NS |
| NS-08 | Confirm task lookup: **`custevent_lifl_opc_task_ref`** = RESTlet `opcTaskId`? | Update matching | | NS |
| NS-09 | Is `custentity_lifl_opc_ref` populated on all projects created via existing NS → OPC integration? | Ensures OPC tasks find correct NS project | | NS |
| NS-10 | If multiple NetSuite projects share the same OPC ref (data error), what should RESTlet do? | Error handling | | NS |
| NS-11 | For **update mode**, if task not found by `opcTaskId`, should middleware retry as **create** or return error? | Update-fallback behavior | | NS |
| NS-12 | Confirm RESTlet **auto-switches create → update** when task already exists — can middleware rely on this? | Simplifies `mode` logic | | NS |
| NS-13 | Should middleware store returned **`netSuiteTaskId`** anywhere for cross-reference (OPC, NS custom field)? | Traceability | | NS |

#### C. Field Mapping & Valid Values

| # | Question | Why It Matters | Response | Owner |
|---|----------|----------------|----------|-------|
| NS-14 | What are all valid **Project Task status** values in NetSuite? Provide list for OPC status mapping. | Prevents RESTlet rejection | | NS |
| NS-15 | For **parent**, RESTlet searches by exact task name within same project — is this acceptable vs internal ID? | Parent mapping from OPC | | NS |
| NS-16 | For **plannedwork**, confirm unit (hours?) and confirm it is skipped when `isMilestone = true`. | Milestone vs task behavior | | NS |
| NS-17 | Confirm date fields accept **`YYYY-MM-DD`** strings from middleware without timezone issues. | Date validation | | NS |
| NS-18 | Full payload stored in **`custevent_lifl_opc_payload`** — is there a character/size limit? | Large predecessor payloads | | NS |
| NS-19 | Beyond `opcProjectId` and `opcTaskId`, are any other fields **mandatory** for create to succeed? | Validation rules | | NS |
| NS-20 | What NetSuite **status value** should be used for newly created tasks from OPC by default? | Default mapping | | NS |
| NS-21 | Are there NetSuite-side **workflow or approval rules** that block task create/update via RESTlet? | Silent failures | | NS |

#### D. Predecessor Handling

| # | Question | Why It Matters | Response | Owner |
|---|----------|----------------|----------|-------|
| NS-22 | Predecessor lookup: OPC Task ID first, then exact task name — confirm both paths work in sandbox. | Predecessor resolution | | NS |
| NS-23 | **Known issue:** predecessor removeLine logic is commented out in RESTlet — what is expected behavior for: add, change type/lag, remove predecessor on update? | UAT must cover predecessor replace | | NS |
| NS-24 | If predecessor task does not exist yet in NetSuite, does RESTlet fail entirely or save task without predecessor? | Retry ordering with OPC | | NS |
| NS-25 | Maximum number of predecessors supported per task? | Validation | | NS |
| NS-26 | Are all four types confirmed working in sandbox: **FS, FF, SS, SF**? | Predecessor type mapping | | NS |

#### E. Error Handling & RESTlet Behavior

| # | Question | Why It Matters | Response | Owner |
|---|----------|----------------|----------|-------|
| NS-27 | Provide full list of RESTlet **error messages** and recommended middleware action (retry, alert, skip). | Error handler design | | NS |
| NS-28 | What **HTTP status codes** does RESTlet return for: success, business validation error, system error? | Response parsing | | NS |
| NS-29 | Is RESTlet **idempotent** if the same payload is sent twice (duplicate OPC webhook)? | Duplicate event safety | | NS |
| NS-30 | Any **governance unit** or timeout limits per RESTlet call? Max recommended batch size? | Performance design | | NS |
| NS-31 | Does RESTlet support **task delete or inactivate** from OPC? If not, is an enhancement planned? | Delete scenario gap | | NS |
| NS-32 | Who monitors RESTlet **execution logs** in NetSuite during UAT and production? | Support model | | NS |

#### F. NetSuite Testing & Go-Live

| # | Question | Why It Matters | Response | Owner |
|---|----------|----------------|----------|-------|
| NS-33 | Provide **sandbox account** details and test project(s) with `custentity_lifl_opc_ref` already populated. | Integration testing | | NS |
| NS-34 | Can you create test OPC project refs (e.g. `OPC-PROJ-1001`) in sandbox matching OPC test data? | End-to-end UAT | | NS |
| NS-35 | Who validates created/updated tasks in NetSuite UI during UAT? | Sign-off owner | | NS |
| NS-36 | What is the **production deployment plan** for RESTlet changes if fixes are needed during UAT? | Release process | | NS |
| NS-37 | Is there a **rollback plan** if middleware go-live causes bad task data in NetSuite? | Risk mitigation | | NS |

---

### 24.3 Cross-System Scenarios (OPC + NetSuite + LIFL)

Confirm expected behavior for each scenario during joint workshop.

| # | Scenario | OPC Expected Behavior | NetSuite Expected Result | Middleware Action | Confirmed |
|---|----------|----------------------|--------------------------|-------------------|-----------|
| XS-01 | **New task created in OPC** | Send create event/payload | New Project Task created; `netSuiteTaskId` returned | Map, validate, POST `mode=create` | |
| XS-02 | **Existing task updated in OPC** | Send update event/payload | Same task updated by `opcTaskId` | Map, validate, POST `mode=update` | |
| XS-03 | **Milestone created in OPC** | Send with milestone flag | Task created; `plannedwork` not set | Set `isMilestone=true` | |
| XS-04 | **Regular task with planned work** | Send duration/hours | `plannedwork` populated | Set `isMilestone=false`, map plannedwork | |
| XS-05 | **Task with one predecessor (FS + lag)** | Send predecessor array | Predecessor line created | Map `lineFields.predecessor[]` | |
| XS-06 | **Task with multiple predecessors (FS/FF/SS/SF)** | Send full predecessor list | All predecessor lines created | Validate types FS/FF/SS/SF | |
| XS-07 | **Parent/child task hierarchy** | Parent exists before child in OPC | Parent set on child task | Sync parent before child or retry | |
| XS-08 | **Predecessor not yet in NetSuite** | Predecessor task pending sync | TBD — fail or partial save | Queue/retry per agreed rule | |
| XS-09 | **Project exists in OPC but not in NetSuite** | Task event sent | Error: project not found | Log, alert, do not retry indefinitely | |
| XS-10 | **Project created NS → OPC (existing flow)** | OPC project ID stored | NS project has `custentity_lifl_opc_ref` | Confirm ref matches before task sync | |
| XS-11 | **Duplicate event from OPC (retry)** | Same payload sent twice | No duplicate task; idempotent update | Use `opcTaskId` as idempotency key | |
| XS-12 | **NetSuite RESTlet down / 500 error** | OPC may retry webhook | No change | Middleware queue + exponential backoff | |
| XS-13 | **Invalid status sent from OPC** | Status not in NS list | RESTlet error | Map status table; reject before POST if unmapped | |
| XS-14 | **Initial bulk load — existing OPC tasks** | Bulk export or repeated events | All tasks created in NS project | One-time sync job with watermark | |
| XS-15 | **Task deleted in OPC** | Delete event (if any) | TBD — no RESTlet delete today | Document gap; manual or future enhancement | |
| XS-16 | **Predecessor updated (change type/lag)** | Update event with new predecessor data | Predecessor lines updated | Test carefully — removeLine issue | |
| XS-17 | **Predecessor removed in OPC** | Update event without predecessor | Old predecessor lines removed | Test carefully — removeLine issue | |
| XS-18 | **Same task name, different opcTaskId** | Two distinct tasks | Two NS tasks under same project | Never rely on name alone for identity | |
| XS-19 | **Production go-live — first task sync** | First live event | First live NS task | Monitor logs; confirm with all teams | |
| XS-20 | **Status mapping — OPC "In Progress" → NS ?** | OPC status value sent | Correct NS status set | Maintain shared status mapping table | |

---

### 24.4 Status Mapping Template

Complete jointly by OPC and NetSuite teams.

| OPC Status Value | NetSuite Status Value | Notes | Confirmed By |
|------------------|-------------------------|-------|--------------|
| | | | |
| | | | |
| | | | |

---

### 24.5 Error Response Action Matrix (NetSuite)

Complete with NetSuite team.

| RESTlet Error Message | Cause | Middleware Action | Alert Required | Confirmed |
|-----------------------|-------|-------------------|----------------|-----------|
| Missing required parameters: opcProjectId or opcTaskId | Bad payload | Reject before POST; log OPC payload | Yes | |
| NetSuite Project not found for OPC Project ID: {id} | Project ref mismatch | Log; alert LIFL; no infinite retry | Yes | |
| Task not found (update mode) | Task never synced or wrong opcTaskId | Retry as create OR alert — confirm rule | TBD | |
| Invalid status | Unmapped status value | Reject; update status mapping table | Yes | |
| Predecessor not found | Predecessor not synced yet | Queue retry with delay | TBD | |
| NetSuite 500 / timeout | NS system error | Retry 3x with backoff; then dead-letter queue | Yes | |

---

### 24.6 Email Templates

#### To OPC Team

> **Subject:** OPC → NetSuite Task Integration — Information Required from OPC Team
>
> Hi OPC team,
>
> For the OPC → NetSuite Task/Activity integration via LIFL middleware, please provide answers to the following:
>
> 1. API authentication details and base URLs (sandbox + production)
> 2. How you will deliver task create/update events to LIFL middleware (webhook vs interim poll) and expected timeline
> 3. Sample JSON payloads for: task create, task update, milestone, and task with predecessors
> 4. Field mapping document: OPC Task ID, Project ID, name, dates, status, parent, planned work, milestone flag, predecessors
> 5. All OPC status values and date format used in API responses
> 6. Behavior for: task delete, bulk initial sync, predecessor-not-yet-synced, parent-not-yet-synced
> 7. Sandbox test environment access and 1–2 sample projects for joint UAT
>
> Refer to Section 24.1 in `mww.md` for the full questionnaire.
>
> Thanks,  
> LIFL Integration Team

#### To NetSuite Team

> **Subject:** OPC → NetSuite Task Integration — Information Required from NetSuite Team
>
> Hi NetSuite team,
>
> For the LIFL middleware → RESTlet (script 2116, deploy 1) integration, please confirm:
>
> 1. OAuth 2.0 JWT credentials: Client ID, Certificate ID, private key, token URL, algorithm, scopes
> 2. Project lookup via `custentity_lifl_opc_ref` and task lookup via `custevent_lifl_opc_task_ref`
> 3. Valid Project Task status values for OPC status mapping
> 4. Predecessor update behavior (add/change/remove) given removeLine logic status in RESTlet
> 5. Full RESTlet error message list and recommended retry/alert actions
> 6. Sandbox test projects with OPC refs populated for joint UAT
> 7. Idempotency, governance limits, and production deployment/rollback plan
>
> Refer to Section 24.2 in `mww.md` for the full questionnaire.
>
> Thanks,  
> LIFL Integration Team

---

### 24.7 Questionnaire Sign-Off

| Milestone | Date | OPC Sign-Off | NS Sign-Off | LIFL Sign-Off |
|-----------|------|--------------|-------------|---------------|
| Kickoff — questions reviewed | | | | |
| Field mapping agreed | | | | |
| Status mapping agreed | | | | |
| Error handling agreed | | | | |
| UAT scenarios passed | | | | |
| Production go-live | | | | |

