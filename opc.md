# Oracle Primavera Cloud → NetSuite Integration — LIFL Middleware Guide

Source: mww.md | Meeting 01-09-2026 | Push-based architecture agreed

---

## One-Line Summary

LIFL Middleware Server sits between Oracle Primavera Cloud and NetSuite. It receives task create and update events from Oracle Primavera Cloud, validates and maps the data, authenticates to NetSuite, sends Hypertext Transfer Protocol POST requests to the NetSuite RESTlet, and logs every request and response using push-based integration, not polling.

---

## What You Should Do — Action Points

### Phase 1 — Kickoff and Coordination

1. Confirm with Oracle Primavera Cloud team how task events will be delivered to your middleware (webhook, queue, or interim polling).
2. Confirm with Oracle Primavera Cloud team the auto-trigger timeline (estimated three to four months for Oracle Primavera Cloud customization).
3. Share your middleware callback Uniform Resource Locator with Oracle Primavera Cloud team for sandbox and production.
4. Request sample JavaScript Object Notation payloads from Oracle Primavera Cloud for task create, task update, milestone, and predecessors.
5. Request OAuth 2.0 credentials from NetSuite team: Client Identifier, Certificate Identifier, private key, token Uniform Resource Locator, algorithm, scopes.
6. Confirm NetSuite sandbox test projects have `custentity_lifl_opc_ref` populated with Oracle Primavera Cloud Project Identifier values.
7. Complete field mapping and status mapping tables jointly with Oracle Primavera Cloud and NetSuite teams.
8. Send questionnaire emails from mww.md Section 24 to Oracle Primavera Cloud and NetSuite teams.

### Phase 2 — Build Middleware Project

9. Create Python project `lifl-opc-netsuite-middleware` using the folder structure in this document.
10. Configure environment variables in `.env` from `.env.example` (never commit secrets).
11. Build `receivers/opc_webhook.py` to accept Oracle Primavera Cloud task events.
12. Build `validators/payload_validator.py` to enforce required fields and business rules.
13. Build `transformers/task_mapper.py` to map Oracle Primavera Cloud fields to NetSuite RESTlet payload.
14. Build `auth/netsuite_oauth.py` for OAuth 2.0 JSON Web Token authentication to NetSuite.
15. Build `clients/netsuite_client.py` to Hypertext Transfer Protocol POST to NetSuite RESTlet.
16. Build `services/task_sync_service.py` to orchestrate the full pipeline.
17. Build `logging/audit_logger.py` to log raw Oracle Primavera Cloud input and NetSuite response.
18. Build `main.py` as Application Programming Interface server entry point on LIFL existing infrastructure.

### Phase 3 — Connect and Test

19. Whitelist LIFL middleware server Internet Protocol address with Oracle Primavera Cloud and NetSuite if required.
20. Test NetSuite OAuth 2.0 token generation in sandbox.
21. Test manual Hypertext Transfer Protocol POST to NetSuite RESTlet with sample payload.
22. Test Oracle Primavera Cloud webhook delivery to your middleware endpoint in sandbox.
23. Run end-to-end test: create task in Oracle Primavera Cloud → auto-trigger fires → middleware → NetSuite Project Task created.
24. Run update test: edit task in Oracle Primavera Cloud → auto-trigger fires → middleware → NetSuite Project Task updated.
25. Test milestone, parent-child hierarchy, and predecessor scenarios.
26. Test error cases: missing project, missing task on update, invalid status, predecessor not yet synced.

### Phase 4 — Production and Go-Live

27. Deploy middleware to LIFL production infrastructure.
28. Switch Oracle Primavera Cloud auto-trigger to production middleware Uniform Resource Locator.
29. Switch NetSuite credentials and RESTlet Uniform Resource Locator to production.
30. Run bulk initial sync script if existing Oracle Primavera Cloud tasks need one-time migration.
31. Monitor audit logs during first live task sync.
32. Complete joint User Acceptance Testing sign-off with Oracle Primavera Cloud and NetSuite teams.

### What You Must Not Do

- Do not build NetSuite scheduled Get or poll scripts to pull from Oracle Primavera Cloud (rejected in meeting).
- Do not hardcode secrets in code — use environment variables only.
- Do not skip validation before sending to NetSuite RESTlet.
- Do not retry indefinitely when NetSuite Project is not found — alert and stop.

---

## How to Connect to Oracle Primavera Cloud

### Your Role Toward Oracle Primavera Cloud

