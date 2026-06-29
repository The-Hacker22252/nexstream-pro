import streamlit as strl
import re

# 1. Main Page and UI Design Setup
strl.set_page_config(page_title="NexStream Pro | Infinite Native", page_icon="⚡", layout="wide")

strl.markdown("""
    <style>
    .main { background-color: #0B0F19; color: #E2E8F0; }
    .main-title {
        font-size: 3.5rem !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, #00F2FE 0%, #4FACFE 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 5px;
        text-shadow: 0px 4px 20px rgba(79, 172, 254, 0.4);
    }
    .dashboard-card {
        background-color: #161D30;
        border: 1px solid #24324F;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
    }
    .stButton>button {
        width: 100% !important;
        background: linear-gradient(90deg, #10B981 0%, #059669 100%) !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 16px 20px !important;
        font-size: 18px !important;
        font-weight: 800 !important;
        letter-spacing: 1px;
    }
    iframe {
        border: none !important;
        border-radius: 12px;
        background-color: #0B0F19;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Hardened URL Parser Engine
def extract_video_id(url):
    regex_pattern = r'(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^"&?\/\s]{11})'
    match = re.search(regex_pattern, url)
    return match.group(1) if match else None

# 3. Layout Rendering Interface
strl.markdown("<h1 class='main-title'>⚡ NEXSTREAM PRO ULTRA INFINITE ⚡</h1>", unsafe_allow_html=True)
strl.success("🚀 Armored Client-Side Processing active. Server-level 403 blocks bypassed.")

left_col, right_col = strl.columns(2, gap="large")

with left_col:
    strl.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    strl.subheader("🎛 Inland Control Unit")
    url_input = strl.text_input("YouTube Link Input:", placeholder="Paste your link target here...")
    
    media_format = strl.selectbox("Output Stream Format Profile:", [
        "Full High-Definition Video (MP4)", 
        "High Quality Audio Track (MP3)"
    ])
    
    process_btn = strl.button("🚀 INITIALIZE MATRIX DOWNLOAD")
    strl.markdown("</div>", unsafe_allow_html=True)

with right_col:
    strl.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    strl.subheader("📊 Live Processing Monitor")
    
    if process_btn:
        if not url_input:
            strl.error("CRITICAL CONFIGURATION FAULT: Input link signature is missing.")
        else:
            video_id = extract_video_id(url_input)
            if not video_id:
                strl.error("PARSING ERROR: Unable to locate the 11-character token string.")
            else:
                strl.balloons()
                
                # Check user format requirements
                is_audio = "Audio" in media_format
                
                # Bypassing the server block by using unblocked download buttons rendered right inside an isolated frame block
                # This routes the data request directly through the user's browser residential IP instead of the datacenter!
                f_param = "mp3" if is_audio else "1080"
                embed_downloader_url = f"https://loader.to{video_id}&f={f_param}&color=10b981"
                
                strl.markdown(f"""
                    <div style='background-color: #10B981; padding: 15px; border-radius: 8px; color: white; font-weight: 700; margin-bottom: 20px; text-align: center;'>
                        ✅ Unblocked download tunnel generated via your clean client connection!
                    </div>
                    
                    <p style='color: #94A3B8; margin-bottom: 10px; font-weight: 600;'>👇 CLICK INTERNAL EXTRACTOR BUTTON TO RETRIEVE FILE:</p>
                    <iframe src="{embed_downloader_url}" width="100%" height="150px" scrolling="no"></iframe>
                    
                    <span style='display:block; text-align:center; font-size:12px; color:#64748B; margin-top:5px;'>
                        Data isolation block running safely within this browser tab shell box.
                    </span>
                """, unsafe_allow_html=True)
            
    else:
        strl.markdown("<p style='color: #64748B; text-align: center; padding: 40px 0;'>🔴 Standby Status: Active. Awaiting stream layout initialization.</p>", unsafe_allow_html=True)
    strl.markdown("</div>", unsafe_allow_html=True)
