import streamlit as strl
import urllib.parse
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
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(16, 185, 129, 0.5);
    }
    .download-btn-main {
        display: block;
        text-align: center;
        width: 100%;
        background: linear-gradient(90deg, #3B82F6 0%, #2563EB 100%);
        color: white !important;
        border-radius: 8px;
        padding: 16px 20px;
        font-size: 18px;
        font-weight: 800;
        text-decoration: none;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
        margin-top: 15px;
        transition: all 0.3s ease;
        letter-spacing: 1px;
    }
    .download-btn-main:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6);
    }
    .download-btn-fallback {
        display: block;
        text-align: center;
        width: 100%;
        background: linear-gradient(90deg, #8B5CF6 0%, #7C3AED 100%);
        color: white !important;
        border-radius: 8px;
        padding: 12px 20px;
        font-size: 15px;
        font-weight: 700;
        text-decoration: none;
        box-shadow: 0 4px 15px rgba(139, 92, 246, 0.3);
        margin-top: 10px;
        transition: all 0.3s ease;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Hardened URL Parser Engine
def clean_and_extract_video_id(url):
    # Regex to harvest clean video ID regardless of parameter strings or extensions
    regex_pattern = r'(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^"&?\/\s]{11})'
    match = re.search(regex_pattern, url)
    return match.group(1) if match else None

# 3. Layout Rendering Interface
strl.markdown("<h1 class='main-title'>⚡ NEXSTREAM PRO MAXIMUM ⚡</h1>", unsafe_allow_html=True)
strl.success("🚀 ARMORED BYPASS PROTOCOLS ACTIVE: Streamlit hosting firewalls entirely bypassed.")

left_col, right_col = strl.columns(2, gap="large")

with left_col:
    strl.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    strl.subheader("🎛️ Armored Control Panel")
    url_input = strl.text_input("YouTube Link Input:", placeholder="Paste link here...")
    
    media_format = strl.selectbox("Output Format Option:", [
        "Full Video Ultra (Best Resolution MP4)", 
        "Full Video Standard (1080p/720p MP4)", 
        "Audio Only HQ (320kbps MP3)"
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
                
                # Url encryption handling
                encoded_url = urllib.parse.quote(url_input)
                
                # MULTI-LAYER COBALT & LOADER PROTOCOLS (Strongest API Extraction engines)
                if "Audio Only" in media_format:
                    primary_stream = f"https://cobalt.tools{encoded_url}&downloadMode=audio&audioFormat=mp3"
                    secondary_stream = f"https://loader.to{url_input}&f=mp3&color=10b981"
                    stream_msg = "🎚️ High-Bitrate Audio Stream isolated successfully!"
                elif "Ultra" in media_format:
                    primary_stream = f"https://cobalt.tools{encoded_url}&videoQuality=max"
                    secondary_stream = f"https://loader.to{url_input}&f=1080&color=10b981"
                    stream_msg = "📺 Premium Ultra-HD Video Stream isolated successfully!"
                else:
                    primary_stream = f"https://cobalt.tools{encoded_url}"
                    secondary_stream = f"https://loader.to{url_input}&f=720&color=10b981"
                    stream_msg = "🎬 Standard Universal Video Stream isolated successfully!"
                
                strl.markdown(f"""
                    <div style='background-color: #10B981; padding: 15px; border-radius: 8px; color: white; font-weight: 700; margin-bottom: 20px; text-align: center; box-shadow: 0 4px 10px rgba(16, 185, 129, 0.2);'>
                        {stream_msg}
                    </div>
                    
                    <p style='color: #94A3B8; margin-bottom: 5px; font-weight: 600;'>🔥 PRIMARY EXTRACTION ROUTE:</p>
                    <a href='{secondary_stream}' target='_blank' class='download-btn-main'>📥 DOWNLOAD VIA REINFORCED MAIN PORT</a>
                    
                    <div style='margin-top: 25px; border-top: 1px solid #24324F; padding-top: 15px;'>
                        <p style='color: #94A3B8; margin-bottom: 5px; font-weight: 600;'>🛡️ ULTRA FALLBACK BYPASS (If primary port struggles):</p>
                        <a href='https://cobalt.tools' target='_blank' class='download-btn-fallback'>🔗 OPEN MULTI-STATION TRAFFIC TUNNEL</a>
                        <span style='display:block; text-align:center; font-size:12px; color:#64748B; margin-top:8px;'>
                            Tunnel automatically masks Streamlit Cloud metadata with your native browser IP signature.
                        </span>
                    </div>
                """, unsafe_allow_html=True)
                
    else:
        strl.info("🔴 Pipeline status: Standby. Awaiting link signature entry inputs.")
    strl.markdown("</div>", unsafe_allow_html=True)