You do not pull tasks from Oracle Primavera Cloud on a schedule as the primary design. Oracle Primavera Cloud will push events to your middleware once their auto-trigger customization is ready.

### Connection Steps

```
Connect to Oracle Primavera Cloud
│
├── Step 1 — Get credentials from Oracle Primavera Cloud team
│   ├── Oracle Primavera Cloud base Uniform Resource Locator (sandbox and production)
│   ├── Authentication method (OAuth 2.0 client credentials, Application Programming Interface key, or other)
│   ├── Client Identifier and client secret or certificate
│   ├── Token Uniform Resource Locator and token expiry duration
│   ├── Refresh token flow if available
│   └── Application Programming Interface rate limits
│
├── Step 2 — Expose your middleware endpoint
│   ├── Deploy LIFL Middleware Server on LIFL existing infrastructure
│   ├── Open HTTPS endpoint for Oracle Primavera Cloud webhook
│   ├── Sandbox callback Uniform Resource Locator — share with Oracle Primavera Cloud team
│   └── Production callback Uniform Resource Locator — share with Oracle Primavera Cloud team
│
├── Step 3 — Secure inbound calls from Oracle Primavera Cloud
│   ├── Shared secret or Application Programming Interface key validation in receivers/opc_webhook.py
│   ├── Internet Protocol allowlist if required
│   └── Transport Layer Security certificate on your server
│
├── Step 4 — Receive auto-trigger events
│   ├── Oracle Primavera Cloud sends Hypertext Transfer Protocol POST to your webhook on task create
│   ├── Oracle Primavera Cloud sends Hypertext Transfer Protocol POST to your webhook on task update
│   └── receivers/opc_webhook.py accepts payload and passes to task_sync_service.py
│
└── Step 5 — Interim approach if auto-trigger not ready yet
    ├── Confirm with Oracle Primavera Cloud if delta sync Application Programming Interface exists (lastModifiedDate)
    ├── Build optional polling script only as temporary measure
    └── Replace with webhook once Oracle Primavera Cloud auto-trigger is live
```

### Information You Need From Oracle Primavera Cloud Team

```
Required From Oracle Primavera Cloud Team
│
├── How and when task events are sent (save, publish, or schedule recalculation)
├── Planned auto-trigger solution and timeline (estimated three to four months)
├── Webhook Hypertext Transfer Protocol method, headers, and exact payload format
├── Separate create and update event types or single task changed event
├── Webhook retry behavior if middleware returns 500 or timeout
├── Security for Oracle Primavera Cloud to middleware calls
├── Sample JavaScript Object Notation for create, update, milestone, predecessors
├── Oracle Primavera Cloud Project Identifier field name
├── Oracle Primavera Cloud Task Identifier field name
├── Field mapping for name, dates, status, parent, planned work, milestone flag
├── Date format used by Oracle Primavera Cloud
├── All status values in Oracle Primavera Cloud
├── Predecessor field names and relationship types
├── Behavior for task delete, bulk sync, and ordering edge cases
└── Sandbox test projects for joint User Acceptance Testing
```

---

## How to Connect to NetSuite

### Your Role Toward NetSuite

You authenticate using OAuth 2.0 JSON Web Token, then Hypertext Transfer Protocol POST JavaScript Object Notation payloads to the NetSuite RESTlet. You never modify NetSuite directly — only through the RESTlet Application Programming Interface.

### Connection Steps

```
Connect to NetSuite
│
├── Step 1 — Get credentials from NetSuite team
│   ├── OAuth 2.0 Client Identifier
│   ├── Certificate Identifier
│   ├── Private key file (.pem)
│   ├── Token Uniform Resource Locator
│   ├── Signing algorithm (PS256 or RS256)
│   └── Required scopes
│
├── Step 2 — Configure environment in config/settings.py
│   ├── Sandbox RESTlet Uniform Resource Locator
│   │   └── https://12029751-sb1.restlets.api.netsuite.com/app/site/hosting/restlet.nl?script=2116&deploy=1
│   ├── Production RESTlet Uniform Resource Locator (confirm with NetSuite team)
│   ├── Account Identifier
│   └── Credential references via environment variables only
│
├── Step 3 — Build authentication in auth/netsuite_oauth.py
│   ├── Create JSON Web Token with claims: iss, aud, iat, exp
│   ├── Sign with private key using PyJWT and cryptography
│   ├── Exchange JSON Web Token at NetSuite token endpoint
│   └── Cache Bearer access token until expiry
│
├── Step 4 — Build client in clients/netsuite_client.py
│   ├── Set header Content-Type: application/json
│   ├── Set header Authorization: Bearer access_token
│   ├── Hypertext Transfer Protocol POST payload to RESTlet
│   └── Parse response status Success or Error
│
├── Step 5 — Confirm lookup fields with NetSuite team
│   ├── custentity_lifl_opc_ref on NetSuite Project = opcProjectId
│   ├── custevent_lifl_opc_task_ref on NetSuite Project Task = opcTaskId
│   └── custevent_lifl_opc_payload stores full incoming JSON for audit
│
└── Step 6 — Whitelist and test
    ├── Confirm LIFL server Internet Protocol is allowed if NetSuite has restrictions
    ├── Test token generation in sandbox
    └── Test create and update payloads against sandbox RESTlet
```

