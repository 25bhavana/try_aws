import subprocess
import streamlit as st

def install_package(package):
    subprocess.run(["pip", "install", package])

# Example usage
if _name_ == "_main_":
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
