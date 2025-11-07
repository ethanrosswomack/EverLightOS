---
conversation_id: "68a944bd-d61c-832d-885d-1ba65d9c5325"
title: "Corporate payments cheat sheet"
accounts: ["Account1_exports"]
models: []
tags: []
message_count: 17
---
# Corporate payments cheat sheet

##  — user


##  — system


##  — system


## 2025-08-23T04:34:05.460000Z — user


## 2025-08-23T04:34:06.919568Z — assistant
Got your “Corporate Payments – Global” deck. Want a quick, no-nonsense cheat sheet you can use while you work? Here’s a one-pager you can keep open.

# Corporate Procure-to-Pay (non-Retail) — TL;DR

## What counts
- All **non-inventory** goods & services Amazon uses internally (Ops, Legal/HR/IT/Marketing, utilities, CAPEX, data center services, taxes/fees/settlements). Not Retail inventory or Marketplace. fileciteturn0file0

## Who does what (fast map)
- **PO Owner**: end-to-end owner; the bridge to vendor; confirms receipt/approves services.  
- **Vendor Manager / Vendor Maintenance**: get the vendor created/maintained in Payee Central.  
- **FinOps Corp AP**: processes invoices/payments per rules.  
- **Support (Tax, Accounting, Legal, etc.)**: governance; help on edge cases. fileciteturn0file0

## Golden rules (S&TP first!)
1) **Follow S&TP** approvals/controllership **before** any commitment.  
2) **Onboard the vendor** in **Payee Central** (separate onboardings if vendor sells **goods & services**).  
3) **Issue a PO** (Coupa for corporate; SC.OS/Cloudforge for data centers).  
4) **Vendor invoice must include the PO number** and match the PO.  
5) **Goods = 3-way match (receipt required)**; **Services = 2-way & approval workflow**.  
6) FinOps pays **after** receipt/approval; otherwise they open a TT describing the fix. fileciteturn0file0

## Quick workflows

### A) Standard PO flow
Contracting → Vendor onboard (Payee Central) → Create PO (correct supplier site, GL, org, location, type) → Vendor invoices **with PO #/line** → AP validates →  
- **Goods**: you post **receipt** in Coupa/Cloudforge → Pay  
- **Services**: you **approve** Oracle workflow email → Pay. fileciteturn0file0

### B) Blanket/recurring
Use **Blanket PO** for multi-month services/consumption; single PO for one-offs. Keep funds/lines aligned to expected billing cadence. fileciteturn0file0

## Set-up essentials (when creating the PO)
- **Supplier number/site matches the vendor’s tax ID/branch.**  
- **Content group & GL string** (company code, cost center, account).  
  - **Assets** → account 16999; **Spare parts** → 14808; **Expenses** → 6xxxx.  
- **PO type**: Goods = quantity/3-way; Services/Freight = amount/2-way.  
- **Separate POs** for **fixed assets vs consumables**. fileciteturn0file0

## The five most common blockers (and how to clear them)
1) **QTY REC (Quantity Receipt) hold** (Coupa): you forgot to receive. → **Find PO → Truck icon → receive** correct qty/date. (Cloudforge: follow “Receiving POs” wiki.) fileciteturn0file0  
2) **PO Overbilled / Max Ship Amount / Qty Ord**: invoice > PO funds/qty. → **Add funds/lines** in Coupa (Request change → Add line/update), then Holds team re-matches. fileciteturn0file0  
3) **Missing approval (Services)**: approve the Oracle workflow email (**ofa-wf-prod@amazon.com**). fileciteturn0file0  
4) **Incorrect GL/location/supplier site**: fix the PO **or** have vendor **cancel** and re-issue invoice; **attach proof of cancellation** in the TT. **Never** receive/approve if details don’t match. fileciteturn0file0  
5) **Vendor not registered**: get them **onboarded** (Payee Central). Separate invites for **goods** and **services** if both. fileciteturn0file0

## Do / Don’t (rapid fire)
- ✅ Validate **gross** price (incl. taxes/fees) before setting PO funds.  
- ✅ Keep vendor aligned on the **exact PO # and line** they must bill.  
- ✅ Use **separate POs** by product type (asset vs expense) to avoid GL defects.  
- ❌ Don’t confirm receipt or approve services if **anything doesn’t match**—request vendor **cancellation** within local deadlines and attach proof.  
- ❌ Don’t forget **services** need **approval**; goods need **receipts**—no exceptions. fileciteturn0file0

## Critical vendors (know when to escalate)
Utilities, telecom, rent/colo, employee benefits—anything where late/non-payment could **halt buildings/ops, harm reputation, or disrupt sites/fulfillment**. Government critical vendors may need **NSQ** flow with supporting docs. fileciteturn0file0

## Coupa change ops you’re allowed to make
Description (non-catalog), coding (not company code), attachments, match type, need-by date, unit price (amount-based), qty (qty-based), payment terms, close/re-open, ownership transfer—each has a tutorial. fileciteturn0file0

## Special cases you’ll see
- **Import of services**: align PO currency to **invoice currency**; confirm withholding/tax rules before placing PO.  
- **PAS / Pre-approved spend** and exceptions: follow policy; some cases are PO-exempt, but GL reference still required. fileciteturn0file0

---

If you want, I can turn this into a printable mini-poster or a step-by-step checklist for your exact role (e.g., PO Owner on Ops services).

## 2025-08-23T04:34:07.148719Z — system


## 2025-08-23T04:34:07.153282Z — system


## 2025-08-23T04:34:07.155700Z — tool


## 2025-08-23T04:34:07.166283Z — tool
Make sure to include fileciteturn0file0 in your response to cite this file. 


















































Confidencial

Amazon Corporate Procure-to-Pay



Agenda

Confidential

• What’s included in Corporate Payments
• S&TP
• Who does What
• Complex Regulatory environment
• Vendor Onboarding
• Purchase Order
• Vendor Invoicing
• Confirmation, approval and payment
• Appendix

Most Common Issues and How to Solve
Transaction types
Useful Links
Critical Vendors
Other Vendor Onboard Methods and Importation of Services



Executive Summary…. Things you must remember 

Confidential

• S&TP - Follow Amazon´s policy regarding contracting, approvals and controllership. 

• For Complex Regulatory environments - Pay attention to details (ex.:  tax IDs for vendor and Amazon, invoice cancellation 
rules)

• Vendor Onboarding – All vendors onboarded is the 1st step. Required by country (for specific tax interview), with separated 
onboards for goods and services

• Purchase Order – Ensure the correct vendor code, correct Amazon taxID, description, amount and quantity with taxes, 1 PO 
per product type or services

• Vendor Invoicing – There are countries where vendor is required to email invoice pdf to Amazon and invoice must have PO 
number.  The invoice must match the PO. Check with your local AP/BP partner for country specific rules

• Confirmation, approval and payment - Receipt (Goods) or Approval (Services) is required. If all checks passed, FinOps will 
schedule payment. If not, FinOps opens a ticket with actions/fixes required by vendor or by PO requester.

• Most Common Issues and How to Solve – Summary guide on how to respond to FinOps TTs (slides 29-37)



Confidential

If you mean RETAIL Purchases (inventory that will be sold by amazon.com), this is NOT
your place!

If you mean CORPORATE Purchases (Goods or Services that will be used internally) OR 
Datacenter purchases... This is the right place!

NEED TO BUY ON BEHALF OF AMAZON BRAZIL?



What is included in Corporate Payments

Confidential

All goods and services for Amazon as final user 

Includes:

• All non-inventory items used internally (such as office and shipping supplies)

