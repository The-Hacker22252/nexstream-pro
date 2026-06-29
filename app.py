import os
import glob
import time
import shutil
import streamlit as strl
import yt_dlp

# 1. Main Page and UI Design Setup
strl.set_page_config(page_title="NexStream Pro | Armored Matrix", page_icon="⚡", layout="wide")

# Check if FFmpeg is installed on this system
FFMPEG_AVAILABLE = shutil.which("ffmpeg") is not None

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
    </style>
""", unsafe_allow_html=True)

# 2. Tracking System Session Variables
if 'download_progress' not in strl.session_state:
    strl.session_state.download_progress = 0.0
if 'download_speed' not in strl.session_state:
    strl.session_state.download_speed = "0 MB/s"
if 'download_status' not in strl.session_state:
    strl.session_state.download_status = "Idle"

def progress_callback(d):
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate') or 1
        downloaded = d.get('downloaded_bytes', 0)
        speed = d.get('speed', 0)
        if speed:
            strl.session_state.download_speed = f"{speed / (1024 * 1024):.2f} MB/s"
        percent = downloaded / total
        strl.session_state.download_progress = min(percent, 1.0)
        strl.session_state.download_status = "Downloading stream..."
    elif d['status'] == 'finished':
        strl.session_state.download_progress = 1.0
        strl.session_state.download_status = "Finalizing file..."

def clean_old_files():
    for f in glob.glob("downloaded_media.*"):
        try: os.remove(f)
        except: pass

def get_output_file():
    files = glob.glob("downloaded_media.*")
    return files[0] if files else None

# 3. Layout Rendering Interface
strl.markdown("<h1 class='main-title'>⚡ NEXSTREAM PRO ULTRA INFINITE ⚡</h1>", unsafe_allow_html=True)

if FFMPEG_AVAILABLE:
    strl.success("🚀 FFmpeg system engine detected! HD and MP3 conversions unlocked.")
else:
    strl.warning("⚠️ FFmpeg not found on computer. Running in Compatibility Mode (720p Video Max, Audio conversion disabled).")

left_col, right_col = strl.columns(2, gap="large")

with left_col:
    strl.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    strl.subheader("🎛️ Armored Control Panel")
    url_input = strl.text_input("YouTube Link Input:", placeholder="https://youtube.com...")
    
    format_options = ["Full Video (MP4)", "Audio Only (MP3)"] if FFMPEG_AVAILABLE else ["Full Video (MP4)"]
    media_format = strl.selectbox("Output Format:", format_options)
    
    if media_format == "Full Video (MP4)":
        quality_options = ["Best Available (Requires FFmpeg)", "720p Max (No FFmpeg Needed)"] if FFMPEG_AVAILABLE else ["720p Max (No FFmpeg Needed)"]
        quality = strl.selectbox("Quality Profile:", quality_options)
    else:
        quality = strl.selectbox("Audio Bitrate:", ["320kbps", "192kbps", "128kbps"])
        
    process_btn = strl.button("🚀 INITIALIZE MATRIX DOWNLOADING")
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

# 4. Engine Run Pipeline Logic
if process_btn:
    if not url_input:
        strl.error("Configuration Execution Blocked: Link String Missing.")
    else:
        # ULTRA INFINITE LOOP MATRIX: Rotates client configurations automatically if errors strike
        client_rotations = [
            ['web_embedded', 'tv'],
            ['web'],
            ['ios'],
            ['default', '-android_sdkless']
        ]
        
        format_rotations = [
            'best',
            'bestvideo+bestaudio/best',
            'mp4'
        ]
        
        success = False
        last_error = ""
        
        for client in client_rotations:
            if success: break
            for fmt in format_rotations:
                try:
                    strl.session_state.download_status = f"Deploying security bypass node..."
                    clean_old_files()
                    
                    ydl_opts = {
                        'outtmpl': 'downloaded_media.%(ext)s',
                        'progress_hooks': [progress_callback],
                        'quiet': True,
                        'no_warnings': True,
                        'cachedir': False,
                        'format': fmt,
                        'extractor_args': {
                            'youtube': {
                                'player_client': client,
                                'player_skip': ['js']
                            }
                        },
                        'http_headers': {
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
                        }
                    }
                    
                    # Mount cookies file securely if present in repository root folder
                    if os.path.exists("cookies.txt"):
                        ydl_opts['cookiefile'] = 'cookies.txt'

                    if media_format == "Audio Only (MP3)":
                        ydl_opts.update({
                            'format': 'bestaudio/best',
                            'postprocessors': [{
                                'key': 'FFmpegExtractAudio',
                                'preferredcodec': 'mp3',
                                'preferredquality': quality.replace("kbps", ""),
                            }]
                        })
                    elif quality == "Best Available (Requires FFmpeg)" and FFMPEG_AVAILABLE and fmt != 'best':
                        ydl_opts['format'] = 'bestvideo+bestaudio/best'
                        ydl_opts['merge_output_format'] = 'mp4'

                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        meta = ydl.extract_info(url_input, download=False)
                        
                        with right_col:
                            strl.markdown(f"""
                                <div class='dashboard-card' style='border-color: #3B82F6;'>
                                    <b>Title:</b> {meta.get('title', 'Unknown')}<br>
                                    <b>Creator:</b> {meta.get('uploader', 'Unknown')}<br>
                                    <b>Length:</b> {time.strftime('%H:%M:%S', time.gmtime(meta.get('duration', 0)))}
                                </div>
                            """, unsafe_allow_html=True)
                        
                        ydl.download([url_input])
                    
                    success = True
                    break
                except Exception as e:
                    last_error = str(e)
                    continue
                    
        if success:
            output_file_path = get_output_file()
            if output_file_path and os.path.exists(output_file_path):
                p_bar.progress(1.0)
                strl.session_state.download_status = "Finished Stream Transfer"
                strl.toast("Transcoding Process Completed!", icon="🎉")
                
                with open(output_file_path, "rb") as final_data:
                    binary_payload = final_data.read()
                    
                # FIXED: Extracted file extension string dynamically via selection mapping
                ext_lbl = "mp3" if media_format == "Audio Only (MP3)" else "mp4"
                
                with left_col:
                    strl.download_button(
                        label=f"📥 RETRIEVE COMPLETED .{ext_lbl.upper()} FILE",
                        data=binary_payload,
                        file_name=f"Download_{int(time.time())}.{ext_lbl}",
                        mime="audio/mpeg" if ext_lbl == "mp3" else "video/mp4"
                    )
        else:
            strl.error(f"Matrix Loop Exhausted: YouTube Firewall Hard-Blocked Request. ({last_error})")
            strl.session_state.download_status = "Pipeline Halted"