### NetSuite RESTlet Details

```
NetSuite RESTlet
│
├── Hypertext Transfer Protocol Method
│   └── POST
│
├── Endpoint (Sandbox)
│   └── https://12029751-sb1.restlets.api.netsuite.com/app/site/hosting/restlet.nl?script=2116&deploy=1
│
├── Request Headers
│   ├── Content-Type: application/json
│   └── Authorization: Bearer OAuth 2.0 Access Token
│
├── Mode
│   ├── create — new Project Task when Oracle Primavera Cloud Task Identifier does not exist
│   ├── update — update existing Project Task by Oracle Primavera Cloud Task Identifier
│   └── If mode omitted, defaults to create; RESTlet auto-switches to update if task already exists
│
├── Required Payload Fields
│   ├── opcProjectId
│   └── opcTaskId
│
├── Success Response
│   ├── status: Success
│   ├── message: Project Task Created successfully
│   └── netSuiteTaskId: internal NetSuite task identifier
│
└── Error Response Examples
    ├── Missing required parameters: opcProjectId or opcTaskId
    └── NetSuite Project not found for Oracle Primavera Cloud Project Identifier
```

### Information You Need From NetSuite Team

```
Required From NetSuite Team
│
├── OAuth 2.0 JSON Web Token credentials and token expiry guidance
├── Confirm script 2116 deploy 1 for sandbox and production
├── Internet Protocol restriction on integration role if any
├── Confirm custentity_lifl_opc_ref and custevent_lifl_opc_task_ref mapping
├── Valid Project Task status values for status mapping table
├── Predecessor update behavior (add, change, remove — removeLine issue in RESTlet)
├── Full RESTlet error message list and retry guidance
├── Sandbox test projects with Oracle Primavera Cloud reference populated
├── Idempotency behavior for duplicate webhook events
└── Production deployment and rollback plan
```

---

## How to Transfer Data Using Auto-Trigger From Oracle Primavera Cloud

### Important Context

Oracle Primavera Cloud does not have a native after-save trigger today like NetSuite. The Oracle Primavera Cloud team will build customization to call your middleware when a task is created or updated. This is the agreed push-based auto-trigger approach. Estimated timeline for Oracle Primavera Cloud side: three to four months.

### Auto-Trigger Data Transfer Flow