• Services covering Fulfillment Centers, Transportation and other services related to Operations

• Services for diverse Corporate purposes, such as Legal, Marketing, HR and IT advisors, intermediary and 
infrastructure services

• Taxes, bank charges, fines & penalties, legal settlements

• Essencial site services as water, energy, telecom (Critical Vendors)

• Fixed assets (CAPEX)

• Services related to datacenters, digital, music and video (content creators, producers, partners)

Does NOT include:

• Inventory items that will be sold by Amazon

• Marketplace purchases (3P)



Every Transaction has ONE PURPOSE and SEVERAL IMPACTS

Confidential

THE PURPOSE

• A service to be provided for our 
Business

• A maintenance item

• An input for our Operations

• An asset for our Launches

• A critical service

reputation

taxes

expansions

operations

suppliers quality financials

business 
efficiency

compliance

sales

accounting

supply chain

withholding 
tax

procurement

THE 
IMPACTS



First Things First - The Spending & Transaction Policy

Confidential

The purpose of this policy is to ensure that all transactions are properly approved, 
contracted for, and in the best overall interests of Amazon. Prior to agreeing to any 
transaction (even if no expenditure is involved) and before initiating or requesting any 
payment to or from a third party, you must complete or comply with the approvals and 
controllership described in the Policy.

• S&TP POLICY

https://inside.amazon.com/en/services/legal/us/spendingandtransaction/Pages/default.aspx 

https://knet2.amazon.com?%252fDeepLink%252fProcessRedirect.aspx%253fmodule%253dlodetails%2526lo%
253d863591e0-763e-4f02-a8aa-bf600e24e8b7

• S&TP TRAINING SESSION

https://inside.amazon.com/en/services/legal/us/spendingandtransaction/Pages/default.aspx
https://knet2.amazon.com/?%252fDeepLink%252fProcessRedirect.aspx%253fmodule%253dlodetails%2526lo%253d863591e0-763e-4f02-a8aa-bf600e24e8b7
https://knet2.amazon.com/?%252fDeepLink%252fProcessRedirect.aspx%253fmodule%253dlodetails%2526lo%253d863591e0-763e-4f02-a8aa-bf600e24e8b7
https://knet2.amazon.com/?%252fDeepLink%252fProcessRedirect.aspx%253fmodule%253dlodetails%2526lo%253d863591e0-763e-4f02-a8aa-bf600e24e8b7
https://knet2.amazon.com/?%252fDeepLink%252fProcessRedirect.aspx%253fmodule%253dlodetails%2526lo%253d863591e0-763e-4f02-a8aa-bf600e24e8b7
https://knet2.amazon.com/?%252fDeepLink%252fProcessRedirect.aspx%253fmodule%253dlodetails%2526lo%253d863591e0-763e-4f02-a8aa-bf600e24e8b7
https://knet2.amazon.com/?%252fDeepLink%252fProcessRedirect.aspx%253fmodule%253dlodetails%2526lo%253d863591e0-763e-4f02-a8aa-bf600e24e8b7
https://knet2.amazon.com/?%252fDeepLink%252fProcessRedirect.aspx%253fmodule%253dlodetails%2526lo%253d863591e0-763e-4f02-a8aa-bf600e24e8b7
https://knet2.amazon.com/?%252fDeepLink%252fProcessRedirect.aspx%253fmodule%253dlodetails%2526lo%253d863591e0-763e-4f02-a8aa-bf600e24e8b7
https://knet2.amazon.com/?%252fDeepLink%252fProcessRedirect.aspx%253fmodule%253dlodetails%2526lo%253d863591e0-763e-4f02-a8aa-bf600e24e8b7
https://knet2.amazon.com/?%252fDeepLink%252fProcessRedirect.aspx%253fmodule%253dlodetails%2526lo%253d863591e0-763e-4f02-a8aa-bf600e24e8b7


Roles & Responsibilities Who Does What?

Confidential

PO Owner - Responsible for the Order inclusion and specific purchase management end to end. In case there is any issue with 
the PO or the invoice, the PO Owner is the bridge between Amazon and the vendor.

Vendor Manager Responsible for the Vendor registration,  administration and contact

Vendor Maintenance Responsible for the Vendor creation, maintenance and administration

FinOps Corp AP Responsible for performing transactions within AP based on the predetermined rules.

Corporate Support  Functions Responsible for providing technical support and guideline for Corp AP and Businesses.
- International Tax
- Accounting
- Legal
- Taskless Tax
- Tax Compliance

FinOps BP Support the operating effectiveness, connecting Business/Corporate with FinOps AP



NOW LET’S START!

Confidential



1) Contract Negotiation

2) Supplier Onboard

3) Creating a PO

4) Vendor Invoicing

5) Invoice Receipt

6) Validation

7) Payment

How the Process Works – Purchase Order cases 



How the Process Works* – Purchase Order cases 

Depends on the Business: 
- Procurement 
- Program Managers
- Business Managers
- Centrallized support area
etc

The Business contact that will be 
responsible for the Vendor relations

1) Contract Negotiation

2) Supplier Onboard

3) Creating a PO

4) Vendor Invoicing

5) Invoice Receipt

6) Validation

7) Payment

• One Business contact to create the requisition
• One PO Owner
• Eventually, there are other Business contacts that support with PO issues 

resolution or service/item delivery follow up 

• Interaction between ALL Vendors and Amazon FinOPs

• FinOps Process



Business Contact Who Does What?

Confidential

PO Owner - Responsible for the Order inclusion and specific purchase management end 
to end. In case there is any issue with the PO or the invoice, the PO Owner is the bridge 
between Amazon and the vendor.

• Vendor Manager Responsible for the Vendor registration,  administration and 
contact

• Purchase requisition creator – Connected to the PO Owner’s organization. Must 
comply with the Purchase details and attend to details once creating the starting 
requisition to ensure no defects will be generated along the processing

• Procurement POC

• Program Managers

• PO Funds 

• PO Approvers

• PO Management Support

Let’s avoid payment issues as we 
are Customer Obsessed!



Vendor Onboard

Confidential

GPO AND RELATED TEAMS: please check specific rules for Vendor Onboard for Global Procurement Share 
Services (GPSS) PROJECT GALILEO. Reach out to your Site Procurement POC or: 

https://w.amazon.com/bin/view/Global_Procurement_Shared_Services/Vendor_Onboarding

GPSS POC galileoproject@amazon.com ; gpo-gpss-vm-communication-smb@amazon.com 

https://w.amazon.com/bin/view/Global_Procurement_Shared_Services/Vendor_Onboarding
mailto:galileoproject@amazon.com
mailto:gpo-gpss-vm-communication-smb@amazon.com
mailto:gpo-gpss-vm-communication-smb@amazon.com
mailto:gpo-gpss-vm-communication-smb@amazon.com
mailto:gpo-gpss-vm-communication-smb@amazon.com
mailto:gpo-gpss-vm-communication-smb@amazon.com
mailto:gpo-gpss-vm-communication-smb@amazon.com
mailto:gpo-gpss-vm-communication-smb@amazon.com
mailto:gpo-gpss-vm-communication-smb@amazon.com
mailto:gpo-gpss-vm-communication-smb@amazon.com


Vendor Onboard: Basic Steps (1 of 3)

The Vendor Onboard is necessary for ALL countries via Payee Central. 
The standard payment terms is 60 days. 

• Check if the Vendor already exists in Amazon Payee Central. Click on the link:
https://w.amazon.com/index.php/GFS/VPS/SSC/UserGuide/PayeeManagement#How_do_I_find_a_supplier

• If the Vendor does not exist in Payee Central, then Vendor Onboard is required. Vendor Managers are 
responsible for sending the invitation to the Vendors. 

• Payee Central Scope referral https://w.amazon.com/bin/view/Payee_Central/Payee_Central_Current_Scope_Matrix/ 

• Foreign Vendors: of a vendor has already onboarded at any other Amazon country, they will have to onboard 
again to submit to the specific country tax interview

• If your Vendor will supply both SERVICES and GOODS, two separated onboard invitations are required. When 
creating the PO, the corresponding Supplier Code must be used for that specific purchase.

https://w.amazon.com/index.php/GFS/VPS/SSC/UserGuide/PayeeManagement#How_do_I_find_a_supplier
https://w.amazon.com/bin/view/Payee_Central/Payee_Central_Current_Scope_Matrix/


Vendor Onboard: in Payee Central (2 of 3)

Confidential

1) Payee Central Wiki Page

https://w.amazon.com/bin/view/Payee_Central/   

2) Get access to Payee Central

https://w.amazon.com/bin/view/Corporate_AP_Guide/payeecentral/permissions

3) Ask your Vendor to complete the Training Session for Vendors

https://amazonfinops.au1.qualtrics.com/jfe/form/SV_cDcgMB6mLASWZOC 

4) Send and invitation for the supplier
https://w.amazon.com/bin/view/Payee_Central/Payee_Central_Payee_Setup/#HHowdoIsetupaPayee3F 

https://broadcast.amazon.com/videos/360950 

https://w.amazon.com/bin/view/Payee_Central/
https://w.amazon.com/bin/view/Corporate_AP_Guide/payeecentral/permissions
https://amazonfinops.au1.qualtrics.com/jfe/form/SV_cDcgMB6mLASWZOC
https://w.amazon.com/bin/view/Payee_Central/Payee_Central_Payee_Setup/#HHowdoIsetupaPayee3F
https://broadcast.amazon.com/videos/360950


Vendor Contact with FinOps: Creating Ticket in Payee Central (3 of 3)

Confidential

https://amazonexteu.qualtrics.com/jfe/form/SV_cOL2E5ISvOTVcjQ

https://amazonexteu.qualtrics.com/jfe/form/SV_cOL2E5ISvOTVcjQ


Purchase Order (PO)

Confidential



Purchase Order (1 of 3)
https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx 

1) ONE TIME ORDER OR RECURRING ORDER?

In case of SINGLE PO: 
PO-Only Guideline https://inside.amazon.com/en/services/legal/us/spendingandtransaction/Pages/PO-OnlyGuidelines.aspx 

In case of RECURRING PURCHASE (ex. 12 months contract for supplies monthly charged)
Blanket PO Wiki https://w.amazon.com/bin/view/Blanket_PO_Definition

 COUPA → GCP tool for Corporate Purchases

 SC.OS/CLOUDFORGE → AWS tool for Datacenter Purchases

2) Creating a PO

PO EXEMPTS: https://policy.amazon.com/policy/1578

MANDATORY: THE VENDOR 

MUST INFORM THE PO 

NUMBER IN THE INVOICE.

https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx
https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx
https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx
https://inside.amazon.com/en/services/legal/us/spendingandtransaction/Pages/PO-OnlyGuidelines.aspx
https://inside.amazon.com/en/services/legal/us/spendingandtransaction/Pages/PO-OnlyGuidelines.aspx
https://inside.amazon.com/en/services/legal/us/spendingandtransaction/Pages/PO-OnlyGuidelines.aspx
https://w.amazon.com/bin/view/Blanket_PO_Definition


Purchase Order (2 of 3)
https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx 

3) PO DETAILS

• Supplier number: refer to the exact Vendor TAX ID/Branch(correct TAX ID, fully onboarded) → review the correct 
supplier code, ensure to select the correct supplier site

• Amazon Content Group: double check your organization
• Amazon Location (identified in the GL String)
• Service or goods description: exactly match the described in the invoice
• GL String: matching location, org and cost center. Reach out to your Finance POC
• Fixed Assets x Consumable Goods need separated POs
• Product type (assets, spare parts, expense) or service needs to match the GL string:
 Company codes (4R, MG, 5B, MN, B903, B868)
 GL String Account Code 16999 to indicate Assets
 GL String Account Code 14808 to indicate Spare Parts
 GL String Account Code that begins with 6XXXX indicate Expenses
• PO type: 
Goods: PO must be 3-way match and quantity-based
Services or Freights: PO must be 2-way match and amount-based

https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx
https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx
https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx


Purchase Order (3 of 3) – useful links
https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx 

COUPA
COUPA Wiki Page & Office Hours Information https://w.amazon.com/bin/view/Buy_stuff_at_amazon

Wikis and Training Resources:   https://broadcast.amazon.com/videos/53057
https://w.amazon.com/bin/view/Coupa_Training
https://w.amazon.com/bin/view/Corporate_AP_Guide/coupa/

What amount should I include in the PO?  https://policy.amazon.com/procedure/8314

#Coupa-interest Slack channel to ask general questions: https://amzn-fgbs.slack.com/archives/C018HS9U60L

Company code to Coupa content group mapping: https://w.amazon.com/index.php/GCP%20OU%20Company%20Code%20Mapping%20Help

PAS (Pre-Approved Spend) Queries: https://w.amazon.com/bin/Coupa_Pre_Approved_Spend_PAS_NonPAS_Budget_Periods/

SIM Ticket creation for other requests: https://t.corp.amazon.com/ (C : CORP NON-INV PROC COUPA / T: COUPA / I: [pick one])

SC.OS/CLOUDFORGE
https://w.amazon.com/bin/view/ISCaP/InfraOpsProcurement/
https://w.amazon.com/bin/view/DCEO/PDX/Cloudforge_Purchasing/
https://w.amazon.com/bin/view/Corporate_AP_Guide/cloudforge/https://w.amazon.com/bin/view/InfraProcurement/CloudForgeRequisit ion/UserGuide/
https://w.amazon.com/bin/view/AWSProcurement/
https://w.amazon.com/index.php/InfraProcurement/CloudForgeRequisition/UserGuide

https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx
https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx
https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx
https://w.amazon.com/bin/view/Buy_stuff_at_amazon
https://broadcast.amazon.com/videos/53057
https://w.amazon.com/bin/view/Coupa_Training
https://w.amazon.com/bin/view/Corporate_AP_Guide/coupa/
https://policy.amazon.com/procedure/8314
https://amzn-fgbs.slack.com/archives/C018HS9U60L
https://amzn-fgbs.slack.com/archives/C018HS9U60L
https://amzn-fgbs.slack.com/archives/C018HS9U60L
https://w.amazon.com/index.php/GCP%20OU%20Company%20Code%20Mapping%20Help
https://w.amazon.com/bin/Coupa_Pre_Approved_Spend_PAS_NonPAS_Budget_Periods/
https://t.corp.amazon.com/
https://w.amazon.com/bin/view/ISCaP/InfraOpsProcurement/
https://w.amazon.com/bin/view/DCEO/PDX/Cloudforge_Purchasing/
https://w.amazon.com/bin/view/Corporate_AP_Guide/cloudforge/https:/w.amazon.com/bin/view/InfraProcurement/CloudForgeRequisition/UserGuide/
https://w.amazon.com/bin/view/Corporate_AP_Guide/cloudforge/https:/w.amazon.com/bin/view/InfraProcurement/CloudForgeRequisition/UserGuide/
https://w.amazon.com/bin/view/Corporate_AP_Guide/cloudforge/https:/w.amazon.com/bin/view/InfraProcurement/CloudForgeRequisition/UserGuide/
https://w.amazon.com/bin/view/AWSProcurement/
https://w.amazon.com/index.php/InfraProcurement/CloudForgeRequisition/UserGuide


