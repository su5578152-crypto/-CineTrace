import os
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)

def run_sample_report(property_id="properties/536961974"):
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=property_id,
        dimensions=[Dimension(name="date")],
        metrics=[
            Metric(name="activeUsers"),
            Metric(name="sessions"),
            Metric(name="screenPageViews"),
            Metric(name="eventCount")
        ],
        date_ranges=[DateRange(start_date="7daysAgo", end_date="today")],
    )
    
    print(f"Fetching data for {property_id}...")
    try:
        response = client.run_report(request)
        
        print("Report Results (Last 7 Days):")
        print("-" * 50)
        print("Date | Active Users | Sessions | Page Views | Event Count")
        print("-" * 50)
        
        total_users = 0
        total_sessions = 0
        total_page_views = 0
        total_events = 0

        for row in response.rows:
            date = row.dimension_values[0].value
            users = int(row.metric_values[0].value)
            sessions = int(row.metric_values[1].value)
            page_views = int(row.metric_values[2].value)
            events = int(row.metric_values[3].value)
            
            total_users += users
            total_sessions += sessions
            total_page_views += page_views
            total_events += events
            
            print(f"{date} | {users} | {sessions} | {page_views} | {events}")
            
        print("-" * 50)
        print(f"TOTAL: Users: {total_users}, Sessions: {total_sessions}, Page Views: {total_page_views}, Events: {total_events}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_sample_report()
