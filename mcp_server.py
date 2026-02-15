from mcp.server.fastmcp import FastMCP
from src.job_api import fetch_linkedin_jobs, fetch_naukri_jobs  
#MCP server will expose job scraping as tools to AI.
#initializing the FastMCP server
#This server will tell AI:
#“I have tools to fetch jobs.”
mcp =FastMCP("Job Recommender ")

#This decorator registers a function as an MCP tool.
@mcp.tool()
async def fetchlinkedin(listofkey):
    return fetch_linkedin_jobs(listofkey)

@mcp.tool()
async def fetchnaukri(listofkey):
    return fetch_naukri_jobs(listofkey) 

if __name__ == "__main__":
    mcp.run(transport='stdio')#means communication happens via standard input/output
    
    
    
    
    
    
#AI calls MCP → MCP calls your function → returns job list.
#