PO Modifications– DOs and DON’T’s

Confidential

Coupa allows for PO modifications to Change the following.

• Item description for Non -Catalog POs
• PO Coding changes except for the Company Code
• Adding the Attachments
• Match Type Change https://broadcast.amazon.com/videos/165813
• Need By Date Change → https://broadcast.amazon.com/videos/566765
• Unit Price Change for Amount Based POs → Refer to the Tutorial https://broadcast.amazon.com/videos/164031
• Qty Changes on Qty Based PO → Refer to the Tutorial https://broadcast.amazon.com/videos/164031
• Payment Terms Update → https://broadcast.amazon.com/videos/566832
• PO Closure → Refer to the Tutorial → https://broadcast.amazon.com/videos/566932
• PO Re-Opening → Refer to the Tutorial → https://broadcast.amazon.com/videos/566862
• PO ownership changes → Refer to the Tutorial https://broadcast.amazon.com/videos/566962

https://broadcast.amazon.com/videos/165813
https://broadcast.amazon.com/videos/566765
https://broadcast.amazon.com/videos/164031
https://broadcast.amazon.com/videos/164031
https://broadcast.amazon.com/videos/566832
https://broadcast.amazon.com/videos/566932
https://broadcast.amazon.com/videos/566862


Vendor Invoicing

Confidential



Vendors

Confidential

• Double check the information given in the onboard

• The invoice needs to inform the PO number

• Goods: inform the corresponding PO line item in the invoice



Confirmation, Approval and Payment

Confidential



Confirmation, Approval and Payment (1 of 3)
https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx 

GOODS:  3-Way match The PO Owner is responsible for confirming that the item was 
received and there is match between the ordered and received material. 
COUPA: https://broadcast.amazon.com/videos/72541

SC.OS/Cloudforge https://w.amazon.com/bin/viewrev/AWS_SCM_OPS_SUPPORT_FAQ/WebHome?rev=71.1#HReceivingorReturningonCFPlatform

SERVICES: Confirmation of Service and Approval for Payment → Once the invoice is
processed, the PO Owner receives an e-mail from an automatic Oracle workfow requesting
the verification and approval for payment. The payment will only be performed once the
approval is given. In case there is no response from the PO Owner, the workflow is escalated.

The payment is triggered only after the Confirmation of Goods Receipt (3-way match) or Service approval.

If the invoice is on Hold due to missing receipt/approval, an automatic e-mail is sent to the user/approver 

requesting action.

https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx
https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx
https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx
https://broadcast.amazon.com/videos/72541
https://w.amazon.com/bin/viewrev/AWS_SCM_OPS_SUPPORT_FAQ/WebHome?rev=71.1#HReceivingorReturningonCFPlatform


Vendor Invoicing  Cancellation
PO Requestors: validate all PO and vendor invoice information in order to avoid incorrect remittance. If an error 
was identified after the invoice was issued, request the vendor the immediate proof of cancellation of the 
invoice. 

Confirmation, Approval and Payment (2 of 3)
https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx 

If: 
- You are unsure of the invoice data
- The material doesn’t match what was ordered
- There are any inconsistencies with the purchase
NEVER confirm the receipt of a Good (3-way match) because of potential compliance issues

ALWAYS keep a close communication with the vendor in order to require any necessary corrections or cancellations on time. 
There is a DEADLINE FOR CANCELLATIONS according to local regulation.

https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx
https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx
https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx


Invoice Receipt & Validation 
The Invoice Receipt team will verify, validate and ingest all data related to the invoice received by the Vendor 
versus the PO that was created by the PO Owner.  

Payment 
If all previous steps were correctly followed, your vendor should expect the payment on the agreed due date. The 
vendor can view the payment status in Payee Central.

For Internal use: Payee Central Training Guide Link
See pages 43-45 at the link

If there is any issue, a Ticket will be created and adressed to the PO Owner containing the issue description to be 
solved. The Payment will be kept On Hold until the issue is resolved. 

Confirmation, Approval and Payment (3 of 3)
https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx 

https://document-versions-production.s3.us-west-2.amazonaws.com/23b3a052-029f-4752-8e93-dc2fd420f7a5?response-content-disposition=attachment%3B%20filename%3D%22Payee%20Central%20Internal%20Training%20Guide.pdf%22&response-content-type=application%2Fpdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIA2DQ7HDUA3A3ZVB4W%2F20230329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230329T153124Z&X-Amz-Expires=300&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFPgxsaYpNS0sLteoGzv4IT5ckWPqUSa9%2BW6xknu1hWRAiEAxcCwnX7Cd35YmZ0rmVZJwRx%2BsWHoNvC9gdWzr9TbUloqyAMIYBADGgw2OTQ3NzY0MzgwMTciDJj%2F16Rj4lp6s%2B2QzyqlA9A2qXhjWeC5ED3ycmN1TNojm7cRkU3BeZIkmwsi17Ok47ZO4BCLBTqShVpfw5byOMfsZ87wTiNtDL1qRna2iQrYeLzxrmGkTQWv1tlDhTM0Sn%2BfhqphDb1kiTNqtFNZCv5nSk%2F465eRK%2B%2FllIYHs9pQ1w%2FhGSfiwSNdEZl98kKpPeBs7gtcJ5UVwosFi7Kl%2FD1RmzcxommHKjBhC8F4F2LlqIkfRUK9sAKhRZZOCkKm14X9UqDjD8U5jj4KSJ%2F4CAC4vmDLlhLoqrtVSJFd2%2FyaeQHZV%2FhWNikvVkInDtR29UWVLVkeyAK%2BxF3vN%2FNYrso1EZuG%2BBaRxlQbvB6vRNYiuhn9RvWQefKu1tmPMlsIyKNd5Kdu0FQKIMD7aLdx%2BMV2yJH%2B7Q5asiluRULnuU4Pud8HLQPcbuFWotaerNlRqxYi0z19iFCjx9laETHLEfSso6udbuU98ixdair3veYdUxcYbnq53%2FZOXt%2BZtkj2WxJUvLRKl%2FrrUmyVbT%2FpFaUklJyKmqBTpVN6HCCBVpI30%2FfvWzMzMx%2BLo5kAmn%2BUXseJhjwwspmRoQY6oQHcsaQG16dwczqS%2BneT8WTgZar38o9Ygsy2SJpjMA2ShXzv4dRMVP6CMJi5WYddn%2BkOMSHq36o5uezNV%2F4REcGORpN5h%2Fd%2FGD3uYWjvXo52dInjw7XGdLH0wEGfZ2Wtce%2Bl3NMK7s1vNF3W8Kih8tfo93l8BZZcEv3NoLuFpwyLkU7EqIkDN8f8N6wdPY0b1FTiIr83ML6hjVlNBhFRLKRIaQ%3D%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=4352043309f8db37a2211a498b1aed7a07c1d7c825925a1e239d71f2c34293c6
https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx
https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx
https://inside.amazon.com/en/services/finance/accountspayable/Pages/SA-AP.aspx


Support Links

• Corporate AP Wiki → https://w.amazon.com/bin/view/Corporate_AP_FinOps_BP

• Payee Central Search Invoice→ https://finopscentral-na.amazon.com/payeecentral/invoices#/search

• Payee Central Invoice Holds → https://finopscentral-na.amazon.com/payeecentral/invoices#/hold/search

• The ALL-IN-1 guide for PO requesters → https://w.amazon.com/bin/view/Corporate_AP_Guide/

