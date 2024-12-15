from crewai import Task
from agents import blog_researcher,blog_writer

def create_research_task(yt_tool, blog_researcher):
    return Task(
        description=(
            "Identify the video {topic}. "
            "Get detailed information about the video from the channel videos."
        ),
        expected_output="A comprehensive 3-paragraph-long report based on the {topic} of video content.",
        tools=[yt_tool],
        agent=blog_researcher,
    )

def create_write_task(blog_writer):
    return Task(
        description=(
            "Get the info from the YouTube channel on the topic {topic}."
        ),
        expected_output="Summarize the info from the YouTube channel video on the topic {topic} and create the content for the blog.",
        tools=[],
        agent=blog_writer,
        async_execution=False,
    )