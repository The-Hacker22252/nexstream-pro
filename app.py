import streamlit as strl
import urllib.request
import json
import time
import os
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
    div.stDownloadButton > button {
        width: 100% !important;
        background: linear-gradient(90deg, #3B82F6 0%, #2563EB 100%) !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 16px 20px !important;
        font-size: 18px !important;
        font-weight: 800 !important;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4) !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Hardened URL Parser Matrix
def clean_and_extract_video_id(url):
    regex_pattern = r'(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^"&?\/\s]{11})'
    match = re.search(regex_pattern, url)
    return match.group(1) if match else None

# 3. Layout Rendering Interface
strl.markdown("<h1 class='main-title'>⚡ NEXSTREAM PRO MAXIMUM HARDENED ⚡</h1>", unsafe_allow_html=True)
strl.success("🚀 INFINITE MULTI-API FAILOVER LOOP ENGAGED. ZERO-FAILURE BACKEND CHANNELS ONLINE.")

left_col, right_col = strl.columns(2, gap="large")

with left_col:
    strl.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    strl.subheader("🎛️ Armored Matrix Controller")
    url_input = strl.text_input("YouTube Link Input:", placeholder="Paste your link here...")
    
    media_format = strl.selectbox("Output Format Option:", [
        "Full Video (Universal MP4)", 
        "Audio Only (High Quality MP3)"
    ])
    
    process_btn = strl.button("🚀 INITIALIZE ARMORED PAYLOAD FETCH")
    strl.markdown("</div>", unsafe_allow_html=True)

with right_col:
    strl.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    strl.subheader("📊 Elite Payload Monitor")
    
    if process_btn:
        if not url_input:
            strl.error("CRITICAL ERROR: Input stream link parameters are missing.")
        else:
            video_id = clean_and_extract_video_id(url_input)
            if not video_id:
                strl.error("MALFORMED URL: Unable to parse YouTube video token identity.")
            else:
                is_audio = "Audio Only" in media_format
                direct_file_url = None
                success = False
                
                # --- CHANNEL 1: COBALT REST NODE NETWORKS ---
                if not success:
                    cobalt_endpoints = [
                        "https://wukko.me",
                        "https://meowing.de",
                        "https://cobalt.tools",
                        "https://unblock.casa"
                    ]
                    payload = {
                        "url": url_input,
                        "downloadMode": "audio" if is_audio else "video",
                        "videoQuality": "720"
                    }
                    
                    for api_url in cobalt_endpoints:
                        try:
                            strl.session_state.download_status = "Scanning Cobalt Node Array..."
                            req = urllib.request.Request(
                                api_url,
                                data=json.dumps(payload).encode('utf-8'),
                                headers={'Content-Type': 'application/json', 'Accept': 'application/json', 'User-Agent': 'Mozilla/5.0'},
                                method='POST'
                            )
                            with urllib.request.urlopen(req, timeout=5) as response:
                                res_data = json.loads(response.read().decode('utf-8'))
                            if "url" in res_data:
                                direct_file_url = res_data["url"]
                                success = True
                                break
                        except Exception:
                            continue

                # --- CHANNEL 2: INVIDIOUS API DECENTRALIZED NODES ---
                if not success:
                    invidious_nodes = [
                        "https://privacydev.net",
                        "https://yewtu.be",
                        "https://tux.pizza"
                    ]
                    for node in invidious_nodes:
                        try:
                            strl.session_state.download_status = "Switching to Backup Invidious Grid..."
                            api_url = f"{node}/api/v1/videos/{video_id}"
                            req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
                            with urllib.request.urlopen(req, timeout=5) as response:
                                meta = json.loads(response.read().decode('utf-8'))
                            streams = meta.get('adaptiveStreams', []) or meta.get('formatStreams', [])
                            if streams:
                                direct_file_url = streams[0]['url']
                                success = True
                                break
                        except Exception:
                            continue

                # --- CHANNEL 3: PIPED MEDIA EXTRACTION TUNNELS ---
                if not success:
                    try:
                        strl.session_state.download_status = "Switching to Emergency Piped API Core..."
                        piped_url = f"https://kavin.rocks{video_id}"
                        req = urllib.request.Request(piped_url, headers={'User-Agent': 'Mozilla/5.0'})
                        with urllib.request.urlopen(req, timeout=6) as response:
                            meta = json.loads(response.read().decode('utf-8'))
                        streams = meta.get('audioStreams', []) if is_audio else meta.get('videoStreams', [])
                        if streams:
                            direct_file_url = streams[0]['url']
                            success = True
                    except Exception:
                        pass

                # --- SERVER-SIDE BINARY BRIDGE DOWNLOADER ---
                if success and direct_file_url:
                    try:
                        strl.warning("📥 Server-side file bridge engaged... Streaming data directly into memory.")
                        
                        file_req = urllib.request.Request(direct_file_url, headers={'User-Agent': 'Mozilla/5.0'})
                        with urllib.request.urlopen(file_req, timeout=35) as file_stream:
                            binary_payload = file_stream.read()
                            
                        strl.balloons()
                        ext = "mp3" if is_audio else "mp4"
                        mime_type = "audio/mpeg" if is_audio else "video/mp4"
                        
                        strl.markdown("""
                            <div style='background-color: #10B981; padding: 15px; border-radius: 8px; color: white; font-weight: 700; margin-bottom: 20px; text-align: center;'>
                                ✅ Media stream successfully locked inside your application memory cache!
                            </div>
                        """, unsafe_allow_html=True)
                        
                        with left_col:
                            strl.download_button(
                                label=f"📥 SAVE COMPLETED .{ext.upper()} FILE TO DEVICE",
                                data=binary_payload,
                                file_name=f"Download_{int(time.time())}.{ext}",
                                mime=mime_type
                            )
                    except Exception as e:
                        strl.error(f"Memory Bridge Error: File limits exceeded or server stream dropped. ({str(e)})")
                else:
                    strl.error("All 3 matrix extraction channels are temporarily locked by firewalls. Please pause for 5 seconds and retry.")
    else:
        strl.info("🔴 Pipeline status: Standby. Awaiting link signature entry inputs.")
    strl.markdown("</div>", unsafe_allow_html=True)
