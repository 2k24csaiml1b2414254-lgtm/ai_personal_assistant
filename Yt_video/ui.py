import re
import streamlit as st
from youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title="YouTube Video Analyzer",
    page_icon="🎥",
    layout="wide"
)

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

        html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

        .block-container { padding: 2rem 4rem; max-width: 1100px; }

        .hero {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            border-radius: 16px;
            padding: 2.5rem 3rem;
            margin-bottom: 2rem;
            color: white;
        }
        .hero h1 { font-size: 2.2rem; font-weight: 700; margin: 0 0 0.4rem 0; }
        .hero p  { font-size: 1rem; opacity: 0.75; margin: 0; }

        .stTextInput > div > div > input {
            border-radius: 10px;
            font-size: 1rem;
            padding: 0.65rem 1rem;
            border: 2px solid #e0e0e0;
        }
        .stTextInput > div > div > input:focus {
            border-color: #FF0000 !important;
            box-shadow: 0 0 0 2px rgba(255,0,0,0.15);
        }

        .stButton > button {
            border-radius: 10px;
            padding: 0.6rem 2rem;
            font-size: 1rem;
            font-weight: 600;
            background: linear-gradient(135deg, #FF0000, #cc0000);
            color: white;
            border: none;
            width: 100%;
            transition: opacity 0.2s;
        }
        .stButton > button:hover { opacity: 0.88; color: white; }

        .video-card {
            background: #f8f9fa;
            border-radius: 12px;
            padding: 1rem 1.2rem;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            border: 1px solid #eee;
        }
        .video-card img { border-radius: 8px; width: 160px; }
        .video-card .url { font-size: 0.85rem; color: #555; word-break: break-all; }

        .result-card {
            background: #ffffff;
            border-radius: 14px;
            padding: 2rem;
            border: 1px solid #f0f0f0;
            box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        }
        .section-label {
            font-size: 0.75rem;
            font-weight: 600;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: #FF0000;
            margin-bottom: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)


def extract_video_id(url: str):
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", url)
    return match.group(1) if match else None


@st.cache_resource
def get_agent():
    return build_youtube_agent()


agent = get_agent()

# Hero banner
st.markdown("""
    <div class="hero">
        <h1>🎥 YouTube Video Analyzer</h1>
        <p>Paste any YouTube URL and get AI-powered timestamps, topic breakdowns, and key insights.</p>
    </div>
""", unsafe_allow_html=True)

# Input row
col_input, col_btn = st.columns([5, 1.2])
with col_input:
    video_url = st.text_input(
        label="url",
        placeholder="https://www.youtube.com/watch?v=...",
        label_visibility="collapsed"
    )
with col_btn:
    st.markdown("<div style='padding-top:0.35rem'>", unsafe_allow_html=True)
    button = st.button("🔍 Analyze")
    st.markdown("</div>", unsafe_allow_html=True)

# Video preview card
if video_url:
    vid_id = extract_video_id(video_url)
    if vid_id:
        thumb = f"https://img.youtube.com/vi/{vid_id}/mqdefault.jpg"
        st.markdown(f"""
            <div class="video-card">
                <img src="{thumb}" alt="thumbnail"/>
                <div class="url">🔗 {video_url}</div>
            </div>
        """, unsafe_allow_html=True)

# Analyze
if button and video_url:
    with st.spinner("Analyzing video, this may take a moment..."):
        response = agent.run(f"Analyze this video: {video_url}")

    st.markdown('<div class="section-label">📋 Analysis Report</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="result-card">', unsafe_allow_html=True)
    st.markdown(response.content)
    st.markdown('</div>', unsafe_allow_html=True)

elif button and not video_url:
    st.warning("Please enter a YouTube URL first.")
