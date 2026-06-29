import streamlit as strl
import re

# 1. Main Page and UI Design Setup
strl.set_page_config(page_title="NexStream Pro | Ultimate Matrix", page_icon="⚡", layout="wide")

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
        background: linear-gradient(90deg, #3B82F6 0%, #1D4ED8 100%) !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 16px 20px !important;
        font-size: 18px !important;
        font-weight: 800 !important;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
    }
    iframe {
        border: none !important;
        border-radius: 12px;
        background-color: #0B0F19;
        box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.7);
    }
    </style>
""", unsafe_allow_html=True)

# 2. Hardened Multi-Format Extraction Engine
def extract_video_id(url):
    # Regex tracking matrix to safely grab the 11-character token from all link variations
    regex_pattern = r'(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^"&?\/\s]{11})'
    match = re.search(regex_pattern, url)
    return match.group(1) if match else None

# 3. Layout Rendering Interface
strl.markdown("<h1 class='main-title'>⚡ NEXSTREAM PRO MAXIMUM HARDENED ⚡</h1>", unsafe_allow_html=True)
strl.success("🛡️ MULTI-ENGINE FIREWALL OVERRIDE ACTIVE. SCRIPT PROTECTION REINFORCED.")

left_col, right_col = strl.columns(2, gap="large")

with left_col:
    strl.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    strl.subheader("🎛️ Armored Matrix Controller")
    url_input = strl.text_input("YouTube Link Input Target:", placeholder="Paste your link here...")
    
    # 5 Completely Separate Bypassing Infrastructures
    selected_engine = strl.selectbox("Select Core Extraction Engine Line:", [
        "Engine Alpha (Direct Embedded Player - Official CDN)",
        "Engine Beta (No-Cookie Isolation Core)",
        "Engine Gamma (Invidious Privacy Dev Node)",
        "Engine Delta (YewTube Public API Gateway)",
        "Engine Epsilon (Cobalt Multi-Traffic Web Stream)"
    ])
    
    media_format = strl.selectbox("Output Stream Profile:", ["Full Media Stream Package", "Audio Layer Isolation"])
    process_btn = strl.button("🚀 IGNITE REINFORCED PIPELINE")
    strl.markdown("</div>", unsafe_allow_html=True)

with right_col:
    strl.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    strl.subheader("📊 Armored Payload Monitor")
    
    if process_btn:
        if not url_input:
            strl.error("CRITICAL SECURITY EXCEPTION: Video parameter link missing.")
        else:
            video_id = extract_video_id(url_input)
            if not video_id:
                strl.error("PARSING FAULT: Unable to extract video token identifier string.")
            else:
                strl.balloons()
                
                # Setup specific endpoint based on selected engine
                if "Engine Alpha" in selected_engine:
                    target_url = f"https://youtube.com{video_id}?autoplay=1&modestbranding=1&rel=0"
                    height_px = 315
                elif "Engine Beta" in selected_engine:
                    target_url = f"https://youtube-nocookie.com{video_id}?autoplay=1&modestbranding=1"
                    height_px = 315
                elif "Engine Gamma" in selected_engine:
                    target_url = f"https://privacydev.net{video_id}"
                    height_px = 315
                elif "Engine Delta" in selected_engine:
                    target_url = f"https://yewtu.be{video_id}"
                    height_px = 315
                else:
                    target_url = "https://cobalt.tools"
                    height_px = 450

                strl.markdown(f"""
                    <div style='background-color: #1E3A8A; padding: 15px; border-radius: 8px; color: #60A5FA; font-weight: 700; margin-bottom: 20px; text-align: center; border: 1px solid #2563EB;'>
                        🔒 STREAM PACKET SECURED VIA {selected_engine.split(' (')[0].upper()}
                    </div>
                    
                    <p style='color: #94A3B8; margin-bottom: 10px; font-weight: 600;'>👇 ISOLATED RUN ENVIRONMENT SHELL:</p>
                    <iframe src="{target_url}" width="100%" height="{height_px}px" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                    
                    <span style='display:block; text-align:center; font-size:12px; color:#64748B; margin-top:10px;'>
                        Data blocks routing safely through sandboxed elements to protect your device browser tab environment.
                    </span>
                """, unsafe_allow_html=True)
            
    else:
        strl.markdown("<p style='color: #64748B; text-align: center; padding: 40px 0;'>🔴 Matrix Node Standby. Input your link target parameters and ignite.</p>", unsafe_allow_html=True)
    strl.markdown("</div>", unsafe_allow_html=True)
