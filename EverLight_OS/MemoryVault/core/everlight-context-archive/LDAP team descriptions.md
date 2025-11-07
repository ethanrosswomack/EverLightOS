---
conversation_id: "68b6adde-7094-8325-be4c-c1c9d9c28645"
title: "LDAP team descriptions"
accounts: ["Account1_exports"]
models: []
tags: []
message_count: 7
---
# LDAP team descriptions

##  — system


##  — user


##  — system


## 2025-09-02T08:42:42.652853Z — assistant


## 2025-09-02T08:42:42.662411Z — assistant
Got it — I can break this down for you.

### What These Are  
The list you pasted are **LDAP / POSIX group memberships** inside Amazon’s internal identity system.  
- **LDAP (Lightweight Directory Access Protocol)** is how Amazon manages user access across thousands of systems.  
- Each “team” or “group” listed is basically an **access bucket**: if you’re in the group, you inherit the permissions, dashboards, tools, or reporting visibility tied to that group.  
- They’re not always literal “teams of people” — a lot of them are for systems access, QuickSight dashboards, reporting, compliance tools, VPN entry, etc.  
- That’s why you see things like `NA-RME-all`, `FC-VPN-Access`, `Carts_Dashboard_FC_OPS`, and `Adapt-conversation-hub` — these are access control handles, not necessarily org charts.

### Why “BBM-user” says *Base Building Maintenance – Management Team*  
- The **hover text** you saw is the **long-form description** attached to that LDAP group.  
- “BBM” expands to **Base Building Maintenance**. In Amazon RME/Facilities world, **Base Building** means the physical site infrastructure: HVAC, electrical, water, fire systems, etc.  
- The “Management Team” part likely means this group ties into reporting or access used by managers (but in practice, many non-managers get dropped into it if they need to pull those reports or see related dashboards).  
- So when you hover, you’re just seeing the **admin-set description of the group**, not a new title for you.

### Why You’re in So Many  
- Amazon associates get added automatically to groups depending on their **role, site (TPA4), department (RME), and job level (L3 in your case)**.  
- Example:  
  - `NA-RME-all` = all North America RME associates.  
  - `TPA4-RME` = everyone in RME at your building.  
  - `RME - QuickSight Access` = lets you read dashboards.  
  - `BBM-user` = ties you into Base Building Maintenance dashboards or permissions, even if you’re not personally doing HVAC work.  

### TL;DR  
These LDAP teams are your **system access and reporting groups**, not literal “teams of people you report into.”  
The **BBM-user** group expands to “Base Building Maintenance – Management Team” because that’s the description attached to that LDAP group in the directory. It doesn’t mean you were promoted or reassigned — it just means you’ve got access to tools/dashboards that BBM management uses.  

---

Want me to go through your list and **map out which of these are “core to RME job function” vs. which are “reporting/dashboard only”**? That way you’d have a cleaner picture of what’s essential and what’s just passive access.

## 2025-09-02T08:42:42.814424Z — system


## 2025-09-02T08:42:44.990000Z — user
Tell me what these are and why the BBM one when i hover over it says Base Building Maintenance - Management Team 

These are all of the LDAP teams I'm a part of 


TEAMS Logo
0 Pending Actions 

Home

Create a Team

Your Teams

Bulk Ownership Management

Search Teams by Rules


+
Teams You Are Primary Owner Of

+
Teams You Are Secondary Owner Of

+
Teams You Are Member Of

+
Teams You Are Permanent Override Of

+
Switch Region
Lookup another user