```
Auto-Trigger Data Transfer Flow
│
├── Trigger Event in Oracle Primavera Cloud
│   ├── User creates Task or Activity in Oracle Primavera Cloud
│   ├── User updates Task or Activity in Oracle Primavera Cloud
│   └── Oracle Primavera Cloud auto-trigger customization fires (after save, publish, or recalculation — confirm with Oracle Primavera Cloud team)
│
├── Oracle Primavera Cloud Sends to LIFL Middleware
│   ├── Hypertext Transfer Protocol POST to LIFL webhook Uniform Resource Locator
│   ├── Payload contains Oracle Primavera Cloud task data
│   └── Security header or shared secret validated by middleware
│
├── LIFL Middleware Receives — receivers/opc_webhook.py
│   ├── Accept incoming request
│   ├── Verify security (Application Programming Interface key, shared secret, Internet Protocol)
│   └── Pass raw payload to services/task_sync_service.py
│
├── LIFL Middleware Validates — validators/payload_validator.py
│   ├── Confirm valid JavaScript Object Notation
│   ├── Confirm opcProjectId present
│   ├── Confirm opcTaskId present
│   ├── Confirm date format year-month-day
│   └── Confirm predecessor types: Finish-to-Start, Finish-to-Finish, Start-to-Start, Start-to-Finish
│
├── LIFL Middleware Transforms — transformers/task_mapper.py
│   ├── Map Oracle Primavera Cloud Project Identifier → opcProjectId
│   ├── Map Oracle Primavera Cloud Task Identifier → opcTaskId
│   ├── Map task name → taskName
│   ├── Map start date → startDate
│   ├── Map end date → endDate
│   ├── Map status → status (using agreed status mapping table)
│   ├── Map parent task → parent
│   ├── Map planned work → plannedwork
│   ├── Map milestone flag → isMilestone
│   ├── Map predecessors → lineFields.predecessor array
│   └── Set mode: create or update based on event type
│
├── LIFL Middleware Authenticates — auth/netsuite_oauth.py
│   ├── Build JSON Web Token
│   ├── Sign with NetSuite private key
│   └── Get Bearer access token from NetSuite token endpoint
│
├── LIFL Middleware Pushes — clients/netsuite_client.py
│   ├── Hypertext Transfer Protocol POST to NetSuite RESTlet
│   ├── Headers: Content-Type application/json, Authorization Bearer token
│   └── Body: transformed JavaScript Object Notation payload
│
├── NetSuite RESTlet Processes
│   ├── Validate opcProjectId and opcTaskId
│   ├── Find NetSuite Project using custentity_lifl_opc_ref
│   ├── Find or create Project Task using custevent_lifl_opc_task_ref
│   ├── Set name, dates, status, parent, planned work
│   ├── Process predecessor relationships
│   ├── Store full payload in custevent_lifl_opc_payload
│   └── Return netSuiteTaskId or error
│
├── LIFL Middleware Handles Response — services/task_sync_service.py
│   ├── If Success: log netSuiteTaskId, return 200 to Oracle Primavera Cloud
│   ├── If business error: log error, return appropriate status, alert if needed
│   └── If NetSuite system error: retry with exponential backoff, then dead-letter queue
│
└── LIFL Middleware Audits — logging/audit_logger.py
    ├── Log raw Oracle Primavera Cloud payload received
    ├── Log transformed payload sent to NetSuite
    └── Log NetSuite response received
```

### Create Event Transfer

```
Create Event
│
├── Oracle Primavera Cloud auto-trigger fires on new task
├── Oracle Primavera Cloud sends create payload to middleware webhook
├── Middleware sets mode: create
├── Middleware maps all fields to RESTlet payload
├── Middleware POSTs to NetSuite RESTlet
└── NetSuite creates new Project Task and returns netSuiteTaskId
```

### Update Event Transfer

```
Update Event
│
├── Oracle Primavera Cloud auto-trigger fires on task edit
├── Oracle Primavera Cloud sends update payload to middleware webhook
├── Middleware sets mode: update
├── Middleware maps changed fields to RESTlet payload
├── Middleware POSTs to NetSuite RESTlet
└── NetSuite updates existing Project Task by opcTaskId
```

### Duplicate and Retry Handling

```
Duplicate and Retry Handling
│
├── Oracle Primavera Cloud retries webhook if middleware returns 500
│   └── Middleware uses opcTaskId as idempotency key — same task updated not duplicated
│
├── Predecessor not yet in NetSuite
│   └── Queue retry with delay per agreed rule with all teams
│
├── Parent task not yet in NetSuite
│   └── Sync parent first or retry child after delay per agreed rule
│
└── NetSuite RESTlet down
    ├── Retry three times with exponential backoff
    └── Move to dead-letter queue and alert LIFL team
```

---

## Integration Landscape

```
Integration Landscape
│
├── Already Live
│   └── NetSuite
│       └── Project Creation
│           └── Oracle Primavera Cloud
│
└── This Project — LIFL Middleware
    └── Oracle Primavera Cloud
        └── Task Create or Update (auto-trigger)
            └── LIFL Middleware Server
                └── Hypertext Transfer Protocol POST with JavaScript Object Notation
                    └── NetSuite RESTlet script 2116 deploy 1
                        └── NetSuite Project Task
```

---

## Three-Party Roles

