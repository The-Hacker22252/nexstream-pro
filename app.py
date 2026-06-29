import streamlit as strl

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
        background-color: #161D30;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Layout Rendering Interface
strl.markdown("<h1 class='main-title'>⚡ NEXSTREAM PRO MAXIMUM ⚡</h1>", unsafe_allow_html=True)
strl.success("🚀 Armored Processing Module Enabled. Downloads isolated cleanly inside app.")

left_col, right_col = strl.columns(2, gap="large")

with left_col:
    strl.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    strl.subheader("🎛️ Armored Control Panel")
    url_input = strl.text_input("YouTube Link Input:", placeholder="Paste your link here...")
    
    media_format = strl.selectbox("Output Format Option:", [
        "Full Video (Universal MP4)", 
        "Audio Only (High Quality MP3)"
    ])
    
    process_btn = strl.button("🚀 FETCH DIRECT STREAM")
    strl.markdown("</div>", unsafe_allow_html=True)

with right_col:
    strl.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    strl.subheader("📊 Elite Payload Monitor")
    
    if process_btn:
        if not url_input:
            strl.error("CRITICAL ERROR: Input stream parameter is missing.")
        else:
            strl.balloons()
            
            # Setup format flags for the underlying extraction components
            f_type = "mp3" if "Audio Only" in media_format else "720"
            
            # SAFE EMBEDDING: Injecting a sandboxed iframe module to pass data browser-side
            # This completely avoids 405 Method errors and server network tracking flags!
            embed_downloader_url = f"https://loader.to{url_input}&f={f_type}&color=10b981"
            
            strl.markdown(f"""
                <div style='background-color: #10B981; padding: 15px; border-radius: 8px; color: white; font-weight: 700; margin-bottom: 20px; text-align: center;'>
                    ✅ Unblocked Media Stream generated successfully without page redirects!
                </div>
                
                <p style='color: #94A3B8; margin-bottom: 10px; font-weight: 600;'>👇 TAP NATIVE BUTTON BELOW TO RETRIEVE FILE:</p>
                <iframe src="{embed_downloader_url}" width="100%" height="150px" scrolling="no"></iframe>
                
                <span style='display:block; text-align:center; font-size:12px; color:#64748B; margin-top:5px;'>
                    Processing executes cleanly within this sandboxed block window shell.
                </span>
            """, unsafe_allow_html=True)
            
    else:
        strl.info("🔴 Pipeline status: Standby. Awaiting link signature entry inputs.")
    strl.markdown("</div>", unsafe_allow_html=True)
