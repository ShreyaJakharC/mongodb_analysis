# AirBnB MongoDB Analysis

## Overview

Imported and explored real-world AirBnB listings data for Nashville using MongoDB. I ingested a 70,000+-row CSV into a `listings` collection, cleaned missing neighbourhood values, and leveraged MongoDB’s flexible schema to run a variety of find and aggregation queries.

## Features

- **Flexible Import:** Loaded compressed CSV into MongoDB with `mongoimport`
- **Data Scrubbing:** Programmatically removed records lacking key fields (e.g., blank neighbourhoods)
- **Query Showcase:** Demonstrated basic `.find()`, `.pretty()` output and exact‐limit retrieval
- **Filtered Views:** Retrieved superhost listings and high-bed-count properties sorted by rating
- **Aggregations:** Computed per-host listing counts and per-neighbourhood average ratings

## Tech & Tools

- **Database:** MongoDB (v4.x)
- **Import Utility:** `mongoimport` (CSV → BSON)
- **Scripting:** Bash for import commands, Python for pre‐import munging
- **Analysis:** Mongo shell queries and aggregation pipeline
- **Environment:** i6.cims.nyu.edu server, gzip for decompression

## Results & Key Takeaways

- **Large Dataset:** Successfully cleaned and loaded 70k+ listings into MongoDB
- **Superhost AirBnB:** Identified all listings by two superhosts with a single, concise query
- **Bed-Count Insights:** Found homes with >2 beds in Nashville, ordered by review scores
- **Host Activity:** Discovered top hosts by number of listings (e.g., host 101426897 with 185 listings)
- **Top Neighbourhoods:** Revealed neighbourhoods averaging 5.0 ratings (“Ashland City”, “NASHVILLE”, etc.)

## Skills Gained

MongoDB Import & Shell, Aggregation Pipelines, Schema-On-Read, Data Cleaning, and Insight Communication.

## Quick Start

1. **Clone & enter project**
   ```bash
   git clone https://github.com/yourusername/airbnb-mongodb-analysis.git
   cd airbnb-mongodb-analysis
   ```