```
Three-Party Roles
│
├── Oracle Primavera Cloud Role
│   ├── Source of truth for tasks and activities
│   ├── LIFL team creates and edits tasks in Oracle Primavera Cloud
│   ├── Build auto-trigger customization to push events to LIFL Middleware (three to four months)
│   └── Sends task create and update events to LIFL Middleware Server webhook
│
├── LIFL Middleware Role — Your Responsibility
│   ├── Expose webhook endpoint for Oracle Primavera Cloud auto-trigger
│   ├── Receive task create and update events
│   ├── Validate JavaScript Object Notation and required fields
│   ├── Transform Oracle Primavera Cloud fields to NetSuite RESTlet payload
│   ├── Authenticate to NetSuite via OAuth 2.0 JSON Web Token
│   ├── Hypertext Transfer Protocol POST create or update to NetSuite RESTlet
│   ├── Handle success and error responses
│   ├── Audit log every request and response
│   └── Retry with exponential backoff and dead-letter queue on failure
│
└── NetSuite Role
    ├── Expose RESTlet script 2116 deploy 1
    ├── Find project by Oracle Primavera Cloud Project Identifier (custentity_lifl_opc_ref)
    ├── Create or update Project Task by Oracle Primavera Cloud Task Identifier (custevent_lifl_opc_task_ref)
    └── Return NetSuite Task Identifier or error message
```

---

## Agreed Architecture

```
Agreed Architecture
│
├── Oracle Primavera Cloud Task or Activity Created or Updated
│   └── Oracle Primavera Cloud Auto-Trigger Customization
│       └── LIFL Middleware Server
│           └── Receive, Transform, Validate
│               └── NetSuite RESTlet Hypertext Transfer Protocol POST
│                   └── NetSuite Project Task Created or Updated
│
└── Rejected Approach — Not Used
    └── NetSuite Scheduled Get or Poll from Oracle Primavera Cloud
```

---

## LIFL Middleware — Detailed Responsibilities

```
LIFL Middleware Server
│
├── Receive
│   ├── Expose webhook or Application Programming Interface endpoint
│   ├── Accept task create events from Oracle Primavera Cloud auto-trigger
│   ├── Accept task update events from Oracle Primavera Cloud auto-trigger
│   └── Coordinate with Oracle Primavera Cloud on delivery mechanism and timeline
│
├── Validate
│   ├── Valid JavaScript Object Notation object
│   ├── Required Oracle Primavera Cloud Project Identifier (opcProjectId)
│   ├── Required Oracle Primavera Cloud Task Identifier (opcTaskId)
│   ├── Date format year-month-day
│   ├── Predecessor types
│   │   ├── Finish-to-Start (FS)
│   │   ├── Finish-to-Finish (FF)
│   │   ├── Start-to-Start (SS)
│   │   └── Start-to-Finish (SF)
│   └── Reject invalid payloads before NetSuite call
│
├── Transform
│   ├── Map Oracle Primavera Cloud Project Identifier to opcProjectId
│   ├── Map Oracle Primavera Cloud Task Identifier to opcTaskId
│   ├── Map task name, start date, end date, status, parent task
│   ├── Map planned work and milestone flag
│   ├── Map predecessors to lineFields.predecessor array
│   └── Set mode create or update
│
├── Authenticate
│   ├── Build JSON Web Token with private key
│   ├── Exchange JSON Web Token for Bearer access token
│   └── Attach Authorization header on Hypertext Transfer Protocol POST
│
├── Push
│   ├── Hypertext Transfer Protocol POST to NetSuite RESTlet Uniform Resource Locator
│   ├── RESTlet script 2116 deploy 1
│   ├── Content-Type application/json
│   └── Timeout and error handling
│
├── Handle Response
│   ├── Parse status Success
│   ├── Store NetSuite Task Identifier (netSuiteTaskId)
│   ├── Log and surface RESTlet errors
│   └── Retry transient failures
│
└── Audit
    ├── Log raw Oracle Primavera Cloud payload
    ├── Log JavaScript Object Notation sent to NetSuite
    ├── Log NetSuite response
    └── Dead-letter queue for permanent failures
```

---

## Middleware Processing Pipeline

```
Oracle Primavera Cloud Auto-Trigger Event
│
├── Step 1 Receive
│   └── receivers/opc_webhook.py
│
├── Step 2 Validate
│   └── validators/payload_validator.py
│
├── Step 3 Transform
│   └── transformers/task_mapper.py
│
├── Step 4 Authenticate
│   └── auth/netsuite_oauth.py
│
├── Step 5 Push
│   └── clients/netsuite_client.py
│
├── Step 6 Handle Response
│   └── services/task_sync_service.py
│
├── Step 7 Audit Log
│   └── logging/audit_logger.py
│
└── Complete — Success or Error Handled
```

---

## Project Folder Structure — Core

