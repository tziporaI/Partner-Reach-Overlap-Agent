# Partner Reach Overlap Agent

This repository contains a basic implementation of a media analytics agent using the **Google ADK (Agent Development Kit) framework** for web-based deployment.

Its purpose is to help evaluate the performance of media sources based on reach, overlap, and engagement data retrieved from BigQuery.

---

## 📌 Purpose

This agent is designed to assist marketers and analysts in answering key media planning questions:

- **Which media sources provide the most incremental reach?**
- **Where does user overlap occur between partners?**
- **Which sources show the highest engagement quality?**

---

## 📊 Key Metrics Calculated

- **total_users** – Number of unique users reached by impressions or clicks  
- **unique_users** – Users reached by only one media source  
- **overlap_rate** – Percentage of users also reached by other sources  
- **engagement_rate** – Ratio of engaged users to viewers  
- **incrementality_score** – unique_users / total_users  
- **engagement_subtype_distribution** – Distribution of interaction types per media source

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Shani-396/Partner-Reach-Overlap-Agent.git
cd Partner-Reach-Overlap-Agent
```

### 2. Configure Credentials

- Sensitive files such as `.env` and `*.json` Google credentials are **not** included in this repository.
- You must provide your own Google Cloud and BigQuery credentials in your environment.

### 3. Run the Agent (example command)

```bash
adk web http://127.0.0.1:8001/
```

---

## 🧑‍💻 Technologies

- **Google ADK (Agent Development Kit) Web** – Agent orchestration and interface  
- **BigQuery** – Data storage and analytics  
- *(Planned:)* **A2A**, **MCP**, **GCS** integrations
- **send to slack toools:**by MCP ,send to slack photos

---

## 🚧 Status

This is a **basic starting point**.  
It is functional and provides foundational analytics, with potential for future extensions such as:

- Visualizations and dashboards
- Campaign-level breakdowns
- Geographic segmentation
- Additional filters and richer UX

---

## 🔐 Security# Partner Reach Overlap Agent

This agent provides Appsflyer services, focused on analyzing advertising data from multiple media sources and identifying those offering the best value for investment. Support A2A.

---

## Overview

The agent receives parameters (for example, via API or CLI) and analyzes data per media source, identifying the best ones to invest in based on metrics such as:
- Unique users
- Overlap rate
- Incrementality score

The processed data is then sent to Slack.

---

## Example Prompt

```
Please analyze the data per media source and return which ones provide the best value for investment, based on metrics like unique users, overlap rate, and incrementality score. Format and send the data to Slack

Parameters:

- app_id: ad_1  
- date_range: 2025-06-26 to 2025-06-30  
- campaign_name: adnet_adrevenue_raw_all_on  
- media_sources:
    1. advprivacy_int  
    2. reengage_int  
    3. adrevenueqa_int
```

---

## Setup & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shani-396/Partner-Reach-Overlap-Agent.git
   cd Partner-Reach-Overlap-Agent
   ```

2. **Install dependencies:**
   - Make sure you have Python 3.8+ installed.
   - Install required packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set environment variables:**
   - Configure the following environment variables in a `.env` file or your shell:
     - `SLACK_BOT_TOKEN`: Your Slack bot token.
     - `CHANNEL_NAME`: Slack channel name for posting results.
     - `CHANNEL_ID`: Slack channel ID for posting files (visualizations).
     - `GOOGLE_APPLICATION_CREDENTIALS`: Path to your Google Cloud credentials JSON.
     - `GOOGLE_CLOUD_PROJECT`: Your Google Cloud project ID.
     - `DATASET_ID`: BigQuery dataset ID.
     - `TABLE_ID`: BigQuery table ID.
     - `BUCKET_NAME`: Google Cloud Storage bucket for visualizations.

     Example:
     ```bash
     export SLACK_BOT_TOKEN=your-slack-token
     export CHANNEL_NAME=your-channel
     export CHANNEL_ID=your-channel-id
     export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json
     export GOOGLE_CLOUD_PROJECT=your-gcp-project
     export DATASET_ID=your_bigquery_dataset
     export TABLE_ID=your_bigquery_table
     export BUCKET_NAME=your-gcs-bucket
     ```

4. **Run the agent:**
   - You can run the agent manually or as a background process.
   - Example command:
     ```bash
     python main.py --app_id ad_1 --date_range "2025-06-26:2025-06-30" --campaign_name adnet_adrevenue_raw_all_on --media_sources advprivacy_int reengage_int adrevenueqa_int
     ```

---

## Tools Structure

- **Formatting & Slack Agent:** (`tools/slack_tools.py`)
  - Sends formatted results (text or JSON) to Slack.
  - Uploads visualizations from GCS to Slack.

- **Visualization Agent:** (`tools/visual_tools.py`)
  - Generates overlap heatmaps between media sources and uploads them to GCS.

- **BigQuery:** (`tools/big_qwery_tools.py`)
  - Queries user, campaign, and overlap data directly from BigQuery.

---

## Notes

- **A2A support:** protocol to communicate with agents .
- **Contributions:** Pull requests and feedback are welcome!

---

## Resources

- [Appsflyer](https://www.appsflyer.com/)
- [Slack API](https://api.slack.com/)
- [Google Cloud Storage](https://cloud.google.com/storage)
- [Google BigQuery](https://cloud.google.com/bigquery)

---

Sensitive files such as `.env` and `*.json` credentials are **not committed** to this repository and should be manually configured in your environment.

---

## ✅ Contributing

Feel free to fork, customize, and contribute improvements!

---

[Shani-396 on GitHub](https://github.com/Shani-396)
