
from apify_client import ApifyClient #ApifyClient is a Python client for the Apify API, which allows you to interact with Apify's web scraping and automation services.
import os
from dotenv import load_dotenv
load_dotenv()

apify_client=ApifyClient(os.getenv("APIFY_API_KEY")) #apify_client is an instance of the ApifyClient class, which is used to interact with the Apify API. The api_key parameter is set to the value of OPENROUTER_API_KEY, which is retrieved from the environment variables using os.getenv().
#creating two functions for naukri.com and linkedin.com based on search_query
def fetch_linkedin_jobs(search_query,location="india",rows=60):
    run_input={
        "title":search_query,
        "location":location,
        "rows":rows,
        #proxy settings to use Apify's residential proxy for web scraping, which helps to avoid IP blocking and ensures more reliable data extraction from websites like LinkedIn.
        "proxy":{
            "useApifyProxy":True,
            "apifyProxyGroups":["RESIDENTIAL"],
        }
      }
    run=apify_client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)
    jobs=list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs
    

def fetch_naukri_jobs(search_query,location="india",rows=60):
    #got this code form https://apify.com/apify/naukri-jobs-scraper#input-schema and modified it according my needs
    run_input={
        "keywords":search_query,
        "maxJobs":60,
        "freshness":"all",
        "sortBy":"relevance",
        "experienceLevel":"all",
        "location":location,
      }
    run=apify_client.actor("wsrn5gy5C4EDeYCcD").call(run_input=run_input)
    jobs=list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs