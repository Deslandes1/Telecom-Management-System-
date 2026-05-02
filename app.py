import streamlit as st
import pandas as pd
from datetime import datetime
import io

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Telecom Management System – Built by Gesner Deslandes",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- AUTHENTICATION ----------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "lang" not in st.session_state:
    st.session_state.lang = "en"

# ---------- LANGUAGE DICTIONARIES ----------
text = {
    "en": {
        "login_title": "🔐 Telecom Management System Login",
        "login_password": "Password",
        "login_button": "Login",
        "login_error": "Incorrect password. Please try again.",
        "logout_button": "🚪 Logout",
        "built_by": "Built by Gesner Deslandes – GlobalInternet.py",
        "company_name": "GlobalInternet.py Telecom",
        "nav_dashboard": "📊 Dashboard",
        "nav_customers": "👥 Customers",
        "nav_calls": "📞 Call Logs",
        "nav_sms": "✉️ SMS Logs",
        "nav_billing": "💰 Billing",
        "add_customer": "➕ Add New Customer",
        "customer_name": "Customer Name",
        "customer_phone": "Phone Number",
        "customer_plan": "Subscription Plan",
        "customer_add_btn": "Add Customer",
        "customer_list": "Customer List",
        "customer_id": "ID",
        "customer_no": "No.",
        "edit": "Edit",
        "delete": "Delete",
        "save": "Save",
        "cancel": "Cancel",
        "call_logs": "Call Logs",
        "call_from": "From (Phone)",
        "call_to": "To (Phone)",
        "call_duration": "Duration (seconds)",
        "call_add": "Add Call Record",
        "sms_logs": "SMS Logs",
        "sms_from": "From (Phone)",
        "sms_to": "To (Phone)",
        "sms_text": "Message",
        "sms_add": "Add SMS Record",
        "billing_title": "Billing & Invoicing",
        "billing_customer": "Select Customer",
        "billing_month": "Month (YYYY-MM)",
        "billing_generate": "Generate Invoice",
        "billing_amount": "Amount Due (USD)",
        "billing_paid": "Mark as Paid",
        "invoice_history": "Invoice History",
        "total_customers": "Total Customers",
        "total_calls": "Total Calls",
        "total_sms": "Total SMS",
        "sidebar_contact": "📞 Contact Us",
        "sidebar_email": "✉️ deslandes78@gmail.com",
        "sidebar_phone": "📱 (509)-47385663",
        "sidebar_pricing_title": "💰 Software Pricing",
        "sidebar_monthly": "📅 Monthly subscription: $99 USD / month",
        "sidebar_full": "💎 Full package (one‑time): $2,499 USD",
        "sidebar_note": "Includes source code, setup, and 1 year support",
        "language_selector": "🌐 Language",
        "download_report": "📥 Download Report (CSV)",
        "download_customers": "Download Customers CSV",
        "download_calls": "Download Call Logs CSV",
        "download_sms": "Download SMS Logs CSV",
        "download_invoices": "Download Invoices CSV",
    },
    "fr": {
        "login_title": "🔐 Connexion au Système de Gestion Télécom",
        "login_password": "Mot de passe",
        "login_button": "Se connecter",
        "login_error": "Mot de passe incorrect. Veuillez réessayer.",
        "logout_button": "🚪 Déconnexion",
        "built_by": "Construit par Gesner Deslandes – GlobalInternet.py",
        "company_name": "GlobalInternet.py Télécom",
        "nav_dashboard": "📊 Tableau de bord",
        "nav_customers": "👥 Clients",
        "nav_calls": "📞 Journaux d'appels",
        "nav_sms": "✉️ Journaux SMS",
        "nav_billing": "💰 Facturation",
        "add_customer": "➕ Ajouter un client",
        "customer_name": "Nom du client",
        "customer_phone": "Numéro de téléphone",
        "customer_plan": "Forfait",
        "customer_add_btn": "Ajouter",
        "customer_list": "Liste des clients",
        "customer_id": "ID",
        "customer_no": "N°",
        "edit": "Modifier",
        "delete": "Supprimer",
        "save": "Enregistrer",
        "cancel": "Annuler",
        "call_logs": "Journaux d'appels",
        "call_from": "De (téléphone)",
        "call_to": "Vers (téléphone)",
        "call_duration": "Durée (secondes)",
        "call_add": "Ajouter un appel",
        "sms_logs": "Journaux SMS",
        "sms_from": "De (téléphone)",
        "sms_to": "Vers (téléphone)",
        "sms_text": "Message",
        "sms_add": "Ajouter un SMS",
        "billing_title": "Facturation",
        "billing_customer": "Choisir un client",
        "billing_month": "Mois (AAAA-MM)",
        "billing_generate": "Générer la facture",
        "billing_amount": "Montant dû (USD)",
        "billing_paid": "Marquer comme payé",
        "invoice_history": "Historique des factures",
        "total_customers": "Total clients",
        "total_calls": "Total appels",
        "total_sms": "Total SMS",
        "sidebar_contact": "📞 Contactez‑nous",
        "sidebar_email": "✉️ deslandes78@gmail.com",
        "sidebar_phone": "📱 (509)-47385663",
        "sidebar_pricing_title": "💰 Tarifs du logiciel",
        "sidebar_monthly": "📅 Abonnement mensuel : 99 $US / mois",
        "sidebar_full": "💎 Licence complète (unique) : 2 499 $US",
        "sidebar_note": "Code source, installation et 1 an de support inclus",
        "language_selector": "🌐 Langue",
        "download_report": "📥 Télécharger le rapport (CSV)",
        "download_customers": "Télécharger la liste des clients (CSV)",
        "download_calls": "Télécharger les journaux d'appels (CSV)",
        "download_sms": "Télécharger les journaux SMS (CSV)",
        "download_invoices": "Télécharger les factures (CSV)",
    },
    "es": {
        "login_title": "🔐 Inicio de Sesión – Sistema de Gestión Telecom",
        "login_password": "Contraseña",
        "login_button": "Iniciar sesión",
        "login_error": "Contraseña incorrecta. Intente de nuevo.",
        "logout_button": "🚪 Cerrar sesión",
        "built_by": "Construido por Gesner Deslandes – GlobalInternet.py",
        "company_name": "GlobalInternet.py Telecom",
        "nav_dashboard": "📊 Panel de control",
        "nav_customers": "👥 Clientes",
        "nav_calls": "📞 Registros de llamadas",
        "nav_sms": "✉️ Registros SMS",
        "nav_billing": "💰 Facturación",
        "add_customer": "➕ Agregar cliente",
        "customer_name": "Nombre del cliente",
        "customer_phone": "Número de teléfono",
        "customer_plan": "Plan",
        "customer_add_btn": "Agregar",
        "customer_list": "Lista de clientes",
        "customer_id": "ID",
        "customer_no": "N°",
        "edit": "Editar",
        "delete": "Eliminar",
        "save": "Guardar",
        "cancel": "Cancelar",
        "call_logs": "Registros de llamadas",
        "call_from": "De (teléfono)",
        "call_to": "Para (teléfono)",
        "call_duration": "Duración (segundos)",
        "call_add": "Agregar llamada",
        "sms_logs": "Registros SMS",
        "sms_from": "De (teléfono)",
        "sms_to": "Para (teléfono)",
        "sms_text": "Mensaje",
        "sms_add": "Agregar SMS",
        "billing_title": "Facturación",
        "billing_customer": "Seleccionar cliente",
        "billing_month": "Mes (AAAA-MM)",
        "billing_generate": "Generar factura",
        "billing_amount": "Monto adeudado (USD)",
        "billing_paid": "Marcar como pagado",
        "invoice_history": "Historial de facturas",
        "total_customers": "Total clientes",
        "total_calls": "Total llamadas",
        "total_sms": "Total SMS",
        "sidebar_contact": "📞 Contáctenos",
        "sidebar_email": "✉️ deslandes78@gmail.com",
        "sidebar_phone": "📱 (509)-47385663",
        "sidebar_pricing_title": "💰 Precios del software",
        "sidebar_monthly": "📅 Suscripción mensual: $99 USD / mes",
        "sidebar_full": "💎 Licencia completa (única): $2,499 USD",
        "sidebar_note": "Incluye código fuente, instalación y 1 año de soporte",
        "language_selector": "🌐 Idioma",
        "download_report": "📥 Descargar informe (CSV)",
        "download_customers": "Descargar lista de clientes (CSV)",
        "download_calls": "Descargar registros de llamadas (CSV)",
        "download_sms": "Descargar registros SMS (CSV)",
        "download_invoices": "Descargar facturas (CSV)",
    }
}

