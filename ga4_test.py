import os
from google.analytics.admin import AnalyticsAdminServiceClient

def list_account_summaries():
    # Set the GOOGLE_APPLICATION_CREDENTIALS if it's not automatically picked up, 
    # but the gcloud auth application-default login should set it implicitly or we can just rely on the default ADC path.
    client = AnalyticsAdminServiceClient()
    
    print("Fetching GA4 Accounts and Properties...")
    try:
        results = client.list_account_summaries()
        found = False
        for summary in results:
            found = True
            print(f"Account: {summary.account} | Name: {summary.display_name}")
            for property_summary in summary.property_summaries:
                print(f"  - Property ID: {property_summary.property}")
                print(f"  - Property Name: {property_summary.display_name}")
        
        if not found:
            print("No GA4 accounts found for this user.")
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    list_account_summaries()
