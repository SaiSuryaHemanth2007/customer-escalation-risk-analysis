# Customer Escalation Risk Analysis
### DIET Hackathon | Team 10 — Luminary Logic

An evidence-led exploratory data analysis (EDA) project examining customer-support ticket workload, data quality, ticket segments, service timestamp patterns, and recorded customer satisfaction.

**Repository:** [customer-escalation-risk-analysis](https://github.com/SaiSuryaHemanth2007/customer-escalation-risk-analysis)

---

## 1. Project Overview

Customer-support teams need visibility into where unresolved work accumulates and which ticket categories or support channels may require operational review.

This project analyses the Customer Support Tickets dataset supplied for the DIET hackathon to:

- Understand dataset structure, completeness, and quality.
- Define transparent and reproducible workload KPIs.
- Compare ticket status across ticket types, priorities, and support channels.
- Examine available service timestamp information and recorded customer satisfaction.
- Consolidate evidence-backed findings into exactly three prioritised management actions.

> **Important:** The supplied dataset does not contain an explicit escalation indicator. Confirmed escalation counts and escalation rates therefore cannot be calculated. Tickets with status **Open** or **Pending Customer Response** are described as *unresolved workload*, not confirmed escalations.

## 2. Team Details

**Team 10 — Luminary Logic**  
Dhanekula Institute of Engineering and Technology (DIET), Ganguru, Vijayawada, Andhra Pradesh.

| Member | Name | Responsibility |
|---|---|---|
| Member 1 | V. Purna Chandra Sai | Data Understanding & Data Quality |
| Member 2 | G. Kapil Varun Babu | KPI Analysis |
| Member 3 | Shaik Taniya Jasmin | Segment & Hotspot Analysis |
| Member 4 | Makarla Chahnitha | Service Performance |
| Member 5 | Sai Surya Hemanth Sanapathi | Integration & Final Findings |

## 3. Repository Structure

```text
customer-escalation-risk-analysis/
├── dashboard/
│   └── app.py
├── data/
│   ├── raw/
│   │   └── customer_support_tickets.csv   # Local dataset; do not commit
│   └── processed/
├── docs/
│   ├── HLD.md
│   ├── LLD.md
│   ├── architecture.md
│   ├── data_flow.md
│   ├── module_design.md
│   ├── technology_stack.md
│   └── testing_strategy.md
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_quality.ipynb
│   ├── 03_kpi_analysis.ipynb
│   ├── 04_segment_hotspot_analysis.ipynb
│   ├── 05_service_performance.ipynb
│   └── 06_final_findings.ipynb
├── reports/
│   └── charts/
├── tests/
├── .gitignore
├── requirements.txt
└── README.md
```

## 4. Dataset

The project uses the **Customer Support Tickets** dataset supplied through the hackathon.

| Dataset attribute | Value |
|---|---:|
| Records | 8,469 |
| Columns | 17 |
| Exact duplicate rows | 0 |
| Duplicate Ticket IDs | 0 |

The challenge documentation describes the dataset as synthetic/simulated. Results must not be represented as live production customer outcomes.

### Dataset setup

The raw CSV is not included in this public repository. Obtain the dataset through the official hackathon channel and place it locally at:

```text
data/raw/customer_support_tickets.csv
```

The consolidated notebook includes a dataset-path configuration cell. If the CSV is stored elsewhere, update that path instead of changing downstream analysis code.

## 5. Technology Stack

- **Language:** Python
- **Data analysis:** pandas, NumPy
- **Visualisation:** Matplotlib, Seaborn, Plotly
- **Notebook environment:** Jupyter Notebook
- **Testing:** pytest
- **Additional file support:** openpyxl

Dependencies are listed in `requirements.txt`.

## 6. Getting Started

### Step 1 — Clone the repository

```bash
git clone https://github.com/SaiSuryaHemanth2007/customer-escalation-risk-analysis.git
cd customer-escalation-risk-analysis
```

### Step 2 — Create and activate a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt**

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3 — Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4 — Add the dataset

Place the organiser-provided CSV at `data/raw/customer_support_tickets.csv`, or enter its local path in the notebook's dataset-path configuration cell.

### Step 5 — Run the notebooks

Open the repository in VS Code or Jupyter and execute the notebooks in this order:

| Order | Notebook | Purpose |
|---:|---|---|
| 1 | `01_data_understanding.ipynb` | Dataset dimensions, fields, data types, and initial profiling |
| 2 | `02_data_quality.ipynb` | Missing values, duplicates, and validation |
| 3 | `03_kpi_analysis.ipynb` | Supported KPI calculations and denominators |
| 4 | `04_segment_hotspot_analysis.ipynb` | Ticket type, channel, and priority comparisons |
| 5 | `05_service_performance.ipynb` | Timestamp coverage, timestamp intervals, and CSAT |
| 6 | `06_final_findings.ipynb` | Evidence register, limitations, and management actions |

Run each notebook from a clean kernel, from top to bottom. Confirm the dataset path and expected column names before execution.

## 7. Analysis Scope

| Area | Analysis |
|---|---|
| Data understanding | Dataset dimensions, field types, and initial profiling |
| Data quality | Missingness, exact duplicates, duplicate IDs, and timestamp validation |
| KPI framework | Ticket volume, unresolved count, unresolved share, and eligible denominators |
| Ticket status | Open, Pending Customer Response, and Closed status mix |
| Ticket type | Ticket counts and unresolved share by ticket category |
| Channel | Ticket counts and status composition by support channel |
| Priority | Distribution of Low, Medium, High, and Critical tickets |
| Service timestamps | Valid interval between recorded first-response and resolution timestamps |
| Customer satisfaction | Distribution and descriptive statistics for recorded CSAT values |
| Final findings | Evidence register, interpretation boundaries, and management actions |

## 8. Key Findings

The values below are the team's currently established aggregate findings. Re-run all notebooks against the final hackathon dataset before using them in the final presentation or submission.

### 8.1 Overall ticket workload

| Metric | Observed result |
|---|---:|
| Total tickets | 8,469 |
| Open | 2,819 |
| Pending Customer Response | 2,881 |
| Closed | 2,769 |
| Unresolved workload (Open + Pending) | 5,700 |
| Unresolved share | 67.30% |

### 8.2 Unresolved workload by ticket type

| Ticket type | Total tickets | Unresolved tickets | Unresolved share |
|---|---:|---:|---:|
| Cancellation request | 1,695 | 1,179 | 69.56% |
| Product inquiry | 1,641 | 1,108 | 67.52% |
| Technical issue | 1,747 | 1,167 | 66.80% |
| Billing inquiry | 1,634 | 1,090 | 66.71% |
| Refund request | 1,752 | 1,156 | 65.98% |

Cancellation requests have the highest unresolved share among the listed ticket types.

### 8.3 Unresolved workload by support channel

| Channel | Total tickets | Unresolved tickets | Unresolved share |
|---|---:|---:|---:|
| Social media | 2,121 | 1,437 | 67.75% |
| Phone | 2,132 | 1,441 | 67.59% |
| Chat | 2,073 | 1,399 | 67.49% |
| Email | 2,143 | 1,423 | 66.40% |

Social Media has the highest unresolved share among the listed channels. The spread across channels is modest and should be interpreted descriptively.

### 8.4 Priority distribution

| Priority | Tickets |
|---|---:|
| Medium | 2,192 |
| Critical | 2,129 |
| High | 2,085 |
| Low | 2,063 |

Priority is a workload classification in this dataset; it is not an escalation indicator.

### 8.5 Customer satisfaction

- Available ratings: **2,769**
- Missing ratings: **5,700 (67.30%)**
- Mean recorded CSAT: **2.99 / 5**
- Median recorded CSAT: **3.00 / 5**

Missing CSAT values are not treated as zero. Satisfaction statistics describe recorded ratings only.

## 9. Exactly Three Prioritised Management Actions

### 1. Instrument escalation explicitly

Add a governed escalation indicator, escalation timestamp, escalation tier, and reason code to the ticket schema. Define the eligible-ticket population and denominator centrally. This will make confirmed escalation counts and rates measurable in future analysis.

### 2. Review cancellation-request handling

Cancellation requests have the highest observed unresolved share (**1,179 of 1,695; 69.56%**). Review routing, ownership, customer-wait states, required information, and hand-offs before changing operational processes.

### 3. Investigate Social Media unresolved workload

Social Media has the highest observed channel unresolved share (**1,437 of 2,121; 67.75%**). Review ticket routing and pending-response handling, then validate the pattern over a broader time window and with operational context.

These are evidence-based investigation priorities. The descriptive dataset does not prove that any single process factor caused the observed workload.

## 10. Data Limitations and Responsible Interpretation

The supplied dataset does not support every metric requested in the hackathon brief. The project records the following limitations:

- **No escalation indicator:** confirmed escalated-ticket counts and escalation rates cannot be computed.
- **Priority is not escalation:** Critical or High priority must not be relabelled as escalated.
- **No queue/department field:** queue-level comparisons are unavailable.
- **No ticket-created timestamp:** true first-response duration, total resolution duration from creation, backlog age, and long-running rate cannot be calculated.
- **Timestamp interval only:** the difference between First Response Time and Time to Resolution describes the interval between those two recorded events, where both values parse and pass validation. It is not total ticket-resolution time from creation.
- **No SLA target:** SLA breach rates cannot be calculated.
- **Missing CSAT:** missing ratings are not zero and are not evidence of dissatisfaction.
- **Synthetic/simulated data:** the dataset must not be presented as live production customer data.
- **Descriptive analysis:** observed patterns do not establish causation.

Do not publish customer names, email addresses, or raw ticket descriptions in notebooks, reports, screenshots, or public repository outputs.

## 11. Project Documentation

Architecture and implementation documents are maintained in the `docs/` folder:

- [High-Level Design](docs/HLD.md)
- [Low-Level Design](docs/LLD.md)
- [Architecture](docs/architecture.md)
- [Data Flow](docs/data_flow.md)
- [Module Design](docs/module_design.md)
- [Technology Stack](docs/technology_stack.md)
- [Testing Strategy](docs/testing_strategy.md)

## 12. Team Workflow and Git Guidelines

- Work on the assigned feature or workstream branch.
- Keep commits focused and use descriptive commit messages.
- Review changes before merging into the integration branch.
- Resolve notebook conflicts carefully and re-run affected notebooks.
- Keep `.venv`, secrets, and the raw dataset out of Git.
- Publish only approved, aggregated, non-identifying outputs.

Example Git workflow:

```bash
git checkout -b feature/your-workstream
git add notebooks/ docs/
git commit -m "Add workstream analysis"
git push -u origin feature/your-workstream
```

Open a pull request to the integration branch and have the changes reviewed before merging.

## 13. Repository

**GitHub:** [SaiSuryaHemanth2007/customer-escalation-risk-analysis](https://github.com/SaiSuryaHemanth2007/customer-escalation-risk-analysis)

---

**Team 10 — Luminary Logic**  
Dhanekula Institute of Engineering and Technology (DIET)  
DIET Hackathon | Customer Escalation Risk Analysis
