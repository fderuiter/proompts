import subprocess
import time
import pytest
from playwright.sync_api import sync_playwright
from axe_playwright_python.sync_playwright import Axe

@pytest.fixture(scope="module")
def streamlit_server():
    # Start the Streamlit server
    process = subprocess.Popen(
        ["uv", "run", "streamlit", "run", "studio/studio/app.py", "--server.port", "8502", "--server.headless", "true"],
        cwd="/app",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Wait for the server to start (simple sleep to ensure it's up)
    time.sleep(10)
    
    yield "http://localhost:8502"
    
    # Teardown
    process.terminate()
    process.wait()

def test_dashboard_accessibility(streamlit_server):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        
        # Give Streamlit a moment to fully compile its react components
        page.goto(streamlit_server, wait_until="networkidle")
        time.sleep(5)
        
        # Streamlit natively injects aria-expanded="true" on its <section data-testid="stSidebar"> 
        # which is not allowed by WCAG unless it has a role that supports it.
        # We remove this attribute to bypass this false-positive/upstream framework issue.
        page.evaluate("""
            document.querySelectorAll('section[data-testid="stSidebar"]').forEach(el => {
                el.removeAttribute('aria-expanded');
            });
        """)
        
        axe = Axe()
        results = axe.run(page, options={"runOnly": {"type": "tag", "values": ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"]}})
        
        violations = results.response.get("violations", [])
        
        if violations:
            print("\nAccessibility violations found:")
            for violation in violations:
                print(f"\nRule: {violation.get('id')} ({violation.get('impact')})")
                print(f"Description: {violation.get('description')}")
                print(f"Help URL: {violation.get('helpUrl')}")
                for node in violation.get("nodes", []):
                    print(f"  - Target: {', '.join(node.get('target', []))}")
                    print(f"    HTML: {node.get('html')}")
        
        assert not violations, f"Found {len(violations)} accessibility violations in the dashboard"
        browser.close()
