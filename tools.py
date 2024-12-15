from crewai_tools import YoutubeChannelSearchTool

def get_youtube_tool(channel_handle):
    return YoutubeChannelSearchTool(youtube_channel_handle=channel_handle)