```
lifl-opc-netsuite-middleware
│
├── config
│   └── settings.py
│       ├── NetSuite RESTlet Uniform Resource Locator sandbox and production
│       ├── NetSuite account and OAuth settings references
│       ├── Oracle Primavera Cloud webhook security settings
│       └── Environment name and runtime settings
│
├── auth
│   └── netsuite_oauth.py
│       ├── Create JSON Web Token
│       ├── Sign with private key
│       ├── Exchange for Bearer access token
│       └── Token cache until expiry
│
├── receivers
│   └── opc_webhook.py
│       ├── Hypertext Transfer Protocol endpoint for Oracle Primavera Cloud auto-trigger
│       ├── Validate inbound security
│       └── Pass payload to task sync service
│
├── validators
│   └── payload_validator.py
│       ├── Validate JavaScript Object Notation structure
│       ├── Enforce opcProjectId and opcTaskId required
│       ├── Validate date format
│       └── Validate predecessor relationship types
│
├── transformers
│   └── task_mapper.py
│       ├── Map Oracle Primavera Cloud fields to RESTlet payload
│       ├── Apply status mapping table
│       └── Set mode create or update
│
├── clients
│   └── netsuite_client.py
│       ├── Hypertext Transfer Protocol POST to NetSuite RESTlet
│       ├── Attach OAuth Bearer token
│       └── Parse success and error response
│
├── services
│   └── task_sync_service.py
│       ├── Orchestrate receive → validate → transform → authenticate → push → handle response
│       ├── Retry logic with exponential backoff
│       └── Dead-letter queue on permanent failure
│
├── logging
│   └── audit_logger.py
│       ├── Log raw Oracle Primavera Cloud payload
│       ├── Log payload sent to NetSuite
│       └── Log NetSuite response
│
├── main.py
│   └── Application Programming Interface server or worker entry point
│
├── requirements.txt
│   └── Python dependencies (httpx or requests, PyJWT, cryptography)
│
└── .env.example
    └── Environment variable template for secrets (never commit actual .env)
```

---

## Project Folder Structure — Production Optional

```
lifl-opc-netsuite-middleware
│
├── tests
│   ├── test_payload_validator.py
│   ├── test_task_mapper.py
│   └── test_netsuite_client.py
│
├── docs
│   └── mww.md
│       └── Full integration specification and questionnaires
│
├── scripts
│   └── bulk_sync.py
│       └── One-time bulk initial sync for existing Oracle Primavera Cloud tasks
│
└── docker
    └── Dockerfile
        └── Container deployment for LIFL infrastructure
```

---

## Folder Responsibilities Tree

```
Folder Responsibilities
│
├── config/settings.py
│   └── Sandbox and production Uniform Resource Locators, credential references, runtime settings
│
├── receivers/opc_webhook.py
│   └── Receive task and activity events from Oracle Primavera Cloud auto-trigger
│
├── validators/payload_validator.py
│   └── Validate JavaScript Object Notation and enforce opcProjectId and opcTaskId
│
├── transformers/task_mapper.py
│   └── Map Oracle Primavera Cloud fields to NetSuite RESTlet payload format
│
├── auth/netsuite_oauth.py
│   └── Obtain NetSuite Bearer token using OAuth 2.0 private key JSON Web Token
│
├── clients/netsuite_client.py
│   └── Hypertext Transfer Protocol POST create and update requests to NetSuite RESTlet
│
├── services/task_sync_service.py
│   └── Orchestrate full pipeline from receive to response handling
│
├── logging/audit_logger.py
│   └── Audit trail of raw Oracle Primavera Cloud payload and NetSuite response
│
├── main.py
│   └── Application entry point for Application Programming Interface server or worker
│
├── requirements.txt
│   └── Python dependencies
│
└── .env.example
    └── Environment variable template for secrets
```

---

## Field Mapping — Oracle Primavera Cloud to NetSuite RESTlet

```
Field Mapping
│
├── Oracle Primavera Cloud Source Fields
│   ├── Oracle Primavera Cloud Project Identifier
│   ├── Oracle Primavera Cloud Task Identifier
│   ├── Task Name
│   ├── Start Date
│   ├── End Date
│   ├── Status
│   ├── Parent Task
│   ├── Planned Work
│   ├── Milestone Flag
│   └── Predecessors (task reference, relationship type, lag days)
│
├── LIFL Transform Layer
│   └── transformers/task_mapper.py
│
├── NetSuite RESTlet Payload Fields
│   ├── opcProjectId
│   ├── opcTaskId
│   ├── taskName
│   ├── startDate
│   ├── endDate
│   ├── status
│   ├── parent
│   ├── plannedwork
│   ├── isMilestone
│   ├── mode (create or update)
│   └── lineFields.predecessor
│       ├── task
│       ├── type (Finish-to-Start, Finish-to-Finish, Start-to-Start, Start-to-Finish)
│       └── lagdays
│
└── NetSuite Record Fields (after RESTlet processing)
    ├── custentity_lifl_opc_ref ← opcProjectId (Project lookup)
    ├── custevent_lifl_opc_task_ref ← opcTaskId (Task lookup)
    ├── custevent_lifl_opc_payload ← full incoming JSON (audit)
    ├── title ← taskName
    ├── startdate ← startDate
    ├── enddate ← endDate
    ├── status ← status
    ├── parent ← parent (searched by exact task name in same project)
    ├── plannedwork ← plannedwork (skipped when isMilestone is true)
    └── predecessor lines ← lineFields.predecessor
```

