import os
import glob
import time
import shutil
import urllib.request
import json
import streamlit as strl

# 1. Main Page and UI Design Setup
strl.set_page_config(page_title="NexStream Pro | Media Downloader", page_icon="⚡", layout="wide")

# Check if FFmpeg is installed on this system
FFMPEG_AVAILABLE = shutil.which("ffmpeg") is not None

strl.markdown("""
    <style>
    .main { background-color: #0B0F19; color: #E2E8F0; }
    .main-title {
        font-size: 3rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #FF416C 0%, #FF4B2B 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 5px;
    }
    .dashboard-card {
        background-color: #161D30;
        border: 1px solid #24324F;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    .stButton>button {
        width: 100% !important;
        background: linear-gradient(90deg, #10B981 0%, #059669 100%) !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 14px 20px !important;
        font-size: 16px !important;
        font-weight: 700 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Tracking System Session Variables
if 'download_progress' not in strl.session_state:
    strl.session_state.download_progress = 0.0
if 'download_speed' not in strl.session_state:
    strl.session_state.download_speed = "0 MB/s"
if 'download_status' not in strl.session_state:
    strl.session_state.download_status = "Idle"

def clean_old_files():
    for f in glob.glob("downloaded_media.*"):
        try: os.remove(f)
        except: pass

def extract_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return None

# 3. Layout Rendering Interface
strl.markdown("<h1 class='main-title'>NEXSTREAM PRO</h1>", unsafe_allow_html=True)

if FFMPEG_AVAILABLE:
    strl.success("🚀 FFmpeg system engine detected! HD and MP3 conversions unlocked.")
else:
    strl.warning("⚠️ FFmpeg not found on computer. Running in Compatibility Mode (720p Video Max, Audio conversion disabled).")

left_col, right_col = strl.columns(2, gap="large")

with left_col:
    strl.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    strl.subheader("🎛️ Control Panel")
    url_input = strl.text_input("YouTube Link Input:", placeholder="https://youtube.com...")
    
    format_options = ["Full Video (MP4)"]
    media_format = strl.selectbox("Output Format:", format_options)
    quality = strl.selectbox("Quality Profile:", ["Direct Format (Proxy Bypass)"])
        
    process_btn = strl.button("🚀 EXECUTE DOWNLOADING")
    strl.markdown("</div>", unsafe_allow_html=True)

with right_col:
    strl.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    strl.subheader("📊 Live Display Monitor")
    m_col1, m_col2 = strl.columns(2)
    with m_col1:
        strl.metric(label="System Status", value=strl.session_state.download_status)
    with m_col2:
        strl.metric(label="Bandwidth Speed", value=strl.session_state.download_speed)
    p_bar = strl.progress(strl.session_state.download_progress)
    strl.markdown("</div>", unsafe_allow_html=True)

# 4. Engine Run Pipeline Logic (Placed securely below element creation flags)
if process_btn:
    if not url_input:
        strl.error("Configuration Execution Blocked: Link String Missing.")
    else:
        video_id = extract_video_id(url_input)
        if not video_id:
            strl.error("Invalid YouTube URL provided.")
        else:
            try:
                strl.session_state.download_status = "Bypassing YouTube Firewalls..."
                strl.session_state.download_progress = 0.2
                clean_old_files()
                
                # Resolving 403 limits by routing around datacenter IP blocks via a public API instance
                proxy_api_url = f"https://nerdvpn.de{video_id}"
                
                req = urllib.request.Request(proxy_api_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req) as response:
                    meta = json.loads(response.read().decode())
                
                with right_col:
                    strl.markdown(f"""
                        <div class='dashboard-card' style='border-color: #3B82F6;'>
                            <b>Title:</b> {meta.get('title', 'Unknown')}<br>
                            <b>Creator:</b> {meta.get('author', 'Unknown')}<br>
                            <b>Length:</b> {time.strftime('%H:%M:%S', time.gmtime(meta.get('lengthSeconds', 0)))}
                        </div>
                    """, unsafe_allow_html=True)
                
                video_streams = meta.get('formatStreams', [])
                if not video_streams:
                    video_streams = meta.get('adaptiveStreams', [])
                    
                if not video_streams:
                    raise Exception("No active data streams found via proxy endpoints.")
                    
                # Grabbing the first clean video block structure 
                direct_download_url = video_streams[0]['url']
                output_file_path = "downloaded_media.mp4"
                
                strl.session_state.download_status = "Streaming file chunks..."
                strl.session_state.download_progress = 0.6
                
                req_file = urllib.request.Request(direct_download_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req_file) as stream_source, open(output_file_path, "wb") as output_disk:
                    output_disk.write(stream_source.read())
                
                if os.path.exists(output_file_path):
                    p_bar.progress(1.0)
                    strl.session_state.download_status = "Finished Stream Transfer"
                    strl.toast("Transcoding Process Completed!", icon="🎉")
                    
                    with open(output_file_path, "rb") as final_data:
                        binary_payload = final_data.read()
                        
                    with left_col:
                        strl.download_button(
                            label="📥 RETRIEVE COMPLETED .MP4 FILE",
                            data=binary_payload,
                            file_name=f"Download_{int(time.time())}.mp4",
                            mime="video/mp4"
                        )
            except Exception as system_fault:
                strl.error(f"Error Processing Subsystem Chain: Proxy Endpoint Blocked. ({str(system_fault)})")
                strl.session_state.download_status = "Pipeline Halted"
