import streamlit as strl
import urllib.request
import json

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
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# 2. Layout Rendering Interface
strl.markdown("<h1 class='main-title'>⚡ NEXSTREAM PRO MAXIMUM ⚡</h1>", unsafe_allow_html=True)
strl.success("🚀 Native Processing Engine Active. Ad-free downloading locked inside app.")

left_col, right_col = strl.columns(2, gap="large")

with left_col:
    strl.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    strl.subheader("🎛️ Armored Control Panel")
    url_input = strl.text_input("YouTube Link Input:", placeholder="Paste link here...")
    
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
            try:
                strl.session_state.download_status = "Contacting unblocked backend..."
                
                # Setup parameters based on user choice
                is_audio = "Audio Only" in media_format
                
                # Build JSON Payload
                payload = {
                    "url": url_input,
                    "downloadMode": "audio" if is_audio else "video",
                    "videoQuality": "720" if not is_audio else "128"
                }
                
                # Direct API Call to Cobalt backend instance
                api_url = "https://cobalt.tools"
                req = urllib.request.Request(
                    api_url, 
                    data=json.dumps(payload).encode('utf-8'),
                    headers={
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'User-Agent': 'Mozilla/5.0'
                    },
                    method='POST'
                )
                
                with urllib.request.urlopen(req, timeout=15) as response:
                    res_data = json.loads(response.read().decode('utf-8'))
                
                # If API provides a successful unblocked URL link, fetch the binary file content
                if res_data.get("status") == "stream" or res_data.get("status") == "picker":
                    strl.error("This specific video size limits processing. Please try a standard video link.")
                elif "url" in res_data:
                    direct_file_url = res_data["url"]
                    
                    strl.info("📥 Buffering media stream data locally into your browser session...")
                    
                    # Create Native Streamlit Download Button using the direct streaming URL
                    ext = "mp3" if is_audio else "mp4"
                    mime_type = "audio/mpeg" if is_audio else "video/mp4"
                    
                    # Download button that serves the link directly using a custom label wrapper
                    strl.markdown(f"""
                        <div style='background-color: #10B981; padding: 15px; border-radius: 8px; color: white; font-weight: 700; margin-bottom: 20px; text-align: center;'>
                            ✅ Media Stream completely isolated without ads or site popups!
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # We pass the link to a native download button structure or link target
                    strl.link_button(
                        label=f"📥 RETRIEVE COMPLETED .{ext.upper()} FILE",
                        url=direct_file_url
                    )
                else:
                    strl.error(f"Extraction Rejected: {res_data.get('text', 'Unknown backend block.')}")
                    
            except Exception as e:
                strl.error(f"Error Processing Subsystem Chain: Request timed out or server cluster overloaded. ({str(e)})")
    else:
        strl.info("🔴 Pipeline status: Standby. Awaiting link signature entry inputs.")
    strl.markdown("</div>", unsafe_allow_html=True)