def _(key):
    return text[st.session_state.lang].get(key, key)

# ---------- INITIALISE DATA STORES ----------
if "customers" not in st.session_state:
    st.session_state.customers = {}
    st.session_state.next_customer_id = 1
    # Demo customers
    st.session_state.customers[1] = {"name": "Jean Dupont", "phone": "50912345678", "plan": "Prepaid"}
    st.session_state.customers[2] = {"name": "Marie Celeste", "phone": "50987654321", "plan": "Postpaid"}
    st.session_state.next_customer_id = 3

if "calls" not in st.session_state:
    st.session_state.calls = []
    st.session_state.calls.append({"from_phone": "50912345678", "to_phone": "50987654321", "duration": 120, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

if "sms" not in st.session_state:
    st.session_state.sms = []
    st.session_state.sms.append({"from_phone": "50987654321", "to_phone": "50912345678", "message": "Hello, test SMS", "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

if "invoices" not in st.session_state:
    st.session_state.invoices = []

# ---------- CUSTOM CSS (LIGHT BLUE BACKGROUND) ----------
st.markdown("""
<style>
    .stApp, [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #e6f7ff 0%, #cceeff 100%) !important;
    }
    .main-header {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        padding: 1rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        background-color: rgba(255,255,255,0.6);
        border-radius: 20px;
        color: #1e3c72;
    }
    .stButton button {
        background-color: #2a5298;
        color: white;
        border-radius: 30px;
        padding: 0.3rem 1.2rem;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #1e3c72;
    }
    h1, h2, h3 {
        color: #1e3c72;
    }
</style>
""", unsafe_allow_html=True)

# ---------- LOGIN PAGE ----------
if not st.session_state.authenticated:
    st.markdown(f"<div class='main-header'><h1>{_('login_title')}</h1></div>", unsafe_allow_html=True)
    password = st.text_input(_("login_password"), type="password")
    if st.button(_("login_button")):
        if password == "20082010":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error(_("login_error"))
    st.stop()

# ---------- LOGGED IN – MAIN INTERFACE ----------
lang_options = {"English": "en", "Français": "fr", "Español": "es"}
selected_lang = st.sidebar.selectbox(_("language_selector"), list(lang_options.keys()))
st.session_state.lang = lang_options[selected_lang]

page = st.sidebar.radio(
    "",
    [_("nav_dashboard"), _("nav_customers"), _("nav_calls"), _("nav_sms"), _("nav_billing")]
)

# ---------- SIDEBAR INFO ----------
st.sidebar.markdown(f"## {_('company_name')}")
st.sidebar.markdown("---")
st.sidebar.markdown(f"### {_('sidebar_contact')}")
st.sidebar.markdown(_("sidebar_email"))
st.sidebar.markdown(_("sidebar_phone"))
st.sidebar.markdown("---")
st.sidebar.markdown(f"### {_('sidebar_pricing_title')}")
st.sidebar.markdown(_("sidebar_monthly"))
st.sidebar.markdown(_("sidebar_full"))
st.sidebar.caption(_("sidebar_note"))
st.sidebar.markdown("---")

if st.sidebar.button(_("logout_button"), use_container_width=True):
    st.session_state.authenticated = False
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown(f"*{_('built_by')}*")

def get_customer_name(phone):
    for _, data in st.session_state.customers.items():
        if data["phone"] == phone:
            return data["name"]
    return "Unknown"

# ---------- DASHBOARD ----------
if page == _("nav_dashboard"):
    st.markdown(f"<div class='main-header'><h1>📊 {_('nav_dashboard')}</h1></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(_("total_customers"), len(st.session_state.customers))
    with col2:
        st.metric(_("total_calls"), len(st.session_state.calls))
    with col3:
        st.metric(_("total_sms"), len(st.session_state.sms))
    
    st.subheader("📞 Recent Calls")
    if st.session_state.calls:
        df_calls = pd.DataFrame(st.session_state.calls[-5:])
        df_calls["From"] = df_calls["from_phone"].apply(get_customer_name)
        df_calls["To"] = df_calls["to_phone"].apply(get_customer_name)
        st.dataframe(df_calls[["From", "To", "duration", "timestamp"]], use_container_width=True)
    else:
        st.info("No calls yet.")
    
    st.subheader("✉️ Recent SMS")
    if st.session_state.sms:
        df_sms = pd.DataFrame(st.session_state.sms[-5:])
        df_sms["From"] = df_sms["from_phone"].apply(get_customer_name)
        df_sms["To"] = df_sms["to_phone"].apply(get_customer_name)
        st.dataframe(df_sms[["From", "To", "message", "timestamp"]], use_container_width=True)
    else:
        st.info("No SMS yet.")

# ---------- CUSTOMERS (with download) ----------
elif page == _("nav_customers"):
    st.markdown(f"<div class='main-header'><h1>👥 {_('nav_customers')}</h1></div>", unsafe_allow_html=True)
    
    with st.expander(_("add_customer")):
        with st.form("add_customer"):
            name = st.text_input(_("customer_name"))
            phone = st.text_input(_("customer_phone"))
            plan = st.selectbox(_("customer_plan"), ["Prepaid", "Postpaid"])
            if st.form_submit_button(_("customer_add_btn")):
                if name and phone:
                    new_id = st.session_state.next_customer_id
                    st.session_state.customers[new_id] = {"name": name, "phone": phone, "plan": plan}
                    st.session_state.next_customer_id += 1
                    st.rerun()
    
    st.subheader(_("customer_list"))
    if st.session_state.customers:
        # Build dataframe for display and download
        customers_data = []
        for cid, data in st.session_state.customers.items():
            customers_data.append({
                "ID": cid,
                "Name": data["name"],
                "Phone": data["phone"],
                "Plan": data["plan"]
            })
        df_customers = pd.DataFrame(customers_data)
        st.dataframe(df_customers, use_container_width=True)
        
        # Download button
        csv_buffer = io.StringIO()
        df_customers.to_csv(csv_buffer, index=False)
        st.download_button(
            label=_("download_customers"),
            data=csv_buffer.getvalue(),
            file_name=f"customers_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
            key="download_customers"
        )
        
        # Edit/Delete inline (keep original functionality)
        for cid, data in st.session_state.customers.items():
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.markdown(f"**ID {cid}:** {data['name']} – {data['phone']} – Plan: {data['plan']}")
            with col2:
                if st.button(_("edit"), key=f"edit_{cid}"):
                    with st.form(key=f"edit_form_{cid}"):
                        new_name = st.text_input(_("customer_name"), value=data["name"])
                        new_phone = st.text_input(_("customer_phone"), value=data["phone"])
                        new_plan = st.selectbox(_("customer_plan"), ["Prepaid", "Postpaid"], index=0 if data["plan"]=="Prepaid" else 1)
                        if st.form_submit_button(_("save")):
                            st.session_state.customers[cid] = {"name": new_name, "phone": new_phone, "plan": new_plan}
                            st.rerun()
            with col3:
                if st.button(_("delete"), key=f"del_{cid}"):
                    del st.session_state.customers[cid]
                    st.rerun()
    else:
        st.info("No customers yet.")

# ---------- CALL LOGS (with download) ----------
elif page == _("nav_calls"):
    st.markdown(f"<div class='main-header'><h1>📞 {_('nav_calls')}</h1></div>", unsafe_allow_html=True)
    
    with st.expander(_("call_add")):
        with st.form("add_call"):
            from_phone = st.text_input(_("call_from"))
            to_phone = st.text_input(_("call_to"))
            duration = st.number_input(_("call_duration"), min_value=1, step=1)
            if st.form_submit_button(_("call_add")):
                if from_phone and to_phone:
                    st.session_state.calls.append({
                        "from_phone": from_phone,
                        "to_phone": to_phone,
                        "duration": duration,
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                    st.rerun()
    
    st.subheader(_("call_logs"))
    if st.session_state.calls:
        calls_data = []
        for call in st.session_state.calls:
            calls_data.append({
                "From Phone": call["from_phone"],
                "From Name": get_customer_name(call["from_phone"]),
                "To Phone": call["to_phone"],
                "To Name": get_customer_name(call["to_phone"]),
                "Duration (sec)": call["duration"],
                "Timestamp": call["timestamp"]
            })
        df_calls = pd.DataFrame(calls_data)
        st.dataframe(df_calls, use_container_width=True)
        
        csv_buffer = io.StringIO()
        df_calls.to_csv(csv_buffer, index=False)
        st.download_button(
            label=_("download_calls"),
            data=csv_buffer.getvalue(),
            file_name=f"call_logs_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
            key="download_calls"
        )
    else:
        st.info("No call records.")

# ---------- SMS LOGS (with download) ----------
elif page == _("nav_sms"):
    st.markdown(f"<div class='main-header'><h1>✉️ {_('nav_sms')}</h1></div>", unsafe_allow_html=True)
    
    with st.expander(_("sms_add")):
        with st.form("add_sms"):
            from_phone = st.text_input(_("sms_from"))
            to_phone = st.text_input(_("sms_to"))
            message = st.text_area(_("sms_text"))
            if st.form_submit_button(_("sms_add")):
                if from_phone and to_phone and message:
                    st.session_state.sms.append({
                        "from_phone": from_phone,
                        "to_phone": to_phone,
                        "message": message,
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                    st.rerun()
    
    st.subheader(_("sms_logs"))
    if st.session_state.sms:
        sms_data = []
        for sms in st.session_state.sms:
            sms_data.append({
                "From Phone": sms["from_phone"],
                "From Name": get_customer_name(sms["from_phone"]),
                "To Phone": sms["to_phone"],
                "To Name": get_customer_name(sms["to_phone"]),
                "Message": sms["message"],
                "Timestamp": sms["timestamp"]
            })
        df_sms = pd.DataFrame(sms_data)
        st.dataframe(df_sms, use_container_width=True)
        
        csv_buffer = io.StringIO()
        df_sms.to_csv(csv_buffer, index=False)
        st.download_button(
            label=_("download_sms"),
            data=csv_buffer.getvalue(),
            file_name=f"sms_logs_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
            key="download_sms"
        )
    else:
        st.info("No SMS records.")

# ---------- BILLING (with invoice download) ----------
elif page == _("nav_billing"):
    st.markdown(f"<div class='main-header'><h1>💰 {_('nav_billing')}</h1></div>", unsafe_allow_html=True)
    
    if not st.session_state.customers:
        st.warning("No customers. Please add customers first.")
    else:
        customer_options = {cid: f"{data['name']} ({data['phone']})" for cid, data in st.session_state.customers.items()}
        selected_cid = st.selectbox(_("billing_customer"), list(customer_options.keys()), format_func=lambda x: customer_options[x])
        
        with st.expander(_("billing_generate")):
            month = st.text_input(_("billing_month"), value=datetime.now().strftime("%Y-%m"))
            amount = st.number_input(_("billing_amount"), min_value=0.0, step=5.0, value=50.0)
            if st.button(_("billing_generate")):
                existing = any(i["customer_id"] == selected_cid and i["month"] == month for i in st.session_state.invoices)
                if not existing:
                    st.session_state.invoices.append({
                        "customer_id": selected_cid,
                        "month": month,
                        "amount": amount,
                        "paid": False
                    })
                    st.rerun()
                else:
                    st.warning("Invoice for this month already exists.")
        
        st.subheader(_("invoice_history"))
        customer_invoices = [i for i in st.session_state.invoices if i["customer_id"] == selected_cid]
        if customer_invoices:
            inv_data = []
            for inv in customer_invoices:
                inv_data.append({
                    "Month": inv["month"],
                    "Amount (USD)": inv["amount"],
                    "Paid": "Yes" if inv["paid"] else "No"
                })
            df_inv = pd.DataFrame(inv_data)
            st.dataframe(df_inv, use_container_width=True)
            
            # Download invoices for this customer
            csv_buffer = io.StringIO()
            df_inv.to_csv(csv_buffer, index=False)
            st.download_button(
                label=_("download_invoices"),
                data=csv_buffer.getvalue(),
                file_name=f"invoices_customer_{selected_cid}_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                key="download_invoices"
            )
            
            unpaid = [inv for inv in customer_invoices if not inv["paid"]]
            if unpaid:
                with st.form("mark_paid"):
                    inv_index = st.selectbox("Select unpaid invoice", range(len(unpaid)), format_func=lambda i: f"{unpaid[i]['month']} - ${unpaid[i]['amount']}")
                    if st.form_submit_button(_("billing_paid")):
                        target = unpaid[inv_index]
                        for inv in st.session_state.invoices:
                            if inv["customer_id"] == target["customer_id"] and inv["month"] == target["month"]:
                                inv["paid"] = True
                                break
                        st.rerun()
        else:
            st.info("No invoices for this customer.")

# ---------- FOOTER ----------
st.markdown(f"""
<div class="footer">
    <p>© {datetime.now().year} – {_('built_by')}</p>
</div>
""", unsafe_allow_html=True)
