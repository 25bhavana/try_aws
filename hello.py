import subprocess
import streamlit as st

import streamlit as st
import requests
from urllib.parse import urlparse

# Your website URL
your_website = "https://www.microbiotx.com/pages/gutchat"

# Get the referrer
referrer = st.experimental_get_query_params().get("referrer", [""])[0]

# Function to check if the referrer is your website
def is_valid_referrer(referrer):
    if not referrer:
        return False
    parsed_url = urlparse(referrer)
    return parsed_url.netloc == urlparse(your_website).netloc

# If the referrer is not valid, redirect to your website
if not is_valid_referrer(referrer):
    st.write(f"Redirecting to {your_website}...")
    st.experimental_set_query_params(referrer=your_website)
    st.experimental_rerun()



def install_package(package):
    subprocess.run(["pip", "install", package])

# Example usage
if __name__ == "__main__":
    st.title("Streamlit App with Dynamic Package Installation")

    # Package name to install
    package_name = "langchain"

    # Install the package
    st.write(f"Installing package: {package_name}")
    install_package(package_name)

    # Import the package after installation
    try:
        import langchain
        st.write(f"{package_name} installed and imported successfully!")
    except ImportError as e:
        st.write(f"Failed to import {package_name}: {e}")

    # Your Streamlit app logic goes here
    st.write("Streamlit app is running with dynamically installed package.")



import subprocess
import streamlit as st

def install_package(package):
    subprocess.run(["pip", "install", package])
'''
# Example usage
if __name__ == "__main__":
    st.title("Streamlit App with Dynamic Package Installation")

    # Package name to install
    package_name = "langchain"

    # Install the package
    st.write(f"Installing package: {package_name}")
    install_package(package_name)

    # Import the package after installation
    try:
        import langchain
        st.write(f"{package_name} installed and imported successfully!")
    except ImportError as e:
        st.write(f"Failed to import {package_name}: {e}")

    # Your Streamlit app logic goes here
    st.write("Streamlit app is running with dynamically installed package.")
'''