• Invoice on Hold SOP to take action → https://w.amazon.com/bin/view/Payee_Central/Payee_Central_Invoice_Holds/action

• Amazon Payee Central link for Vendors → https://payeecentral.amazon.com/

• Company code to Coupa content group mapping → https://w.amazon.com/index.php/GCP%20OU%20Company%20Code%20Mapping%20Help

• Payee Central Invoice on Hold (IOH) - How to Resolve → https://broadcast.amazon.com/videos/1179170

• Payee Central Invoice Holds Training → Training Video

• PO Creation Steps → https://broadcast.amazon.com/videos/897710

• Extending a Payee to additional countries, business or payment types → Wiki Link

• How to send and invitation for the supplier → Video Training , Wiki Link

• Check if the Vendor already exists in Amazon Payee Central → Wiki

• PO Approver Delegation when OOO → Video Training

https://w.amazon.com/bin/view/Corporate_AP_FinOps_BP
https://finopscentral-na.amazon.com/payeecentral/invoices#/search
https://finopscentral-na.amazon.com/payeecentral/invoices#/search
https://finopscentral-na.amazon.com/payeecentral/invoices#/search
https://finopscentral-na.amazon.com/payeecentral/invoices#/hold/search
https://finopscentral-na.amazon.com/payeecentral/invoices#/hold/search
https://finopscentral-na.amazon.com/payeecentral/invoices#/hold/search
https://w.amazon.com/bin/view/Corporate_AP_Guide/
https://w.amazon.com/bin/view/Payee_Central/Payee_Central_Invoice_Holds/action
https://payeecentral.amazon.com/
https://w.amazon.com/index.php/GCP%20OU%20Company%20Code%20Mapping%20Help
https://broadcast.amazon.com/videos/1179170
https://broadcast.amazon.com/videos/137384?query=Hold+resolution&focus=body&match=and+complete+++the+receipts+that+in+West+hold+++can+be+resolved+.+Um+%2C+so
https://broadcast.amazon.com/videos/897710
https://w.amazon.com/bin/view/Payee_Central/Payee_Central_Payee_Setup/Extend_New_Country
https://broadcast.amazon.com/videos/360950
https://w.amazon.com/bin/view/Payee_Central/Payee_Central_Payee_Setup/#HHowdoIsetupaPayee3F
https://w.amazon.com/index.php/GFS/VPS/SSC/UserGuide/PayeeManagement#How_do_I_find_a_supplier
https://broadcast.amazon.com/videos/164523


Payee Modification Links

• Update Payment Terms https://tt.amazon.com/quicklink/Q000763124 
• New Site Creation https://t.corp.amazon.com/create/quicklink/Q001059954 
• Update Remit Email https://t.corp.amazon.com/create/templates/8532acae-28d9-4df9-9353-6f788c6b0f2c 
• Update Payment Method https://t.corp.amazon.com/create/templates/cbd92c4e-5d33-4c37-8110-e7421d65ad4b 
• Update Bank Details https://t.corp.amazon.com/create/templates/0dbaab90-e402-4f97-9177-5460894fb859 
• Supplier Name Change https://t.corp.amazon.com/create/templates/98390975-3817-4e6c-a350-adf866cc5046 
• Enable Purchasing Box https://t.corp.amazon.com/create/templates/ad129c21-4f7e-4d6d-bd30-afe5a9252cda 
• Payee Central - Backfill https://t.corp.amazon.com/create/quicklink/Q001014527 
• Deactivate Payee https://t.corp.amazon.com/create/quicklink/Q000889750 
• Activate Payee https://tt.amazon.com/quicklink/Q001319913

https://tt.amazon.com/quicklink/Q000763124
https://t.corp.amazon.com/create/quicklink/Q001059954
https://t.corp.amazon.com/create/templates/8532acae-28d9-4df9-9353-6f788c6b0f2c
https://t.corp.amazon.com/create/templates/8532acae-28d9-4df9-9353-6f788c6b0f2c
https://t.corp.amazon.com/create/templates/8532acae-28d9-4df9-9353-6f788c6b0f2c
https://t.corp.amazon.com/create/templates/8532acae-28d9-4df9-9353-6f788c6b0f2c
https://t.corp.amazon.com/create/templates/8532acae-28d9-4df9-9353-6f788c6b0f2c
https://t.corp.amazon.com/create/templates/8532acae-28d9-4df9-9353-6f788c6b0f2c
https://t.corp.amazon.com/create/templates/8532acae-28d9-4df9-9353-6f788c6b0f2c
https://t.corp.amazon.com/create/templates/8532acae-28d9-4df9-9353-6f788c6b0f2c
https://t.corp.amazon.com/create/templates/8532acae-28d9-4df9-9353-6f788c6b0f2c
https://t.corp.amazon.com/create/templates/cbd92c4e-5d33-4c37-8110-e7421d65ad4b
https://t.corp.amazon.com/create/templates/cbd92c4e-5d33-4c37-8110-e7421d65ad4b
https://t.corp.amazon.com/create/templates/cbd92c4e-5d33-4c37-8110-e7421d65ad4b
https://t.corp.amazon.com/create/templates/cbd92c4e-5d33-4c37-8110-e7421d65ad4b
https://t.corp.amazon.com/create/templates/cbd92c4e-5d33-4c37-8110-e7421d65ad4b
https://t.corp.amazon.com/create/templates/cbd92c4e-5d33-4c37-8110-e7421d65ad4b
https://t.corp.amazon.com/create/templates/cbd92c4e-5d33-4c37-8110-e7421d65ad4b
https://t.corp.amazon.com/create/templates/cbd92c4e-5d33-4c37-8110-e7421d65ad4b
https://t.corp.amazon.com/create/templates/cbd92c4e-5d33-4c37-8110-e7421d65ad4b
https://t.corp.amazon.com/create/templates/0dbaab90-e402-4f97-9177-5460894fb859
https://t.corp.amazon.com/create/templates/0dbaab90-e402-4f97-9177-5460894fb859
https://t.corp.amazon.com/create/templates/0dbaab90-e402-4f97-9177-5460894fb859
https://t.corp.amazon.com/create/templates/0dbaab90-e402-4f97-9177-5460894fb859
https://t.corp.amazon.com/create/templates/0dbaab90-e402-4f97-9177-5460894fb859
https://t.corp.amazon.com/create/templates/0dbaab90-e402-4f97-9177-5460894fb859
https://t.corp.amazon.com/create/templates/0dbaab90-e402-4f97-9177-5460894fb859
https://t.corp.amazon.com/create/templates/0dbaab90-e402-4f97-9177-5460894fb859
https://t.corp.amazon.com/create/templates/0dbaab90-e402-4f97-9177-5460894fb859
https://t.corp.amazon.com/create/templates/98390975-3817-4e6c-a350-adf866cc5046
https://t.corp.amazon.com/create/templates/98390975-3817-4e6c-a350-adf866cc5046
https://t.corp.amazon.com/create/templates/98390975-3817-4e6c-a350-adf866cc5046
https://t.corp.amazon.com/create/templates/98390975-3817-4e6c-a350-adf866cc5046
https://t.corp.amazon.com/create/templates/98390975-3817-4e6c-a350-adf866cc5046
https://t.corp.amazon.com/create/templates/98390975-3817-4e6c-a350-adf866cc5046
https://t.corp.amazon.com/create/templates/98390975-3817-4e6c-a350-adf866cc5046
https://t.corp.amazon.com/create/templates/98390975-3817-4e6c-a350-adf866cc5046
https://t.corp.amazon.com/create/templates/98390975-3817-4e6c-a350-adf866cc5046
https://t.corp.amazon.com/create/templates/ad129c21-4f7e-4d6d-bd30-afe5a9252cda
https://t.corp.amazon.com/create/templates/ad129c21-4f7e-4d6d-bd30-afe5a9252cda
https://t.corp.amazon.com/create/templates/ad129c21-4f7e-4d6d-bd30-afe5a9252cda
https://t.corp.amazon.com/create/templates/ad129c21-4f7e-4d6d-bd30-afe5a9252cda
https://t.corp.amazon.com/create/templates/ad129c21-4f7e-4d6d-bd30-afe5a9252cda
https://t.corp.amazon.com/create/templates/ad129c21-4f7e-4d6d-bd30-afe5a9252cda
https://t.corp.amazon.com/create/templates/ad129c21-4f7e-4d6d-bd30-afe5a9252cda
https://t.corp.amazon.com/create/templates/ad129c21-4f7e-4d6d-bd30-afe5a9252cda
https://t.corp.amazon.com/create/templates/ad129c21-4f7e-4d6d-bd30-afe5a9252cda
https://t.corp.amazon.com/create/quicklink/Q001014527
https://t.corp.amazon.com/create/quicklink/Q000889750
https://tt.amazon.com/quicklink/Q001319913


