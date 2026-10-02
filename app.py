```python
from pathlib import Path
from datetime import datetime
import streamlit as st


# ============================================================
# APP CONFIG
# ============================================================

st.set_page_config(
    page_title="FileDesk",
    page_icon="📁",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# DESIGN SYSTEM
# ============================================================

BABY_BLUE = "#B7D8F5"
BABY_BLUE_DARK = "#79B6E8"

YELLOW = "#FFD700"
YELLOW_SOFT = "#FFF6BF"

RED = "#E10600"
RED_SOFT = "#FFF0F0"

INK = "#111827"
INK_LIGHT = "#374151"

WHITE = "#FFFFFF"
BG = "#F5F7FA"

GRAY = "#6B7280"
GRAY_LIGHT = "#9CA3AF"

BORDER = "#E5E7EB"


# ============================================================
# WORKSPACE
# ============================================================

WORKSPACE = Path("workspace")
WORKSPACE.mkdir(exist_ok=True)


# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown(
    f"""
    <style>

    @import url(
        'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800;900&display=swap'
    );

    /* ========================================================
       GLOBAL
       ======================================================== */

    html, body, [class*="css"] {{
        font-family: 'DM Sans', sans-serif;
    }}

    .stApp {{
        background: {BG};
    }}

    .block-container {{
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 5rem;
    }}

    #MainMenu {{
        visibility: hidden;
    }}

    header {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}


    /* ========================================================
       SIDEBAR
       ======================================================== */

    section[data-testid="stSidebar"] {{
        background: {WHITE};
        border-right: 1px solid {BORDER};
    }}

    section[data-testid="stSidebar"] > div {{
        padding: 1.5rem 1rem;
    }}

    .logo {{
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 5px;
    }}

    .logo-icon {{
        width: 42px;
        height: 42px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: {BABY_BLUE};
        border-radius: 12px;
        font-size: 21px;
    }}

    .logo-text {{
        font-size: 1.45rem;
        font-weight: 900;
        letter-spacing: -1px;
        color: {INK};
    }}

    .logo-text span {{
        color: #2373AA;
    }}

    .sidebar-subtitle {{
        color: {GRAY};
        font-size: 0.78rem;
        margin: 0 0 28px 52px;
    }}

    .nav-label {{
        color: {GRAY_LIGHT};
        font-size: 0.68rem;
        font-weight: 800;
        letter-spacing: 1.4px;
        text-transform: uppercase;
        margin: 15px 10px 8px;
    }}

    section[data-testid="stSidebar"] .stRadio label {{
        border-radius: 11px;
        padding: 9px 11px;
        margin-bottom: 4px;
        color: {INK_LIGHT} !important;
        font-weight: 600;
        transition: 0.15s ease;
    }}

    section[data-testid="stSidebar"] .stRadio label:hover {{
        background: #F0F7FC;
    }}

    .workspace-card {{
        margin-top: 25px;
        padding: 14px;
        border: 1px solid {BORDER};
        border-radius: 14px;
        background: {BG};
    }}

    .workspace-title {{
        color: {GRAY};
        font-size: 0.68rem;
        font-weight: 800;
        letter-spacing: 1px;
        text-transform: uppercase;
    }}

    .workspace-path {{
        color: {INK};
        font-size: 0.82rem;
        font-weight: 700;
        margin-top: 5px;
    }}


    /* ========================================================
       PAGE HEADER
       ======================================================== */

    .page-kicker {{
        color: #2776AE;
        font-size: 0.72rem;
        font-weight: 900;
        letter-spacing: 1.7px;
        text-transform: uppercase;
        margin-bottom: 6px;
    }}

    h1 {{
        font-size: 3rem !important;
        font-weight: 900 !important;
        letter-spacing: -2.8px !important;
        line-height: 1 !important;
        color: {INK} !important;
        margin-bottom: 8px !important;
    }}

    .page-description {{
        color: {GRAY};
        font-size: 0.98rem;
        margin-bottom: 30px;
    }}


    /* ========================================================
       DASHBOARD HERO
       ======================================================== */

    .hero {{
        position: relative;
        overflow: hidden;
        background: {INK};
        border-radius: 24px;
        padding: 42px;
        min-height: 250px;
        margin-bottom: 28px;
    }}

    .hero-grid {{
        position: absolute;
        inset: 0;
        opacity: 0.07;
        background-image:
            linear-gradient(#fff 1px, transparent 1px),
            linear-gradient(90deg, #fff 1px, transparent 1px);
        background-size: 30px 30px;
    }}

    .hero-content {{
        position: relative;
        z-index: 2;
        max-width: 680px;
    }}

    .hero-eyebrow {{
        display: inline-block;
        background: {YELLOW};
        color: {INK};
        padding: 6px 11px;
        border-radius: 999px;
        font-size: 0.68rem;
        font-weight: 900;
        letter-spacing: 1px;
        margin-bottom: 18px;
    }}

    .hero-title {{
        color: {WHITE};
        font-size: 3.6rem;
        font-weight: 900;
        letter-spacing: -4px;
        line-height: 0.95;
        margin: 0;
    }}

    .hero-title span {{
        color: {BABY_BLUE};
    }}

    .hero-description {{
        color: #CBD5E1;
        font-size: 0.98rem;
        line-height: 1.7;
        max-width: 600px;
        margin-top: 17px;
    }}

    .hero-shape {{
        position: absolute;
        width: 300px;
        height: 300px;
        right: -70px;
        top: -70px;
        border-radius: 50%;
        background: {BABY_BLUE};
    }}

    .hero-shape-two {{
        position: absolute;
        width: 130px;
        height: 130px;
        right: 150px;
        bottom: -65px;
        border-radius: 50%;
        background: {YELLOW};
    }}


    /* ========================================================
       STAT CARDS
       ======================================================== */

    div[data-testid="stMetric"] {{
        background: {WHITE};
        border: 1px solid {BORDER};
        border-radius: 18px;
        padding: 20px;
        box-shadow: 0 4px 15px rgba(15,23,42,0.03);
    }}

    div[data-testid="stMetricLabel"] {{
        color: {GRAY} !important;
        font-weight: 600 !important;
    }}

    div[data-testid="stMetricValue"] {{
        color: {INK} !important;
        font-weight: 900 !important;
        letter-spacing: -1px;
    }}


    /* ========================================================
       SECTION HEADERS
       ======================================================== */

    .section-header {{
        display: flex;
        align-items: end;
        justify-content: space-between;
        margin-top: 34px;
        margin-bottom: 15px;
    }}

    .section-title {{
        font-size: 1.3rem;
        font-weight: 900;
        letter-spacing: -0.7px;
        color: {INK};
    }}

    .section-caption {{
        color: {GRAY};
        font-size: 0.8rem;
    }}


    /* ========================================================
       FILE CARDS
       ======================================================== */

    .file-card {{
        display: flex;
        align-items: center;
        gap: 15px;
        background: {WHITE};
        border: 1px solid {BORDER};
        border-radius: 16px;
        padding: 15px;
        margin-bottom: 9px;
        transition: 0.18s ease;
    }}

    .file-card:hover {{
        border-color: {BABY_BLUE_DARK};
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(15,23,42,0.07);
    }}

    .file-icon {{
        width: 42px;
        height: 42px;
        flex-shrink: 0;
        border-radius: 11px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #EDF6FD;
        font-size: 19px;
    }}

    .file-information {{
        flex: 1;
    }}

    .file-name {{
        font-weight: 800;
        font-size: 0.91rem;
        color: {INK};
    }}

    .file-meta {{
        color: {GRAY};
        font-size: 0.72rem;
        margin-top: 3px;
    }}

    .file-size {{
        color: {GRAY};
        font-size: 0.75rem;
        font-weight: 700;
    }}


    /* ========================================================
       EMPTY STATE
       ======================================================== */

    .empty-state {{
        text-align: center;
        background: {WHITE};
        border: 1px dashed #CBD5E1;
        border-radius: 20px;
        padding: 55px 25px;
    }}

    .empty-icon {{
        width: 60px;
        height: 60px;
        margin: 0 auto 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: {BABY_BLUE};
        border-radius: 17px;
        font-size: 28px;
    }}

    .empty-title {{
        font-size: 1.15rem;
        font-weight: 900;
        color: {INK};
    }}

    .empty-description {{
        color: {GRAY};
        font-size: 0.86rem;
        margin-top: 5px;
    }}


    /* ========================================================
       PANELS
       ======================================================== */

    .panel {{
        background: {WHITE};
        border: 1px solid {BORDER};
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 4px 15px rgba(15,23,42,0.025);
    }}

    .panel-title {{
        font-size: 1.05rem;
        font-weight: 900;
        color: {INK};
    }}

    .panel-description {{
        color: {GRAY};
        font-size: 0.82rem;
        margin-top: 3px;
        margin-bottom: 20px;
    }}


    /* ========================================================
       INPUTS
       ======================================================== */

    .stTextInput input,
    .stTextArea textarea {{
        border: 1px solid {BORDER} !important;
        border-radius: 11px !important;
        background: {WHITE} !important;
    }}

    .stTextInput input:focus,
    .stTextArea textarea:focus {{
        border: 2px solid {BABY_BLUE_DARK} !important;
        box-shadow: 0 0 0 3px rgba(183,216,245,0.3) !important;
    }}

    .stTextArea textarea {{
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.85rem !important;
    }}


    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button,
    .stDownloadButton > button {{
        min-height: 43px;
        border-radius: 11px;
        font-weight: 800;
        transition: 0.15s ease;
    }}

    .stButton > button:hover,
    .stDownloadButton > button:hover {{
        transform: translateY(-2px);
    }}

    .stButton > button[kind="primary"] {{
        background: {INK};
        border-color: {INK};
        color: {WHITE};
    }}

    .stButton > button[kind="primary"]:hover {{
        background: #25313C;
        border-color: #25313C;
    }}


    /* ========================================================
       DANGER AREA
       ======================================================== */

    .danger-panel {{
        background: {RED_SOFT};
        border: 1px solid #FFCCCC;
        border-radius: 17px;
        padding: 17px;
        margin: 20px 0;
    }}

    .danger-title {{
        color: {RED};
        font-weight: 900;
        font-size: 0.92rem;
    }}

    .danger-description {{
        color: #8B3030;
        font-size: 0.78rem;
        margin-top: 4px;
    }}


    /* ========================================================
       INFO BADGE
       ======================================================== */

    .info-badge {{
        display: inline-block;
        background: {YELLOW_SOFT};
        color: #765D00;
        border-radius: 999px;
        padding: 5px 9px;
        font-size: 0.67rem;
        font-weight: 800;
    }}


    /* ========================================================
       FOOTER
       ======================================================== */

    .footer {{
        text-align: center;
        border-top: 1px solid {BORDER};
        padding-top: 25px;
        margin-top: 70px;
        color: {GRAY};
        font-size: 0.75rem;
    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HELPERS
# ============================================================

def safe_path(name):
    clean_name = Path(name.strip()).name

    if not clean_name:
        return None

    return WORKSPACE / clean_name


def list_files():
    return sorted(
        [p for p in WORKSPACE.iterdir() if p.is_file()],
        key=lambda p: p.name.lower()
    )


def human_size(size):
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            if unit == "B":
                return f"{size:.0f} {unit}"
            return f"{size:.1f} {unit}"
        size /= 1024

    return f"{size:.1f} TB"


def page_header(kicker, title, description):

    st.markdown(
        f'<div class="page-kicker">{kicker}</div>',
        unsafe_allow_html=True
    )

    st.title(title)

    st.markdown(
        f'<div class="page-description">{description}</div>',
        unsafe_allow_html=True
    )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div class="logo">
            <div class="logo-icon">📁</div>
            <div class="logo-text">File<span>Desk</span></div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">FILE MANAGEMENT SYSTEM</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="nav-label">Workspace</div>',
        unsafe_allow_html=True
    )

    navigation = st.radio(
        "Navigation",
        [
            "🏠  Overview",
            "➕  Create",
            "📖  Read",
            "🔧  Update",
            "🗑️  Delete",
        ],
        label_visibility="collapsed"
    )

    st.markdown(
        """
        <div class="workspace-card">
            <div class="workspace-title">
                Current workspace
            </div>

            <div class="workspace-path">
                📂 workspace/
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.caption("Python • pathlib • Streamlit")


page = navigation.split("  ")[1]


# ============================================================
# OVERVIEW
# ============================================================

def overview():

    files = list_files()

    total_size = sum(
        file.stat().st_size
        for file in files
    )

    latest = max(
        [file.stat().st_mtime for file in files],
        default=0
    )

    latest_text = (
        datetime.fromtimestamp(latest).strftime("%d %b")
        if latest
        else "—"
    )

    # Hero
    st.markdown(
        """
        <div class="hero">

            <div class="hero-grid"></div>

            <div class="hero-shape"></div>
            <div class="hero-shape-two"></div>

            <div class="hero-content">

                <div class="hero-eyebrow">
                    FILE MANAGEMENT • 01
                </div>

                <div class="hero-title">
                    Your files.<br>
                    <span>Your workspace.</span>
                </div>

                <div class="hero-description">
                    A focused file management dashboard for creating,
                    reading, updating and deleting files — built entirely
                    with Python and Streamlit.
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # Stats

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "📄 Files",
        len(files)
    )

    c2.metric(
        "💾 Storage",
        human_size(total_size)
    )

    c3.metric(
        "🕒 Last activity",
        latest_text
    )

    # File list

    st.markdown(
        """
        <div class="section-header">
            <div class="section-title">
                Recent files
            </div>

            <div class="section-caption">
                Your workspace
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if not files:

        st.markdown(
            """
            <div class="empty-state">

                <div class="empty-icon">
                    📁
                </div>

                <div class="empty-title">
                    Nothing here yet
                </div>

                <div class="empty-description">
                    Create your first file to start building your workspace.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        return

    for file in files:

        stat = file.stat()

        modified = datetime.fromtimestamp(
            stat.st_mtime
        ).strftime("%d %b %Y • %H:%M")

        st.markdown(
            f"""
            <div class="file-card">

                <div class="file-icon">
                    📄
                </div>

                <div class="file-information">

                    <div class="file-name">
                        {file.name}
                    </div>

                    <div class="file-meta">
                        Modified {modified}
                    </div>

                </div>

                <div class="file-size">
                    {human_size(stat.st_size)}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# CREATE
# ============================================================

def create():

    page_header(
        "CREATE",
        "Create a new file",
        "Start with a name, add your content, and save it to your workspace."
    )

    st.markdown(
        """
        <div class="panel">

            <div class="panel-title">
                New file
            </div>

            <div class="panel-description">
                Your file will be saved inside the workspace folder.
            </div>

        """,
        unsafe_allow_html=True
    )

    name = st.text_input(
        "File name",
        placeholder="notes.txt"
    )

    content = st.text_area(
        "Content",
        placeholder="Write something beautiful...",
        height=240
    )

    st.markdown(
        '<span class="info-badge">SAVED LOCALLY</span>',
        unsafe_allow_html=True
    )

    st.write("")

    if st.button(
        "Create file  →",
        type="primary",
        use_container_width=True
    ):

        if not name.strip():

            st.error("Please enter a file name.")

            return

        path = safe_path(name)

        if path.exists():

            st.error(
                f"'{path.name}' already exists."
            )

            return

        try:

            path.write_text(
                content,
                encoding="utf-8"
            )

            st.success(
                f"'{path.name}' was created successfully."
            )

            st.rerun()

        except Exception as error:

            st.error(
                f"Could not create the file: {error}"
            )

    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# READ
# ============================================================

def read():

    page_header(
        "READ",
        "Read a file",
        "Choose a file and inspect its contents."
    )

    files = list_files()

    if not files:

        st.markdown(
            """
            <div class="empty-state">

                <div class="empty-icon">📖</div>

                <div class="empty-title">
                    No files to read
                </div>

                <div class="empty-description">
                    Create a file first and it will appear here.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        return

    selected = st.selectbox(
        "Select file",
        [file.name for file in files]
    )

    path = safe_path(selected)

    try:

        content = path.read_text(
            encoding="utf-8"
        )

        stat = path.stat()

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "File size",
            human_size(stat.st_size)
        )

        c2.metric(
            "Lines",
            len(content.splitlines())
        )

        c3.metric(
            "Characters",
            len(content)
        )

        st.write("")

        st.markdown(
            """
            <div class="panel">

                <div class="panel-title">
                    📄 Content preview
                </div>

                <div class="panel-description">
                    Read-only preview of your selected file.
                </div>

            """,
            unsafe_allow_html=True
        )

        if content:

            st.code(
                content,
                language=None,
                line_numbers=True
            )

        else:

            st.info(
                "This file is empty."
            )

        st.download_button(
            "Download file",
            data=content,
            file_name=path.name,
            use_container_width=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

    except Exception as error:

        st.error(
            f"Could not read the file: {error}"
        )


# ============================================================
# UPDATE
# ============================================================

def update():

    page_header(
        "UPDATE",
        "Update a file",
        "Rename it, add new content, or replace everything inside."
    )

    files = list_files()

    if not files:

        st.markdown(
            """
            <div class="empty-state">

                <div class="empty-icon">🔧</div>

                <div class="empty-title">
                    Nothing to update
                </div>

                <div class="empty-description">
                    Create a file before using the update tools.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        return

    selected = st.selectbox(
        "Select file",
        [file.name for file in files]
    )

    path = safe_path(selected)

    operation = st.radio(
        "Operation",
        [
            "✏️ Rename",
            "➕ Append",
            "🔄 Overwrite"
        ],
        horizontal=True
    )

    st.write("")

    # Rename

    if operation == "✏️ Rename":

        st.markdown(
            """
            <div class="panel">

                <div class="panel-title">
                    Rename file
                </div>

                <div class="panel-description">
                    Change the file name without changing its contents.
                </div>

            """,
            unsafe_allow_html=True
        )

        new_name = st.text_input(
            "New name",
            value=path.name
        )

        if st.button(
            "Rename file  →",
            type="primary",
            use_container_width=True
        ):

            if not new_name.strip():

                st.error(
                    "Enter a new file name."
                )

            else:

                new_path = safe_path(new_name)

                if new_path.exists():

                    st.error(
                        f"'{new_path.name}' already exists."
                    )

                else:

                    try:

                        path.rename(new_path)

                        st.success(
                            f"Renamed to '{new_path.name}'."
                        )

                        st.rerun()

                    except Exception as error:

                        st.error(
                            f"Could not rename file: {error}"
                        )

        st.markdown("</div>", unsafe_allow_html=True)

    # Append

    elif operation == "➕ Append":

        st.markdown(
            """
            <div class="panel">

                <div class="panel-title">
                    Append content
                </div>

                <div class="panel-description">
                    Add new text to the end of the existing file.
                </div>

            """,
            unsafe_allow_html=True
        )

        data = st.text_area(
            "Content to append",
            height=220,
            placeholder="Add something new..."
        )

        if st.button(
            "Append content  →",
            type="primary",
            use_container_width=True
        ):

            try:

                with path.open(
                    "a",
                    encoding="utf-8"
                ) as file:

                    if path.stat().st_size > 0:
                        file.write("\n")

                    file.write(data)

                st.success(
                    f"Content added to '{path.name}'."
                )

            except Exception as error:

                st.error(
                    f"Could not append content: {error}"
                )

        st.markdown("</div>", unsafe_allow_html=True)

    # Overwrite

    else:

        st.markdown(
            """
            <div class="panel">

                <div class="panel-title">
                    Overwrite content
                </div>

                <div class="panel-description">
                    Replace the existing content with new content.
                </div>

            """,
            unsafe_allow_html=True
        )

        try:

            old_content = path.read_text(
                encoding="utf-8"
            )

        except Exception:

            old_content = ""

        data = st.text_area(
            "New content",
            value=old_content,
            height=250
        )

        st.markdown(
            """
            <div class="danger-panel">

                <div class="danger-title">
                    ⚠️ Existing content will be replaced
                </div>

                <div class="danger-description">
                    This operation cannot be undone.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "Overwrite file  →",
            type="primary",
            use_container_width=True
        ):

            try:

                path.write_text(
                    data,
                    encoding="utf-8"
                )

                st.success(
                    f"'{path.name}' has been overwritten."
                )

            except Exception as error:

                st.error(
                    f"Could not overwrite file: {error}"
                )

        st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# DELETE
# ============================================================

def delete():

    page_header(
        "DELETE",
        "Delete a file",
        "Permanently remove a file from your workspace."
    )

    files = list_files()

    if not files:

        st.markdown(
            """
            <div class="empty-state">

                <div class="empty-icon">🗑️</div>

                <div class="empty-title">
                    Nothing to delete
                </div>

                <div class="empty-description">
                    Your workspace currently has no files.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        return

    selected = st.selectbox(
        "Select file",
        [file.name for file in files]
    )

    path = safe_path(selected)

    st.markdown(
        f"""
        <div class="danger-panel">

            <div class="danger-title">
                Delete {path.name}
            </div>

            <div class="danger-description">
                This file will be permanently removed from your workspace.
                This action cannot be undone.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    confirm = st.checkbox(
        f"I understand that '{path.name}' will be permanently deleted."
    )

    if st.button(
        "Delete permanently",
        type="primary",
        use_container_width=True,
        disabled=not confirm
    ):

        try:

            path.unlink()

            st.success(
                f"'{path.name}' was deleted."
            )

            st.rerun()

        except Exception as error:

            st.error(
                f"Could not delete file: {error}"
            )


# ============================================================
# ROUTER
# ============================================================

if page == "Overview":

    overview()

elif page == "Create":

    create()

elif page == "Read":

    read()

elif page == "Update":

    update()

elif page == "Delete":

    delete()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        <strong>FileDesk</strong>
        &nbsp;•&nbsp;
        Python + Streamlit
        &nbsp;•&nbsp;
        File Handling CRUD Project
    </div>
    """,
    unsafe_allow_html=True
)