from crewai import Crew, Process
from tools import get_youtube_tool
from agents import blog_researcher, blog_writer
from tasks import create_research_task, create_write_task

def run_crew(channel_handle , topic):
    yt_tool = get_youtube_tool(channel_handle)

    research_task = create_research_task(yt_tool, blog_researcher)
    write_task = create_write_task(blog_writer)

    crew = Crew(
        agents=[blog_researcher, blog_writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
        memory=True,
        cache=True,
        max_rpm=100,
        share_crew=True,
    )

    result = crew.kickoff(inputs={'topic': topic})
    return result 

if __name__ == "__main__":
    run_crew()