THANK YOU

Confidential

Appendix
• Most Common Issues and How to Solve
• Transactions included in Corporate Payments
• Useful Links
• Critical vendors



Most Common PO Issues and How to Solve

Confidential



Most Common PO Issues and How to Solve

Defect Name Description Root Cause What to Do (TT resolving) How to Prevent This Issue Long Term Solution

The negotiation with the Vendor 

have inconsistencies.

(1) PO Requestor must ensure what is 

the correct one (invoice or PO);

(2) If the invoice is correct and the PO is 

incorrect, add funds to the PO; 

(3) If the PO is correct and the Invoice is 

incorrect, ask the vendor to cancel the 

invoice and send the proof of 

cancellation immediately and trough the 

same TT;

PO requestor to validate a 

preview of the invoice with the 

Vendor before its submitted to 

AP mailbox

None. PO and invoice 

must match.

The PO has only enough funds for 

the net purchase amount.

Since Brazil system requires the full 

amount in the processing, the user must 

add funds to cover the taxes and 

additional charges.

PO requestor to validate a gross 

price preview with the Vendor 

before to use as reference for 

the PO creation 

Being analized through 

Volcano. To be 

confirmed.

There was a previous invoice 

issued against the PO, but it was 

wrong/cancelled and should not 

be paid. The PO is consuming 

funds that cannot be reversed due 

to system limitations.

(1) Immediately send the proof of 

cancellation of the previous invoice 

trough the same TT;

(2) Corp AP will analyze case by case and 

define action path to the PO Requetor 

throught the TT

Always keep close control of all 

invoices your Vendor is sending 

Amazon. If there is any wrong 

invoice, always request 

immediate proof of 

cancellation to the Vendor and 

inform Corp AP team (within 

same month of the original 

invoice, preferably)

Being analized through 

Volcano. To be 

confirmed.

Happens when the PO does not 

have enough budgets to process 

the payment. The invoice 

amount (or sum of invoices 

issued against the PO) is more 

than the total PO approved 

fund.

Short of Funds



Most Common PO Issues

Defect Name Description Root Cause What to Do (TT resolving) How to Prevent This Issue Long Term Solution

Missing PO Number

Missing GL String

Incorrect/ Invalid Location

Happens when the PO or invoice 

location are different, or it 

doesn't match with the GL String 

Location.

The PO and invoice location 

information was not properly 

validated before the negotiation 

or the GL String was not prior 

verified by a Finance POC.

(1) PO Requestor must ensure what is 

the correct one (invoice or PO);

(2) If the invoice is correct and the PO is 

incorrect, correct the PO information; 

(3) If the PO is correct and the Invoice is 

incorrect, ask the vendor to cancel the 

invoice and send the proof of 

cancellation immediately and send it 

trough the same TT;

PO requestor to validate a 

preview of the invoice with the 

Vendor before its submitted to 

AP mailbox. Also validate teh 

GL String with a Finance POC.

None. This requirement 

will be kept.

PO Closed

Happens when the PO is already 

closed by the Requestor and 

cannot be used to process any 

more invoices.

If all invoices were already issued 

to the PO before closing it, the PO 

requestor didn't create a new PO 

and updated the Vendor with the 

new correct PO number.

(1) Re-Open the PO and add funds so the 

invoice can be processed;

(2) OR Create a new PO and inform Corp 

AP in the TT

Always monitor your POs and 

ensure the Vendor mentions 

the correct one in the invoice

None. This requirement 

will be kept.

Incorrect PO / GL String

Happens when the PO don't 

refer to the same Vendor in the 

invoice, or the GL String is not 

correspondent to the correct 

expense account x product type

(1) The PO Requestor didn't select 

the correct supplier number to 

create the PO; 

(2) OR the Vendor issued the 

invoice from the wrong branch;

(3) AND the PO requestor didn't 

select the correct GL String for the 

specific product type

(1) PO Requestor must ensure what is 

the correct one (invoice or PO);

(2) If the invoice is correct and the PO is 

incorrect, correct the PO; 

(3) If the PO is correct and the Invoice is 

incorrect, ask the vendor to cancel the 

invoice and send the proof of 

cancellation immediately and send it 

trough the same TT - and issue a new 

correct invoice

PO requestor to validate a 

preview of the invoice with the 

Vendor before its submitted to 

AP mailbox. Also validate the 

GL String with a Finance POC. 

None. This requirement 

will be kept.

Happens when the invoice 

doesn´t mention the PO number 

(or GL string - in PO exempt 

cases) and Corp AP cannot match 

the invoice to the proper 

approved budget.

The Vendor was not informed or 

forgot to add the mandatory 

information in the invoice.

Inform the PO number or GL String (if PO 

exempt) in the TT

None. This requirement 

will be kept.

Inform the Vendor that PO 

reference (or GL string) is 

mandatory to be referenced in 

the invoice and always send 

the updated PO copy to the 

vendor. 



Most Common PO Issues

Defect Name Description Root Cause What to Do (TT resolving) How to Prevent This Issue Long Term Solution

Vendor Not Registered in OFA

Happens when the invoice was 

received by a Vendor in the 

Mailbox but there is no Vendor 

Oboard for that Vendor CNPJ.

There was no onboard invitation 

made to that Vendor, or the 

onboard was not completed.

Vendor Manager send the Vendor 

Onboard invitation to the Vendor and 

ask them to complete the onboard 

steps.

PO Requestors should always 

verify the correct supplier 

number exists for the Vendor's 

branch before asking them to 

send invoices to Amazon 

mailbox.

Being analized through 

Volcano. To be 

confirmed.

Quantity Rec (AP Holds)

Happens when there is no 

confirmation of the material 

receipt (3-way match)

PO Requestor forgot to confirm 

receipt.
Confirm receipt. Confirm receipt.

None. This requirement 

will be kept.

Max Ship Amount (AP Holds)

Qty Ord (AP Holds)

Missing Approval (Services)

Happens when a Service invoice 

is on Hold waiting for the 

Business approval in OFA to 

move forward

PO Approver received an e-mail 

from ofa-wf-prod@amazon.com 

but didn't realize there is an action 

pending

Approve the Service in OFA so it can be 

paid.

Approve the Service in OFA so 

it can be paid.

None. This requirement 

will be kept.

Similar to Short of Funds. PO 

does not have sufficient funds 

to cover total invoice amount.

Total PO and invoice amount and 

quantity discrepancies by line.

Corp AP will indicate the correct path 

case by case.

PO Line vs Invoice Line ideally 

should match 100% (net + 

taxes)

Being analized through 

Volcano. To be 

confirmed.



Most Common PO Issues – AP HOLDS: QTY REC COUPA

How is the QTY REC hold resolved in Coupa?
wiki: https://broadcast.amazon.com/videos/164520

1. The requester must search for the PO to receive.



Most Common PO Issues – AP HOLDS: QTY REC COUPA

2. Click on the truck Icon

3. Choose the line, quantity and date you want to receive and 
save the changes.



Most Common PO Issues – QTY REC SC.OS/CLOUDFORGE

How is the QTY REC hold resolved in SC.OS/Cloudforge?

Wiki: https://w.amazon.com/bin/view/ARN_Logistics_-_Receiving_POs_in_Cloudforge_Procurement/



Most Common PO Issues – AP HOLDS: PO OVERBILLED

Note: In Payee Central Hold is described as "PO Overbilled" and in Oracle as "Max Ship Amount“. It also adds "Qty Ord", 
which is released at the same time as the Po Overbilled hold.



Most Common PO Issues – AP HOLDS: PO OVERBILLED COUPA

How is the PO OVERBILLED hold resolved in COUPA?

Video Explaining adding funds to PO https://broadcast.amazon.com/videos/164031 

Step by Step:
1-Select your name on the top 

2-Select Activity 

3- Then Select Orders

4- Provide PO in search 

5- Select PO

6- Scroll down to Bottom you will find Request change.

7-Click on Request change.

8- Scroll down to Bottom you will Find Add Line

9-Select Add line.  Once you provide the details( like Description, Qty, amount Need by date, category, invoice matching type)

10-click on Submit change request

Once the funds are added to the PO, and the holds team gets notified we proceed to correct the matching in Oracle in order to release the hold. 



Most Common PO Issues – PO OVERBILLED SC.OS/Cloudforge

How is the PO OVERBILLED hold resolved in SC.OS/Cloudforge?
ALL PO management instructions can be found at the Wiki https://w.amazon.com/bin/view/AWSProcurement 

https://w.amazon.com/bin/view/AWSProcurement


Types of Transaction included in Corporate Payments

Confidential

• Purchase Ordering (COUPA/SC.OS/ 
Cloudforge)

• Legal Firms (Legal Billing)

• Tax services (Tax Billing)

• Colocation

• Direct Debts

• Royalty payments

• Funding

• Remessas (bookkeeping only)

• Early Payments

• Pre-Payment

• Remessas (bookkeeping only)

• Transportation payments (TIPS)

• Litigation payments

• Corporate Card (P-Card)

• Ops Rentals

• Office Rentals

• BR Associates

• Critical Vendors

• others



Useful Links (1 of 2)

Confidential

CORPORATE AP GUIDE https://w.amazon.com/bin/view/Corporate_AP_Guide

S&TP https://inside.amazon.com/en/services/legal/us/spendingandtransaction/Pages/default.aspx

PO-Only Guideline https://inside.amazon.com/en/services/legal/us/spendingandtransaction/Pages/PO-OnlyGuidelines.aspx

AWS Procurement https://w.amazon.com/bin/view/AWSProcurement/

COMPANY CODES https://w.amazon.com/bin/view/GCP_OU_Company_Code_Mapping_Help/

GLOBAL PO & APPROVAL THRESHOLD EXCEPTIONS https://policy.amazon.com/policy/1578

BRAZIL CORP AP PAGE https://inside.amazon.com/en/services/finance/accountspayable/Pages/Brazil-Ap-Page.aspx

COUPA TRAINING https://w.amazon.com/bin/view/Coupa_Training

PAYEE MANAGEMENT https://w.amazon.com/index.php/GFS/VPS/SSC/UserGuide/PayeeManagement#How_do_I_find_a_supplier

PAYMENT TERMS https://w.amazon.com/index.php/Global_Corporate_Standard_Payment_Terms_Policy_(Non-Inventory)

NGOs https://legal.amazon.com/sites/LegalTeams/InternationalConsumerLegal/LiBra/Pages/ngos.aspx

LATAM FINOPS WHO IS WHO https://w.amazon.com/bin/view/FinOpsLATAMwhoiswho/

CHART OF ACCOUNTS https://share.amazon.com/sites/Corporate_Accounting/global_accounting/COA/Listings/OFA/cost_center.html

INVOICE RECEIVING (BRAZIL) https://w.amazon.com/bin/view/Invoice_Receiving_Process_Brazil/



Useful Links (2 of 2)

Confidential

LATAM CRITICAL VENDORS https://w.amazon.com/index.php/Latam%20Critical%20Vendors%20Guide

PAYEE CENTRAL https://w.amazon.com/bin/view/Payee_Central

P2P GUIDE https://river-dub.amazon.com/BTS13/home?buildingType=FinComBTS

CREATURE https://w.amazon.com/bin/view/FinanceAutomation/FinanceApprovals/Creature/

VENDOR MANAGEMENT ROLES & RESPONSIBILITIES https://w.amazon.com/bin/view/Roles&Responsabilities

VENDOR MAINTENANCE https://w.amazon.com/bin/view/AP-VM/Home

RETAIL ACCOUNTS PAYABLE https://w.amazon.com/bin/view/AccountsPayables/RetailBrazil/

INVOICE HOLDS TOOL https://w.amazon.com/bin/view/Payee_Central/Payee_Central_Invoice_Holds/

INVOICE REQUIREMENTS https://w.amazon.com/bin/view/Corporate_Accounts_Payable_Invoice_Requirements/

BLANKET PO https://w.amazon.com/bin/view/Blanket_PO_Definition/

INTERNAL SEARCH TOOL https://is.amazon.com/

PAYEE CENTRAL COMPLETE GUIDE https://document-versions-production.s3.us-west-2.amazonaws.com/23b3a052-029f-4752-8e93-dc2fd420f7a5?response-content-disposition=attachment%3B%20filename%3D%22Payee%20Central%20Internal%20Training%20Guide.pdf%22&response-content-type=application%2Fpdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIA2DQ7HDUA3A3ZVB4W%2F20230329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230329T153124Z&X-Amz-Expires=300&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFPgxsaYpNS0sLteoGzv4IT5ckWPqUSa9%2BW6xknu1hWRAiEAxcCwnX7Cd35YmZ0rmVZJwRx%2BsWHoNvC9gdWzr9TbUloqyAMIYBADGgw2OTQ3NzY0MzgwMTciDJj%2F16Rj4lp6s%2B2QzyqlA9A2qXhjWeC5ED3ycmN1TNojm7cRkU3BeZIkmwsi17Ok47ZO4BCLBTqShVpfw5byOMfsZ87wTiNtDL1qRna2iQrYeLzxrmGkTQWv1tlDhTM0Sn%2BfhqphDb1kiTNqtFNZCv5nSk%2F465eRK%2B%2FllIYHs9pQ1w%2FhGSfiwSNdEZl98kKpPeBs7gtcJ5UVwosFi7Kl%2FD1RmzcxommHKjBhC8F4F2LlqIkfRUK9sAKhRZZOCkKm14X9UqDjD8U5jj4KSJ%2F4CAC4vmDLlhLoqrtVSJFd2%2FyaeQHZV%2FhWNikvVkInDtR29UWVLVkeyAK%2BxF3vN%2FNYrso1EZuG%2BBaRxlQbvB6vRNYiuhn9RvWQefKu1tmPMlsIyKNd5Kdu0FQKIMD7aLdx%2BMV2yJH%2B7Q5asiluRULnuU4Pud8HLQPcbuFWotaerNlRqxYi0z19iFCjx9laETHLEfSso6udbuU98ixdair3veYdUxcYbnq53%2FZOXt%2BZtkj2WxJUvLRKl%2FrrUmyVbT%2FpFaUklJyKmqBTpVN6HCCBVpI30%2FfvWzMzMx%2BLo5kAmn%2BUXseJhjwwspmRoQY6oQHcsaQG16dwczqS%2BneT8WTgZar38o9Ygsy2SJpjMA2ShXzv4dRMVP6CMJi5WYddn%2BkOMSHq36o5uezNV%2F4REcGORpN5h%2Fd%2FGD3uYWjvXo52dInjw7XGdLH0wEGfZ2Wtce%2Bl3NMK7s1vNF3W8Kih8tfo93l8BZZcEv3NoLuFpwyLkU7EqIkDN8f8N6wdPY0b1FTiIr83ML6hjVlNBhFRLKRIaQ%3D%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=4352043309f8db37a2211a498b1aed7a07c1d7c825925a1e239d71f2c34293c6



