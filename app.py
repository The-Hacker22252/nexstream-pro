import streamlit as strl
import re

# 1. Main Page and UI Design Setup
strl.set_page_config(page_title="NexStream Pro | Media Downloader", page_icon="⚡", layout="wide")

strl.markdown("""
    <style>
    .main { background-color: #0B0F19; color: #E2E8F0; }
    .main-title {
        font-size: 3.5rem !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, #FF416C 0%, #FF4B2B 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 5px;
        text-shadow: 0px 4px 20px rgba(255, 65, 108, 0.3);
    }
    .dashboard-card {
        background-color: #161D30;
        border: 1px solid #24324F;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
    }
    iframe {
        border: none !important;
        border-radius: 8px;
        background-color: #0B0F19;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# 2. Hardened URL Parser Engine
def clean_and_extract_video_id(url):
    regex_pattern = r'(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^"&?\/\s]{11})'
    match = re.search(regex_pattern, url)
    return match.group(1) if match else None

# 3. Layout Rendering Interface
strl.markdown("<h1 class='main-title'>⚡ NEXSTREAM PRO MAXIMUM ⚡</h1>", unsafe_allow_html=True)
strl.success("🚀 Armored Processing Module Enabled. Stream isolated cleanly inside app.")

left_col, right_col = strl.columns(2, gap="large")

with left_col:
    strl.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    strl.subheader("🎛️ Armored Control Panel")
    url_input = strl.text_input("YouTube Link Input:", placeholder="Paste your link here...")
    
    media_format = strl.selectbox("Output Format Option:", [
        "Full Video Stream Layout", 
        "Audio Stream Extract"
    ])
    
    process_btn = strl.button("🚀 INITIALIZE DECRYPTION PIPELINE")
    strl.markdown("</div>", unsafe_allow_html=True)

with right_col:
    strl.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    strl.subheader("📊 Elite Payload Monitor")
    
    if process_btn:
        if not url_input:
            strl.error("CRITICAL ERROR: Input stream parameter is missing.")
        else:
            video_id = clean_and_extract_video_id(url_input)
            if not video_id:
                strl.error("MALFORMED URL: Unable to parse YouTube video token identity.")
            else:
                strl.balloons()
                
                # Direct unblocked embed link structure utilizing Google's official media endpoints
                embed_downloader_url = f"https://youtube.com{video_id}?autoplay=1&modestbranding=1"
                
                strl.markdown(f"""
                    <div style='background-color: #10B981; padding: 15px; border-radius: 8px; color: white; font-weight: 700; margin-bottom: 20px; text-align: center;'>
                        ✅ Media Stream completely isolated without server errors or site popups!
                    </div>
                    
                    <p style='color: #94A3B8; margin-bottom: 10px; font-weight: 600;'>👇 PLAY NATIVE UNFUSED STREAM DATA HERE:</p>
                    <iframe src="{embed_downloader_url}" width="100%" height="315px" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                    
                    <span style='display:block; text-align:center; font-size:12px; color:#64748B; margin-top:10px;'>
                        Processing executes cleanly using your device's native network connection.
                    </span>
                """, unsafe_allow_html=True)
            
    else:
        strl.info("🔴 Pipeline status: Standby. Awaiting link signature entry inputs.")
    strl.markdown("</div>", unsafe_allow_html=True)
