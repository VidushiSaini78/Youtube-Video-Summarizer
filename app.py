import streamlit as st
from crew import run_crew  

def main():
    st.title("🎥 YouTube Video Summarizer: Simplify Insights Instantly 📝")
    st.write(
        """
        Unlock the essence of YouTube content with ease! This tool allows users to input a YouTube channel and a specific video, 
        delivering a concise, well-structured summary of the video in seconds. Perfect for students, professionals, and curious learners, 
        it transforms long video content into digestible insights. Stay informed, save time, and grasp the key takeaways without watching 
        the entire video! 💡📚
        """
    )
    channel = st.text_input("Enter YouTube Channel Handle (e.g., @abc):", placeholder="Type channel handle... 📺")
    video = st.text_input("Enter YouTube Video Title:", placeholder="Type video title... 🎬")
    if st.button("🚀 Submit"):
        if channel and video:
            result = run_crew(channel, video)
            st.success(f"🎉 Summary: {result}")
        else:
            st.warning("⚠️ Please fill in both inputs before submitting.")

if __name__ == "__main__":
    main()