Critical Vendors

Confidential



Critical Vendors (1 of 2)
https://w.amazon.com/bin/view/Critical_vendor_creation/ 

WHO IS A CRITICAL VENDOR?

A Critical Vendor can be defined as vendors who as a result of non/late payment of invoices could impact Amazon by:

• causing any of our buildings/office spaces to be unfit and/or unsafe for use

• causing reputational damage to Amazon or result in non-negotiable penalties/fees.

• disturbing traffic to Amazon websites or impairing our commitment to deliver customer orders on time.

• risk of service interruption affecting core operations

TYPES OF CRITICAL VENDORS LATAM:

• Utility (Gas / Electric / Water / Waste / Etc.)

• Telecommunication (Voice Service / Data Circuits / Transit or Transport / Etc.)

• Building Rent / Lease / Colocations (https://w.amazon.com/bin/view/Dglenny%40/Training/CoLo/ )

• Employee Benefits ( Employee Benefits like Insurance, Health care, Meal passes & Relocation charges etc.)

https://w.amazon.com/bin/view/Critical_vendor_creation/
https://w.amazon.com/bin/view/Dglenny%40/Training/CoLo/


Critical Vendors (2 of 2)
https://w.amazon.com/bin/view/Critical_vendor_creation/ 

CRITICAL VENDOR SUPPLIER ONBOARD

The Critical Vendor Supplier Onboard must follow the general steps in Payee Central. 

Exceptions: Government Critical Vendors. Check below:

• Non-Governmental Critical Vendor Onboard: Vendor Managers are responsible for sending the invitation to the 
Vendors via Payee Central.  

• Governmental Critical Vendor Onboard: Vendor Managers must fill NSQ Form and attach supporting offical 
documentation.

For more information, check LATAM Wiki  https://w.amazon.com/bin/view/Latam_Critical_Vendors_Guide/

https://w.amazon.com/bin/view/Critical_vendor_creation/
https://w.amazon.com/bin/view/Latam_Critical_Vendors_Guide/


Other topics

Confidential



Other Vendor Onboarding Methods

Confidential

• What are the other methods & systems used outside of Payee Central and when they are applicable

NSQ – The NSQ process was in place before Payee Central rollout. It is still ONLY valid for NGO (Non Governmental

Organizations) and Public Sector payments (such as Critical Vendors). DO NOT set up a regular vendor creation via
NSQ.

NSQ Form & Instructions: https://inside.amazon.com/en/services/finance/accountspayable/Pages/NSQ.aspx  

Contracting with NGOs: https://legal.amazon.com/sites/LegalTeams/InternationalConsumerLegal/LiBra/Pages/ngos.aspx

To request a Vendor Creation via NSQ, open a ticket in the following CTI:
C – Accounts Payable – Vendor Maintenance
T – Payee Set-up
I – Payee Setup by NSQ – LATAM ---

https://inside.amazon.com/en/services/finance/accountspayable/Pages/NSQ.aspx
https://legal.amazon.com/sites/LegalTeams/InternationalConsumerLegal/LiBra/Pages/ngos.aspx


Importation of Services 

Before placing an importation order, be aware of:

- Taxation rules based on the destination country

- Withholding Tax rules by country

- COUPA / SC.OS/Cloudforge Purchase Order placement requirements 

- The PO currency MUST match the invoice currency

https://policy.amazon.com/procedure/8314 

https://policy.amazon.com/procedure/8314

	Slide 1: Amazon Corporate Procure-to-Pay 
	Slide 2
	Slide 3
	Slide 4: NEED TO BUY ON BEHALF OF AMAZON BRAZIL?
	Slide 5
	Slide 6
	Slide 7
	Slide 8
	Slide 9: NOW LET’S START!
	Slide 10
	Slide 11
	Slide 12
	Slide 13: Vendor Onboard
	Slide 14
	Slide 15
	Slide 16
	Slide 17: Purchase Order (PO)
	Slide 18
	Slide 19
	Slide 20
	Slide 21
	Slide 22: Vendor Invoicing
	Slide 23
	Slide 24: Confirmation, Approval and Payment
	Slide 25
	Slide 26
	Slide 27
	Slide 28
	Slide 29
	Slide 30: THANK YOU
	Slide 31: Most Common PO Issues and How to Solve
	Slide 32
	Slide 33
	Slide 34
	Slide 35
	Slide 36
	Slide 37
	Slide 38
	Slide 39
	Slide 40
	Slide 41
	Slide 42
	Slide 43
	Slide 44: Critical Vendors
	Slide 45
	Slide 46
	Slide 47: Other topics
	Slide 48
	Slide 49



## 2025-08-23T04:34:07.185018Z — tool
All the files uploaded by the user have been fully loaded. Searching won't provide additional information.

## 2025-08-23T04:34:07.227721Z — assistant


## 2025-08-23T04:34:07.918838Z — assistant


## 2025-08-23T04:34:15.543817Z — assistant


## 2025-08-23T04:35:39.451000Z — user
I'm just wondering why it was sent to me through microsoft teams

## 2025-08-23T04:35:39.881640Z — system


## 2025-08-23T04:35:39.905649Z — assistant
That training deck most likely came through Microsoft Teams because Amazon (and a lot of big enterprises) push out **mandatory compliance and process refreshers** using Teams as the broadcast channel.  

Here’s why it would land with you:

- **Role-based targeting** – Since you’re in RME/PMO/WHS, you fall into a group that sometimes needs to understand *corporate procure-to-pay* rules (even if you don’t directly raise POs every day). They’ll push the training file to everyone in that org or cost center through Teams.  
- **Distribution efficiency** – Teams is often used as a broadcast hub for decks that aren’t tracked in official LMS (like Embark/Learn). It gets around email bloat and ensures you at least *see* the file.  
- **Audit trail** – Sending through Teams (and storing the file in the channel) creates a lightweight record that “training was provided” in case Finance or Legal ever audits.  
- **Cross-functional exposure** – You may not be an AP person, but knowing how **POs, receipts, and services approvals** work matters if you ever touch Coupa/Cloudforge, interact with vendors, or request capital/parts.  

So in short: it wasn’t random—it’s **pushed broadly so you know the guardrails**, even if you won’t use every detail daily.  

👉 Do you want me to strip that big deck into just the **pieces actually relevant to an RME Tech 2 / Ops support role** so you don’t drown in finance jargon? That way, you’d know exactly why *you* were looped in.

## 2025-08-23T04:35:40.004798Z — system