---

## Sample Create Payload

```
Sample Create Payload
│
├── mode: create
├── opcProjectId: OPC-PROJ-1001
├── opcTaskId: OPC-TASK-2001
├── taskName: Foundation Work
├── startDate: 2026-08-28
├── endDate: 2026-09-05
├── isMilestone: false
├── status: In Progress
├── parent: Civil Works
├── plannedwork: 40
└── lineFields
    └── predecessor
        └── task: OPC-TASK-1999
            type: Finish-to-Start
            lagdays: 2
```

---

## Sample Update Payload

```
Sample Update Payload
│
├── mode: update
├── opcProjectId: OPC-PROJ-1001
├── opcTaskId: OPC-TASK-2001
├── taskName: Foundation Work - Updated
├── startDate: 2026-08-29
├── endDate: 2026-09-08
├── isMilestone: false
├── status: Completed
├── parent: Civil Works
├── plannedwork: 45
└── lineFields
    └── predecessor
        └── task: OPC-TASK-1999
            type: Finish-to-Start
            lagdays: 0
```

---

## NetSuite RESTlet Processing Flow

```
NetSuite RESTlet Processing Flow
│
├── Step 1 — Validate opcProjectId and opcTaskId
├── Step 2 — Find NetSuite Project using custentity_lifl_opc_ref
├── Step 3 — Find existing Project Task using custevent_lifl_opc_task_ref and Project
├── Step 4 — Create or load Project Task based on mode
├── Step 5 — Set task name, dates, status, planned work, parent, raw payload
├── Step 6 — Process predecessor relationships when supplied
│   └── Search predecessor first by Oracle Primavera Cloud Task Identifier, then by exact task name
└── Step 7 — Save record and return NetSuite Task Internal Identifier
```

---

## Predecessor Relationship Types

```
Predecessor Relationship Types
│
├── Finish-to-Start (FS)
│   └── Predecessor task must finish before current task can start
│
├── Finish-to-Finish (FF)
│   └── Predecessor task must finish before current task can finish
│
├── Start-to-Start (SS)
│   └── Predecessor task must start before current task can start
│
└── Start-to-Finish (SF)
    └── Predecessor task must start before current task can finish
```

---

## What LIFL Middleware Is Not Responsible For

```
Not LIFL Middleware Scope
│
├── NetSuite to Oracle Primavera Cloud project creation — already done
├── Building the NetSuite RESTlet — NetSuite team
├── Building Oracle Primavera Cloud auto-trigger customization — Oracle Primavera Cloud team
├── Storing tasks inside Oracle Primavera Cloud — Oracle Primavera Cloud system
├── NetSuite scheduled scripts polling Oracle Primavera Cloud — rejected approach
└── Populating custentity_lifl_opc_ref on NetSuite Projects — done by existing NetSuite to Oracle Primavera Cloud integration
```

---

## Middleware Design Notes

```
Middleware Design Notes
│
├── From RESTlet Application Programming Interface
│   ├── Default mode is create; RESTlet auto-switches to update if task already exists
│   ├── On update mode, missing Oracle Primavera Cloud task returns error from RESTlet
│   ├── Predecessor removeLine logic is commented out in RESTlet — test replace versus append carefully
│   └── Full payload stored in custevent_lifl_opc_payload on NetSuite Project Task
│
└── From Meeting Decision
    ├── NetSuite to Oracle Primavera Cloud project creation is already live
    ├── This middleware covers Oracle Primavera Cloud to NetSuite Task and Activity only
    ├── Push via LIFL middleware is the agreed pattern
    ├── Oracle Primavera Cloud has no native after-submit trigger — auto-trigger depends on Oracle Primavera Cloud team (three to four months)
    ├── Reuse LIFL existing integration infrastructure (same as bank integrations)
    └── Coordination required across LIFL, Oracle Primavera Cloud, and NetSuite teams
```

