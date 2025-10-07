# Django Research Milestone (Individual)
A small Django web app that filters industrial network records and visualizes **Top Destination Ports** with a bar chart. Built as the individual research milestone using the team’s tech stack.

## Features

- Filter by **Source IP**, **Destination IP**, **Protocol**, and **Destination Port range**
- **Bar chart** of top destination ports (X = Destination Port, Y = Record Count) with axis labels
- **Paginated** results table (50 rows/page)
- Clean layout with clearly labeled inputs and a right-side **Filter** button


## Quickstart

```bash
# Python 3.11+ recommended
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt

# Initialize DB
python manage.py migrate
python manage.py loaddata network/fixtures/sample_records.json

# Run
python manage.py runserver
```

Open http://127.0.0.1:8000/ and try filters (IP contains, proto, port range).
The chart updates from the filtered queryset (first 5,000 rows).

