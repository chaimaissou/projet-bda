def get_custom_css():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: #f8fafc;
    }
    
    /* Fix text visibility */
    .stMarkdown, .stText, p, span, div, h1, h2, h3, h4, h5, h6, label {
        color: #1e293b !important;
    }
    
    /* Input fields */
    .stTextInput input, .stSelectbox select, .stDateInput input, .stNumberInput input, textarea {
        color: #0f172a !important;
        background: #ffffff !important;
        border: 1.5px solid #cbd5e1 !important;
        border-radius: 8px !important;
        padding: 0.75rem !important;
        transition: all 0.2s ease !important;
        font-size: 1rem !important;
    }
    
    /* Selectbox specific - green background */
    .stSelectbox {
        background: transparent !important;
    }
    
    .stSelectbox > div {
        background: #dcfce7 !important;
        border-radius: 8px !important;
    }
    
    .stSelectbox select, [data-testid="stSelectbox"] select {
        color: #0f172a !important;
        background: #dcfce7 !important;
        border: 2px solid #86efac !important;
        border-radius: 8px !important;
        padding: 0.75rem !important;
        transition: all 0.2s ease !important;
        font-size: 1rem !important;
    }
    
    .stSelectbox select:hover, [data-testid="stSelectbox"] select:hover {
        border-color: #4ade80 !important;
        box-shadow: 0 0 0 3px rgba(74, 222, 128, 0.1) !important;
    }
    
    .stSelectbox select:focus, [data-testid="stSelectbox"] select:focus {
        border-color: #22c55e !important;
        box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.2) !important;
    }
    
    .stTextInput input:focus, .stDateInput input:focus, textarea:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1) !important;
    }
    
    /* Text areas visibility */
    textarea, .stTextArea textarea {
        color: #0f172a !important;
        background: #ffffff !important;
        border: 1.5px solid #cbd5e1 !important;
        font-size: 1rem !important;
        line-height: 1.5 !important;
    }
    
    textarea::placeholder {
        color: #94a3b8 !important;
        opacity: 1 !important;
    }
    
    .main-header {
        background: linear-gradient(135deg, #3b82f6 0%, #60a5fa 100%);
        padding: 3rem 2rem;
        border-radius: 16px;
        margin-bottom: 2.5rem;
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.15);
    }
    
    .main-header h1, .main-header p {
        color: white !important;
    }
    
    .main-header h1 {
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        margin-bottom: 0.5rem !important;
    }
    
    .card {
        background: #ffffff;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
        margin-bottom: 2rem;
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
    }
    
    .card:hover {
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        padding: 2rem;
        border-radius: 14px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 24px rgba(59, 130, 246, 0.12);
        background: #ffffff;
        border-color: #3b82f6;
    }
    
    .metric-card h3 {
        color: #64748b !important;
        font-size: 0.85rem !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
        margin: 0 0 0.5rem 0 !important;
    }
    
    .metric-card h2 {
        color: #1e293b !important;
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        margin: 0.5rem 0 !important;
    }
    
    .success-banner {
        background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
        color: white !important;
        padding: 1.4rem 1.6rem;
        border-radius: 10px;
        font-weight: 600;
        text-align: center;
        margin: 1.5rem 0;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.15);
    }
    
    .success-banner * {
        color: white !important;
    }
    
    .alert-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-left: 5px solid #f59e0b;
        padding: 1.2rem 1.5rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 8px rgba(245, 158, 11, 0.1);
    }
    
    .alert-box strong, .alert-box * {
        color: #92400e !important;
    }
    
    .error-box {
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        border-left: 5px solid #ef4444;
        padding: 1.2rem 1.5rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 8px rgba(239, 68, 68, 0.1);
    }
    
    .error-box strong, .error-box * {
        color: #991b1b !important;
    }
    
    div[data-testid="stButton"] button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white !important;
        border: none;
        padding: 0.85rem 1.8rem;
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 0.3px;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.15);
    }
    
    div[data-testid="stButton"] button:hover {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.3);
        transform: translateY(-2px);
    }
    
    div[data-testid="stButton"] button:active {
        transform: translateY(0);
    }
    
    .section-title {
        color: #1e293b !important;
        font-size: 1.35rem !important;
        font-weight: 700 !important;
        margin-bottom: 1.5rem !important;
        padding-bottom: 0.75rem !important;
        border-bottom: 3px solid #e2e8f0 !important;
    }
    
    .login-container {
        background: #ffffff;
        border-radius: 18px;
        padding: 3.5rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
        max-width: 450px;
        margin: 0 auto;
        border: 1px solid #e2e8f0;
    }
    
    .login-container h1, .login-container p, .login-container label {
        color: #1e293b !important;
    }
    
    .logout-btn button {
        background: linear-gradient(135deg, #ef4444 0%, #f87171 100%) !important;
        border-color: #f87171 !important;
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.15) !important;
    }
    
    .logout-btn button:hover {
        box-shadow: 0 8px 20px rgba(239, 68, 68, 0.3) !important;
    }
    
    .exam-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 1.8rem;
        margin-bottom: 1.5rem;
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
    }
    
    .exam-card:hover {
        border-color: #3b82f6;
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.1);
        transform: translateY(-2px);
    }
    
    .exam-card h3, .exam-card p, .exam-card strong, .exam-card div {
        color: #1e293b !important;
    }
    
    .badge {
        display: inline-block;
        padding: 0.4rem 0.9rem;
        border-radius: 14px;
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.3px;
    }
    
    .badge-blue {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        color: #1e40af !important;
        box-shadow: 0 2px 6px rgba(30, 64, 175, 0.1);
    }
    
    .badge-green {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        color: #065f46 !important;
        box-shadow: 0 2px 6px rgba(6, 95, 70, 0.1);
    }
    
    .badge-orange {
        background: linear-gradient(135deg, #fed7aa 0%, #fdba74 100%);
        color: #92400e !important;
        box-shadow: 0 2px 6px rgba(146, 64, 14, 0.1);
    }
    
    /* Fix Streamlit native components */
    .stAlert {
        color: #1e293b !important;
        border-radius: 10px !important;
    }
    
    .stDataFrame {
        color: #1e293b !important;
        border-radius: 10px !important;
    }
    
    /* Fix expander */
    .streamlit-expanderHeader {
        color: #1e293b !important;
        background: #f8fafc !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
    }
    
    /* Fix checkbox and radio */
    .stCheckbox label, .stRadio label {
        color: #1e293b !important;
        font-weight: 500 !important;
    }
    
    /* Sidebar styling - MENU CLAIR */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%) !important;
        border-right: 1px solid #e2e8f0 !important;
    }
    
    [data-testid="stSidebar"] [data-testid="stSidebarNav"] {
        background: transparent;
    }
    
    [data-testid="stSidebar"] .stTabs [role="tablist"] button {
        background: transparent !important;
        border-color: #e2e8f0 !important;
        color: #1e293b !important;
        font-weight: 600 !important;
    }
    
    [data-testid="stSidebar"] .stTabs [role="tablist"] button[aria-selected="true"] {
        background: linear-gradient(90deg, #3b82f6 0%, #2563eb 100%) !important;
        color: white !important;
        border-color: #2563eb !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.2) !important;
    }
    
    [data-testid="stSidebar"] .stTabs [role="tablist"] button:hover {
        background: rgba(59, 130, 246, 0.1) !important;
        color: #3b82f6 !important;
    }
    
    [data-testid="stSidebar"] a {
        color: #1e293b !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
    }
    
    [data-testid="stSidebar"] a:hover {
        color: #3b82f6 !important;
        background: rgba(59, 130, 246, 0.1) !important;
        border-radius: 8px !important;
    }
    
    [data-testid="stSidebar"] .stRadio {
        background: transparent;
    }
    
    [data-testid="stSidebar"] [role="option"] {
        background: transparent !important;
        color: #1e293b !important;
        border-radius: 8px !important;
        transition: all 0.2s ease !important;
    }
    
    [data-testid="stSidebar"] [role="option"][aria-selected="true"] {
        background: linear-gradient(90deg, rgba(59, 130, 246, 0.2) 0%, rgba(37, 99, 235, 0.15) 100%) !important;
        color: #1e40af !important;
        font-weight: 700 !important;
        box-shadow: inset 0 2px 8px rgba(59, 130, 246, 0.1) !important;
    }
    
    [data-testid="stSidebar"] [role="option"]:hover {
        background: rgba(59, 130, 246, 0.1) !important;
    }
    
    [data-testid="stSidebar"] .stSelectbox {
        background: #dcfce7 !important;
        border-radius: 8px !important;
    }
    
    [data-testid="stSidebar"] .stSelectbox div {
        background: #dcfce7 !important;
        border-radius: 8px !important;
    }
    
    /* Page navigation pages links */
    [data-testid="stSidebarNav"] li a {
        border-radius: 10px;
        margin: 0.6rem 0;
        padding: 0.9rem 1.2rem;
        color: #1e293b !important;
        transition: all 0.2s ease;
        font-weight: 600;
    }
    
    [data-testid="stSidebarNav"] li a:hover {
        background: rgba(59, 130, 246, 0.12) !important;
        color: #3b82f6 !important;
        transform: translateX(4px);
    }
    
    [data-testid="stSidebarNav"] li a[aria-current="page"] {
        background: linear-gradient(90deg, rgba(59, 130, 246, 0.2) 0%, rgba(37, 99, 235, 0.15) 100%) !important;
        color: #1e40af !important;
        border-left: 5px solid #3b82f6 !important;
        font-weight: 700 !important;
        box-shadow: 0 2px 8px rgba(59, 130, 246, 0.12) !important;
    }
    
    /* Sidebar header */
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: #1e293b !important;
        font-weight: 700 !important;
    }
    
    /* Sidebar text */
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
        color: #1e293b !important;
    }
    
    /* Divider in sidebar */
    [data-testid="stSidebar"] hr {
        border-color: #e2e8f0 !important;
    }
    
    /* Tabs styling */
    [role="tablist"] {
        border-bottom: 2px solid #e2e8f0 !important;
    }
    
    [role="tab"] {
        color: #64748b !important;
        font-weight: 600 !important;
    }
    
    [role="tab"][aria-selected="true"] {
        color: #3b82f6 !important;
        border-bottom: 3px solid #3b82f6 !important;
    }
    
    /* Tables */
    .stDataFrame {
        border-radius: 12px !important;
    }
    
    .stDataFrame tbody tr:hover {
        background-color: rgba(59, 130, 246, 0.05) !important;
    }
    
    /* General improvements */
    hr {
        border-color: #e2e8f0 !important;
    }
    </style>
    """