---

## Python Technology Stack

```
Python Technology Stack
│
├── Hypertext Transfer Protocol client
│   └── httpx or requests
│
├── JSON Web Token and private key signing
│   └── PyJWT and cryptography
│
├── Configuration and secrets
│   └── Environment variables or secrets vault
│
├── Middleware hosting
│   └── LIFL existing integration infrastructure
│
├── Event receive layer
│   └── REST endpoint for Oracle Primavera Cloud auto-trigger webhook
│
└── Retry and resilience
    ├── Exponential backoff
    └── Dead-letter logging for failed NetSuite pushes
```

---

## Cross-System Test Scenarios

```
Cross-System Test Scenarios
│
├── New task created in Oracle Primavera Cloud
│   └── Auto-trigger → middleware POST mode create → NetSuite Project Task created
│
├── Existing task updated in Oracle Primavera Cloud
│   └── Auto-trigger → middleware POST mode update → NetSuite Project Task updated
│
├── Milestone created in Oracle Primavera Cloud
│   └── isMilestone true, plannedwork not set in NetSuite
│
├── Task with predecessors (Finish-to-Start with lag)
│   └── lineFields.predecessor mapped and created in NetSuite
│
├── Parent and child task hierarchy
│   └── Sync parent before child or retry child after parent synced
│
├── Predecessor not yet in NetSuite
│   └── Queue retry per agreed rule
│
├── Project exists in Oracle Primavera Cloud but not in NetSuite
│   └── Error logged, alert sent, no infinite retry
│
├── Duplicate event from Oracle Primavera Cloud webhook retry
│   └── Idempotent update using opcTaskId
│
├── NetSuite RESTlet down or 500 error
│   └── Retry three times with backoff, then dead-letter queue
│
├── Invalid status from Oracle Primavera Cloud
│   └── Reject before POST if status not in mapping table
│
├── Initial bulk load of existing Oracle Primavera Cloud tasks
│   └── One-time scripts/bulk_sync.py with watermark
│
└── Predecessor updated or removed in Oracle Primavera Cloud
    └── Test carefully — RESTlet removeLine issue
```

---

## Error Response Action Matrix

```
Error Response Action Matrix
│
├── Missing required parameters: opcProjectId or opcTaskId
│   ├── Cause: Bad payload from Oracle Primavera Cloud or mapper error
│   └── Action: Reject before POST, log payload, alert LIFL team
│
├── NetSuite Project not found for Oracle Primavera Cloud Project Identifier
│   ├── Cause: Project reference mismatch — custentity_lifl_opc_ref not set
│   └── Action: Log, alert LIFL team, do not retry indefinitely
│
├── Task not found in update mode
│   ├── Cause: Task never synced or wrong opcTaskId
│   └── Action: Confirm with NetSuite team — retry as create or alert
│
├── Invalid status
│   ├── Cause: Unmapped status value
│   └── Action: Reject before POST, update status mapping table
│
├── Predecessor not found
│   ├── Cause: Predecessor task not yet synced to NetSuite
│   └── Action: Queue retry with delay per agreed rule
│
└── NetSuite 500 or timeout
    ├── Cause: NetSuite system error
    └── Action: Retry three times with exponential backoff, then dead-letter queue, alert LIFL team
```

---

## Status Mapping Template

```
Status Mapping Template — Complete with Oracle Primavera Cloud and NetSuite Teams
│
├── Oracle Primavera Cloud Status Value → NetSuite Status Value → Notes → Confirmed By
├── (row 1 — to be filled in kickoff meeting)
├── (row 2 — to be filled in kickoff meeting)
└── (row 3 — to be filled in kickoff meeting)
```

---

## Questionnaire Sign-Off Milestones

```
Questionnaire Sign-Off Milestones
│
├── Kickoff — questions reviewed
├── Field mapping agreed
├── Status mapping agreed
├── Error handling agreed
├── User Acceptance Testing scenarios passed
└── Production go-live
```

---

## Meeting Attendees Reference

```
Meeting Attendees — 01-09-2026
│
├── LIFL
│   └── Mr. Surendra
│
├── Oracle Primavera Cloud
│   ├── Mr. Raj
│   ├── Mr. Maanikanta
│   └── Mr. Krishna
│
└── BONbLOC
    ├── Dharnish
    ├── Dhaksha
    └── Logeshwaran
```
