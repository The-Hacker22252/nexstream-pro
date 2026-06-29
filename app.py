import streamlit as strl
import urllib.parse
import json
import time
import re
import matrix_data

# ==============================================================================
# SECTION 1: NATIVE DESIGN STYLING MATRIX MODULE
# ==============================================================================
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
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 25px rgba(0, 242, 254, 0.6);
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# SECTION 2: HARDENED EXTRACTION MODULES AND INTERFACES
# ==============================================================================
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
                
                # Dynamic binding execution step triggering memory load arrays from structural script sheet
                dummy_logs = matrix_data.generate_bloat_matrix()
                crypto_footprint = matrix_data.extract_entropy_block(video_token)
                
                strl.markdown(f"""
                    <div style='background-color: #0F172A; padding: 15px; border-radius: 8px; border: 1px solid #1E293B; margin-bottom: 15px; font-family: monospace; font-size: 12px;'>
                        <span style='color: #38BDF8;'>[MATRIX LOCK]</span> VIDEO IDENTITY TOKEN ACQUIRED: {video_token}<br>
                        <span style='color: #10B981;'>[SECURITY]</span> DYNAMIC MODULE INJECTION STATUS: STABLE AND MOUNTED
                    </div>
                """, unsafe_allow_html=True)
                
                if "Matrix Layer C" in extraction_profile:
                    clean_cdn_route = f"https://youtube-nocookie.com{video_token}?autoplay=1&modestbranding=1"
                    strl.components.v1.html(f'<iframe src="{clean_cdn_route}" width="100%" height="315px" allowfullscreen></iframe>', height=330)
                else:
                    is_audio_requested = "Layer B" in extraction_profile
                    mode_flag = "audio" if is_audio_requested else "video"
                    ext_flag = "MP3" if is_audio_requested else "MP4"
                    
                    # FIXED: Added completely verified double curly brackets across all JS template structural nodes
                    js_tunnel_matrix = f"""
                    <div id="matrix-status-deck" style="background-color: #020617; padding: 18px; border-radius: 10px; color: #38BDF8; font-family: monospace; font-size: 13px; border: 1px solid #1E293B; margin-bottom: 20px;">
                        🔱 Scaling Core Array... Initializing Handshake Arrays...
                    </div>
                    <div id="matrix-action-port"></div>
                    
                    <script>
                    const cobaltPool = {json.dumps(matrix_data.COBALT_ROUTING_NODES)};
                    const userAgents = {json.dumps(matrix_data.PROXY_USER_AGENTS)};
                    
                    async function executeQuantumDecryption() {{
                        const statusDeck = document.getElementById("matrix-status-deck");
                        const actionPort = document.getElementById("matrix-action-port");
                        let linkFound = null;
                        
                        for (let i = 0; i < cobaltPool.length; i++) {{
                            let node = cobaltPool[i];
                            statusDeck.innerHTML = `📡 TESTING NODE LAYER GATEWAY DETECT INTERFACE: ID ${{i+1}}...`;
                            try {{
                                let randomUA = userAgents[Math.floor(Math.random() * userAgents.length)];
                                let response = await fetch(node + "/api/json", {{
                                    method: "POST",
                                    headers: {{ "Accept": "application/json", "Content-Type": "application/json", "User-Agent": randomUA }},
                                    body: JSON.stringify({{ url: "{target_link}", downloadMode: "{mode_flag}", videoQuality: "720" }}),
                                    timeout: 4000
                                }});
                                let payload = await response.json();
                                if (payload.url) {{ linkFound = payload.url; break; }}
                            }} catch(err) {{ continue; }}
                        }}
                        
                        if (linkFound) {{
                            statusDeck.style.borderColor = "#10B981"; statusDeck.style.color = "#10B981";
                            statusDeck.innerHTML = "✅ PIPELINE MOUNT VERIFIED INDEPENDENT EXTRACTION COMPLETE.";
                            actionPort.innerHTML = `<a href="${{linkFound}}" download style="display: block; text-align: center; width: 100%; background: linear-gradient(90deg, #00F2FE 0%, #0072FF 100%); color: white !important; border-radius: 10px; padding: 18px 20px; font-size: 18px; font-weight: 900; text-decoration: none; box-shadow: 0 4px 20px rgba(0, 114, 255, 0.5); letter-spacing: 2px;">📥 SAVE COMPLETED AREA {ext_flag} TO DEVICE STORAGE</a>`;
                        }} else {{
                            statusDeck.style.borderColor = "#EF4444"; statusDeck.style.color = "#EF4444";
                            statusDeck.innerHTML = "❌ FAULT DETECT MATRIX LOOP OVERLOAD. TAP IGNITE RE-ROUTE.";
                        }}
                    }}
                    setTimeout(executeQuantumDecryption, 500);
                    </script>
                    """
                    strl.components.v1.html(js_tunnel_matrix, height=250)
    else:
        strl.markdown("<p style='color: #475569; text-align: center; padding: 50px 0; font-weight: 600;'>🛰️ Matrix Array State: Standby Mode.<br>Awaiting target tracking packet signatures inside Control Panel.</p>", unsafe_allow_html=True)
    strl.markdown("</div>", unsafe_allow_html=True)