Ethan Womack (erwomack)
Title
Mech & Robotics Tech
Department
RME - FC - VAR
Job Family
Real Estate/Facilities
Job Level
3
Location
TPA4-SFC(Temple Terrace,FL,US)
Manager
James Rodriguez
View Ethan Womack's POSIX/LDAP/ANT groups
Primary Owner Manage Ownership
None
Secondary Owner
None
Member
02 RAP Group 2 - P4
ACES-Bi-SCC-dashboard-view
adapt-conversation-hub-feedback-subtype-uat-wave-1
adapt-conversation-hub-migration-uat-wave-1
adapt-conversation-hub-stu-uat-wave-1
AimsInsightsPlatform_MoreIO_BlueBadge_Users
all-rme-temp
AMZL L3
amzlbia-quicksight-ro-team
AMZLStations-NA-SCC-Work-Items
AQAT_QS_Reporting_L3
AR KB Maintenance
ar-programs-l3plus-qs-viewer
aranea-fop-l3-preview
ATA Metrics
atlas-k
atzptl-dashboard-maintenance
ava-2-prod-na-users-TPA4
Avatar-Access-Group
avp-raft-access
BBM-user
bifrost-compliance-tool-team
BIM Quicksight Dashboard
btn-users
CAMP-Deep-Dive
Capacity-Snapshot-QS-Access
Cardinal-Remote-Access
Carts_Compliance_Dashboard_ro_ant_auto_migration_2021-10-11
Carts_Dashboard_FC_OPS
cedric-access-l3-stores-1
controllership_hub_grc_5254_ops_rme
cpex-product-inspector
diesel-website-access
DORA-UI-RME-Access
dpr-fire-iot-qs-access-3
DQI-PROD-ACCESS
DST-woeye-users
e4l-thrive-ops-prof-conv-engagee-pop-test
EAM-NA-SSO-USERS-TEAM
EOS-Full-Access
EPP IMTP OPS dashboard access
eu-aces-finance-reporting
eu-cpex-team-sharefolder-read_only_ruled_L3
EU-ICQA-quicksight
EU_ACES_SME_POWERBI_USERS
eucf-ops-managers
eugrt-asm-swread
eurme-eam-aws-sso-users2
eurme-ignition-rme
eurme-ignition-users
eurme-ignition-users-na
eurme-software-access
FC-VPN-Access
Fleet-QS-Parameter
fop-all-kw-l3
fop-m365-fc-knowledge-worker-license-override-list
fp-fm-prod-na
GLO2-ENGINEERING
Global-AMS-PBI
Global_Learning_Dashboard_NA
gpo-bi-clm-ssa
GRT-APM-NA-SSO-USERS
grt-cluster-na-cf-rme-user
gts-strategic-projects-powerbi-ro
Huddles Reports Tagawa 2
HylasFrontendWebsite-Read-Access
IDS-Kickout-RME_ldap_auto_migration_2024-03-14
ipex_analytics_reporting_L3
ixd-t3-quicksight-read
Kiva DU and Station Provisioning
Kiva Support
lawrereb-l3-test
LMPayments-na-amzl-ops-viewers
mapbi-qs-readers
Measurement Quicksight
MHE Quicksight Reports Readers
MindYourStepProgram_Team4
MLU-Eligible-Other-4
mobile-optic-read-access-prod
NA Quality ReLo Standard Report Audience
NA RME DMS SSO Users
NA-AR-RME-ALL
NA-FC-myvoice-TPA4
NA-FT-Read-Only-MRU-MRT-MJT
na-rme-all
na-rme-all-bb
NA-RME-Fld-all
NA-RME-Fld-L1-8-bb
NA-RME-RMET-all
NA_RME_AR_MGMT
NACF LQ360 Dashboard
NACF-AE-READ-PERMISSIONS
nacf-rme-all
nacf-rme-bb-all
nasc_quicksight_access
OneStopShopSharedDrive
OPERATIONS_L3_BELOW_5YRS_NA
Ops Exchange Migration Wave 20
opus-idp-group-ops-2
osp-hc-dashboard
OTSMT-Permissions-052
People-Leaders-Directs
pi-e4l-ops-reports
pi-e4l-ops-reports-test
pi-engage-conversation-hub-l3
ProcessEngineering
qs-tagawa-joblevel3-notEqual-jrzeppa-org
qs-user-worldwide-consumer-org-cl3-reader
qs-user-worldwide-consumer-org-cl3-reader-quick
Quattro-RME-Customers
qubit-team-qs-viewer
qubit-terra-access-operations-3
RAP Blue Badge User L3
RME
RME - QuickSight Access
RME COE
RME-compass-asd-manager
rme-compass-users
rme-helios-users team
RME-Troubleshooting-Center-Contributors
RME_AND_OPS_Team
RME_Controls_RemoteAccess
RME_Coupa Roles
RME_IC
robin-ssh-access
ROC-IPEX
ROC_IPEX_Usrs_FC_L3
ROME_Permissions_Team
scar-odyssey-readers
scot-yde2-report
SecureAttach_Onboarded_Users_5
sfv-viewer
SPPR Wiki Access NAFC T3
STE Ava US Browser Extension Group 3
t3-and-up-operations
T3s in NACF
TApp-Admin-RME
test_fop-m365-fc-knowledge-worker-license-override-list
Tim Collins Team
Token Grantor to All Vendors
TPA4-FC-general
TPA4-RME
TPA4-VOA-ALL
TPA4-VOA-Associates
TPA4-VOA-L1-L3
tsa-2024-yonatang
TSSL TAB QS
Umbrella_Transcript_Tracking
Utility Consumption and ECM Reporting
VOD Boards
webmtt_teams_test_group
wwci-ava-2-prod-na-engineer
wwde_ext_tableau_viewers_alternate
WWDE_GEN11x_ACAT_Access
WWS Dashboard Access - NACF
ZOOM-PROD-AUTH-EXCLUDE-OPS
ZOOM-PROD-LICENSE-INCLUDE-FULL-OPS-4
Need help?

    FAQ
    Permissions
    Teams Support
    About Teams

