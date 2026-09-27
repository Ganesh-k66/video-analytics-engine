# video-analytics-engine

# Video Analytics Engine

A Python data analytics pipeline built with **Pandas** to process video performance datasets, compute viewer drop-off metrics, and evaluate engagement scores across content categories.

## Key Features
* **Drop-off Rate Calculation:** Analyzes retention loss between 5-minute marks and video completion, automatically triggering high drop-off alerts.
* **Engagement Scoring:** Calculates custom engagement ratings factoring in likes, weighted comments, total view count, and final retention.
* **Category Aggregation:** Evaluates summary statistics (sum, count, min, max) grouped by video categories using Pandas `groupby`.

## Tech Stack
* **Language:** Python
* **Library:** Pandas

## Usage
Ensure your input dataset `Video_ID_VID_50.csv` is in the same directory and run:
```bash
python main.py
