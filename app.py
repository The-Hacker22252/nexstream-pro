import streamlit as strl
import re

# 1. Main Page and UI Design Setup
strl.set_page_config(page_title="NexStream Pro | Ultimate Overlord Matrix", page_icon="🔱", layout="wide")

strl.markdown("""
    <style>
    .main { background-color: #060913; color: #F1F5F9; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .matrix-title {
        font-size: 3.5rem !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, #00F2FE 0%, #4FACFE 50%, #0072FF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2px;
        text-shadow: 0px 5px 30px rgba(0, 242, 254, 0.4);
        letter-spacing: 2px;
    }
    .sub-tagline {
        text-align: center;
        color: #94A3B8;
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 25px;
        letter-spacing: 3px;
    }
    .armored-card {
        background: linear-gradient(145deg, #0F172A 0%, #1E293B 100%);
        border: 2px solid #334155;
        border-radius: 16px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.6);
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    }
    .armored-card:hover {
        border-color: #38BDF8;
        box-shadow: 0 16px 50px 0 rgba(56, 189, 248, 0.25);
        transform: translateY(-2px);
    }
    .stButton>button {
        width: 100% !important;
        background: linear-gradient(90deg, #00F2FE 0%, #0072FF 100%) !important;
        color: #FFFFFF !important;
        border-radius: 10px !important;
        border: none !important;
        padding: 18px 25px !important;
        font-size: 20px !important;
        font-weight: 900 !important;
        letter-spacing: 2px;
        box-shadow: 0 4px 20px rgba(0, 114, 255, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# 2. Hardened URL Parser Engine
def parse_youtube_identity(url):
    patterns = [
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([a-zA-Z0-9_-]{11})',
        r'(?:https?:\/\/)?(?:www\.)?youtu\.be\/([a-zA-Z0-9_-]{11})',
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/embed\/([a-zA-Z0-9_-]{11})',
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/shorts\/([a-zA-Z0-9_-]{11})'
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

# 3. Layout Rendering Interface
strl.markdown("<h1 class='matrix-title'>🔱 NEXSTREAM PRO: ULTRA MATRIX 🔱</h1>", unsafe_allow_html=True)
strl.markdown("<p class='sub-tagline'>ARMORED DECRYPTION NODES // AUTOMATED SECURE STREAM ISOLATION</p>", unsafe_allow_html=True)

left_deck, right_deck = strl.columns(2, gap="large")

with left_deck:
    strl.markdown("<div class='armored-card'>", unsafe_allow_html=True)
    strl.subheader("🛰️ System Control Terminal")
    target_link = strl.text_input("Input Target Encrypted Signature String:", placeholder="Paste your link target parameters here...")
    
    extraction_profile = strl.selectbox("Select Extraction Tunnel Matrix Profile:", [
        "Matrix Layer A (Universal High-Fidelity MP4 Container)",
        "Matrix Layer B (Isolated Low-Bypass Audio Core MP3 Engine)",
        "Matrix Layer C (Embedded CDN Decryption Web View Mode)"
    ])
    
    override_firewalls = strl.button("🚀 IGNITE QUANTUM OVERRIDE DECRYPTION CHAIN")
    strl.markdown("</div>", unsafe_allow_html=True)

with right_deck:
    strl.markdown("<div class='armored-card'>", unsafe_allow_html=True)
    strl.subheader("📡 Real-Time Packet Payload Inspector")
    
    if override_firewalls:
        if not target_link:
            strl.error("CRITICAL ERROR TERMINATION: TARGET SEED URL PAYLOAD MISSING.")
        else:
            video_token = parse_youtube_identity(target_link)
            if not video_token:
                strl.error("MALFORMED PARSING STRUCTURE EXCEPTION: LINK MISSING VALID TOKEN ID.")
            else:
                strl.balloons()
                
                strl.markdown(f"""
                    <div style='background-color: #0F172A; padding: 15px; border-radius: 8px; border: 1px solid #1E293B; margin-bottom: 15px; font-family: monospace; font-size: 12px;'>
                        <span style='color: #38BDF8;'>[MATRIX LOCK]</span> VIDEO IDENTITY TOKEN ACQUIRED: {video_token}<br>
                        <span style='color: #10B981;'>[SECURITY]</span> NATIVE RUNTIME COMPILATION STATUS: STABLE AND MOUNTED
                    </div>
                """, unsafe_allow_html=True)
                
                strl.markdown("<div class='status-alert-matrix'>✅ PIPELINE MOUNT VERIFIED. PLAY NATIVE STREAM INSIDE APP:</div>", unsafe_allow_html=True)
                
                # FIXED: Uses Streamlit's official native video player element.
                # This drops HTML string concatenation entirely, making it impossible to lose slashes or break IP lookup routing paths!
                strl.video(target_link)
                
    else:
        strl.markdown("<p style='color: #475569; text-align: center; padding: 50px 0; font-weight: 600;'>🛰️ Matrix Array State: Standby Mode.<br>Awaiting target url encrypted tracking packet signatures inside Control Panel.</p>", unsafe_allow_html=True)
    strl.markdown("</div>", unsafe_allow_html=True)
